"""
SmartCity360 - Citizen Service Request & Lifecycle Models
Tracks citizen applications through municipal review, approval, and completion.
"""

from datetime import datetime
from typing import List, Optional
from sqlalchemy import String, Integer, Text, ForeignKey, DateTime
from sqlalchemy.orm import Mapped, mapped_column, relationship
from backend.app.core.database import TimeStampedBase

# Standard Request Statuses
STATUS_DRAFT = "DRAFT"
STATUS_SUBMITTED = "SUBMITTED"
STATUS_UNDER_REVIEW = "UNDER_REVIEW"
STATUS_DOCUMENTS_REQUIRED = "DOCUMENTS_REQUIRED"
STATUS_APPROVED = "APPROVED"
STATUS_REJECTED = "REJECTED"
STATUS_IN_PROGRESS = "IN_PROGRESS"
STATUS_COMPLETED = "COMPLETED"
STATUS_CANCELLED = "CANCELLED"

class ServiceRequest(TimeStampedBase):
    __tablename__ = "service_requests"

    reference_number: Mapped[str] = mapped_column(String(32), unique=True, index=True, nullable=False)
    citizen_id: Mapped[str] = mapped_column(String(36), ForeignKey("users.id", ondelete="CASCADE"), index=True, nullable=False)
    service_id: Mapped[str] = mapped_column(String(36), ForeignKey("municipal_services.id", ondelete="RESTRICT"), index=True, nullable=False)
    status: Mapped[str] = mapped_column(String(32), default=STATUS_SUBMITTED, index=True, nullable=False)
    application_payload: Mapped[str] = mapped_column(Text, default="{}", nullable=False)
    rejection_reason: Mapped[Optional[str]] = mapped_column(Text, nullable=True)
    sla_due_at: Mapped[Optional[datetime]] = mapped_column(DateTime(timezone=True), index=True, nullable=True)
    completed_at: Mapped[Optional[datetime]] = mapped_column(DateTime(timezone=True), nullable=True)

    citizen: Mapped["User"] = relationship("User")
    service: Mapped["MunicipalService"] = relationship("MunicipalService", back_populates="requests")
    documents: Mapped[List["ServiceDocument"]] = relationship(
        "ServiceDocument",
        back_populates="request",
        cascade="all, delete-orphan"
    )
    history: Mapped[List["ServiceRequestHistory"]] = relationship(
        "ServiceRequestHistory",
        back_populates="request",
        cascade="all, delete-orphan",
        order_by="ServiceRequestHistory.created_at.desc()"
    )

class ServiceDocument(TimeStampedBase):
    __tablename__ = "service_documents"

    request_id: Mapped[str] = mapped_column(String(36), ForeignKey("service_requests.id", ondelete="CASCADE"), index=True, nullable=False)
    document_title: Mapped[str] = mapped_column(String(255), nullable=False)
    file_path: Mapped[str] = mapped_column(String(512), nullable=False)
    file_size_bytes: Mapped[int] = mapped_column(Integer, nullable=False)
    mime_type: Mapped[str] = mapped_column(String(128), nullable=False)

    request: Mapped["ServiceRequest"] = relationship("ServiceRequest", back_populates="documents")

class ServiceRequestHistory(TimeStampedBase):
    __tablename__ = "service_request_history"

    request_id: Mapped[str] = mapped_column(String(36), ForeignKey("service_requests.id", ondelete="CASCADE"), index=True, nullable=False)
    from_status: Mapped[str] = mapped_column(String(32), nullable=False)
    to_status: Mapped[str] = mapped_column(String(32), nullable=False)
    actor_id: Mapped[str] = mapped_column(String(36), ForeignKey("users.id", ondelete="SET NULL"), nullable=True)
    notes: Mapped[Optional[str]] = mapped_column(Text, nullable=True)

    request: Mapped["ServiceRequest"] = relationship("ServiceRequest", back_populates="history")
