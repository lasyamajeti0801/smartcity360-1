"""
SmartCity360 - Infrastructure, Utilities & Mobility Pydantic Schemas (Pydantic v2)
"""

from datetime import datetime
from typing import Optional, List
from pydantic import BaseModel, ConfigDict, Field

class AssetInspectionResponse(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: str
    asset_id: str
    inspection_date: datetime
    condition_found: str
    notes: str
    defects_observed: Optional[str] = None
    recommended_action: Optional[str] = None

class InfrastructureAssetResponse(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: str
    asset_tag: str
    name: str
    asset_type: str
    department_id: str
    latitude: float
    longitude: float
    location_description: str
    ward_number: Optional[int] = None
    condition_status: str
    health_score: int
    last_inspection_date: Optional[datetime] = None
    inspections: List[AssetInspectionResponse] = []

class InfrastructureAssetCreateRequest(BaseModel):
    name: str = Field(min_length=3, max_length=255)
    asset_type: str = Field(min_length=2, max_length=64)
    department_id: str
    latitude: float
    longitude: float
    location_description: str
    ward_number: Optional[int] = None
    condition_status: str = "GOOD"
    health_score: int = Field(default=100, ge=0, le=100)

class AssetInspectionCreateRequest(BaseModel):
    condition_found: str = Field(pattern="^(GOOD|FAIR|POOR|CRITICAL)$")
    notes: str = Field(min_length=3)
    defects_observed: Optional[str] = None
    recommended_action: Optional[str] = None
    health_score_adjustment: Optional[int] = Field(None, ge=0, le=100)

class StreetlightAssetResponse(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: str
    pole_number: str
    latitude: float
    longitude: float
    street_name: str
    luminaire_type: str
    wattage: int
    is_operational: bool
    last_bulb_replacement: Optional[datetime] = None

class StreetlightStatusUpdateRequest(BaseModel):
    is_operational: bool
    replace_bulb: bool = False

class WaterAssetResponse(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: str
    facility_code: str
    facility_type: str
    latitude: float
    longitude: float
    current_supply_status: str
    capacity_liters: Optional[float] = None
    pipe_diameter_mm: Optional[int] = None

class WasteZoneResponse(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: str
    zone_code: str
    name: str
    collection_frequency: str
    daily_tonnage_capacity: float

class WasteCollectionCreateRequest(BaseModel):
    zone_id: str
    waste_type: str = Field(pattern="^(BULK|HAZARDOUS|E_WASTE|GREEN_WASTE)$")
    preferred_date: datetime
    pickup_address: str = Field(min_length=3, max_length=255)
    notes: Optional[str] = None

class WasteCollectionResponse(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: str
    request_number: str
    citizen_id: str
    zone_id: str
    waste_type: str
    status: str
    preferred_date: datetime
    pickup_address: str
    notes: Optional[str] = None
    created_at: datetime

class TrafficIncidentResponse(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: str
    incident_code: str
    incident_type: str
    severity: str
    status: str
    latitude: float
    longitude: float
    location_name: str
    description: str
    lane_blockage: str

class ParkingLocationResponse(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: str
    name: str
    zone_code: str
    latitude: float
    longitude: float
    total_capacity: int
    occupied_spaces: int
    hourly_rate: float
    is_ev_charging_available: bool
