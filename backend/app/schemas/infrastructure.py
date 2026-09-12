"""
SmartCity360 - Infrastructure, Utilities & Mobility Pydantic Schemas (Pydantic v2)
"""

from typing import Optional
from pydantic import BaseModel, ConfigDict

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

class WaterAssetResponse(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: str
    facility_code: str
    facility_type: str
    latitude: float
    longitude: float
    current_supply_status: str

class WasteZoneResponse(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: str
    zone_code: str
    name: str
    collection_frequency: str
    daily_tonnage_capacity: float

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
