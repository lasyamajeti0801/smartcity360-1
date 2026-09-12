"""
SmartCity360 - Municipal Work Order Management Endpoints
"""

from typing import List, Optional
from fastapi import APIRouter, Depends, Query, status
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
from sqlalchemy.orm import selectinload
from backend.app.core.database import get_db
from backend.app.core.security import decode_token, oauth2_scheme
from backend.app.models.work_order import WorkOrder
from backend.app.schemas.work_order import (
    WorkOrderCreateRequest,
    WorkOrderResponse,
    WorkOrderStatusUpdateRequest,
    WorkOrderEvidenceCreateRequest,
    WorkOrderAssignRequest,
    WorkOrderVerifyRequest
)
from backend.app.services.work_order_service import WorkOrderService

router = APIRouter(prefix="/work-orders", tags=["Field Work Orders"])

@router.get("", response_model=List[WorkOrderResponse], summary="List work orders with multi-parameter filter")
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

@router.get("/{work_order_id}", response_model=WorkOrderResponse, summary="Get work order details by ID")
async def get_work_order(work_order_id: str, db: AsyncSession = Depends(get_db)):
    service = WorkOrderService(db)
    wo = await service.get_by_id(work_order_id)
    return WorkOrderResponse.model_validate(wo)

@router.post("", response_model=WorkOrderResponse, status_code=status.HTTP_201_CREATED, summary="Create field work order")
async def create_work_order(
    req: WorkOrderCreateRequest,
    token: str = Depends(oauth2_scheme),
    db: AsyncSession = Depends(get_db)
):
    service = WorkOrderService(db)
    wo = await service.create_work_order(req)
    return WorkOrderResponse.model_validate(wo)

@router.patch("/{work_order_id}/status", response_model=WorkOrderResponse, summary="Update work order status")
async def update_work_order_status(
    work_order_id: str,
    req: WorkOrderStatusUpdateRequest,
    db: AsyncSession = Depends(get_db)
):
    service = WorkOrderService(db)
    wo = await service.update_status(work_order_id, req)
    return WorkOrderResponse.model_validate(wo)

@router.post("/{work_order_id}/tasks/{task_id}/toggle", response_model=WorkOrderResponse, summary="Toggle checklist task completion")
async def toggle_work_order_task(
    work_order_id: str,
    task_id: str,
    db: AsyncSession = Depends(get_db)
):
    service = WorkOrderService(db)
    wo = await service.toggle_task(work_order_id, task_id)
    return WorkOrderResponse.model_validate(wo)

@router.post("/{work_order_id}/evidence", response_model=WorkOrderResponse, summary="Attach field photographic evidence")
async def attach_work_order_evidence(
    work_order_id: str,
    req: WorkOrderEvidenceCreateRequest,
    token: str = Depends(oauth2_scheme),
    db: AsyncSession = Depends(get_db)
):
    payload = decode_token(token)
    staff_id = payload.get("sub")
    service = WorkOrderService(db)
    wo = await service.attach_evidence(work_order_id, staff_id, req)
    return WorkOrderResponse.model_validate(wo)

@router.post("/{work_order_id}/assign", response_model=WorkOrderResponse, summary="Assign technician and supervisor to work order")
async def assign_work_order_staff(
    work_order_id: str,
    req: WorkOrderAssignRequest,
    db: AsyncSession = Depends(get_db)
):
    service = WorkOrderService(db)
    wo = await service.assign_staff(work_order_id, req)
    return WorkOrderResponse.model_validate(wo)

@router.post("/{work_order_id}/verify", response_model=WorkOrderResponse, summary="Supervisor verification and sign-off")
async def verify_work_order(
    work_order_id: str,
    req: WorkOrderVerifyRequest,
    db: AsyncSession = Depends(get_db)
):
    service = WorkOrderService(db)
    wo = await service.verify_work_order(work_order_id, req)
    return WorkOrderResponse.model_validate(wo)
