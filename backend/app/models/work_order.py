"""
SmartCity360 - Municipal Work Order Management Models
Tracks conversion of complaints/maintenance into field tasks, evidence verification,
and supervisor approval.
"""

from datetime import datetime
from typing import List, Optional
from sqlalchemy import String, Float, Text, ForeignKey, DateTime, Integer, Boolean
from sqlalchemy.orm import Mapped, mapped_column, relationship
from backend.app.core.database import TimeStampedBase

# Standard Work Order Statuses
WO_STATUS_CREATED = "CREATED"
WO_STATUS_ASSIGNED = "ASSIGNED"
WO_STATUS_ACCEPTED = "ACCEPTED"
WO_STATUS_IN_PROGRESS = "IN_PROGRESS"
WO_STATUS_BLOCKED = "BLOCKED"
WO_STATUS_SUBMITTED = "SUBMITTED"
WO_STATUS_VERIFICATION = "VERIFICATION"
WO_STATUS_COMPLETED = "COMPLETED"
WO_STATUS_CANCELLED = "CANCELLED"

ALL_WO_STATUSES = [
    WO_STATUS_CREATED,
    WO_STATUS_ASSIGNED,
    WO_STATUS_ACCEPTED,
    WO_STATUS_IN_PROGRESS,
    WO_STATUS_BLOCKED,
    WO_STATUS_SUBMITTED,
    WO_STATUS_VERIFICATION,
    WO_STATUS_COMPLETED,
    WO_STATUS_CANCELLED
]

class WorkOrder(TimeStampedBase):
    __tablename__ = "work_orders"

    order_number: Mapped[str] = mapped_column(String(32), unique=True, index=True, nullable=False)
    complaint_id: Mapped[Optional[str]] = mapped_column(String(36), ForeignKey("complaints.id", ondelete="SET NULL"), unique=True, nullable=True)
    department_id: Mapped[str] = mapped_column(String(36), ForeignKey("departments.id", ondelete="RESTRICT"), index=True, nullable=False)
    assigned_technician_id: Mapped[Optional[str]] = mapped_column(String(36), ForeignKey("department_staff.id", ondelete="SET NULL"), index=True, nullable=True)
    supervisor_id: Mapped[Optional[str]] = mapped_column(String(36), ForeignKey("department_staff.id", ondelete="SET NULL"), nullable=True)

    title: Mapped[str] = mapped_column(String(255), nullable=False)
    description: Mapped[str] = mapped_column(Text, nullable=False)
    priority: Mapped[str] = mapped_column(String(32), default="MEDIUM", nullable=False)
    status: Mapped[str] = mapped_column(String(32), default=WO_STATUS_CREATED, index=True, nullable=False)
    
    completion_percentage: Mapped[int] = mapped_column(Integer, default=0, nullable=False)
    field_notes: Mapped[Optional[str]] = mapped_column(Text, nullable=True)
    
    # Location
    latitude: Mapped[float] = mapped_column(Float, nullable=False)
    longitude: Mapped[float] = mapped_column(Float, nullable=False)
    location_address: Mapped[str] = mapped_column(String(255), nullable=False)
    
    due_date: Mapped[Optional[datetime]] = mapped_column(DateTime(timezone=True), nullable=True)
    completed_at: Mapped[Optional[datetime]] = mapped_column(DateTime(timezone=True), nullable=True)
    verified_at: Mapped[Optional[datetime]] = mapped_column(DateTime(timezone=True), nullable=True)

    # Relationships
    complaint: Mapped[Optional["Complaint"]] = relationship("Complaint", back_populates="work_order")
    department: Mapped["Department"] = relationship("Department")
    assigned_technician: Mapped[Optional["DepartmentStaff"]] = relationship("DepartmentStaff", foreign_keys=[assigned_technician_id])
    supervisor: Mapped[Optional["DepartmentStaff"]] = relationship("DepartmentStaff", foreign_keys=[supervisor_id])
    tasks: Mapped[List["WorkOrderTask"]] = relationship(
        "WorkOrderTask",
        back_populates="work_order",
        cascade="all, delete-orphan",
        order_by="WorkOrderTask.order_index.asc()"
    )
    evidence: Mapped[List["WorkOrderEvidence"]] = relationship(
        "WorkOrderEvidence",
        back_populates="work_order",
        cascade="all, delete-orphan"
    )

class WorkOrderTask(TimeStampedBase):
    __tablename__ = "work_order_tasks"

    work_order_id: Mapped[str] = mapped_column(String(36), ForeignKey("work_orders.id", ondelete="CASCADE"), index=True, nullable=False)
    title: Mapped[str] = mapped_column(String(255), nullable=False)
    is_completed: Mapped[bool] = mapped_column(Boolean, default=False, nullable=False)
    order_index: Mapped[int] = mapped_column(Integer, default=0, nullable=False)
    completed_at: Mapped[Optional[datetime]] = mapped_column(DateTime(timezone=True), nullable=True)

    work_order: Mapped["WorkOrder"] = relationship("WorkOrder", back_populates="tasks")

class WorkOrderEvidence(TimeStampedBase):
    __tablename__ = "work_order_evidence"

    work_order_id: Mapped[str] = mapped_column(String(36), ForeignKey("work_orders.id", ondelete="CASCADE"), index=True, nullable=False)
    evidence_type: Mapped[str] = mapped_column(String(32), default="PHOTO", nullable=False)  # BEFORE, AFTER, RECEIPT, PERMIT
    file_url: Mapped[str] = mapped_column(String(512), nullable=False)
    caption: Mapped[Optional[str]] = mapped_column(String(255), nullable=True)
    uploaded_by_staff_id: Mapped[Optional[str]] = mapped_column(String(36), ForeignKey("department_staff.id", ondelete="SET NULL"), nullable=True)

    work_order: Mapped["WorkOrder"] = relationship("WorkOrder", back_populates="evidence")
