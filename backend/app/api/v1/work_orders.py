"""
SmartCity360 - Municipal Work Order Management Endpoints
"""

from datetime import datetime, timezone
import uuid
from typing import List, Optional
from fastapi import APIRouter, Depends, Query, status
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
from sqlalchemy.orm import selectinload
from backend.app.core.database import get_db
from backend.app.core.security import decode_token, oauth2_scheme
from backend.app.core.exceptions import EntityNotFoundException
from backend.app.models.work_order import WorkOrder, WorkOrderTask, WorkOrderEvidence
from backend.app.schemas.work_order import (
    WorkOrderCreateRequest,
    WorkOrderResponse,
    WorkOrderStatusUpdateRequest,
    WorkOrderTaskResponse
)

router = APIRouter(prefix="/work-orders", tags=["Field Work Orders"])

@router.get("", response_model=List[WorkOrderResponse], summary="List work orders")
async def list_work_orders(
    department_id: Optional[str] = Query(None),
    status: Optional[str] = Query(None),
    technician_id: Optional[str] = Query(None),
    skip: int = Query(0, ge=0),
    limit: int = Query(50, ge=1, le=100),
    db: AsyncSession = Depends(get_db)
):
    query = (
        select(WorkOrder)
        .where(WorkOrder.is_deleted == False)
        .options(
            selectinload(WorkOrder.tasks),
            selectinload(WorkOrder.evidence)
        )
    )
    if department_id:
        query = query.where(WorkOrder.department_id == department_id)
    if status:
        query = query.where(WorkOrder.status == status)
    if technician_id:
        query = query.where(WorkOrder.assigned_technician_id == technician_id)

    query = query.order_by(WorkOrder.created_at.desc()).offset(skip).limit(limit)
    res = await db.execute(query)
    orders = res.scalars().all()
    return [WorkOrderResponse.model_validate(o) for o in orders]

@router.post("", response_model=WorkOrderResponse, status_code=status.HTTP_201_CREATED, summary="Create field work order")
async def create_work_order(
    req: WorkOrderCreateRequest,
    token: str = Depends(oauth2_scheme),
    db: AsyncSession = Depends(get_db)
):
    date_str = datetime.now(timezone.utc).strftime("%Y%m%d")
    rand_suffix = uuid.uuid4().hex[:6].upper()
    order_num = f"WO-{date_str}-{rand_suffix}"

    wo = WorkOrder(
        order_number=order_num,
        complaint_id=req.complaint_id,
        department_id=req.department_id,
        assigned_technician_id=req.assigned_technician_id,
        title=req.title,
        description=req.description,
        priority=req.priority,
        status="ASSIGNED" if req.assigned_technician_id else "CREATED",
        latitude=req.latitude,
        longitude=req.longitude,
        location_address=req.location_address,
        due_date=req.due_date
    )
    db.add(wo)
    await db.flush()

    for idx, t_title in enumerate(req.task_titles):
        task = WorkOrderTask(
            work_order_id=wo.id,
            title=t_title,
            is_completed=False,
            order_index=idx
        )
        db.add(task)
    await db.flush()

    # Fetch loaded
    q = select(WorkOrder).where(WorkOrder.id == wo.id).options(selectinload(WorkOrder.tasks), selectinload(WorkOrder.evidence))
    res = await db.execute(q)
    return WorkOrderResponse.model_validate(res.scalars().first())

@router.patch("/{work_order_id}/status", response_model=WorkOrderResponse, summary="Update work order status")
async def update_work_order_status(
    work_order_id: str,
    req: WorkOrderStatusUpdateRequest,
    db: AsyncSession = Depends(get_db)
):
    query = (
        select(WorkOrder)
        .where(WorkOrder.id == work_order_id, WorkOrder.is_deleted == False)
        .options(selectinload(WorkOrder.tasks), selectinload(WorkOrder.evidence))
    )
    res = await db.execute(query)
    wo = res.scalars().first()
    if not wo:
        raise EntityNotFoundException("WorkOrder", work_order_id)

    wo.status = req.status.upper()
    if req.completion_percentage is not None:
        wo.completion_percentage = req.completion_percentage
    if req.field_notes:
        wo.field_notes = req.field_notes
    if wo.status == "COMPLETED":
        wo.completed_at = datetime.now(timezone.utc)

    await db.flush()
    return WorkOrderResponse.model_validate(wo)
