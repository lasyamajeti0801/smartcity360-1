"""
SmartCity360 - Civic Engagement, Payments, Notifications & Announcements Models
Handles mock payment ledger, in-app notification center, official city bulletins,
public community events, and civic feedback ratings.
"""

from datetime import datetime
from typing import Optional
from sqlalchemy import String, Text, ForeignKey, DateTime, Integer, Boolean, Numeric
from sqlalchemy.orm import Mapped, mapped_column, relationship
from backend.app.core.database import TimeStampedBase

class PaymentTransaction(TimeStampedBase):
    __tablename__ = "payment_transactions"

    transaction_reference: Mapped[str] = mapped_column(String(64), unique=True, index=True, nullable=False)
    user_id: Mapped[str] = mapped_column(String(36), ForeignKey("users.id", ondelete="CASCADE"), index=True, nullable=False)
    service_request_id: Mapped[Optional[str]] = mapped_column(String(36), ForeignKey("service_requests.id", ondelete="SET NULL"), nullable=True)
    
    amount: Mapped[float] = mapped_column(Numeric(10, 2), nullable=False)
    currency: Mapped[str] = mapped_column(String(3), default="USD", nullable=False)
    payment_method: Mapped[str] = mapped_column(String(32), default="CREDIT_CARD", nullable=False)  # CREDIT_CARD, DEBIT_CARD, UPI, BANK_TRANSFER
    status: Mapped[str] = mapped_column(String(32), default="SUCCESS", index=True, nullable=False)  # SUCCESS, FAILED, PENDING, REFUNDED
    
    gateway_provider: Mapped[str] = mapped_column(String(64), default="MOCK_MUNICIPAL_GATEWAY", nullable=False)
    gateway_response_code: Mapped[str] = mapped_column(String(64), default="AUTH_APPROVED", nullable=False)

    user: Mapped["User"] = relationship("User")
    receipt: Mapped[Optional["PaymentReceipt"]] = relationship("PaymentReceipt", back_populates="transaction", uselist=False)

class PaymentReceipt(TimeStampedBase):
    __tablename__ = "payment_receipts"

    receipt_number: Mapped[str] = mapped_column(String(64), unique=True, index=True, nullable=False)
    transaction_id: Mapped[str] = mapped_column(String(36), ForeignKey("payment_transactions.id", ondelete="CASCADE"), unique=True, nullable=False)
    tax_amount: Mapped[float] = mapped_column(Numeric(10, 2), default=0.00, nullable=False)
    total_paid: Mapped[float] = mapped_column(Numeric(10, 2), nullable=False)
    issued_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), nullable=False)
    verification_hash: Mapped[str] = mapped_column(String(64), nullable=False)

    transaction: Mapped["PaymentTransaction"] = relationship("PaymentTransaction", back_populates="receipt")

class NotificationRecord(TimeStampedBase):
    __tablename__ = "notification_records"

    user_id: Mapped[str] = mapped_column(String(36), ForeignKey("users.id", ondelete="CASCADE"), index=True, nullable=False)
    title: Mapped[str] = mapped_column(String(255), nullable=False)
    message: Mapped[str] = mapped_column(Text, nullable=False)
    notification_type: Mapped[str] = mapped_column(String(64), default="GENERAL", index=True, nullable=False)  # COMPLAINT, EMERGENCY, PAYMENT, ANNOUNCEMENT
    priority: Mapped[str] = mapped_column(String(32), default="NORMAL", nullable=False)
    is_read: Mapped[bool] = mapped_column(Boolean, default=False, index=True, nullable=False)
    read_at: Mapped[Optional[datetime]] = mapped_column(DateTime(timezone=True), nullable=True)
    link_url: Mapped[Optional[str]] = mapped_column(String(255), nullable=True)

    user: Mapped["User"] = relationship("User")

class Announcement(TimeStampedBase):
    __tablename__ = "announcements"

    title: Mapped[str] = mapped_column(String(255), nullable=False)
    summary: Mapped[str] = mapped_column(String(512), nullable=False)
    content: Mapped[str] = mapped_column(Text, nullable=False)
    category: Mapped[str] = mapped_column(String(64), default="GENERAL", index=True, nullable=False)  # ROAD_CLOSURE, WATER_OUTAGE, PUBLIC_ALERT
    priority: Mapped[str] = mapped_column(String(32), default="NORMAL", nullable=False)  # NORMAL, URGENT, EMERGENCY
    department_id: Mapped[Optional[str]] = mapped_column(String(36), ForeignKey("departments.id", ondelete="SET NULL"), nullable=True)
    
    published_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), nullable=False)
    expires_at: Mapped[Optional[datetime]] = mapped_column(DateTime(timezone=True), nullable=True)
    is_active: Mapped[bool] = mapped_column(Boolean, default=True, index=True, nullable=False)

    department: Mapped[Optional["Department"]] = relationship("Department")

class CityEvent(TimeStampedBase):
    __tablename__ = "city_events"

    title: Mapped[str] = mapped_column(String(255), nullable=False)
    description: Mapped[str] = mapped_column(Text, nullable=False)
    venue_name: Mapped[str] = mapped_column(String(255), nullable=False)
    venue_address: Mapped[str] = mapped_column(String(255), nullable=False)
    start_time: Mapped[datetime] = mapped_column(DateTime(timezone=True), index=True, nullable=False)
    end_time: Mapped[datetime] = mapped_column(DateTime(timezone=True), nullable=False)
    organizer: Mapped[str] = mapped_column(String(128), nullable=False)
    max_capacity: Mapped[Optional[int]] = mapped_column(Integer, nullable=True)
    is_free_admission: Mapped[bool] = mapped_column(Boolean, default=True, nullable=False)

class FeedbackRecord(TimeStampedBase):
    __tablename__ = "feedback_records"

    user_id: Mapped[Optional[str]] = mapped_column(String(36), ForeignKey("users.id", ondelete="SET NULL"), nullable=True)
    service_id: Mapped[Optional[str]] = mapped_column(String(36), ForeignKey("municipal_services.id", ondelete="SET NULL"), nullable=True)
    rating: Mapped[int] = mapped_column(Integer, nullable=False)  # 1 to 5
    sentiment: Mapped[str] = mapped_column(String(32), default="NEUTRAL", nullable=False)  # POSITIVE, NEUTRAL, NEGATIVE
    comments: Mapped[Optional[str]] = mapped_column(Text, nullable=True)
    channel: Mapped[str] = mapped_column(String(32), default="WEB", nullable=False)
