"""
SmartCity360 - Civic Complaint Management Models
Standard 9-stage complaint lifecycle with GPS coordinates, SLA deadlines,
evidence tracking, and status audit trail.
"""

from datetime import datetime
from typing import List, Optional
from sqlalchemy import String, Float, Text, ForeignKey, DateTime, Integer, Boolean, Index
from sqlalchemy.orm import Mapped, mapped_column, relationship
from backend.app.core.database import TimeStampedBase

# Standard Complaint Statuses
STATUS_NEW = "NEW"
STATUS_UNDER_REVIEW = "UNDER_REVIEW"
STATUS_ASSIGNED = "ASSIGNED"
STATUS_IN_PROGRESS = "IN_PROGRESS"
STATUS_ON_HOLD = "ON_HOLD"
STATUS_RESOLVED = "RESOLVED"
STATUS_CLOSED = "CLOSED"
STATUS_REOPENED = "REOPENED"
STATUS_REJECTED = "REJECTED"

ALL_COMPLAINT_STATUSES = [
    STATUS_NEW,
    STATUS_UNDER_REVIEW,
    STATUS_ASSIGNED,
    STATUS_IN_PROGRESS,
    STATUS_ON_HOLD,
    STATUS_RESOLVED,
    STATUS_CLOSED,
    STATUS_REOPENED,
    STATUS_REJECTED
]

# Priorities
PRIORITY_LOW = "LOW"
PRIORITY_MEDIUM = "MEDIUM"
PRIORITY_HIGH = "HIGH"
PRIORITY_CRITICAL = "CRITICAL"

class ComplaintCategory(TimeStampedBase):
    __tablename__ = "complaint_categories"

    code: Mapped[str] = mapped_column(String(64), unique=True, index=True, nullable=False)
    name: Mapped[str] = mapped_column(String(128), nullable=False)
    default_department_code: Mapped[str] = mapped_column(String(32), nullable=False)
    default_sla_hours: Mapped[int] = mapped_column(Integer, default=48, nullable=False)
    icon_name: Mapped[str] = mapped_column(String(64), default="AlertCircle", nullable=False)
    description: Mapped[Optional[str]] = mapped_column(Text, nullable=True)

    complaints: Mapped[List["Complaint"]] = relationship("Complaint", back_populates="category")

class Complaint(TimeStampedBase):
    __tablename__ = "complaints"

    ticket_number: Mapped[str] = mapped_column(String(32), unique=True, index=True, nullable=False)
    citizen_id: Mapped[str] = mapped_column(String(36), ForeignKey("users.id", ondelete="CASCADE"), index=True, nullable=False)
    category_id: Mapped[str] = mapped_column(String(36), ForeignKey("complaint_categories.id", ondelete="RESTRICT"), index=True, nullable=False)
    department_id: Mapped[str] = mapped_column(String(36), ForeignKey("departments.id", ondelete="RESTRICT"), index=True, nullable=False)
    assigned_staff_id: Mapped[Optional[str]] = mapped_column(String(36), ForeignKey("department_staff.id", ondelete="SET NULL"), index=True, nullable=True)

    title: Mapped[str] = mapped_column(String(255), nullable=False)
    description: Mapped[str] = mapped_column(Text, nullable=False)
    priority: Mapped[str] = mapped_column(String(32), default=PRIORITY_MEDIUM, index=True, nullable=False)
    status: Mapped[str] = mapped_column(String(32), default=STATUS_NEW, index=True, nullable=False)

    # Geospatial location coordinates
    latitude: Mapped[float] = mapped_column(Float, nullable=False, index=True)
    longitude: Mapped[float] = mapped_column(Float, nullable=False, index=True)
    location_address: Mapped[str] = mapped_column(String(255), nullable=False)
    ward_number: Mapped[Optional[int]] = mapped_column(Integer, index=True, nullable=True)

    # SLA & Escalation
    sla_due_at: Mapped[Optional[datetime]] = mapped_column(DateTime(timezone=True), index=True, nullable=True)
    is_escalated: Mapped[bool] = mapped_column(Boolean, default=False, index=True, nullable=False)
    escalated_at: Mapped[Optional[datetime]] = mapped_column(DateTime(timezone=True), nullable=True)
    resolved_at: Mapped[Optional[datetime]] = mapped_column(DateTime(timezone=True), nullable=True)
    citizen_rating: Mapped[Optional[int]] = mapped_column(Integer, nullable=True)
    citizen_feedback: Mapped[Optional[str]] = mapped_column(Text, nullable=True)

    # Uploaded image/evidence reference
    evidence_image_url: Mapped[Optional[str]] = mapped_column(String(512), nullable=True)
    resolution_image_url: Mapped[Optional[str]] = mapped_column(String(512), nullable=True)

    # Relationships
    citizen: Mapped["User"] = relationship("User", lazy="selectin")
    category: Mapped["ComplaintCategory"] = relationship("ComplaintCategory", back_populates="complaints", lazy="selectin")
    department: Mapped["Department"] = relationship("Department", back_populates="complaints", lazy="selectin")
    assigned_staff: Mapped[Optional["DepartmentStaff"]] = relationship("DepartmentStaff", lazy="selectin")
    comments: Mapped[List["ComplaintComment"]] = relationship(
        "ComplaintComment",
        back_populates="complaint",
        cascade="all, delete-orphan",
        lazy="selectin",
        order_by="ComplaintComment.created_at.asc()"
    )
    status_history: Mapped[List["ComplaintStatusHistory"]] = relationship(
        "ComplaintStatusHistory",
        back_populates="complaint",
        cascade="all, delete-orphan",
        lazy="selectin",
        order_by="ComplaintStatusHistory.created_at.asc()"
    )
    work_order: Mapped[Optional["WorkOrder"]] = relationship(
        "WorkOrder",
        back_populates="complaint",
        uselist=False
    )

class ComplaintComment(TimeStampedBase):
    __tablename__ = "complaint_comments"

    complaint_id: Mapped[str] = mapped_column(String(36), ForeignKey("complaints.id", ondelete="CASCADE"), index=True, nullable=False)
    author_id: Mapped[str] = mapped_column(String(36), ForeignKey("users.id", ondelete="SET NULL"), nullable=True)
    comment: Mapped[str] = mapped_column(Text, nullable=False)
    is_internal: Mapped[bool] = mapped_column(Boolean, default=False, nullable=False)

    complaint: Mapped["Complaint"] = relationship("Complaint", back_populates="comments")
    author: Mapped[Optional["User"]] = relationship("User")

class ComplaintStatusHistory(TimeStampedBase):
    __tablename__ = "complaint_status_history"

    complaint_id: Mapped[str] = mapped_column(String(36), ForeignKey("complaints.id", ondelete="CASCADE"), index=True, nullable=False)
    from_status: Mapped[str] = mapped_column(String(32), nullable=False)
    to_status: Mapped[str] = mapped_column(String(32), nullable=False)
    changed_by_user_id: Mapped[Optional[str]] = mapped_column(String(36), ForeignKey("users.id", ondelete="SET NULL"), nullable=True)
    reason: Mapped[Optional[str]] = mapped_column(Text, nullable=True)

    complaint: Mapped["Complaint"] = relationship("Complaint", back_populates="status_history")
