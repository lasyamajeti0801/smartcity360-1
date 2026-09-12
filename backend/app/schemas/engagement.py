"""
SmartCity360 - Civic Engagement, Payments & Notifications Pydantic Schemas (Pydantic v2)
"""

from datetime import datetime
from typing import Optional
from pydantic import BaseModel, ConfigDict, Field

class PaymentInitiateRequest(BaseModel):
    service_request_id: Optional[str] = None
    amount: float = Field(gt=0)
    currency: str = "USD"
    payment_method: str = "CREDIT_CARD"

class PaymentReceiptResponse(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    receipt_number: str
    tax_amount: float
    total_paid: float
    issued_at: datetime
    verification_hash: str

class PaymentTransactionResponse(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: str
    transaction_reference: str
    amount: float
    currency: str
    payment_method: str
    status: str
    gateway_provider: str
    created_at: datetime
    receipt: Optional[PaymentReceiptResponse] = None

class NotificationResponse(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: str
    title: str
    message: str
    notification_type: str
    priority: str
    is_read: bool
    read_at: Optional[datetime] = None
    link_url: Optional[str] = None
    created_at: datetime

class AnnouncementResponse(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: str
    title: str
    summary: str
    content: str
    category: str
    priority: str
    published_at: datetime
    expires_at: Optional[datetime] = None
    is_active: bool

class CityEventResponse(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: str
    title: str
    description: str
    venue_name: str
    venue_address: str
    start_time: datetime
    end_time: datetime
    organizer: str
    max_capacity: Optional[int] = None
    is_free_admission: bool

class FeedbackCreateRequest(BaseModel):
    service_id: Optional[str] = None
    rating: int = Field(ge=1, le=5)
    comments: Optional[str] = None
