"""
SmartCity360 - Municipal Field Work Order Business Service
Enforces field staff task execution, checklist completion tracking, evidence verification,
and automatic complaint resolution syncing.
"""

from datetime import datetime, timezone
import uuid
from typing import List, Optional
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import selectinload
from backend.app.core.exceptions import (
    EntityNotFoundException,
    InvalidStateTransitionException,
    SmartCityException
)
from backend.app.models.work_order import (
    WorkOrder,
    WorkOrderTask,
    WorkOrderEvidence,
    WO_STATUS_CREATED,
    WO_STATUS_ASSIGNED,
    WO_STATUS_ACCEPTED,
    WO_STATUS_IN_PROGRESS,
    WO_STATUS_BLOCKED,
    WO_STATUS_SUBMITTED,
    WO_STATUS_VERIFICATION,
    WO_STATUS_COMPLETED,
    WO_STATUS_CANCELLED
)
from backend.app.models.complaint import Complaint, STATUS_RESOLVED, STATUS_IN_PROGRESS as CMP_IN_PROGRESS
from backend.app.schemas.work_order import (
    WorkOrderCreateRequest,
    WorkOrderStatusUpdateRequest,
    WorkOrderEvidenceCreateRequest,
    WorkOrderAssignRequest,
    WorkOrderVerifyRequest
)

# State machine for field work orders
ALLOWED_WO_TRANSITIONS = {
    WO_STATUS_CREATED: {WO_STATUS_ASSIGNED, WO_STATUS_CANCELLED},
    WO_STATUS_ASSIGNED: {WO_STATUS_ACCEPTED, WO_STATUS_IN_PROGRESS, WO_STATUS_CANCELLED},
    WO_STATUS_ACCEPTED: {WO_STATUS_IN_PROGRESS, WO_STATUS_BLOCKED, WO_STATUS_CANCELLED},
    WO_STATUS_IN_PROGRESS: {WO_STATUS_BLOCKED, WO_STATUS_SUBMITTED, WO_STATUS_VERIFICATION},
    WO_STATUS_BLOCKED: {WO_STATUS_IN_PROGRESS, WO_STATUS_CANCELLED},
    WO_STATUS_SUBMITTED: {WO_STATUS_VERIFICATION, WO_STATUS_IN_PROGRESS},
    WO_STATUS_VERIFICATION: {WO_STATUS_COMPLETED, WO_STATUS_IN_PROGRESS},
    WO_STATUS_COMPLETED: set(),
    WO_STATUS_CANCELLED: set()
}

class WorkOrderService:
    def __init__(self, session: AsyncSession):
        self.session = session

    def _generate_order_number(self) -> str:
        date_str = datetime.now(timezone.utc).strftime("%Y%m%d")
        rand_suffix = uuid.uuid4().hex[:6].upper()
        return f"WO-{date_str}-{rand_suffix}"

    async def get_by_id(self, work_order_id: str) -> WorkOrder:
        query = (
            select(WorkOrder)
            .where(WorkOrder.id == work_order_id, WorkOrder.is_deleted == False)
            .options(
                selectinload(WorkOrder.tasks),
                selectinload(WorkOrder.evidence)
            )
        )
        res = await self.session.execute(query)
        wo = res.scalars().first()
        if not wo:
            raise EntityNotFoundException("WorkOrder", work_order_id)
        return wo

    async def create_work_order(self, req: WorkOrderCreateRequest) -> WorkOrder:
        order_num = self._generate_order_number()
        initial_status = WO_STATUS_ASSIGNED if req.assigned_technician_id else WO_STATUS_CREATED

        wo = WorkOrder(
            order_number=order_num,
            complaint_id=req.complaint_id,
            department_id=req.department_id,
            assigned_technician_id=req.assigned_technician_id,
            title=req.title,
            description=req.description,
            priority=req.priority,
            status=initial_status,
            completion_percentage=0,
            latitude=req.latitude,
            longitude=req.longitude,
            location_address=req.location_address,
            due_date=req.due_date
        )
        self.session.add(wo)
        await self.session.flush()

        # Add initial tasks if specified
        for idx, t_title in enumerate(req.task_titles):
            task = WorkOrderTask(
                work_order_id=wo.id,
                title=t_title,
                is_completed=False,
                order_index=idx
            )
            self.session.add(task)

        # If linked to a complaint, transition complaint to IN_PROGRESS
        if req.complaint_id:
            cmp_q = select(Complaint).where(Complaint.id == req.complaint_id)
            cmp_res = await self.session.execute(cmp_q)
            complaint = cmp_res.scalars().first()
            if complaint:
                complaint.status = CMP_IN_PROGRESS

        await self.session.flush()
        await self.session.refresh(wo, ["tasks", "evidence"])
        return wo

    async def assign_staff(self, work_order_id: str, req: WorkOrderAssignRequest) -> WorkOrder:
        wo = await self.get_by_id(work_order_id)
        wo.assigned_technician_id = req.assigned_technician_id
        if req.supervisor_id:
            wo.supervisor_id = req.supervisor_id

        if wo.status == WO_STATUS_CREATED:
            wo.status = WO_STATUS_ASSIGNED

        await self.session.flush()
        await self.session.refresh(wo, ["tasks", "evidence"])
        return wo

    async def toggle_task(self, work_order_id: str, task_id: str) -> WorkOrder:
        wo = await self.get_by_id(work_order_id)

        task_found = None
        for t in wo.tasks:
            if t.id == task_id:
                task_found = t
                break

        if not task_found:
            raise EntityNotFoundException("WorkOrderTask", task_id)

        task_found.is_completed = not task_found.is_completed
        task_found.completed_at = datetime.now(timezone.utc) if task_found.is_completed else None

        # Recalculate completion percentage
        if wo.tasks:
            completed_count = sum(1 for t in wo.tasks if t.is_completed)
            wo.completion_percentage = int((completed_count / len(wo.tasks)) * 100)

            # Auto transition to VERIFICATION if 100% complete
            if wo.completion_percentage == 100 and wo.status == WO_STATUS_IN_PROGRESS:
                wo.status = WO_STATUS_VERIFICATION

        await self.session.flush()
        await self.session.refresh(wo, ["tasks", "evidence"])
        return wo

    async def attach_evidence(
        self,
        work_order_id: str,
        staff_id: Optional[str],
        req: WorkOrderEvidenceCreateRequest
    ) -> WorkOrder:
        wo = await self.get_by_id(work_order_id)

        evidence = WorkOrderEvidence(
            work_order_id=wo.id,
            evidence_type=req.evidence_type,
            file_url=req.file_url,
            caption=req.caption,
            uploaded_by_staff_id=staff_id
        )
        self.session.add(evidence)
        await self.session.flush()
        await self.session.refresh(wo, ["tasks", "evidence"])
        return wo

    async def update_status(self, work_order_id: str, req: WorkOrderStatusUpdateRequest) -> WorkOrder:
        wo = await self.get_by_id(work_order_id)
        target = req.status.upper()

        allowed = ALLOWED_WO_TRANSITIONS.get(wo.status, set())
        if target not in allowed and target != wo.status:
            raise InvalidStateTransitionException("WorkOrder", wo.status, target)

        wo.status = target
        if req.completion_percentage is not None:
            wo.completion_percentage = req.completion_percentage
        if req.field_notes:
            wo.field_notes = req.field_notes

        if target == WO_STATUS_COMPLETED:
            wo.completed_at = datetime.now(timezone.utc)
            wo.completion_percentage = 100

            # If connected complaint exists, resolve it
            if wo.complaint_id:
                cmp_q = select(Complaint).where(Complaint.id == wo.complaint_id)
                cmp_res = await self.session.execute(cmp_q)
                complaint = cmp_res.scalars().first()
                if complaint:
                    complaint.status = STATUS_RESOLVED
                    complaint.resolved_at = datetime.now(timezone.utc)

        await self.session.flush()
        return await self.get_by_id(work_order_id)

    async def verify_work_order(self, work_order_id: str, req: WorkOrderVerifyRequest) -> WorkOrder:
        wo = await self.get_by_id(work_order_id)

        if req.is_approved:
            wo.status = WO_STATUS_COMPLETED
            wo.completion_percentage = 100
            wo.completed_at = datetime.now(timezone.utc)
            wo.verified_at = datetime.now(timezone.utc)
            if req.notes:
                wo.field_notes = f"{wo.field_notes or ''}\n[Supervisor Approved]: {req.notes}".strip()

            # Resolve associated complaint
            if wo.complaint_id:
                cmp_q = select(Complaint).where(Complaint.id == wo.complaint_id)
                cmp_res = await self.session.execute(cmp_q)
                complaint = cmp_res.scalars().first()
                if complaint:
                    complaint.status = STATUS_RESOLVED
                    complaint.resolved_at = datetime.now(timezone.utc)
        else:
            # Rejection returns to IN_PROGRESS for rectification
            wo.status = WO_STATUS_IN_PROGRESS
            if req.notes:
                wo.field_notes = f"{wo.field_notes or ''}\n[Supervisor Rejected / Changes Requested]: {req.notes}".strip()

        await self.session.flush()
        return await self.get_by_id(work_order_id)
