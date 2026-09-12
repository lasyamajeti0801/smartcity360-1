"""
SmartCity360 - Municipal Departments & Service Catalog Models
Covers Departments, Service Categories, and Public Civic Services.
"""

from typing import List, Optional
from sqlalchemy import String, Boolean, ForeignKey, Text, Integer, Numeric
from sqlalchemy.orm import Mapped, mapped_column, relationship
from backend.app.core.database import TimeStampedBase

class Department(TimeStampedBase):
    __tablename__ = "departments"

    code: Mapped[str] = mapped_column(String(32), unique=True, index=True, nullable=False)
    name: Mapped[str] = mapped_column(String(128), unique=True, nullable=False)
    description: Mapped[str] = mapped_column(Text, nullable=False)
    contact_email: Mapped[str] = mapped_column(String(255), nullable=False)
    contact_phone: Mapped[str] = mapped_column(String(32), nullable=False)
    head_official: Mapped[Optional[str]] = mapped_column(String(128), nullable=True)
    is_active: Mapped[bool] = mapped_column(Boolean, default=True, nullable=False)

    # Relationships
    staff_members: Mapped[List["DepartmentStaff"]] = relationship(
        "DepartmentStaff",
        back_populates="department"
    )
    services: Mapped[List["MunicipalService"]] = relationship(
        "MunicipalService",
        back_populates="department"
    )
    complaints: Mapped[List["Complaint"]] = relationship(
        "Complaint",
        back_populates="department"
    )

class ServiceCategory(TimeStampedBase):
    __tablename__ = "service_categories"

    code: Mapped[str] = mapped_column(String(64), unique=True, index=True, nullable=False)
    name: Mapped[str] = mapped_column(String(128), nullable=False)
    description: Mapped[Optional[str]] = mapped_column(Text, nullable=True)
    icon_name: Mapped[str] = mapped_column(String(64), default="Layers", nullable=False)
    display_order: Mapped[int] = mapped_column(Integer, default=0, nullable=False)

    services: Mapped[List["MunicipalService"]] = relationship(
        "MunicipalService",
        back_populates="category"
    )

class MunicipalService(TimeStampedBase):
    __tablename__ = "municipal_services"

    department_id: Mapped[str] = mapped_column(String(36), ForeignKey("departments.id", ondelete="RESTRICT"), index=True, nullable=False)
    category_id: Mapped[str] = mapped_column(String(36), ForeignKey("service_categories.id", ondelete="RESTRICT"), index=True, nullable=False)
    code: Mapped[str] = mapped_column(String(64), unique=True, index=True, nullable=False)
    title: Mapped[str] = mapped_column(String(255), nullable=False)
    description: Mapped[str] = mapped_column(Text, nullable=False)
    eligibility_criteria: Mapped[str] = mapped_column(Text, nullable=False)
    fee_amount: Mapped[float] = mapped_column(Numeric(10, 2), default=0.00, nullable=False)
    sla_turnaround_days: Mapped[int] = mapped_column(Integer, default=7, nullable=False)
    required_documents: Mapped[str] = mapped_column(Text, default="", nullable=False)  # JSON or comma-separated
    is_online_submission: Mapped[bool] = mapped_column(Boolean, default=True, nullable=False)
    is_active: Mapped[bool] = mapped_column(Boolean, default=True, nullable=False)

    department: Mapped["Department"] = relationship("Department", back_populates="services")
    category: Mapped["ServiceCategory"] = relationship("ServiceCategory", back_populates="services")
    requests: Mapped[List["ServiceRequest"]] = relationship("ServiceRequest", back_populates="service")
