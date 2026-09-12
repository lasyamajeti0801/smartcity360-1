"""
SmartCity360 - Emergency Services & Facility Pydantic Schemas (Pydantic v2)
"""

from datetime import datetime
from typing import List, Optional
from pydantic import BaseModel, ConfigDict, Field

class EmergencyDispatchResponse(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: str
    team_id: str
    dispatched_at: datetime
    arrival_time: Optional[datetime] = None
    departure_time: Optional[datetime] = None
    dispatch_notes: Optional[str] = None

class EmergencyIncidentResponse(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: str
    incident_number: str
    incident_type: str
    severity: str
    status: str
    title: str
    description: str
    latitude: float
    longitude: float
    location_address: str
    caller_name: Optional[str] = None
    caller_phone: Optional[str] = None
    dispatched_at: Optional[datetime] = None
    arrived_at: Optional[datetime] = None
    resolved_at: Optional[datetime] = None
    created_at: datetime
    dispatches: List[EmergencyDispatchResponse] = []

class EmergencyIncidentCreateRequest(BaseModel):
    incident_type: str = Field(min_length=2, max_length=64)
    severity: str = "HIGH"
    title: str = Field(min_length=3, max_length=255)
    description: str
    latitude: float
    longitude: float
    location_address: str
    caller_name: Optional[str] = None
    caller_phone: Optional[str] = None

class EmergencyResponseTeamResponse(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: str
    unit_identifier: str
    department_id: str
    service_type: str
    base_station_name: str
    is_available: bool
    active_crew_count: int
    current_latitude: Optional[float] = None
    current_longitude: Optional[float] = None

class FacilityResponse(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: str
    facility_code: str
    name: str
    category: str
    address: str
    latitude: float
    longitude: float
    contact_phone: str
    operating_hours: str
    is_operational: bool
    is_wheelchair_accessible: bool

class EmergencyDispatchCreateRequest(BaseModel):
    team_id: str
    dispatch_notes: Optional[str] = None

class EmergencyResolveRequest(BaseModel):
    notes: Optional[str] = None

