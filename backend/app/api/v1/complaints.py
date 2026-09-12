"""
SmartCity360 - Civic Complaint Management Endpoints
"""

from typing import List, Optional
from fastapi import APIRouter, Depends, Query, status
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
from sqlalchemy.orm import selectinload
from backend.app.core.database import get_db
from backend.app.core.security import decode_token, oauth2_scheme
from backend.app.core.exceptions import EntityNotFoundException
from backend.app.models.complaint import Complaint, ComplaintCategory
from backend.app.schemas.complaint import (
    ComplaintCategoryResponse,
    ComplaintCommentCreateRequest,
    ComplaintCommentResponse,
    ComplaintCreateRequest,
    ComplaintResponse,
    ComplaintStatusUpdateRequest,
    CitizenFeedbackRequest
)
from backend.app.services.complaint_service import ComplaintService
from backend.app.repositories.complaint_repo import ComplaintRepository

router = APIRouter(prefix="/complaints", tags=["Civic Complaints"])

@router.get("/categories", response_model=List[ComplaintCategoryResponse], summary="List all complaint categories")
async def list_complaint_categories(db: AsyncSession = Depends(get_db)):
    query = select(ComplaintCategory).where(ComplaintCategory.is_deleted == False).order_by(ComplaintCategory.name.asc())
    res = await db.execute(query)
    categories = res.scalars().all()
    return [ComplaintCategoryResponse.model_validate(c) for c in categories]

@router.post("", response_model=ComplaintResponse, status_code=status.HTTP_201_CREATED, summary="Submit a new civic complaint")
async def create_complaint(
    req: ComplaintCreateRequest,
    token: str = Depends(oauth2_scheme),
    db: AsyncSession = Depends(get_db)
):
    payload = decode_token(token)
    citizen_id = payload.get("sub")
    service = ComplaintService(db)
    complaint = await service.create_complaint(citizen_id=citizen_id, req=req)
    
    # Fetch full record
    repo = ComplaintRepository(db)
    full_c = await repo.get_by_ticket_number(complaint.ticket_number)
    return ComplaintResponse.model_validate(full_c)

@router.get("", response_model=List[ComplaintResponse], summary="List civic complaints with filters")
async def list_complaints(
    department_id: Optional[str] = Query(None),
    status: Optional[str] = Query(None),
    priority: Optional[str] = Query(None),
    ward_number: Optional[int] = Query(None),
    is_escalated: Optional[bool] = Query(None),
    skip: int = Query(0, ge=0),
    limit: int = Query(50, ge=1, le=100),
    db: AsyncSession = Depends(get_db)
):
    repo = ComplaintRepository(db)
    complaints = await repo.list_with_filters(
        department_id=department_id,
        status=status,
        priority=priority,
        ward_number=ward_number,
        is_escalated=is_escalated,
        skip=skip,
        limit=limit
    )
    return [ComplaintResponse.model_validate(c) for c in complaints]

@router.get("/{ticket_number}", response_model=ComplaintResponse, summary="Get complaint by ticket number")
async def get_complaint(ticket_number: str, db: AsyncSession = Depends(get_db)):
    repo = ComplaintRepository(db)
    complaint = await repo.get_by_ticket_number(ticket_number)
    if not complaint:
        raise EntityNotFoundException("Complaint", ticket_number)
    return ComplaintResponse.model_validate(complaint)

@router.patch("/{complaint_id}/status", response_model=ComplaintResponse, summary="Update complaint status")
async def update_complaint_status(
    complaint_id: str,
    req: ComplaintStatusUpdateRequest,
    token: str = Depends(oauth2_scheme),
    db: AsyncSession = Depends(get_db)
):
    payload = decode_token(token)
    actor_id = payload.get("sub")
    service = ComplaintService(db)
    complaint = await service.update_status(complaint_id=complaint_id, actor_id=actor_id, req=req)
    
    repo = ComplaintRepository(db)
    full_c = await repo.get_by_ticket_number(complaint.ticket_number)
    return ComplaintResponse.model_validate(full_c)

@router.post("/{complaint_id}/comments", response_model=ComplaintCommentResponse, summary="Add comment to complaint")
async def add_complaint_comment(
    complaint_id: str,
    req: ComplaintCommentCreateRequest,
    token: str = Depends(oauth2_scheme),
    db: AsyncSession = Depends(get_db)
):
    payload = decode_token(token)
    author_id = payload.get("sub")
    service = ComplaintService(db)
    cmt = await service.add_comment(
        complaint_id=complaint_id,
        author_id=author_id,
        comment=req.comment,
        is_internal=req.is_internal
    )
    return ComplaintCommentResponse.model_validate(cmt)

@router.post("/{complaint_id}/feedback", response_model=ComplaintResponse, summary="Submit citizen feedback rating")
async def submit_citizen_feedback(
    complaint_id: str,
    req: CitizenFeedbackRequest,
    token: str = Depends(oauth2_scheme),
    db: AsyncSession = Depends(get_db)
):
    payload = decode_token(token)
    citizen_id = payload.get("sub")
    service = ComplaintService(db)
    complaint = await service.submit_feedback(
        complaint_id=complaint_id,
        citizen_id=citizen_id,
        rating=req.rating,
        feedback=req.feedback
    )
    repo = ComplaintRepository(db)
    full_c = await repo.get_by_ticket_number(complaint.ticket_number)
    return ComplaintResponse.model_validate(full_c)
