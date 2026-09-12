"""
SmartCity360 - Civic Complaint Lifecycle & SLA Business Service
Enforces the 9-stage state machine, SLA target deadlines, ticket numbering, and escalation.
"""

from datetime import datetime, timedelta, timezone
import uuid
from typing import List, Optional
from sqlalchemy import select, update
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import selectinload
from backend.app.core.exceptions import (
    EntityNotFoundException,
    InvalidStateTransitionException,
    SmartCityException
)
from backend.app.models.complaint import (
    Complaint,
    ComplaintCategory,
    ComplaintComment,
    ComplaintStatusHistory,
    STATUS_NEW,
    STATUS_UNDER_REVIEW,
    STATUS_ASSIGNED,
    STATUS_IN_PROGRESS,
    STATUS_ON_HOLD,
    STATUS_RESOLVED,
    STATUS_CLOSED,
    STATUS_REOPENED,
    STATUS_REJECTED
)
from backend.app.models.department import Department
from backend.app.schemas.complaint import ComplaintCreateRequest, ComplaintStatusUpdateRequest

# Valid state machine transitions
ALLOWED_TRANSITIONS = {
    STATUS_NEW: {STATUS_UNDER_REVIEW, STATUS_REJECTED, STATUS_ASSIGNED},
    STATUS_UNDER_REVIEW: {STATUS_ASSIGNED, STATUS_REJECTED, STATUS_ON_HOLD},
    STATUS_ASSIGNED: {STATUS_IN_PROGRESS, STATUS_ON_HOLD, STATUS_UNDER_REVIEW},
    STATUS_IN_PROGRESS: {STATUS_RESOLVED, STATUS_ON_HOLD, STATUS_BLOCKED := "ON_HOLD"},
    STATUS_ON_HOLD: {STATUS_IN_PROGRESS, STATUS_ASSIGNED, STATUS_UNDER_REVIEW},
    STATUS_RESOLVED: {STATUS_CLOSED, STATUS_REOPENED},
    STATUS_CLOSED: {STATUS_REOPENED},
    STATUS_REOPENED: {STATUS_UNDER_REVIEW, STATUS_ASSIGNED, STATUS_IN_PROGRESS},
    STATUS_REJECTED: {STATUS_UNDER_REVIEW}
}

class ComplaintService:
    def __init__(self, session: AsyncSession):
        self.session = session

    def _generate_ticket_number(self) -> str:
        date_str = datetime.now(timezone.utc).strftime("%Y%m%d")
        rand_suffix = uuid.uuid4().hex[:6].upper()
        return f"CMP-{date_str}-{rand_suffix}"

    async def create_complaint(self, citizen_id: str, req: ComplaintCreateRequest) -> Complaint:
        # Validate category
        cat_query = select(ComplaintCategory).where(
            ComplaintCategory.id == req.category_id,
            ComplaintCategory.is_deleted == False
        )
        cat_res = await self.session.execute(cat_query)
        category = cat_res.scalars().first()
        if not category:
            raise EntityNotFoundException("ComplaintCategory", req.category_id)

        # Match department by code
        dept_query = select(Department).where(Department.code == category.default_department_code)
        dept_res = await self.session.execute(dept_query)
        department = dept_res.scalars().first()
        if not department:
            # Fallback to first active department
            first_dept_q = select(Department).limit(1)
            first_dept = (await self.session.execute(first_dept_q)).scalars().first()
            if not first_dept:
                raise SmartCityException("NO_DEPARTMENTS_CONFIGURED", "System has no active departments.", 500)
            department = first_dept

        ticket_number = self._generate_ticket_number()
        sla_due_at = datetime.now(timezone.utc) + timedelta(hours=category.default_sla_hours)

        complaint = Complaint(
            ticket_number=ticket_number,
            citizen_id=citizen_id,
            category_id=category.id,
            department_id=department.id,
            title=req.title,
            description=req.description,
            priority="MEDIUM",
            status=STATUS_NEW,
            latitude=req.latitude,
            longitude=req.longitude,
            location_address=req.location_address,
            ward_number=req.ward_number,
            sla_due_at=sla_due_at,
            is_escalated=False,
            evidence_image_url=req.evidence_image_url
        )
        self.session.add(complaint)
        await self.session.flush()

        # Initial history record
        history = ComplaintStatusHistory(
            complaint_id=complaint.id,
            from_status="NONE",
            to_status=STATUS_NEW,
            changed_by_user_id=citizen_id,
            reason="Complaint lodged by citizen via portal."
        )
        self.session.add(history)
        await self.session.flush()

        return complaint

    async def update_status(
        self,
        complaint_id: str,
        actor_id: str,
        req: ComplaintStatusUpdateRequest
    ) -> Complaint:
        query = (
            select(Complaint)
            .where(Complaint.id == complaint_id, Complaint.is_deleted == False)
            .options(selectinload(Complaint.status_history))
        )
        res = await self.session.execute(query)
        complaint = res.scalars().first()
        if not complaint:
            raise EntityNotFoundException("Complaint", complaint_id)

        target_status = req.status.upper()
        allowed = ALLOWED_TRANSITIONS.get(complaint.status, set())
        if target_status not in allowed:
            raise InvalidStateTransitionException(
                entity="Complaint",
                current_state=complaint.status,
                attempted_state=target_status
            )

        old_status = complaint.status
        complaint.status = target_status
        if req.assigned_staff_id:
            complaint.assigned_staff_id = req.assigned_staff_id
        if req.resolution_image_url:
            complaint.resolution_image_url = req.resolution_image_url
        if target_status == STATUS_RESOLVED:
            complaint.resolved_at = datetime.now(timezone.utc)

        # Record history
        history = ComplaintStatusHistory(
            complaint_id=complaint.id,
            from_status=old_status,
            to_status=target_status,
            changed_by_user_id=actor_id,
            reason=req.reason or f"Status updated to {target_status}"
        )
        self.session.add(history)
        await self.session.flush()
        return complaint

    async def add_comment(
        self,
        complaint_id: str,
        author_id: str,
        comment: str,
        is_internal: bool = False
    ) -> ComplaintComment:
        # Check complaint exists
        c_query = select(Complaint).where(Complaint.id == complaint_id, Complaint.is_deleted == False)
        c_res = await self.session.execute(c_query)
        if not c_res.scalars().first():
            raise EntityNotFoundException("Complaint", complaint_id)

        cmt = ComplaintComment(
            complaint_id=complaint_id,
            author_id=author_id,
            comment=comment,
            is_internal=is_internal
        )
        self.session.add(cmt)
        await self.session.flush()
        return cmt

    async def submit_feedback(
        self,
        complaint_id: str,
        citizen_id: str,
        rating: int,
        feedback: Optional[str] = None
    ) -> Complaint:
        query = select(Complaint).where(
            Complaint.id == complaint_id,
            Complaint.citizen_id == citizen_id,
            Complaint.is_deleted == False
        )
        res = await self.session.execute(query)
        complaint = res.scalars().first()
        if not complaint:
            raise EntityNotFoundException("Complaint", complaint_id)

        if complaint.status not in (STATUS_RESOLVED, STATUS_CLOSED):
            raise SmartCityException(
                code="INVALID_STATE_FOR_FEEDBACK",
                message="Feedback can only be provided for resolved or closed complaints.",
                status_code=400
            )

        complaint.citizen_rating = rating
        complaint.citizen_feedback = feedback
        await self.session.flush()
        return complaint
