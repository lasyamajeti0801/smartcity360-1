"""
SmartCity360 - Payments, Notifications, Announcements & Events Endpoints
"""

from datetime import datetime, timezone
import uuid
from typing import List
from fastapi import APIRouter, Depends, Query, status
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
from sqlalchemy.orm import selectinload
from backend.app.core.database import get_db
from backend.app.core.security import decode_token, oauth2_scheme
from backend.app.models.engagement import (
    PaymentTransaction,
    PaymentReceipt,
    NotificationRecord,
    Announcement,
    CityEvent,
    FeedbackRecord
)
from backend.app.schemas.engagement import (
    AnnouncementResponse,
    CityEventResponse,
    FeedbackCreateRequest,
    NotificationResponse,
    PaymentInitiateRequest,
    PaymentTransactionResponse
)

router = APIRouter(tags=["Civic Engagement, Payments & Bulletins"])

@router.post("/payments/initiate", response_model=PaymentTransactionResponse, status_code=status.HTTP_201_CREATED, summary="Initiate mock civic fee payment")
async def initiate_payment(
    req: PaymentInitiateRequest,
    token: str = Depends(oauth2_scheme),
    db: AsyncSession = Depends(get_db)
):
    payload = decode_token(token)
    user_id = payload.get("sub")
    
    tx_ref = f"TXN-{datetime.now(timezone.utc).strftime('%Y%m%d')}-{uuid.uuid4().hex[:8].upper()}"
    receipt_no = f"RCT-{datetime.now(timezone.utc).strftime('%Y%m%d')}-{uuid.uuid4().hex[:6].upper()}"

    tx = PaymentTransaction(
        transaction_reference=tx_ref,
        user_id=user_id,
        service_request_id=req.service_request_id,
        amount=req.amount,
        currency=req.currency,
        payment_method=req.payment_method,
        status="SUCCESS",
        gateway_provider="MOCK_MUNICIPAL_GATEWAY",
        gateway_response_code="AUTH_APPROVED"
    )
    db.add(tx)
    await db.flush()

    tax = round(float(req.amount) * 0.05, 2)
    receipt = PaymentReceipt(
        receipt_number=receipt_no,
        transaction_id=tx.id,
        tax_amount=tax,
        total_paid=round(float(req.amount) + tax, 2),
        issued_at=datetime.now(timezone.utc),
        verification_hash=uuid.uuid4().hex
    )
    db.add(receipt)
    await db.flush()

    q = select(PaymentTransaction).where(PaymentTransaction.id == tx.id).options(selectinload(PaymentTransaction.receipt))
    res = await db.execute(q)
    return PaymentTransactionResponse.model_validate(res.scalars().first())

@router.get("/announcements", response_model=List[AnnouncementResponse], summary="List active city announcements")
async def list_announcements(db: AsyncSession = Depends(get_db)):
    query = (
        select(Announcement)
        .where(Announcement.is_active == True, Announcement.is_deleted == False)
        .order_by(Announcement.published_at.desc())
    )
    res = await db.execute(query)
    return [AnnouncementResponse.model_validate(a) for a in res.scalars().all()]

@router.get("/events", response_model=List[CityEventResponse], summary="List civic and community events")
async def list_city_events(db: AsyncSession = Depends(get_db)):
    query = (
        select(CityEvent)
        .where(CityEvent.is_deleted == False)
        .order_by(CityEvent.start_time.asc())
    )
    res = await db.execute(query)
    return [CityEventResponse.model_validate(e) for e in res.scalars().all()]

@router.get("/notifications", response_model=List[NotificationResponse], summary="List citizen in-app notifications")
async def list_notifications(
    token: str = Depends(oauth2_scheme),
    db: AsyncSession = Depends(get_db)
):
    payload = decode_token(token)
    user_id = payload.get("sub")
    query = (
        select(NotificationRecord)
        .where(NotificationRecord.user_id == user_id, NotificationRecord.is_deleted == False)
        .order_by(NotificationRecord.created_at.desc())
    )
    res = await db.execute(query)
    return [NotificationResponse.model_validate(n) for n in res.scalars().all()]

@router.post("/feedback", status_code=status.HTTP_201_CREATED, summary="Submit municipal service feedback")
async def submit_feedback(
    req: FeedbackCreateRequest,
    token: str = Depends(oauth2_scheme),
    db: AsyncSession = Depends(get_db)
):
    payload = decode_token(token)
    user_id = payload.get("sub")
    fb = FeedbackRecord(
        user_id=user_id,
        service_id=req.service_id,
        rating=req.rating,
        comments=req.comments,
        sentiment="POSITIVE" if req.rating >= 4 else "NEUTRAL" if req.rating == 3 else "NEGATIVE"
    )
    db.add(fb)
    await db.flush()
    return {"success": True, "message": "Feedback submitted successfully."}
