"""
SmartCity360 - Urban Mobility, Transit & Parking Models
Covers Traffic Incidents, Bus Transit Lines & Stops, and Municipal Parking Sessions.
"""

from datetime import datetime
from typing import List, Optional
from sqlalchemy import String, Float, Text, ForeignKey, DateTime, Integer, Boolean, Numeric
from sqlalchemy.orm import Mapped, mapped_column, relationship
from backend.app.core.database import TimeStampedBase

class TrafficIncident(TimeStampedBase):
    __tablename__ = "traffic_incidents"

    incident_code: Mapped[str] = mapped_column(String(32), unique=True, index=True, nullable=False)
    incident_type: Mapped[str] = mapped_column(String(64), nullable=False)  # CONGESTION, ACCIDENT, ROAD_WORK, SIGNAL_FAILURE
    severity: Mapped[str] = mapped_column(String(32), default="MEDIUM", nullable=False)
    status: Mapped[str] = mapped_column(String(32), default="ACTIVE", index=True, nullable=False)  # ACTIVE, CLEARING, RESOLVED
    
    latitude: Mapped[float] = mapped_column(Float, nullable=False, index=True)
    longitude: Mapped[float] = mapped_column(Float, nullable=False, index=True)
    location_name: Mapped[str] = mapped_column(String(255), nullable=False)
    
    description: Mapped[str] = mapped_column(Text, nullable=False)
    lane_blockage: Mapped[str] = mapped_column(String(64), default="NONE", nullable=False)
    estimated_cleared_at: Mapped[Optional[datetime]] = mapped_column(DateTime(timezone=True), nullable=True)

class TransportRoute(TimeStampedBase):
    __tablename__ = "transport_routes"

    route_number: Mapped[str] = mapped_column(String(32), unique=True, index=True, nullable=False)
    name: Mapped[str] = mapped_column(String(128), nullable=False)
    origin: Mapped[str] = mapped_column(String(128), nullable=False)
    destination: Mapped[str] = mapped_column(String(128), nullable=False)
    frequency_minutes: Mapped[int] = mapped_column(Integer, default=15, nullable=False)
    operating_hours: Mapped[str] = mapped_column(String(64), default="06:00 - 23:00", nullable=False)
    is_active: Mapped[bool] = mapped_column(Boolean, default=True, nullable=False)

    stops: Mapped[List["TransportStop"]] = relationship(
        "TransportStop",
        back_populates="route",
        cascade="all, delete-orphan",
        order_by="TransportStop.stop_sequence.asc()"
    )

class TransportStop(TimeStampedBase):
    __tablename__ = "transport_stops"

    route_id: Mapped[str] = mapped_column(String(36), ForeignKey("transport_routes.id", ondelete="CASCADE"), index=True, nullable=False)
    name: Mapped[str] = mapped_column(String(128), nullable=False)
    stop_sequence: Mapped[int] = mapped_column(Integer, nullable=False)
    latitude: Mapped[float] = mapped_column(Float, nullable=False)
    longitude: Mapped[float] = mapped_column(Float, nullable=False)
    has_shelter: Mapped[bool] = mapped_column(Boolean, default=True, nullable=False)
    is_accessible: Mapped[bool] = mapped_column(Boolean, default=True, nullable=False)

    route: Mapped["TransportRoute"] = relationship("TransportRoute", back_populates="stops")

class ParkingLocation(TimeStampedBase):
    __tablename__ = "parking_locations"

    name: Mapped[str] = mapped_column(String(128), unique=True, nullable=False)
    zone_code: Mapped[str] = mapped_column(String(32), index=True, nullable=False)
    latitude: Mapped[float] = mapped_column(Float, nullable=False, index=True)
    longitude: Mapped[float] = mapped_column(Float, nullable=False, index=True)
    total_capacity: Mapped[int] = mapped_column(Integer, nullable=False)
    occupied_spaces: Mapped[int] = mapped_column(Integer, default=0, nullable=False)
    hourly_rate: Mapped[float] = mapped_column(Numeric(6, 2), default=2.00, nullable=False)
    is_ev_charging_available: Mapped[bool] = mapped_column(Boolean, default=False, nullable=False)

    sessions: Mapped[List["ParkingSession"]] = relationship("ParkingSession", back_populates="parking_lot")

class ParkingSession(TimeStampedBase):
    __tablename__ = "parking_sessions"

    parking_lot_id: Mapped[str] = mapped_column(String(36), ForeignKey("parking_locations.id", ondelete="RESTRICT"), index=True, nullable=False)
    user_id: Mapped[str] = mapped_column(String(36), ForeignKey("users.id", ondelete="CASCADE"), index=True, nullable=False)
    vehicle_plate: Mapped[str] = mapped_column(String(32), index=True, nullable=False)
    started_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), nullable=False)
    ended_at: Mapped[Optional[datetime]] = mapped_column(DateTime(timezone=True), nullable=True)
    total_fee: Mapped[Optional[float]] = mapped_column(Numeric(8, 2), nullable=True)
    payment_status: Mapped[str] = mapped_column(String(32), default="PENDING", nullable=False)  # PENDING, PAID, OVERDUE

    parking_lot: Mapped["ParkingLocation"] = relationship("ParkingLocation", back_populates="sessions")
    user: Mapped["User"] = relationship("User")
