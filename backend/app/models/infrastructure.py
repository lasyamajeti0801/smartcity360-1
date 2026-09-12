"""
SmartCity360 - Urban Infrastructure, Streetlights, Water & Waste Models
Asset tracking, condition health scoring (GOOD, FAIR, POOR, CRITICAL),
inspections, utility nodes, and sanitation sectors.
"""

from datetime import datetime
from typing import List, Optional
from sqlalchemy import String, Float, Text, ForeignKey, DateTime, Integer, Boolean, Numeric
from sqlalchemy.orm import Mapped, mapped_column, relationship
from backend.app.core.database import TimeStampedBase

# Asset Conditions
CONDITION_GOOD = "GOOD"
CONDITION_FAIR = "FAIR"
CONDITION_POOR = "POOR"
CONDITION_CRITICAL = "CRITICAL"

class InfrastructureAsset(TimeStampedBase):
    __tablename__ = "infrastructure_assets"

    asset_tag: Mapped[str] = mapped_column(String(64), unique=True, index=True, nullable=False)
    name: Mapped[str] = mapped_column(String(255), nullable=False)
    asset_type: Mapped[str] = mapped_column(String(64), index=True, nullable=False)  # ROAD, BRIDGE, WATER_PIPE, DRAIN, BUILDING
    department_id: Mapped[str] = mapped_column(String(36), ForeignKey("departments.id", ondelete="RESTRICT"), index=True, nullable=False)

    latitude: Mapped[float] = mapped_column(Float, nullable=False, index=True)
    longitude: Mapped[float] = mapped_column(Float, nullable=False, index=True)
    location_description: Mapped[str] = mapped_column(String(255), nullable=False)
    ward_number: Mapped[Optional[int]] = mapped_column(Integer, index=True, nullable=True)

    condition_status: Mapped[str] = mapped_column(String(32), default=CONDITION_GOOD, index=True, nullable=False)
    installation_date: Mapped[Optional[datetime]] = mapped_column(DateTime(timezone=True), nullable=True)
    last_inspection_date: Mapped[Optional[datetime]] = mapped_column(DateTime(timezone=True), nullable=True)
    health_score: Mapped[int] = mapped_column(Integer, default=100, nullable=False)  # 0 to 100

    department: Mapped["Department"] = relationship("Department")
    inspections: Mapped[List["AssetInspection"]] = relationship("AssetInspection", back_populates="asset", cascade="all, delete-orphan")
    maintenance_records: Mapped[List["AssetMaintenance"]] = relationship("AssetMaintenance", back_populates="asset", cascade="all, delete-orphan")

class AssetInspection(TimeStampedBase):
    __tablename__ = "asset_inspections"

    asset_id: Mapped[str] = mapped_column(String(36), ForeignKey("infrastructure_assets.id", ondelete="CASCADE"), index=True, nullable=False)
    inspector_id: Mapped[Optional[str]] = mapped_column(String(36), ForeignKey("department_staff.id", ondelete="SET NULL"), nullable=True)
    inspection_date: Mapped[datetime] = mapped_column(DateTime(timezone=True), nullable=False)
    condition_found: Mapped[str] = mapped_column(String(32), nullable=False)
    notes: Mapped[str] = mapped_column(Text, nullable=False)
    defects_observed: Mapped[Optional[str]] = mapped_column(Text, nullable=True)
    recommended_action: Mapped[Optional[str]] = mapped_column(String(255), nullable=True)

    asset: Mapped["InfrastructureAsset"] = relationship("InfrastructureAsset", back_populates="inspections")
    inspector: Mapped[Optional["DepartmentStaff"]] = relationship("DepartmentStaff")

class AssetMaintenance(TimeStampedBase):
    __tablename__ = "asset_maintenance"

    asset_id: Mapped[str] = mapped_column(String(36), ForeignKey("infrastructure_assets.id", ondelete="CASCADE"), index=True, nullable=False)
    maintenance_type: Mapped[str] = mapped_column(String(64), nullable=False)  # PREVENTIVE, CORRECTIVE, EMERGENCY
    scheduled_date: Mapped[datetime] = mapped_column(DateTime(timezone=True), nullable=False)
    completed_date: Mapped[Optional[datetime]] = mapped_column(DateTime(timezone=True), nullable=True)
    cost: Mapped[float] = mapped_column(Numeric(10, 2), default=0.00, nullable=False)
    description: Mapped[str] = mapped_column(Text, nullable=False)
    is_completed: Mapped[bool] = mapped_column(Boolean, default=False, nullable=False)

    asset: Mapped["InfrastructureAsset"] = relationship("InfrastructureAsset", back_populates="maintenance_records")

class StreetlightAsset(TimeStampedBase):
    __tablename__ = "streetlight_assets"

    pole_number: Mapped[str] = mapped_column(String(64), unique=True, index=True, nullable=False)
    latitude: Mapped[float] = mapped_column(Float, nullable=False, index=True)
    longitude: Mapped[float] = mapped_column(Float, nullable=False, index=True)
    street_name: Mapped[str] = mapped_column(String(255), nullable=False)
    luminaire_type: Mapped[str] = mapped_column(String(64), default="LED", nullable=False)
    wattage: Mapped[int] = mapped_column(Integer, default=60, nullable=False)
    is_operational: Mapped[bool] = mapped_column(Boolean, default=True, index=True, nullable=False)
    last_bulb_replacement: Mapped[Optional[datetime]] = mapped_column(DateTime(timezone=True), nullable=True)
    smart_controller_id: Mapped[Optional[str]] = mapped_column(String(64), nullable=True)

class WaterAsset(TimeStampedBase):
    __tablename__ = "water_assets"

    facility_code: Mapped[str] = mapped_column(String(64), unique=True, index=True, nullable=False)
    facility_type: Mapped[str] = mapped_column(String(64), nullable=False)  # RESERVOIR, TREATMENT_PLANT, PIPELINE_MAIN, VALVE
    latitude: Mapped[float] = mapped_column(Float, nullable=False)
    longitude: Mapped[float] = mapped_column(Float, nullable=False)
    capacity_liters: Mapped[Optional[float]] = mapped_column(Float, nullable=True)
    current_supply_status: Mapped[str] = mapped_column(String(32), default="NORMAL", nullable=False)  # NORMAL, LOW_PRESSURE, INTERRUPTED
    pipe_diameter_mm: Mapped[Optional[int]] = mapped_column(Integer, nullable=True)
    last_quality_test: Mapped[Optional[datetime]] = mapped_column(DateTime(timezone=True), nullable=True)

class WasteZone(TimeStampedBase):
    __tablename__ = "waste_zones"

    zone_code: Mapped[str] = mapped_column(String(32), unique=True, index=True, nullable=False)
    name: Mapped[str] = mapped_column(String(128), nullable=False)
    collection_frequency: Mapped[str] = mapped_column(String(64), default="DAILY", nullable=False)
    assigned_crew_leader: Mapped[Optional[str]] = mapped_column(String(128), nullable=True)
    daily_tonnage_capacity: Mapped[float] = mapped_column(Float, default=10.0, nullable=False)

class WasteCollectionRequest(TimeStampedBase):
    __tablename__ = "waste_collection_requests"

    request_number: Mapped[str] = mapped_column(String(32), unique=True, index=True, nullable=False)
    citizen_id: Mapped[str] = mapped_column(String(36), ForeignKey("users.id", ondelete="CASCADE"), index=True, nullable=False)
    zone_id: Mapped[str] = mapped_column(String(36), ForeignKey("waste_zones.id", ondelete="RESTRICT"), index=True, nullable=False)
    waste_type: Mapped[str] = mapped_column(String(64), nullable=False)  # BULK, HAZARDOUS, E_WASTE, GREEN_WASTE
    status: Mapped[str] = mapped_column(String(32), default="PENDING", index=True, nullable=False)
    preferred_date: Mapped[datetime] = mapped_column(DateTime(timezone=True), nullable=False)
    pickup_address: Mapped[str] = mapped_column(String(255), nullable=False)
    notes: Mapped[Optional[str]] = mapped_column(Text, nullable=True)

    citizen: Mapped["User"] = relationship("User")
    zone: Mapped["WasteZone"] = relationship("WasteZone")
