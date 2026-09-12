"""
SmartCity360 - Emergency Services, Dispatch & Public Facilities
Critical public safety incident management, response squads, and municipal facility directory.
"""

from datetime import datetime
from typing import List, Optional
from sqlalchemy import String, Float, Text, ForeignKey, DateTime, Integer, Boolean
from sqlalchemy.orm import Mapped, mapped_column, relationship
from backend.app.core.database import TimeStampedBase

# Emergency Severities
EMERGENCY_SEV_LOW = "LOW"
EMERGENCY_SEV_MEDIUM = "MEDIUM"
EMERGENCY_SEV_HIGH = "HIGH"
EMERGENCY_SEV_CRITICAL = "CRITICAL"

# Emergency Lifecycle Statuses
EMERGENCY_STATUS_REPORTED = "REPORTED"
EMERGENCY_STATUS_VALIDATING = "VALIDATING"
EMERGENCY_STATUS_CONFIRMED = "CONFIRMED"
EMERGENCY_STATUS_DISPATCHED = "DISPATCHED"
EMERGENCY_STATUS_RESPONDING = "RESPONDING"
EMERGENCY_STATUS_CONTAINED = "CONTAINED"
EMERGENCY_STATUS_RESOLVED = "RESOLVED"
EMERGENCY_STATUS_CLOSED = "CLOSED"

class EmergencyIncident(TimeStampedBase):
    __tablename__ = "emergency_incidents"

    incident_number: Mapped[str] = mapped_column(String(32), unique=True, index=True, nullable=False)
    incident_type: Mapped[str] = mapped_column(String(64), index=True, nullable=False)  # FIRE, MEDICAL, ACCIDENT, FLOOD, HAZMAT
    severity: Mapped[str] = mapped_column(String(32), default=EMERGENCY_SEV_HIGH, index=True, nullable=False)
    status: Mapped[str] = mapped_column(String(32), default=EMERGENCY_STATUS_REPORTED, index=True, nullable=False)
    
    title: Mapped[str] = mapped_column(String(255), nullable=False)
    description: Mapped[str] = mapped_column(Text, nullable=False)
    
    # Location
    latitude: Mapped[float] = mapped_column(Float, nullable=False, index=True)
    longitude: Mapped[float] = mapped_column(Float, nullable=False, index=True)
    location_address: Mapped[str] = mapped_column(String(255), nullable=False)
    
    caller_name: Mapped[Optional[str]] = mapped_column(String(128), nullable=True)
    caller_phone: Mapped[Optional[str]] = mapped_column(String(32), nullable=True)
    
    dispatched_at: Mapped[Optional[datetime]] = mapped_column(DateTime(timezone=True), nullable=True)
    arrived_at: Mapped[Optional[datetime]] = mapped_column(DateTime(timezone=True), nullable=True)
    resolved_at: Mapped[Optional[datetime]] = mapped_column(DateTime(timezone=True), nullable=True)

    dispatches: Mapped[List["EmergencyDispatch"]] = relationship(
        "EmergencyDispatch",
        back_populates="incident",
        cascade="all, delete-orphan"
    )

class EmergencyResponseTeam(TimeStampedBase):
    __tablename__ = "emergency_response_teams"

    unit_identifier: Mapped[str] = mapped_column(String(64), unique=True, index=True, nullable=False)
    department_id: Mapped[str] = mapped_column(String(36), ForeignKey("departments.id", ondelete="RESTRICT"), nullable=False)
    service_type: Mapped[str] = mapped_column(String(64), nullable=False)  # FIRE, AMBULANCE, POLICE_PATROL, RESCUE
    base_station_name: Mapped[str] = mapped_column(String(128), nullable=False)
    is_available: Mapped[bool] = mapped_column(Boolean, default=True, index=True, nullable=False)
    active_crew_count: Mapped[int] = mapped_column(Integer, default=4, nullable=False)
    
    current_latitude: Mapped[Optional[float]] = mapped_column(Float, nullable=True)
    current_longitude: Mapped[Optional[float]] = mapped_column(Float, nullable=True)

    department: Mapped["Department"] = relationship("Department")

class EmergencyDispatch(TimeStampedBase):
    __tablename__ = "emergency_dispatches"

    incident_id: Mapped[str] = mapped_column(String(36), ForeignKey("emergency_incidents.id", ondelete="CASCADE"), index=True, nullable=False)
    team_id: Mapped[str] = mapped_column(String(36), ForeignKey("emergency_response_teams.id", ondelete="RESTRICT"), index=True, nullable=False)
    dispatched_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), nullable=False)
    arrival_time: Mapped[Optional[datetime]] = mapped_column(DateTime(timezone=True), nullable=True)
    departure_time: Mapped[Optional[datetime]] = mapped_column(DateTime(timezone=True), nullable=True)
    dispatch_notes: Mapped[Optional[str]] = mapped_column(Text, nullable=True)

    incident: Mapped["EmergencyIncident"] = relationship("EmergencyIncident", back_populates="dispatches")
    team: Mapped["EmergencyResponseTeam"] = relationship("EmergencyResponseTeam")

class Facility(TimeStampedBase):
    __tablename__ = "facilities"

    facility_code: Mapped[str] = mapped_column(String(32), unique=True, index=True, nullable=False)
    name: Mapped[str] = mapped_column(String(255), nullable=False)
    category: Mapped[str] = mapped_column(String(64), index=True, nullable=False)  # HOSPITAL, POLICE, FIRE_STATION, SCHOOL, LIBRARY, SHELTER
    address: Mapped[str] = mapped_column(String(255), nullable=False)
    latitude: Mapped[float] = mapped_column(Float, nullable=False, index=True)
    longitude: Mapped[float] = mapped_column(Float, nullable=False, index=True)
    contact_phone: Mapped[str] = mapped_column(String(32), nullable=False)
    operating_hours: Mapped[str] = mapped_column(String(64), default="24/7", nullable=False)
    is_operational: Mapped[bool] = mapped_column(Boolean, default=True, nullable=False)
    is_wheelchair_accessible: Mapped[bool] = mapped_column(Boolean, default=True, nullable=False)
