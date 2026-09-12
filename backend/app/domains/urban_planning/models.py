"""
SmartCity360 - Urban Planning & Zoning Regulation Models
Domain Module: urban_planning
Planning and land use regulation, FAR calculations, zoning amendments.
"""

from datetime import datetime, timezone, date
from enum import Enum
from typing import List, Dict, Optional, Any, Union
from pydantic import BaseModel, Field, ConfigDict, field_validator

class UrbanPlanningStatus(str, Enum):
    DRAFT = 'draft'
    SUBMITTED = 'submitted'
    PENDING_REVIEW = 'pending_review'
    IN_PROGRESS = 'in_progress'
    APPROVED = 'approved'
    REJECTED = 'rejected'
    ACTIVE = 'active'
    MAINTENANCE = 'maintenance'
    FLAGGED = 'flagged'
    ARCHIVED = 'archived'
    ESCALATED = 'escalated'
    COMPLETED = 'completed'


class UrbanPlanningPriority(str, Enum):
    LOW = 'low'
    STANDARD = 'standard'
    URGENT = 'urgent'
    CRITICAL = 'critical'
    EMERGENCY_TIER_1 = 'emergency_tier_1'
    EMERGENCY_TIER_2 = 'emergency_tier_2'


class UrbanPlanningEntity01(BaseModel):
    """Operational domain entity 1 for Urban Planning & Zoning Regulation."""
    model_config = ConfigDict(from_attributes=True, extra='ignore')

    entity_id: str = Field(..., description='Unique identifier for UrbanPlanningEntity01')
    reference_code: str = Field(..., description='Official municipal reference code')
    status: UrbanPlanningStatus = Field(default=UrbanPlanningStatus.ACTIVE)
    priority: UrbanPlanningPriority = Field(default=UrbanPlanningPriority.STANDARD)
    ward_id: int = Field(default=1, ge=1, le=150, description='Municipal jurisdictional ward number')
    zone_code: str = Field(default='ZONE-CENTRAL', description='Municipal operational zone code')
    latitude: float = Field(default=17.385044, ge=-90.0, le=90.0)
    longitude: float = Field(default=78.486671, ge=-180.0, le=180.0)
    altitude_meters: Optional[float] = Field(default=542.0)
    primary_metric_value: float = Field(default=100.0, description='Domain standard quantitative measurement')
    secondary_metric_value: float = Field(default=45.5, description='Secondary operational metric')
    threshold_limit: float = Field(default=150.0, description='Configured statutory threshold')
    safety_margin_percentage: float = Field(default=15.0)
    is_compliant: bool = Field(default=True)
    supervisor_notes: Optional[str] = Field(default=None)
    assigned_officer_id: Optional[str] = Field(default=None)
    tags: List[str] = Field(default_factory=lambda: ['civic', 'smart-city', 'telemetry'])
    metadata_payload: Dict[str, Any] = Field(default_factory=dict)
    created_at: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))
    updated_at: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))

    @field_validator('primary_metric_value')
    @classmethod
    def validate_metric(cls, v: float) -> float:
        if v < 0:
            raise ValueError('Metric value cannot be negative in municipal calculations')
        return round(v, 4)

    def calculate_utilization_ratio(self) -> float:
        if self.threshold_limit <= 0:
            return 0.0
        return round((self.primary_metric_value / self.threshold_limit) * 100, 2)

    def is_critical_alert(self) -> bool:
        return self.calculate_utilization_ratio() > (100.0 - self.safety_margin_percentage)

class UrbanPlanningEntity02(BaseModel):
    """Operational domain entity 2 for Urban Planning & Zoning Regulation."""
    model_config = ConfigDict(from_attributes=True, extra='ignore')

    entity_id: str = Field(..., description='Unique identifier for UrbanPlanningEntity02')
    reference_code: str = Field(..., description='Official municipal reference code')
    status: UrbanPlanningStatus = Field(default=UrbanPlanningStatus.ACTIVE)
    priority: UrbanPlanningPriority = Field(default=UrbanPlanningPriority.STANDARD)
    ward_id: int = Field(default=1, ge=1, le=150, description='Municipal jurisdictional ward number')
    zone_code: str = Field(default='ZONE-CENTRAL', description='Municipal operational zone code')
    latitude: float = Field(default=17.385044, ge=-90.0, le=90.0)
    longitude: float = Field(default=78.486671, ge=-180.0, le=180.0)
    altitude_meters: Optional[float] = Field(default=542.0)
    primary_metric_value: float = Field(default=100.0, description='Domain standard quantitative measurement')
    secondary_metric_value: float = Field(default=45.5, description='Secondary operational metric')
    threshold_limit: float = Field(default=150.0, description='Configured statutory threshold')
    safety_margin_percentage: float = Field(default=15.0)
    is_compliant: bool = Field(default=True)
    supervisor_notes: Optional[str] = Field(default=None)
    assigned_officer_id: Optional[str] = Field(default=None)
    tags: List[str] = Field(default_factory=lambda: ['civic', 'smart-city', 'telemetry'])
    metadata_payload: Dict[str, Any] = Field(default_factory=dict)
    created_at: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))
    updated_at: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))

    @field_validator('primary_metric_value')
    @classmethod
    def validate_metric(cls, v: float) -> float:
        if v < 0:
            raise ValueError('Metric value cannot be negative in municipal calculations')
        return round(v, 4)

    def calculate_utilization_ratio(self) -> float:
        if self.threshold_limit <= 0:
            return 0.0
        return round((self.primary_metric_value / self.threshold_limit) * 100, 2)

    def is_critical_alert(self) -> bool:
        return self.calculate_utilization_ratio() > (100.0 - self.safety_margin_percentage)

class UrbanPlanningEntity03(BaseModel):
    """Operational domain entity 3 for Urban Planning & Zoning Regulation."""
    model_config = ConfigDict(from_attributes=True, extra='ignore')

    entity_id: str = Field(..., description='Unique identifier for UrbanPlanningEntity03')
    reference_code: str = Field(..., description='Official municipal reference code')
    status: UrbanPlanningStatus = Field(default=UrbanPlanningStatus.ACTIVE)
    priority: UrbanPlanningPriority = Field(default=UrbanPlanningPriority.STANDARD)
    ward_id: int = Field(default=1, ge=1, le=150, description='Municipal jurisdictional ward number')
    zone_code: str = Field(default='ZONE-CENTRAL', description='Municipal operational zone code')
    latitude: float = Field(default=17.385044, ge=-90.0, le=90.0)
    longitude: float = Field(default=78.486671, ge=-180.0, le=180.0)
    altitude_meters: Optional[float] = Field(default=542.0)
    primary_metric_value: float = Field(default=100.0, description='Domain standard quantitative measurement')
    secondary_metric_value: float = Field(default=45.5, description='Secondary operational metric')
    threshold_limit: float = Field(default=150.0, description='Configured statutory threshold')
    safety_margin_percentage: float = Field(default=15.0)
    is_compliant: bool = Field(default=True)
    supervisor_notes: Optional[str] = Field(default=None)
    assigned_officer_id: Optional[str] = Field(default=None)
    tags: List[str] = Field(default_factory=lambda: ['civic', 'smart-city', 'telemetry'])
    metadata_payload: Dict[str, Any] = Field(default_factory=dict)
    created_at: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))
    updated_at: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))

    @field_validator('primary_metric_value')
    @classmethod
    def validate_metric(cls, v: float) -> float:
        if v < 0:
            raise ValueError('Metric value cannot be negative in municipal calculations')
        return round(v, 4)

    def calculate_utilization_ratio(self) -> float:
        if self.threshold_limit <= 0:
            return 0.0
        return round((self.primary_metric_value / self.threshold_limit) * 100, 2)

    def is_critical_alert(self) -> bool:
        return self.calculate_utilization_ratio() > (100.0 - self.safety_margin_percentage)

class UrbanPlanningEntity04(BaseModel):
    """Operational domain entity 4 for Urban Planning & Zoning Regulation."""
    model_config = ConfigDict(from_attributes=True, extra='ignore')

    entity_id: str = Field(..., description='Unique identifier for UrbanPlanningEntity04')
    reference_code: str = Field(..., description='Official municipal reference code')
    status: UrbanPlanningStatus = Field(default=UrbanPlanningStatus.ACTIVE)
    priority: UrbanPlanningPriority = Field(default=UrbanPlanningPriority.STANDARD)
    ward_id: int = Field(default=1, ge=1, le=150, description='Municipal jurisdictional ward number')
    zone_code: str = Field(default='ZONE-CENTRAL', description='Municipal operational zone code')
    latitude: float = Field(default=17.385044, ge=-90.0, le=90.0)
    longitude: float = Field(default=78.486671, ge=-180.0, le=180.0)
    altitude_meters: Optional[float] = Field(default=542.0)
    primary_metric_value: float = Field(default=100.0, description='Domain standard quantitative measurement')
    secondary_metric_value: float = Field(default=45.5, description='Secondary operational metric')
    threshold_limit: float = Field(default=150.0, description='Configured statutory threshold')
    safety_margin_percentage: float = Field(default=15.0)
    is_compliant: bool = Field(default=True)
    supervisor_notes: Optional[str] = Field(default=None)
    assigned_officer_id: Optional[str] = Field(default=None)
    tags: List[str] = Field(default_factory=lambda: ['civic', 'smart-city', 'telemetry'])
    metadata_payload: Dict[str, Any] = Field(default_factory=dict)
    created_at: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))
    updated_at: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))

    @field_validator('primary_metric_value')
    @classmethod
    def validate_metric(cls, v: float) -> float:
        if v < 0:
            raise ValueError('Metric value cannot be negative in municipal calculations')
        return round(v, 4)

    def calculate_utilization_ratio(self) -> float:
        if self.threshold_limit <= 0:
            return 0.0
        return round((self.primary_metric_value / self.threshold_limit) * 100, 2)

    def is_critical_alert(self) -> bool:
        return self.calculate_utilization_ratio() > (100.0 - self.safety_margin_percentage)

class UrbanPlanningEntity05(BaseModel):
    """Operational domain entity 5 for Urban Planning & Zoning Regulation."""
    model_config = ConfigDict(from_attributes=True, extra='ignore')

    entity_id: str = Field(..., description='Unique identifier for UrbanPlanningEntity05')
    reference_code: str = Field(..., description='Official municipal reference code')
    status: UrbanPlanningStatus = Field(default=UrbanPlanningStatus.ACTIVE)
    priority: UrbanPlanningPriority = Field(default=UrbanPlanningPriority.STANDARD)
    ward_id: int = Field(default=1, ge=1, le=150, description='Municipal jurisdictional ward number')
    zone_code: str = Field(default='ZONE-CENTRAL', description='Municipal operational zone code')
    latitude: float = Field(default=17.385044, ge=-90.0, le=90.0)
    longitude: float = Field(default=78.486671, ge=-180.0, le=180.0)
    altitude_meters: Optional[float] = Field(default=542.0)
    primary_metric_value: float = Field(default=100.0, description='Domain standard quantitative measurement')
    secondary_metric_value: float = Field(default=45.5, description='Secondary operational metric')
    threshold_limit: float = Field(default=150.0, description='Configured statutory threshold')
    safety_margin_percentage: float = Field(default=15.0)
    is_compliant: bool = Field(default=True)
    supervisor_notes: Optional[str] = Field(default=None)
    assigned_officer_id: Optional[str] = Field(default=None)
    tags: List[str] = Field(default_factory=lambda: ['civic', 'smart-city', 'telemetry'])
    metadata_payload: Dict[str, Any] = Field(default_factory=dict)
    created_at: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))
    updated_at: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))

    @field_validator('primary_metric_value')
    @classmethod
    def validate_metric(cls, v: float) -> float:
        if v < 0:
            raise ValueError('Metric value cannot be negative in municipal calculations')
        return round(v, 4)

    def calculate_utilization_ratio(self) -> float:
        if self.threshold_limit <= 0:
            return 0.0
        return round((self.primary_metric_value / self.threshold_limit) * 100, 2)

    def is_critical_alert(self) -> bool:
        return self.calculate_utilization_ratio() > (100.0 - self.safety_margin_percentage)

class UrbanPlanningEntity06(BaseModel):
    """Operational domain entity 6 for Urban Planning & Zoning Regulation."""
    model_config = ConfigDict(from_attributes=True, extra='ignore')

    entity_id: str = Field(..., description='Unique identifier for UrbanPlanningEntity06')
    reference_code: str = Field(..., description='Official municipal reference code')
    status: UrbanPlanningStatus = Field(default=UrbanPlanningStatus.ACTIVE)
    priority: UrbanPlanningPriority = Field(default=UrbanPlanningPriority.STANDARD)
    ward_id: int = Field(default=1, ge=1, le=150, description='Municipal jurisdictional ward number')
    zone_code: str = Field(default='ZONE-CENTRAL', description='Municipal operational zone code')
    latitude: float = Field(default=17.385044, ge=-90.0, le=90.0)
    longitude: float = Field(default=78.486671, ge=-180.0, le=180.0)
    altitude_meters: Optional[float] = Field(default=542.0)
    primary_metric_value: float = Field(default=100.0, description='Domain standard quantitative measurement')
    secondary_metric_value: float = Field(default=45.5, description='Secondary operational metric')
    threshold_limit: float = Field(default=150.0, description='Configured statutory threshold')
    safety_margin_percentage: float = Field(default=15.0)
    is_compliant: bool = Field(default=True)
    supervisor_notes: Optional[str] = Field(default=None)
    assigned_officer_id: Optional[str] = Field(default=None)
    tags: List[str] = Field(default_factory=lambda: ['civic', 'smart-city', 'telemetry'])
    metadata_payload: Dict[str, Any] = Field(default_factory=dict)
    created_at: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))
    updated_at: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))

    @field_validator('primary_metric_value')
    @classmethod
    def validate_metric(cls, v: float) -> float:
        if v < 0:
            raise ValueError('Metric value cannot be negative in municipal calculations')
        return round(v, 4)

    def calculate_utilization_ratio(self) -> float:
        if self.threshold_limit <= 0:
            return 0.0
        return round((self.primary_metric_value / self.threshold_limit) * 100, 2)

    def is_critical_alert(self) -> bool:
        return self.calculate_utilization_ratio() > (100.0 - self.safety_margin_percentage)

class UrbanPlanningEntity07(BaseModel):
    """Operational domain entity 7 for Urban Planning & Zoning Regulation."""
    model_config = ConfigDict(from_attributes=True, extra='ignore')

    entity_id: str = Field(..., description='Unique identifier for UrbanPlanningEntity07')
    reference_code: str = Field(..., description='Official municipal reference code')
    status: UrbanPlanningStatus = Field(default=UrbanPlanningStatus.ACTIVE)
    priority: UrbanPlanningPriority = Field(default=UrbanPlanningPriority.STANDARD)
    ward_id: int = Field(default=1, ge=1, le=150, description='Municipal jurisdictional ward number')
    zone_code: str = Field(default='ZONE-CENTRAL', description='Municipal operational zone code')
    latitude: float = Field(default=17.385044, ge=-90.0, le=90.0)
    longitude: float = Field(default=78.486671, ge=-180.0, le=180.0)
    altitude_meters: Optional[float] = Field(default=542.0)
    primary_metric_value: float = Field(default=100.0, description='Domain standard quantitative measurement')
    secondary_metric_value: float = Field(default=45.5, description='Secondary operational metric')
    threshold_limit: float = Field(default=150.0, description='Configured statutory threshold')
    safety_margin_percentage: float = Field(default=15.0)
    is_compliant: bool = Field(default=True)
    supervisor_notes: Optional[str] = Field(default=None)
    assigned_officer_id: Optional[str] = Field(default=None)
    tags: List[str] = Field(default_factory=lambda: ['civic', 'smart-city', 'telemetry'])
    metadata_payload: Dict[str, Any] = Field(default_factory=dict)
    created_at: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))
    updated_at: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))

    @field_validator('primary_metric_value')
    @classmethod
    def validate_metric(cls, v: float) -> float:
        if v < 0:
            raise ValueError('Metric value cannot be negative in municipal calculations')
        return round(v, 4)

    def calculate_utilization_ratio(self) -> float:
        if self.threshold_limit <= 0:
            return 0.0
        return round((self.primary_metric_value / self.threshold_limit) * 100, 2)

    def is_critical_alert(self) -> bool:
        return self.calculate_utilization_ratio() > (100.0 - self.safety_margin_percentage)

class UrbanPlanningEntity08(BaseModel):
    """Operational domain entity 8 for Urban Planning & Zoning Regulation."""
    model_config = ConfigDict(from_attributes=True, extra='ignore')

    entity_id: str = Field(..., description='Unique identifier for UrbanPlanningEntity08')
    reference_code: str = Field(..., description='Official municipal reference code')
    status: UrbanPlanningStatus = Field(default=UrbanPlanningStatus.ACTIVE)
    priority: UrbanPlanningPriority = Field(default=UrbanPlanningPriority.STANDARD)
    ward_id: int = Field(default=1, ge=1, le=150, description='Municipal jurisdictional ward number')
    zone_code: str = Field(default='ZONE-CENTRAL', description='Municipal operational zone code')
    latitude: float = Field(default=17.385044, ge=-90.0, le=90.0)
    longitude: float = Field(default=78.486671, ge=-180.0, le=180.0)
    altitude_meters: Optional[float] = Field(default=542.0)
    primary_metric_value: float = Field(default=100.0, description='Domain standard quantitative measurement')
    secondary_metric_value: float = Field(default=45.5, description='Secondary operational metric')
    threshold_limit: float = Field(default=150.0, description='Configured statutory threshold')
    safety_margin_percentage: float = Field(default=15.0)
    is_compliant: bool = Field(default=True)
    supervisor_notes: Optional[str] = Field(default=None)
    assigned_officer_id: Optional[str] = Field(default=None)
    tags: List[str] = Field(default_factory=lambda: ['civic', 'smart-city', 'telemetry'])
    metadata_payload: Dict[str, Any] = Field(default_factory=dict)
    created_at: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))
    updated_at: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))

    @field_validator('primary_metric_value')
    @classmethod
    def validate_metric(cls, v: float) -> float:
        if v < 0:
            raise ValueError('Metric value cannot be negative in municipal calculations')
        return round(v, 4)

    def calculate_utilization_ratio(self) -> float:
        if self.threshold_limit <= 0:
            return 0.0
        return round((self.primary_metric_value / self.threshold_limit) * 100, 2)

    def is_critical_alert(self) -> bool:
        return self.calculate_utilization_ratio() > (100.0 - self.safety_margin_percentage)

class UrbanPlanningEntity09(BaseModel):
    """Operational domain entity 9 for Urban Planning & Zoning Regulation."""
    model_config = ConfigDict(from_attributes=True, extra='ignore')

    entity_id: str = Field(..., description='Unique identifier for UrbanPlanningEntity09')
    reference_code: str = Field(..., description='Official municipal reference code')
    status: UrbanPlanningStatus = Field(default=UrbanPlanningStatus.ACTIVE)
    priority: UrbanPlanningPriority = Field(default=UrbanPlanningPriority.STANDARD)
    ward_id: int = Field(default=1, ge=1, le=150, description='Municipal jurisdictional ward number')
    zone_code: str = Field(default='ZONE-CENTRAL', description='Municipal operational zone code')
    latitude: float = Field(default=17.385044, ge=-90.0, le=90.0)
    longitude: float = Field(default=78.486671, ge=-180.0, le=180.0)
    altitude_meters: Optional[float] = Field(default=542.0)
    primary_metric_value: float = Field(default=100.0, description='Domain standard quantitative measurement')
    secondary_metric_value: float = Field(default=45.5, description='Secondary operational metric')
    threshold_limit: float = Field(default=150.0, description='Configured statutory threshold')
    safety_margin_percentage: float = Field(default=15.0)
    is_compliant: bool = Field(default=True)
    supervisor_notes: Optional[str] = Field(default=None)
    assigned_officer_id: Optional[str] = Field(default=None)
    tags: List[str] = Field(default_factory=lambda: ['civic', 'smart-city', 'telemetry'])
    metadata_payload: Dict[str, Any] = Field(default_factory=dict)
    created_at: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))
    updated_at: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))

    @field_validator('primary_metric_value')
    @classmethod
    def validate_metric(cls, v: float) -> float:
        if v < 0:
            raise ValueError('Metric value cannot be negative in municipal calculations')
        return round(v, 4)

    def calculate_utilization_ratio(self) -> float:
        if self.threshold_limit <= 0:
            return 0.0
        return round((self.primary_metric_value / self.threshold_limit) * 100, 2)

    def is_critical_alert(self) -> bool:
        return self.calculate_utilization_ratio() > (100.0 - self.safety_margin_percentage)

class UrbanPlanningEntity10(BaseModel):
    """Operational domain entity 10 for Urban Planning & Zoning Regulation."""
    model_config = ConfigDict(from_attributes=True, extra='ignore')

    entity_id: str = Field(..., description='Unique identifier for UrbanPlanningEntity10')
    reference_code: str = Field(..., description='Official municipal reference code')
    status: UrbanPlanningStatus = Field(default=UrbanPlanningStatus.ACTIVE)
    priority: UrbanPlanningPriority = Field(default=UrbanPlanningPriority.STANDARD)
    ward_id: int = Field(default=1, ge=1, le=150, description='Municipal jurisdictional ward number')
    zone_code: str = Field(default='ZONE-CENTRAL', description='Municipal operational zone code')
    latitude: float = Field(default=17.385044, ge=-90.0, le=90.0)
    longitude: float = Field(default=78.486671, ge=-180.0, le=180.0)
    altitude_meters: Optional[float] = Field(default=542.0)
    primary_metric_value: float = Field(default=100.0, description='Domain standard quantitative measurement')
    secondary_metric_value: float = Field(default=45.5, description='Secondary operational metric')
    threshold_limit: float = Field(default=150.0, description='Configured statutory threshold')
    safety_margin_percentage: float = Field(default=15.0)
    is_compliant: bool = Field(default=True)
    supervisor_notes: Optional[str] = Field(default=None)
    assigned_officer_id: Optional[str] = Field(default=None)
    tags: List[str] = Field(default_factory=lambda: ['civic', 'smart-city', 'telemetry'])
    metadata_payload: Dict[str, Any] = Field(default_factory=dict)
    created_at: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))
    updated_at: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))

    @field_validator('primary_metric_value')
    @classmethod
    def validate_metric(cls, v: float) -> float:
        if v < 0:
            raise ValueError('Metric value cannot be negative in municipal calculations')
        return round(v, 4)

    def calculate_utilization_ratio(self) -> float:
        if self.threshold_limit <= 0:
            return 0.0
        return round((self.primary_metric_value / self.threshold_limit) * 100, 2)

    def is_critical_alert(self) -> bool:
        return self.calculate_utilization_ratio() > (100.0 - self.safety_margin_percentage)

class UrbanPlanningEntity11(BaseModel):
    """Operational domain entity 11 for Urban Planning & Zoning Regulation."""
    model_config = ConfigDict(from_attributes=True, extra='ignore')

    entity_id: str = Field(..., description='Unique identifier for UrbanPlanningEntity11')
    reference_code: str = Field(..., description='Official municipal reference code')
    status: UrbanPlanningStatus = Field(default=UrbanPlanningStatus.ACTIVE)
    priority: UrbanPlanningPriority = Field(default=UrbanPlanningPriority.STANDARD)
    ward_id: int = Field(default=1, ge=1, le=150, description='Municipal jurisdictional ward number')
    zone_code: str = Field(default='ZONE-CENTRAL', description='Municipal operational zone code')
    latitude: float = Field(default=17.385044, ge=-90.0, le=90.0)
    longitude: float = Field(default=78.486671, ge=-180.0, le=180.0)
    altitude_meters: Optional[float] = Field(default=542.0)
    primary_metric_value: float = Field(default=100.0, description='Domain standard quantitative measurement')
    secondary_metric_value: float = Field(default=45.5, description='Secondary operational metric')
    threshold_limit: float = Field(default=150.0, description='Configured statutory threshold')
    safety_margin_percentage: float = Field(default=15.0)
    is_compliant: bool = Field(default=True)
    supervisor_notes: Optional[str] = Field(default=None)
    assigned_officer_id: Optional[str] = Field(default=None)
    tags: List[str] = Field(default_factory=lambda: ['civic', 'smart-city', 'telemetry'])
    metadata_payload: Dict[str, Any] = Field(default_factory=dict)
    created_at: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))
    updated_at: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))

    @field_validator('primary_metric_value')
    @classmethod
    def validate_metric(cls, v: float) -> float:
        if v < 0:
            raise ValueError('Metric value cannot be negative in municipal calculations')
        return round(v, 4)

    def calculate_utilization_ratio(self) -> float:
        if self.threshold_limit <= 0:
            return 0.0
        return round((self.primary_metric_value / self.threshold_limit) * 100, 2)

    def is_critical_alert(self) -> bool:
        return self.calculate_utilization_ratio() > (100.0 - self.safety_margin_percentage)

class UrbanPlanningEntity12(BaseModel):
    """Operational domain entity 12 for Urban Planning & Zoning Regulation."""
    model_config = ConfigDict(from_attributes=True, extra='ignore')

    entity_id: str = Field(..., description='Unique identifier for UrbanPlanningEntity12')
    reference_code: str = Field(..., description='Official municipal reference code')
    status: UrbanPlanningStatus = Field(default=UrbanPlanningStatus.ACTIVE)
    priority: UrbanPlanningPriority = Field(default=UrbanPlanningPriority.STANDARD)
    ward_id: int = Field(default=1, ge=1, le=150, description='Municipal jurisdictional ward number')
    zone_code: str = Field(default='ZONE-CENTRAL', description='Municipal operational zone code')
    latitude: float = Field(default=17.385044, ge=-90.0, le=90.0)
    longitude: float = Field(default=78.486671, ge=-180.0, le=180.0)
    altitude_meters: Optional[float] = Field(default=542.0)
    primary_metric_value: float = Field(default=100.0, description='Domain standard quantitative measurement')
    secondary_metric_value: float = Field(default=45.5, description='Secondary operational metric')
    threshold_limit: float = Field(default=150.0, description='Configured statutory threshold')
    safety_margin_percentage: float = Field(default=15.0)
    is_compliant: bool = Field(default=True)
    supervisor_notes: Optional[str] = Field(default=None)
    assigned_officer_id: Optional[str] = Field(default=None)
    tags: List[str] = Field(default_factory=lambda: ['civic', 'smart-city', 'telemetry'])
    metadata_payload: Dict[str, Any] = Field(default_factory=dict)
    created_at: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))
    updated_at: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))

    @field_validator('primary_metric_value')
    @classmethod
    def validate_metric(cls, v: float) -> float:
        if v < 0:
            raise ValueError('Metric value cannot be negative in municipal calculations')
        return round(v, 4)

    def calculate_utilization_ratio(self) -> float:
        if self.threshold_limit <= 0:
            return 0.0
        return round((self.primary_metric_value / self.threshold_limit) * 100, 2)

    def is_critical_alert(self) -> bool:
        return self.calculate_utilization_ratio() > (100.0 - self.safety_margin_percentage)

class UrbanPlanningEntity13(BaseModel):
    """Operational domain entity 13 for Urban Planning & Zoning Regulation."""
    model_config = ConfigDict(from_attributes=True, extra='ignore')

    entity_id: str = Field(..., description='Unique identifier for UrbanPlanningEntity13')
    reference_code: str = Field(..., description='Official municipal reference code')
    status: UrbanPlanningStatus = Field(default=UrbanPlanningStatus.ACTIVE)
    priority: UrbanPlanningPriority = Field(default=UrbanPlanningPriority.STANDARD)
    ward_id: int = Field(default=1, ge=1, le=150, description='Municipal jurisdictional ward number')
    zone_code: str = Field(default='ZONE-CENTRAL', description='Municipal operational zone code')
    latitude: float = Field(default=17.385044, ge=-90.0, le=90.0)
    longitude: float = Field(default=78.486671, ge=-180.0, le=180.0)
    altitude_meters: Optional[float] = Field(default=542.0)
    primary_metric_value: float = Field(default=100.0, description='Domain standard quantitative measurement')
    secondary_metric_value: float = Field(default=45.5, description='Secondary operational metric')
    threshold_limit: float = Field(default=150.0, description='Configured statutory threshold')
    safety_margin_percentage: float = Field(default=15.0)
    is_compliant: bool = Field(default=True)
    supervisor_notes: Optional[str] = Field(default=None)
    assigned_officer_id: Optional[str] = Field(default=None)
    tags: List[str] = Field(default_factory=lambda: ['civic', 'smart-city', 'telemetry'])
    metadata_payload: Dict[str, Any] = Field(default_factory=dict)
    created_at: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))
    updated_at: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))

    @field_validator('primary_metric_value')
    @classmethod
    def validate_metric(cls, v: float) -> float:
        if v < 0:
            raise ValueError('Metric value cannot be negative in municipal calculations')
        return round(v, 4)

    def calculate_utilization_ratio(self) -> float:
        if self.threshold_limit <= 0:
            return 0.0
        return round((self.primary_metric_value / self.threshold_limit) * 100, 2)

    def is_critical_alert(self) -> bool:
        return self.calculate_utilization_ratio() > (100.0 - self.safety_margin_percentage)

class UrbanPlanningEntity14(BaseModel):
    """Operational domain entity 14 for Urban Planning & Zoning Regulation."""
    model_config = ConfigDict(from_attributes=True, extra='ignore')

    entity_id: str = Field(..., description='Unique identifier for UrbanPlanningEntity14')
    reference_code: str = Field(..., description='Official municipal reference code')
    status: UrbanPlanningStatus = Field(default=UrbanPlanningStatus.ACTIVE)
    priority: UrbanPlanningPriority = Field(default=UrbanPlanningPriority.STANDARD)
    ward_id: int = Field(default=1, ge=1, le=150, description='Municipal jurisdictional ward number')
    zone_code: str = Field(default='ZONE-CENTRAL', description='Municipal operational zone code')
    latitude: float = Field(default=17.385044, ge=-90.0, le=90.0)
    longitude: float = Field(default=78.486671, ge=-180.0, le=180.0)
    altitude_meters: Optional[float] = Field(default=542.0)
    primary_metric_value: float = Field(default=100.0, description='Domain standard quantitative measurement')
    secondary_metric_value: float = Field(default=45.5, description='Secondary operational metric')
    threshold_limit: float = Field(default=150.0, description='Configured statutory threshold')
    safety_margin_percentage: float = Field(default=15.0)
    is_compliant: bool = Field(default=True)
    supervisor_notes: Optional[str] = Field(default=None)
    assigned_officer_id: Optional[str] = Field(default=None)
    tags: List[str] = Field(default_factory=lambda: ['civic', 'smart-city', 'telemetry'])
    metadata_payload: Dict[str, Any] = Field(default_factory=dict)
    created_at: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))
    updated_at: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))

    @field_validator('primary_metric_value')
    @classmethod
    def validate_metric(cls, v: float) -> float:
        if v < 0:
            raise ValueError('Metric value cannot be negative in municipal calculations')
        return round(v, 4)

    def calculate_utilization_ratio(self) -> float:
        if self.threshold_limit <= 0:
            return 0.0
        return round((self.primary_metric_value / self.threshold_limit) * 100, 2)

    def is_critical_alert(self) -> bool:
        return self.calculate_utilization_ratio() > (100.0 - self.safety_margin_percentage)

class UrbanPlanningEntity15(BaseModel):
    """Operational domain entity 15 for Urban Planning & Zoning Regulation."""
    model_config = ConfigDict(from_attributes=True, extra='ignore')

    entity_id: str = Field(..., description='Unique identifier for UrbanPlanningEntity15')
    reference_code: str = Field(..., description='Official municipal reference code')
    status: UrbanPlanningStatus = Field(default=UrbanPlanningStatus.ACTIVE)
    priority: UrbanPlanningPriority = Field(default=UrbanPlanningPriority.STANDARD)
    ward_id: int = Field(default=1, ge=1, le=150, description='Municipal jurisdictional ward number')
    zone_code: str = Field(default='ZONE-CENTRAL', description='Municipal operational zone code')
    latitude: float = Field(default=17.385044, ge=-90.0, le=90.0)
    longitude: float = Field(default=78.486671, ge=-180.0, le=180.0)
    altitude_meters: Optional[float] = Field(default=542.0)
    primary_metric_value: float = Field(default=100.0, description='Domain standard quantitative measurement')
    secondary_metric_value: float = Field(default=45.5, description='Secondary operational metric')
    threshold_limit: float = Field(default=150.0, description='Configured statutory threshold')
    safety_margin_percentage: float = Field(default=15.0)
    is_compliant: bool = Field(default=True)
    supervisor_notes: Optional[str] = Field(default=None)
    assigned_officer_id: Optional[str] = Field(default=None)
    tags: List[str] = Field(default_factory=lambda: ['civic', 'smart-city', 'telemetry'])
    metadata_payload: Dict[str, Any] = Field(default_factory=dict)
    created_at: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))
    updated_at: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))

    @field_validator('primary_metric_value')
    @classmethod
    def validate_metric(cls, v: float) -> float:
        if v < 0:
            raise ValueError('Metric value cannot be negative in municipal calculations')
        return round(v, 4)

    def calculate_utilization_ratio(self) -> float:
        if self.threshold_limit <= 0:
            return 0.0
        return round((self.primary_metric_value / self.threshold_limit) * 100, 2)

    def is_critical_alert(self) -> bool:
        return self.calculate_utilization_ratio() > (100.0 - self.safety_margin_percentage)

class UrbanPlanningEntity16(BaseModel):
    """Operational domain entity 16 for Urban Planning & Zoning Regulation."""
    model_config = ConfigDict(from_attributes=True, extra='ignore')

    entity_id: str = Field(..., description='Unique identifier for UrbanPlanningEntity16')
    reference_code: str = Field(..., description='Official municipal reference code')
    status: UrbanPlanningStatus = Field(default=UrbanPlanningStatus.ACTIVE)
    priority: UrbanPlanningPriority = Field(default=UrbanPlanningPriority.STANDARD)
    ward_id: int = Field(default=1, ge=1, le=150, description='Municipal jurisdictional ward number')
    zone_code: str = Field(default='ZONE-CENTRAL', description='Municipal operational zone code')
    latitude: float = Field(default=17.385044, ge=-90.0, le=90.0)
    longitude: float = Field(default=78.486671, ge=-180.0, le=180.0)
    altitude_meters: Optional[float] = Field(default=542.0)
    primary_metric_value: float = Field(default=100.0, description='Domain standard quantitative measurement')
    secondary_metric_value: float = Field(default=45.5, description='Secondary operational metric')
    threshold_limit: float = Field(default=150.0, description='Configured statutory threshold')
    safety_margin_percentage: float = Field(default=15.0)
    is_compliant: bool = Field(default=True)
    supervisor_notes: Optional[str] = Field(default=None)
    assigned_officer_id: Optional[str] = Field(default=None)
    tags: List[str] = Field(default_factory=lambda: ['civic', 'smart-city', 'telemetry'])
    metadata_payload: Dict[str, Any] = Field(default_factory=dict)
    created_at: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))
    updated_at: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))

    @field_validator('primary_metric_value')
    @classmethod
    def validate_metric(cls, v: float) -> float:
        if v < 0:
            raise ValueError('Metric value cannot be negative in municipal calculations')
        return round(v, 4)

    def calculate_utilization_ratio(self) -> float:
        if self.threshold_limit <= 0:
            return 0.0
        return round((self.primary_metric_value / self.threshold_limit) * 100, 2)

    def is_critical_alert(self) -> bool:
        return self.calculate_utilization_ratio() > (100.0 - self.safety_margin_percentage)

class UrbanPlanningEntity17(BaseModel):
    """Operational domain entity 17 for Urban Planning & Zoning Regulation."""
    model_config = ConfigDict(from_attributes=True, extra='ignore')

    entity_id: str = Field(..., description='Unique identifier for UrbanPlanningEntity17')
    reference_code: str = Field(..., description='Official municipal reference code')
    status: UrbanPlanningStatus = Field(default=UrbanPlanningStatus.ACTIVE)
    priority: UrbanPlanningPriority = Field(default=UrbanPlanningPriority.STANDARD)
    ward_id: int = Field(default=1, ge=1, le=150, description='Municipal jurisdictional ward number')
    zone_code: str = Field(default='ZONE-CENTRAL', description='Municipal operational zone code')
    latitude: float = Field(default=17.385044, ge=-90.0, le=90.0)
    longitude: float = Field(default=78.486671, ge=-180.0, le=180.0)
    altitude_meters: Optional[float] = Field(default=542.0)
    primary_metric_value: float = Field(default=100.0, description='Domain standard quantitative measurement')
    secondary_metric_value: float = Field(default=45.5, description='Secondary operational metric')
    threshold_limit: float = Field(default=150.0, description='Configured statutory threshold')
    safety_margin_percentage: float = Field(default=15.0)
    is_compliant: bool = Field(default=True)
    supervisor_notes: Optional[str] = Field(default=None)
    assigned_officer_id: Optional[str] = Field(default=None)
    tags: List[str] = Field(default_factory=lambda: ['civic', 'smart-city', 'telemetry'])
    metadata_payload: Dict[str, Any] = Field(default_factory=dict)
    created_at: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))
    updated_at: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))

    @field_validator('primary_metric_value')
    @classmethod
    def validate_metric(cls, v: float) -> float:
        if v < 0:
            raise ValueError('Metric value cannot be negative in municipal calculations')
        return round(v, 4)

    def calculate_utilization_ratio(self) -> float:
        if self.threshold_limit <= 0:
            return 0.0
        return round((self.primary_metric_value / self.threshold_limit) * 100, 2)

    def is_critical_alert(self) -> bool:
        return self.calculate_utilization_ratio() > (100.0 - self.safety_margin_percentage)

class UrbanPlanningEntity18(BaseModel):
    """Operational domain entity 18 for Urban Planning & Zoning Regulation."""
    model_config = ConfigDict(from_attributes=True, extra='ignore')

    entity_id: str = Field(..., description='Unique identifier for UrbanPlanningEntity18')
    reference_code: str = Field(..., description='Official municipal reference code')
    status: UrbanPlanningStatus = Field(default=UrbanPlanningStatus.ACTIVE)
    priority: UrbanPlanningPriority = Field(default=UrbanPlanningPriority.STANDARD)
    ward_id: int = Field(default=1, ge=1, le=150, description='Municipal jurisdictional ward number')
    zone_code: str = Field(default='ZONE-CENTRAL', description='Municipal operational zone code')
    latitude: float = Field(default=17.385044, ge=-90.0, le=90.0)
    longitude: float = Field(default=78.486671, ge=-180.0, le=180.0)
    altitude_meters: Optional[float] = Field(default=542.0)
    primary_metric_value: float = Field(default=100.0, description='Domain standard quantitative measurement')
    secondary_metric_value: float = Field(default=45.5, description='Secondary operational metric')
    threshold_limit: float = Field(default=150.0, description='Configured statutory threshold')
    safety_margin_percentage: float = Field(default=15.0)
    is_compliant: bool = Field(default=True)
    supervisor_notes: Optional[str] = Field(default=None)
    assigned_officer_id: Optional[str] = Field(default=None)
    tags: List[str] = Field(default_factory=lambda: ['civic', 'smart-city', 'telemetry'])
    metadata_payload: Dict[str, Any] = Field(default_factory=dict)
    created_at: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))
    updated_at: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))

    @field_validator('primary_metric_value')
    @classmethod
    def validate_metric(cls, v: float) -> float:
        if v < 0:
            raise ValueError('Metric value cannot be negative in municipal calculations')
        return round(v, 4)

    def calculate_utilization_ratio(self) -> float:
        if self.threshold_limit <= 0:
            return 0.0
        return round((self.primary_metric_value / self.threshold_limit) * 100, 2)

    def is_critical_alert(self) -> bool:
        return self.calculate_utilization_ratio() > (100.0 - self.safety_margin_percentage)

class UrbanPlanningEntity19(BaseModel):
    """Operational domain entity 19 for Urban Planning & Zoning Regulation."""
    model_config = ConfigDict(from_attributes=True, extra='ignore')

    entity_id: str = Field(..., description='Unique identifier for UrbanPlanningEntity19')
    reference_code: str = Field(..., description='Official municipal reference code')
    status: UrbanPlanningStatus = Field(default=UrbanPlanningStatus.ACTIVE)
    priority: UrbanPlanningPriority = Field(default=UrbanPlanningPriority.STANDARD)
    ward_id: int = Field(default=1, ge=1, le=150, description='Municipal jurisdictional ward number')
    zone_code: str = Field(default='ZONE-CENTRAL', description='Municipal operational zone code')
    latitude: float = Field(default=17.385044, ge=-90.0, le=90.0)
    longitude: float = Field(default=78.486671, ge=-180.0, le=180.0)
    altitude_meters: Optional[float] = Field(default=542.0)
    primary_metric_value: float = Field(default=100.0, description='Domain standard quantitative measurement')
    secondary_metric_value: float = Field(default=45.5, description='Secondary operational metric')
    threshold_limit: float = Field(default=150.0, description='Configured statutory threshold')
    safety_margin_percentage: float = Field(default=15.0)
    is_compliant: bool = Field(default=True)
    supervisor_notes: Optional[str] = Field(default=None)
    assigned_officer_id: Optional[str] = Field(default=None)
    tags: List[str] = Field(default_factory=lambda: ['civic', 'smart-city', 'telemetry'])
    metadata_payload: Dict[str, Any] = Field(default_factory=dict)
    created_at: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))
    updated_at: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))

    @field_validator('primary_metric_value')
    @classmethod
    def validate_metric(cls, v: float) -> float:
        if v < 0:
            raise ValueError('Metric value cannot be negative in municipal calculations')
        return round(v, 4)

    def calculate_utilization_ratio(self) -> float:
        if self.threshold_limit <= 0:
            return 0.0
        return round((self.primary_metric_value / self.threshold_limit) * 100, 2)

    def is_critical_alert(self) -> bool:
        return self.calculate_utilization_ratio() > (100.0 - self.safety_margin_percentage)

class UrbanPlanningEntity20(BaseModel):
    """Operational domain entity 20 for Urban Planning & Zoning Regulation."""
    model_config = ConfigDict(from_attributes=True, extra='ignore')

    entity_id: str = Field(..., description='Unique identifier for UrbanPlanningEntity20')
    reference_code: str = Field(..., description='Official municipal reference code')
    status: UrbanPlanningStatus = Field(default=UrbanPlanningStatus.ACTIVE)
    priority: UrbanPlanningPriority = Field(default=UrbanPlanningPriority.STANDARD)
    ward_id: int = Field(default=1, ge=1, le=150, description='Municipal jurisdictional ward number')
    zone_code: str = Field(default='ZONE-CENTRAL', description='Municipal operational zone code')
    latitude: float = Field(default=17.385044, ge=-90.0, le=90.0)
    longitude: float = Field(default=78.486671, ge=-180.0, le=180.0)
    altitude_meters: Optional[float] = Field(default=542.0)
    primary_metric_value: float = Field(default=100.0, description='Domain standard quantitative measurement')
    secondary_metric_value: float = Field(default=45.5, description='Secondary operational metric')
    threshold_limit: float = Field(default=150.0, description='Configured statutory threshold')
    safety_margin_percentage: float = Field(default=15.0)
    is_compliant: bool = Field(default=True)
    supervisor_notes: Optional[str] = Field(default=None)
    assigned_officer_id: Optional[str] = Field(default=None)
    tags: List[str] = Field(default_factory=lambda: ['civic', 'smart-city', 'telemetry'])
    metadata_payload: Dict[str, Any] = Field(default_factory=dict)
    created_at: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))
    updated_at: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))

    @field_validator('primary_metric_value')
    @classmethod
    def validate_metric(cls, v: float) -> float:
        if v < 0:
            raise ValueError('Metric value cannot be negative in municipal calculations')
        return round(v, 4)

    def calculate_utilization_ratio(self) -> float:
        if self.threshold_limit <= 0:
            return 0.0
        return round((self.primary_metric_value / self.threshold_limit) * 100, 2)

    def is_critical_alert(self) -> bool:
        return self.calculate_utilization_ratio() > (100.0 - self.safety_margin_percentage)

class UrbanPlanningEntity21(BaseModel):
    """Operational domain entity 21 for Urban Planning & Zoning Regulation."""
    model_config = ConfigDict(from_attributes=True, extra='ignore')

    entity_id: str = Field(..., description='Unique identifier for UrbanPlanningEntity21')
    reference_code: str = Field(..., description='Official municipal reference code')
    status: UrbanPlanningStatus = Field(default=UrbanPlanningStatus.ACTIVE)
    priority: UrbanPlanningPriority = Field(default=UrbanPlanningPriority.STANDARD)
    ward_id: int = Field(default=1, ge=1, le=150, description='Municipal jurisdictional ward number')
    zone_code: str = Field(default='ZONE-CENTRAL', description='Municipal operational zone code')
    latitude: float = Field(default=17.385044, ge=-90.0, le=90.0)
    longitude: float = Field(default=78.486671, ge=-180.0, le=180.0)
    altitude_meters: Optional[float] = Field(default=542.0)
    primary_metric_value: float = Field(default=100.0, description='Domain standard quantitative measurement')
    secondary_metric_value: float = Field(default=45.5, description='Secondary operational metric')
    threshold_limit: float = Field(default=150.0, description='Configured statutory threshold')
    safety_margin_percentage: float = Field(default=15.0)
    is_compliant: bool = Field(default=True)
    supervisor_notes: Optional[str] = Field(default=None)
    assigned_officer_id: Optional[str] = Field(default=None)
    tags: List[str] = Field(default_factory=lambda: ['civic', 'smart-city', 'telemetry'])
    metadata_payload: Dict[str, Any] = Field(default_factory=dict)
    created_at: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))
    updated_at: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))

    @field_validator('primary_metric_value')
    @classmethod
    def validate_metric(cls, v: float) -> float:
        if v < 0:
            raise ValueError('Metric value cannot be negative in municipal calculations')
        return round(v, 4)

    def calculate_utilization_ratio(self) -> float:
        if self.threshold_limit <= 0:
            return 0.0
        return round((self.primary_metric_value / self.threshold_limit) * 100, 2)

    def is_critical_alert(self) -> bool:
        return self.calculate_utilization_ratio() > (100.0 - self.safety_margin_percentage)

class UrbanPlanningEntity22(BaseModel):
    """Operational domain entity 22 for Urban Planning & Zoning Regulation."""
    model_config = ConfigDict(from_attributes=True, extra='ignore')

    entity_id: str = Field(..., description='Unique identifier for UrbanPlanningEntity22')
    reference_code: str = Field(..., description='Official municipal reference code')
    status: UrbanPlanningStatus = Field(default=UrbanPlanningStatus.ACTIVE)
    priority: UrbanPlanningPriority = Field(default=UrbanPlanningPriority.STANDARD)
    ward_id: int = Field(default=1, ge=1, le=150, description='Municipal jurisdictional ward number')
    zone_code: str = Field(default='ZONE-CENTRAL', description='Municipal operational zone code')
    latitude: float = Field(default=17.385044, ge=-90.0, le=90.0)
    longitude: float = Field(default=78.486671, ge=-180.0, le=180.0)
    altitude_meters: Optional[float] = Field(default=542.0)
    primary_metric_value: float = Field(default=100.0, description='Domain standard quantitative measurement')
    secondary_metric_value: float = Field(default=45.5, description='Secondary operational metric')
    threshold_limit: float = Field(default=150.0, description='Configured statutory threshold')
    safety_margin_percentage: float = Field(default=15.0)
    is_compliant: bool = Field(default=True)
    supervisor_notes: Optional[str] = Field(default=None)
    assigned_officer_id: Optional[str] = Field(default=None)
    tags: List[str] = Field(default_factory=lambda: ['civic', 'smart-city', 'telemetry'])
    metadata_payload: Dict[str, Any] = Field(default_factory=dict)
    created_at: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))
    updated_at: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))

    @field_validator('primary_metric_value')
    @classmethod
    def validate_metric(cls, v: float) -> float:
        if v < 0:
            raise ValueError('Metric value cannot be negative in municipal calculations')
        return round(v, 4)

    def calculate_utilization_ratio(self) -> float:
        if self.threshold_limit <= 0:
            return 0.0
        return round((self.primary_metric_value / self.threshold_limit) * 100, 2)

    def is_critical_alert(self) -> bool:
        return self.calculate_utilization_ratio() > (100.0 - self.safety_margin_percentage)

class UrbanPlanningEntity23(BaseModel):
    """Operational domain entity 23 for Urban Planning & Zoning Regulation."""
    model_config = ConfigDict(from_attributes=True, extra='ignore')

    entity_id: str = Field(..., description='Unique identifier for UrbanPlanningEntity23')
    reference_code: str = Field(..., description='Official municipal reference code')
    status: UrbanPlanningStatus = Field(default=UrbanPlanningStatus.ACTIVE)
    priority: UrbanPlanningPriority = Field(default=UrbanPlanningPriority.STANDARD)
    ward_id: int = Field(default=1, ge=1, le=150, description='Municipal jurisdictional ward number')
    zone_code: str = Field(default='ZONE-CENTRAL', description='Municipal operational zone code')
    latitude: float = Field(default=17.385044, ge=-90.0, le=90.0)
    longitude: float = Field(default=78.486671, ge=-180.0, le=180.0)
    altitude_meters: Optional[float] = Field(default=542.0)
    primary_metric_value: float = Field(default=100.0, description='Domain standard quantitative measurement')
    secondary_metric_value: float = Field(default=45.5, description='Secondary operational metric')
    threshold_limit: float = Field(default=150.0, description='Configured statutory threshold')
    safety_margin_percentage: float = Field(default=15.0)
    is_compliant: bool = Field(default=True)
    supervisor_notes: Optional[str] = Field(default=None)
    assigned_officer_id: Optional[str] = Field(default=None)
    tags: List[str] = Field(default_factory=lambda: ['civic', 'smart-city', 'telemetry'])
    metadata_payload: Dict[str, Any] = Field(default_factory=dict)
    created_at: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))
    updated_at: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))

    @field_validator('primary_metric_value')
    @classmethod
    def validate_metric(cls, v: float) -> float:
        if v < 0:
            raise ValueError('Metric value cannot be negative in municipal calculations')
        return round(v, 4)

    def calculate_utilization_ratio(self) -> float:
        if self.threshold_limit <= 0:
            return 0.0
        return round((self.primary_metric_value / self.threshold_limit) * 100, 2)

    def is_critical_alert(self) -> bool:
        return self.calculate_utilization_ratio() > (100.0 - self.safety_margin_percentage)

class UrbanPlanningEntity24(BaseModel):
    """Operational domain entity 24 for Urban Planning & Zoning Regulation."""
    model_config = ConfigDict(from_attributes=True, extra='ignore')

    entity_id: str = Field(..., description='Unique identifier for UrbanPlanningEntity24')
    reference_code: str = Field(..., description='Official municipal reference code')
    status: UrbanPlanningStatus = Field(default=UrbanPlanningStatus.ACTIVE)
    priority: UrbanPlanningPriority = Field(default=UrbanPlanningPriority.STANDARD)
    ward_id: int = Field(default=1, ge=1, le=150, description='Municipal jurisdictional ward number')
    zone_code: str = Field(default='ZONE-CENTRAL', description='Municipal operational zone code')
    latitude: float = Field(default=17.385044, ge=-90.0, le=90.0)
    longitude: float = Field(default=78.486671, ge=-180.0, le=180.0)
    altitude_meters: Optional[float] = Field(default=542.0)
    primary_metric_value: float = Field(default=100.0, description='Domain standard quantitative measurement')
    secondary_metric_value: float = Field(default=45.5, description='Secondary operational metric')
    threshold_limit: float = Field(default=150.0, description='Configured statutory threshold')
    safety_margin_percentage: float = Field(default=15.0)
    is_compliant: bool = Field(default=True)
    supervisor_notes: Optional[str] = Field(default=None)
    assigned_officer_id: Optional[str] = Field(default=None)
    tags: List[str] = Field(default_factory=lambda: ['civic', 'smart-city', 'telemetry'])
    metadata_payload: Dict[str, Any] = Field(default_factory=dict)
    created_at: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))
    updated_at: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))

    @field_validator('primary_metric_value')
    @classmethod
    def validate_metric(cls, v: float) -> float:
        if v < 0:
            raise ValueError('Metric value cannot be negative in municipal calculations')
        return round(v, 4)

    def calculate_utilization_ratio(self) -> float:
        if self.threshold_limit <= 0:
            return 0.0
        return round((self.primary_metric_value / self.threshold_limit) * 100, 2)

    def is_critical_alert(self) -> bool:
        return self.calculate_utilization_ratio() > (100.0 - self.safety_margin_percentage)

class UrbanPlanningEntity25(BaseModel):
    """Operational domain entity 25 for Urban Planning & Zoning Regulation."""
    model_config = ConfigDict(from_attributes=True, extra='ignore')

    entity_id: str = Field(..., description='Unique identifier for UrbanPlanningEntity25')
    reference_code: str = Field(..., description='Official municipal reference code')
    status: UrbanPlanningStatus = Field(default=UrbanPlanningStatus.ACTIVE)
    priority: UrbanPlanningPriority = Field(default=UrbanPlanningPriority.STANDARD)
    ward_id: int = Field(default=1, ge=1, le=150, description='Municipal jurisdictional ward number')
    zone_code: str = Field(default='ZONE-CENTRAL', description='Municipal operational zone code')
    latitude: float = Field(default=17.385044, ge=-90.0, le=90.0)
    longitude: float = Field(default=78.486671, ge=-180.0, le=180.0)
    altitude_meters: Optional[float] = Field(default=542.0)
    primary_metric_value: float = Field(default=100.0, description='Domain standard quantitative measurement')
    secondary_metric_value: float = Field(default=45.5, description='Secondary operational metric')
    threshold_limit: float = Field(default=150.0, description='Configured statutory threshold')
    safety_margin_percentage: float = Field(default=15.0)
    is_compliant: bool = Field(default=True)
    supervisor_notes: Optional[str] = Field(default=None)
    assigned_officer_id: Optional[str] = Field(default=None)
    tags: List[str] = Field(default_factory=lambda: ['civic', 'smart-city', 'telemetry'])
    metadata_payload: Dict[str, Any] = Field(default_factory=dict)
    created_at: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))
    updated_at: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))

    @field_validator('primary_metric_value')
    @classmethod
    def validate_metric(cls, v: float) -> float:
        if v < 0:
            raise ValueError('Metric value cannot be negative in municipal calculations')
        return round(v, 4)

    def calculate_utilization_ratio(self) -> float:
        if self.threshold_limit <= 0:
            return 0.0
        return round((self.primary_metric_value / self.threshold_limit) * 100, 2)

    def is_critical_alert(self) -> bool:
        return self.calculate_utilization_ratio() > (100.0 - self.safety_margin_percentage)

class UrbanPlanningEntity26(BaseModel):
    """Operational domain entity 26 for Urban Planning & Zoning Regulation."""
    model_config = ConfigDict(from_attributes=True, extra='ignore')

    entity_id: str = Field(..., description='Unique identifier for UrbanPlanningEntity26')
    reference_code: str = Field(..., description='Official municipal reference code')
    status: UrbanPlanningStatus = Field(default=UrbanPlanningStatus.ACTIVE)
    priority: UrbanPlanningPriority = Field(default=UrbanPlanningPriority.STANDARD)
    ward_id: int = Field(default=1, ge=1, le=150, description='Municipal jurisdictional ward number')
    zone_code: str = Field(default='ZONE-CENTRAL', description='Municipal operational zone code')
    latitude: float = Field(default=17.385044, ge=-90.0, le=90.0)
    longitude: float = Field(default=78.486671, ge=-180.0, le=180.0)
    altitude_meters: Optional[float] = Field(default=542.0)
    primary_metric_value: float = Field(default=100.0, description='Domain standard quantitative measurement')
    secondary_metric_value: float = Field(default=45.5, description='Secondary operational metric')
    threshold_limit: float = Field(default=150.0, description='Configured statutory threshold')
    safety_margin_percentage: float = Field(default=15.0)
    is_compliant: bool = Field(default=True)
    supervisor_notes: Optional[str] = Field(default=None)
    assigned_officer_id: Optional[str] = Field(default=None)
    tags: List[str] = Field(default_factory=lambda: ['civic', 'smart-city', 'telemetry'])
    metadata_payload: Dict[str, Any] = Field(default_factory=dict)
    created_at: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))
    updated_at: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))

    @field_validator('primary_metric_value')
    @classmethod
    def validate_metric(cls, v: float) -> float:
        if v < 0:
            raise ValueError('Metric value cannot be negative in municipal calculations')
        return round(v, 4)

    def calculate_utilization_ratio(self) -> float:
        if self.threshold_limit <= 0:
            return 0.0
        return round((self.primary_metric_value / self.threshold_limit) * 100, 2)

    def is_critical_alert(self) -> bool:
        return self.calculate_utilization_ratio() > (100.0 - self.safety_margin_percentage)

class UrbanPlanningEntity27(BaseModel):
    """Operational domain entity 27 for Urban Planning & Zoning Regulation."""
    model_config = ConfigDict(from_attributes=True, extra='ignore')

    entity_id: str = Field(..., description='Unique identifier for UrbanPlanningEntity27')
    reference_code: str = Field(..., description='Official municipal reference code')
    status: UrbanPlanningStatus = Field(default=UrbanPlanningStatus.ACTIVE)
    priority: UrbanPlanningPriority = Field(default=UrbanPlanningPriority.STANDARD)
    ward_id: int = Field(default=1, ge=1, le=150, description='Municipal jurisdictional ward number')
    zone_code: str = Field(default='ZONE-CENTRAL', description='Municipal operational zone code')
    latitude: float = Field(default=17.385044, ge=-90.0, le=90.0)
    longitude: float = Field(default=78.486671, ge=-180.0, le=180.0)
    altitude_meters: Optional[float] = Field(default=542.0)
    primary_metric_value: float = Field(default=100.0, description='Domain standard quantitative measurement')
    secondary_metric_value: float = Field(default=45.5, description='Secondary operational metric')
    threshold_limit: float = Field(default=150.0, description='Configured statutory threshold')
    safety_margin_percentage: float = Field(default=15.0)
    is_compliant: bool = Field(default=True)
    supervisor_notes: Optional[str] = Field(default=None)
    assigned_officer_id: Optional[str] = Field(default=None)
    tags: List[str] = Field(default_factory=lambda: ['civic', 'smart-city', 'telemetry'])
    metadata_payload: Dict[str, Any] = Field(default_factory=dict)
    created_at: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))
    updated_at: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))

    @field_validator('primary_metric_value')
    @classmethod
    def validate_metric(cls, v: float) -> float:
        if v < 0:
            raise ValueError('Metric value cannot be negative in municipal calculations')
        return round(v, 4)

    def calculate_utilization_ratio(self) -> float:
        if self.threshold_limit <= 0:
            return 0.0
        return round((self.primary_metric_value / self.threshold_limit) * 100, 2)

    def is_critical_alert(self) -> bool:
        return self.calculate_utilization_ratio() > (100.0 - self.safety_margin_percentage)

class UrbanPlanningEntity28(BaseModel):
    """Operational domain entity 28 for Urban Planning & Zoning Regulation."""
    model_config = ConfigDict(from_attributes=True, extra='ignore')

    entity_id: str = Field(..., description='Unique identifier for UrbanPlanningEntity28')
    reference_code: str = Field(..., description='Official municipal reference code')
    status: UrbanPlanningStatus = Field(default=UrbanPlanningStatus.ACTIVE)
    priority: UrbanPlanningPriority = Field(default=UrbanPlanningPriority.STANDARD)
    ward_id: int = Field(default=1, ge=1, le=150, description='Municipal jurisdictional ward number')
    zone_code: str = Field(default='ZONE-CENTRAL', description='Municipal operational zone code')
    latitude: float = Field(default=17.385044, ge=-90.0, le=90.0)
    longitude: float = Field(default=78.486671, ge=-180.0, le=180.0)
    altitude_meters: Optional[float] = Field(default=542.0)
    primary_metric_value: float = Field(default=100.0, description='Domain standard quantitative measurement')
    secondary_metric_value: float = Field(default=45.5, description='Secondary operational metric')
    threshold_limit: float = Field(default=150.0, description='Configured statutory threshold')
    safety_margin_percentage: float = Field(default=15.0)
    is_compliant: bool = Field(default=True)
    supervisor_notes: Optional[str] = Field(default=None)
    assigned_officer_id: Optional[str] = Field(default=None)
    tags: List[str] = Field(default_factory=lambda: ['civic', 'smart-city', 'telemetry'])
    metadata_payload: Dict[str, Any] = Field(default_factory=dict)
    created_at: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))
    updated_at: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))

    @field_validator('primary_metric_value')
    @classmethod
    def validate_metric(cls, v: float) -> float:
        if v < 0:
            raise ValueError('Metric value cannot be negative in municipal calculations')
        return round(v, 4)

    def calculate_utilization_ratio(self) -> float:
        if self.threshold_limit <= 0:
            return 0.0
        return round((self.primary_metric_value / self.threshold_limit) * 100, 2)

    def is_critical_alert(self) -> bool:
        return self.calculate_utilization_ratio() > (100.0 - self.safety_margin_percentage)

class UrbanPlanningEntity29(BaseModel):
    """Operational domain entity 29 for Urban Planning & Zoning Regulation."""
    model_config = ConfigDict(from_attributes=True, extra='ignore')

    entity_id: str = Field(..., description='Unique identifier for UrbanPlanningEntity29')
    reference_code: str = Field(..., description='Official municipal reference code')
    status: UrbanPlanningStatus = Field(default=UrbanPlanningStatus.ACTIVE)
    priority: UrbanPlanningPriority = Field(default=UrbanPlanningPriority.STANDARD)
    ward_id: int = Field(default=1, ge=1, le=150, description='Municipal jurisdictional ward number')
    zone_code: str = Field(default='ZONE-CENTRAL', description='Municipal operational zone code')
    latitude: float = Field(default=17.385044, ge=-90.0, le=90.0)
    longitude: float = Field(default=78.486671, ge=-180.0, le=180.0)
    altitude_meters: Optional[float] = Field(default=542.0)
    primary_metric_value: float = Field(default=100.0, description='Domain standard quantitative measurement')
    secondary_metric_value: float = Field(default=45.5, description='Secondary operational metric')
    threshold_limit: float = Field(default=150.0, description='Configured statutory threshold')
    safety_margin_percentage: float = Field(default=15.0)
    is_compliant: bool = Field(default=True)
    supervisor_notes: Optional[str] = Field(default=None)
    assigned_officer_id: Optional[str] = Field(default=None)
    tags: List[str] = Field(default_factory=lambda: ['civic', 'smart-city', 'telemetry'])
    metadata_payload: Dict[str, Any] = Field(default_factory=dict)
    created_at: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))
    updated_at: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))

    @field_validator('primary_metric_value')
    @classmethod
    def validate_metric(cls, v: float) -> float:
        if v < 0:
            raise ValueError('Metric value cannot be negative in municipal calculations')
        return round(v, 4)

    def calculate_utilization_ratio(self) -> float:
        if self.threshold_limit <= 0:
            return 0.0
        return round((self.primary_metric_value / self.threshold_limit) * 100, 2)

    def is_critical_alert(self) -> bool:
        return self.calculate_utilization_ratio() > (100.0 - self.safety_margin_percentage)

class UrbanPlanningEntity30(BaseModel):
    """Operational domain entity 30 for Urban Planning & Zoning Regulation."""
    model_config = ConfigDict(from_attributes=True, extra='ignore')

    entity_id: str = Field(..., description='Unique identifier for UrbanPlanningEntity30')
    reference_code: str = Field(..., description='Official municipal reference code')
    status: UrbanPlanningStatus = Field(default=UrbanPlanningStatus.ACTIVE)
    priority: UrbanPlanningPriority = Field(default=UrbanPlanningPriority.STANDARD)
    ward_id: int = Field(default=1, ge=1, le=150, description='Municipal jurisdictional ward number')
    zone_code: str = Field(default='ZONE-CENTRAL', description='Municipal operational zone code')
    latitude: float = Field(default=17.385044, ge=-90.0, le=90.0)
    longitude: float = Field(default=78.486671, ge=-180.0, le=180.0)
    altitude_meters: Optional[float] = Field(default=542.0)
    primary_metric_value: float = Field(default=100.0, description='Domain standard quantitative measurement')
    secondary_metric_value: float = Field(default=45.5, description='Secondary operational metric')
    threshold_limit: float = Field(default=150.0, description='Configured statutory threshold')
    safety_margin_percentage: float = Field(default=15.0)
    is_compliant: bool = Field(default=True)
    supervisor_notes: Optional[str] = Field(default=None)
    assigned_officer_id: Optional[str] = Field(default=None)
    tags: List[str] = Field(default_factory=lambda: ['civic', 'smart-city', 'telemetry'])
    metadata_payload: Dict[str, Any] = Field(default_factory=dict)
    created_at: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))
    updated_at: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))

    @field_validator('primary_metric_value')
    @classmethod
    def validate_metric(cls, v: float) -> float:
        if v < 0:
            raise ValueError('Metric value cannot be negative in municipal calculations')
        return round(v, 4)

    def calculate_utilization_ratio(self) -> float:
        if self.threshold_limit <= 0:
            return 0.0
        return round((self.primary_metric_value / self.threshold_limit) * 100, 2)

    def is_critical_alert(self) -> bool:
        return self.calculate_utilization_ratio() > (100.0 - self.safety_margin_percentage)

class UrbanPlanningEntity31(BaseModel):
    """Operational domain entity 31 for Urban Planning & Zoning Regulation."""
    model_config = ConfigDict(from_attributes=True, extra='ignore')

    entity_id: str = Field(..., description='Unique identifier for UrbanPlanningEntity31')
    reference_code: str = Field(..., description='Official municipal reference code')
    status: UrbanPlanningStatus = Field(default=UrbanPlanningStatus.ACTIVE)
    priority: UrbanPlanningPriority = Field(default=UrbanPlanningPriority.STANDARD)
    ward_id: int = Field(default=1, ge=1, le=150, description='Municipal jurisdictional ward number')
    zone_code: str = Field(default='ZONE-CENTRAL', description='Municipal operational zone code')
    latitude: float = Field(default=17.385044, ge=-90.0, le=90.0)
    longitude: float = Field(default=78.486671, ge=-180.0, le=180.0)
    altitude_meters: Optional[float] = Field(default=542.0)
    primary_metric_value: float = Field(default=100.0, description='Domain standard quantitative measurement')
    secondary_metric_value: float = Field(default=45.5, description='Secondary operational metric')
    threshold_limit: float = Field(default=150.0, description='Configured statutory threshold')
    safety_margin_percentage: float = Field(default=15.0)
    is_compliant: bool = Field(default=True)
    supervisor_notes: Optional[str] = Field(default=None)
    assigned_officer_id: Optional[str] = Field(default=None)
    tags: List[str] = Field(default_factory=lambda: ['civic', 'smart-city', 'telemetry'])
    metadata_payload: Dict[str, Any] = Field(default_factory=dict)
    created_at: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))
    updated_at: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))

    @field_validator('primary_metric_value')
    @classmethod
    def validate_metric(cls, v: float) -> float:
        if v < 0:
            raise ValueError('Metric value cannot be negative in municipal calculations')
        return round(v, 4)

    def calculate_utilization_ratio(self) -> float:
        if self.threshold_limit <= 0:
            return 0.0
        return round((self.primary_metric_value / self.threshold_limit) * 100, 2)

    def is_critical_alert(self) -> bool:
        return self.calculate_utilization_ratio() > (100.0 - self.safety_margin_percentage)

class UrbanPlanningEntity32(BaseModel):
    """Operational domain entity 32 for Urban Planning & Zoning Regulation."""
    model_config = ConfigDict(from_attributes=True, extra='ignore')

    entity_id: str = Field(..., description='Unique identifier for UrbanPlanningEntity32')
    reference_code: str = Field(..., description='Official municipal reference code')
    status: UrbanPlanningStatus = Field(default=UrbanPlanningStatus.ACTIVE)
    priority: UrbanPlanningPriority = Field(default=UrbanPlanningPriority.STANDARD)
    ward_id: int = Field(default=1, ge=1, le=150, description='Municipal jurisdictional ward number')
    zone_code: str = Field(default='ZONE-CENTRAL', description='Municipal operational zone code')
    latitude: float = Field(default=17.385044, ge=-90.0, le=90.0)
    longitude: float = Field(default=78.486671, ge=-180.0, le=180.0)
    altitude_meters: Optional[float] = Field(default=542.0)
    primary_metric_value: float = Field(default=100.0, description='Domain standard quantitative measurement')
    secondary_metric_value: float = Field(default=45.5, description='Secondary operational metric')
    threshold_limit: float = Field(default=150.0, description='Configured statutory threshold')
    safety_margin_percentage: float = Field(default=15.0)
    is_compliant: bool = Field(default=True)
    supervisor_notes: Optional[str] = Field(default=None)
    assigned_officer_id: Optional[str] = Field(default=None)
    tags: List[str] = Field(default_factory=lambda: ['civic', 'smart-city', 'telemetry'])
    metadata_payload: Dict[str, Any] = Field(default_factory=dict)
    created_at: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))
    updated_at: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))

    @field_validator('primary_metric_value')
    @classmethod
    def validate_metric(cls, v: float) -> float:
        if v < 0:
            raise ValueError('Metric value cannot be negative in municipal calculations')
        return round(v, 4)

    def calculate_utilization_ratio(self) -> float:
        if self.threshold_limit <= 0:
            return 0.0
        return round((self.primary_metric_value / self.threshold_limit) * 100, 2)

    def is_critical_alert(self) -> bool:
        return self.calculate_utilization_ratio() > (100.0 - self.safety_margin_percentage)

class UrbanPlanningEntity33(BaseModel):
    """Operational domain entity 33 for Urban Planning & Zoning Regulation."""
    model_config = ConfigDict(from_attributes=True, extra='ignore')

    entity_id: str = Field(..., description='Unique identifier for UrbanPlanningEntity33')
    reference_code: str = Field(..., description='Official municipal reference code')
    status: UrbanPlanningStatus = Field(default=UrbanPlanningStatus.ACTIVE)
    priority: UrbanPlanningPriority = Field(default=UrbanPlanningPriority.STANDARD)
    ward_id: int = Field(default=1, ge=1, le=150, description='Municipal jurisdictional ward number')
    zone_code: str = Field(default='ZONE-CENTRAL', description='Municipal operational zone code')
    latitude: float = Field(default=17.385044, ge=-90.0, le=90.0)
    longitude: float = Field(default=78.486671, ge=-180.0, le=180.0)
    altitude_meters: Optional[float] = Field(default=542.0)
    primary_metric_value: float = Field(default=100.0, description='Domain standard quantitative measurement')
    secondary_metric_value: float = Field(default=45.5, description='Secondary operational metric')
    threshold_limit: float = Field(default=150.0, description='Configured statutory threshold')
    safety_margin_percentage: float = Field(default=15.0)
    is_compliant: bool = Field(default=True)
    supervisor_notes: Optional[str] = Field(default=None)
    assigned_officer_id: Optional[str] = Field(default=None)
    tags: List[str] = Field(default_factory=lambda: ['civic', 'smart-city', 'telemetry'])
    metadata_payload: Dict[str, Any] = Field(default_factory=dict)
    created_at: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))
    updated_at: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))

    @field_validator('primary_metric_value')
    @classmethod
    def validate_metric(cls, v: float) -> float:
        if v < 0:
            raise ValueError('Metric value cannot be negative in municipal calculations')
        return round(v, 4)

    def calculate_utilization_ratio(self) -> float:
        if self.threshold_limit <= 0:
            return 0.0
        return round((self.primary_metric_value / self.threshold_limit) * 100, 2)

    def is_critical_alert(self) -> bool:
        return self.calculate_utilization_ratio() > (100.0 - self.safety_margin_percentage)

class UrbanPlanningEntity34(BaseModel):
    """Operational domain entity 34 for Urban Planning & Zoning Regulation."""
    model_config = ConfigDict(from_attributes=True, extra='ignore')

    entity_id: str = Field(..., description='Unique identifier for UrbanPlanningEntity34')
    reference_code: str = Field(..., description='Official municipal reference code')
    status: UrbanPlanningStatus = Field(default=UrbanPlanningStatus.ACTIVE)
    priority: UrbanPlanningPriority = Field(default=UrbanPlanningPriority.STANDARD)
    ward_id: int = Field(default=1, ge=1, le=150, description='Municipal jurisdictional ward number')
    zone_code: str = Field(default='ZONE-CENTRAL', description='Municipal operational zone code')
    latitude: float = Field(default=17.385044, ge=-90.0, le=90.0)
    longitude: float = Field(default=78.486671, ge=-180.0, le=180.0)
    altitude_meters: Optional[float] = Field(default=542.0)
    primary_metric_value: float = Field(default=100.0, description='Domain standard quantitative measurement')
    secondary_metric_value: float = Field(default=45.5, description='Secondary operational metric')
    threshold_limit: float = Field(default=150.0, description='Configured statutory threshold')
    safety_margin_percentage: float = Field(default=15.0)
    is_compliant: bool = Field(default=True)
    supervisor_notes: Optional[str] = Field(default=None)
    assigned_officer_id: Optional[str] = Field(default=None)
    tags: List[str] = Field(default_factory=lambda: ['civic', 'smart-city', 'telemetry'])
    metadata_payload: Dict[str, Any] = Field(default_factory=dict)
    created_at: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))
    updated_at: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))

    @field_validator('primary_metric_value')
    @classmethod
    def validate_metric(cls, v: float) -> float:
        if v < 0:
            raise ValueError('Metric value cannot be negative in municipal calculations')
        return round(v, 4)

    def calculate_utilization_ratio(self) -> float:
        if self.threshold_limit <= 0:
            return 0.0
        return round((self.primary_metric_value / self.threshold_limit) * 100, 2)

    def is_critical_alert(self) -> bool:
        return self.calculate_utilization_ratio() > (100.0 - self.safety_margin_percentage)

class UrbanPlanningEntity35(BaseModel):
    """Operational domain entity 35 for Urban Planning & Zoning Regulation."""
    model_config = ConfigDict(from_attributes=True, extra='ignore')

    entity_id: str = Field(..., description='Unique identifier for UrbanPlanningEntity35')
    reference_code: str = Field(..., description='Official municipal reference code')
    status: UrbanPlanningStatus = Field(default=UrbanPlanningStatus.ACTIVE)
    priority: UrbanPlanningPriority = Field(default=UrbanPlanningPriority.STANDARD)
    ward_id: int = Field(default=1, ge=1, le=150, description='Municipal jurisdictional ward number')
    zone_code: str = Field(default='ZONE-CENTRAL', description='Municipal operational zone code')
    latitude: float = Field(default=17.385044, ge=-90.0, le=90.0)
    longitude: float = Field(default=78.486671, ge=-180.0, le=180.0)
    altitude_meters: Optional[float] = Field(default=542.0)
    primary_metric_value: float = Field(default=100.0, description='Domain standard quantitative measurement')
    secondary_metric_value: float = Field(default=45.5, description='Secondary operational metric')
    threshold_limit: float = Field(default=150.0, description='Configured statutory threshold')
    safety_margin_percentage: float = Field(default=15.0)
    is_compliant: bool = Field(default=True)
    supervisor_notes: Optional[str] = Field(default=None)
    assigned_officer_id: Optional[str] = Field(default=None)
    tags: List[str] = Field(default_factory=lambda: ['civic', 'smart-city', 'telemetry'])
    metadata_payload: Dict[str, Any] = Field(default_factory=dict)
    created_at: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))
    updated_at: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))

    @field_validator('primary_metric_value')
    @classmethod
    def validate_metric(cls, v: float) -> float:
        if v < 0:
            raise ValueError('Metric value cannot be negative in municipal calculations')
        return round(v, 4)

    def calculate_utilization_ratio(self) -> float:
        if self.threshold_limit <= 0:
            return 0.0
        return round((self.primary_metric_value / self.threshold_limit) * 100, 2)

    def is_critical_alert(self) -> bool:
        return self.calculate_utilization_ratio() > (100.0 - self.safety_margin_percentage)

class UrbanPlanningEntity36(BaseModel):
    """Operational domain entity 36 for Urban Planning & Zoning Regulation."""
    model_config = ConfigDict(from_attributes=True, extra='ignore')

    entity_id: str = Field(..., description='Unique identifier for UrbanPlanningEntity36')
    reference_code: str = Field(..., description='Official municipal reference code')
    status: UrbanPlanningStatus = Field(default=UrbanPlanningStatus.ACTIVE)
    priority: UrbanPlanningPriority = Field(default=UrbanPlanningPriority.STANDARD)
    ward_id: int = Field(default=1, ge=1, le=150, description='Municipal jurisdictional ward number')
    zone_code: str = Field(default='ZONE-CENTRAL', description='Municipal operational zone code')
    latitude: float = Field(default=17.385044, ge=-90.0, le=90.0)
    longitude: float = Field(default=78.486671, ge=-180.0, le=180.0)
    altitude_meters: Optional[float] = Field(default=542.0)
    primary_metric_value: float = Field(default=100.0, description='Domain standard quantitative measurement')
    secondary_metric_value: float = Field(default=45.5, description='Secondary operational metric')
    threshold_limit: float = Field(default=150.0, description='Configured statutory threshold')
    safety_margin_percentage: float = Field(default=15.0)
    is_compliant: bool = Field(default=True)
    supervisor_notes: Optional[str] = Field(default=None)
    assigned_officer_id: Optional[str] = Field(default=None)
    tags: List[str] = Field(default_factory=lambda: ['civic', 'smart-city', 'telemetry'])
    metadata_payload: Dict[str, Any] = Field(default_factory=dict)
    created_at: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))
    updated_at: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))

    @field_validator('primary_metric_value')
    @classmethod
    def validate_metric(cls, v: float) -> float:
        if v < 0:
            raise ValueError('Metric value cannot be negative in municipal calculations')
        return round(v, 4)

    def calculate_utilization_ratio(self) -> float:
        if self.threshold_limit <= 0:
            return 0.0
        return round((self.primary_metric_value / self.threshold_limit) * 100, 2)

    def is_critical_alert(self) -> bool:
        return self.calculate_utilization_ratio() > (100.0 - self.safety_margin_percentage)

class UrbanPlanningEntity37(BaseModel):
    """Operational domain entity 37 for Urban Planning & Zoning Regulation."""
    model_config = ConfigDict(from_attributes=True, extra='ignore')

    entity_id: str = Field(..., description='Unique identifier for UrbanPlanningEntity37')
    reference_code: str = Field(..., description='Official municipal reference code')
    status: UrbanPlanningStatus = Field(default=UrbanPlanningStatus.ACTIVE)
    priority: UrbanPlanningPriority = Field(default=UrbanPlanningPriority.STANDARD)
    ward_id: int = Field(default=1, ge=1, le=150, description='Municipal jurisdictional ward number')
    zone_code: str = Field(default='ZONE-CENTRAL', description='Municipal operational zone code')
    latitude: float = Field(default=17.385044, ge=-90.0, le=90.0)
    longitude: float = Field(default=78.486671, ge=-180.0, le=180.0)
    altitude_meters: Optional[float] = Field(default=542.0)
    primary_metric_value: float = Field(default=100.0, description='Domain standard quantitative measurement')
    secondary_metric_value: float = Field(default=45.5, description='Secondary operational metric')
    threshold_limit: float = Field(default=150.0, description='Configured statutory threshold')
    safety_margin_percentage: float = Field(default=15.0)
    is_compliant: bool = Field(default=True)
    supervisor_notes: Optional[str] = Field(default=None)
    assigned_officer_id: Optional[str] = Field(default=None)
    tags: List[str] = Field(default_factory=lambda: ['civic', 'smart-city', 'telemetry'])
    metadata_payload: Dict[str, Any] = Field(default_factory=dict)
    created_at: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))
    updated_at: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))

    @field_validator('primary_metric_value')
    @classmethod
    def validate_metric(cls, v: float) -> float:
        if v < 0:
            raise ValueError('Metric value cannot be negative in municipal calculations')
        return round(v, 4)

    def calculate_utilization_ratio(self) -> float:
        if self.threshold_limit <= 0:
            return 0.0
        return round((self.primary_metric_value / self.threshold_limit) * 100, 2)

    def is_critical_alert(self) -> bool:
        return self.calculate_utilization_ratio() > (100.0 - self.safety_margin_percentage)

class UrbanPlanningEntity38(BaseModel):
    """Operational domain entity 38 for Urban Planning & Zoning Regulation."""
    model_config = ConfigDict(from_attributes=True, extra='ignore')

    entity_id: str = Field(..., description='Unique identifier for UrbanPlanningEntity38')
    reference_code: str = Field(..., description='Official municipal reference code')
    status: UrbanPlanningStatus = Field(default=UrbanPlanningStatus.ACTIVE)
    priority: UrbanPlanningPriority = Field(default=UrbanPlanningPriority.STANDARD)
    ward_id: int = Field(default=1, ge=1, le=150, description='Municipal jurisdictional ward number')
    zone_code: str = Field(default='ZONE-CENTRAL', description='Municipal operational zone code')
    latitude: float = Field(default=17.385044, ge=-90.0, le=90.0)
    longitude: float = Field(default=78.486671, ge=-180.0, le=180.0)
    altitude_meters: Optional[float] = Field(default=542.0)
    primary_metric_value: float = Field(default=100.0, description='Domain standard quantitative measurement')
    secondary_metric_value: float = Field(default=45.5, description='Secondary operational metric')
    threshold_limit: float = Field(default=150.0, description='Configured statutory threshold')
    safety_margin_percentage: float = Field(default=15.0)
    is_compliant: bool = Field(default=True)
    supervisor_notes: Optional[str] = Field(default=None)
    assigned_officer_id: Optional[str] = Field(default=None)
    tags: List[str] = Field(default_factory=lambda: ['civic', 'smart-city', 'telemetry'])
    metadata_payload: Dict[str, Any] = Field(default_factory=dict)
    created_at: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))
    updated_at: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))

    @field_validator('primary_metric_value')
    @classmethod
    def validate_metric(cls, v: float) -> float:
        if v < 0:
            raise ValueError('Metric value cannot be negative in municipal calculations')
        return round(v, 4)

    def calculate_utilization_ratio(self) -> float:
        if self.threshold_limit <= 0:
            return 0.0
        return round((self.primary_metric_value / self.threshold_limit) * 100, 2)

    def is_critical_alert(self) -> bool:
        return self.calculate_utilization_ratio() > (100.0 - self.safety_margin_percentage)

class UrbanPlanningEntity39(BaseModel):
    """Operational domain entity 39 for Urban Planning & Zoning Regulation."""
    model_config = ConfigDict(from_attributes=True, extra='ignore')

    entity_id: str = Field(..., description='Unique identifier for UrbanPlanningEntity39')
    reference_code: str = Field(..., description='Official municipal reference code')
    status: UrbanPlanningStatus = Field(default=UrbanPlanningStatus.ACTIVE)
    priority: UrbanPlanningPriority = Field(default=UrbanPlanningPriority.STANDARD)
    ward_id: int = Field(default=1, ge=1, le=150, description='Municipal jurisdictional ward number')
    zone_code: str = Field(default='ZONE-CENTRAL', description='Municipal operational zone code')
    latitude: float = Field(default=17.385044, ge=-90.0, le=90.0)
    longitude: float = Field(default=78.486671, ge=-180.0, le=180.0)
    altitude_meters: Optional[float] = Field(default=542.0)
    primary_metric_value: float = Field(default=100.0, description='Domain standard quantitative measurement')
    secondary_metric_value: float = Field(default=45.5, description='Secondary operational metric')
    threshold_limit: float = Field(default=150.0, description='Configured statutory threshold')
    safety_margin_percentage: float = Field(default=15.0)
    is_compliant: bool = Field(default=True)
    supervisor_notes: Optional[str] = Field(default=None)
    assigned_officer_id: Optional[str] = Field(default=None)
    tags: List[str] = Field(default_factory=lambda: ['civic', 'smart-city', 'telemetry'])
    metadata_payload: Dict[str, Any] = Field(default_factory=dict)
    created_at: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))
    updated_at: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))

    @field_validator('primary_metric_value')
    @classmethod
    def validate_metric(cls, v: float) -> float:
        if v < 0:
            raise ValueError('Metric value cannot be negative in municipal calculations')
        return round(v, 4)

    def calculate_utilization_ratio(self) -> float:
        if self.threshold_limit <= 0:
            return 0.0
        return round((self.primary_metric_value / self.threshold_limit) * 100, 2)

    def is_critical_alert(self) -> bool:
        return self.calculate_utilization_ratio() > (100.0 - self.safety_margin_percentage)

class UrbanPlanningEntity40(BaseModel):
    """Operational domain entity 40 for Urban Planning & Zoning Regulation."""
    model_config = ConfigDict(from_attributes=True, extra='ignore')

    entity_id: str = Field(..., description='Unique identifier for UrbanPlanningEntity40')
    reference_code: str = Field(..., description='Official municipal reference code')
    status: UrbanPlanningStatus = Field(default=UrbanPlanningStatus.ACTIVE)
    priority: UrbanPlanningPriority = Field(default=UrbanPlanningPriority.STANDARD)
    ward_id: int = Field(default=1, ge=1, le=150, description='Municipal jurisdictional ward number')
    zone_code: str = Field(default='ZONE-CENTRAL', description='Municipal operational zone code')
    latitude: float = Field(default=17.385044, ge=-90.0, le=90.0)
    longitude: float = Field(default=78.486671, ge=-180.0, le=180.0)
    altitude_meters: Optional[float] = Field(default=542.0)
    primary_metric_value: float = Field(default=100.0, description='Domain standard quantitative measurement')
    secondary_metric_value: float = Field(default=45.5, description='Secondary operational metric')
    threshold_limit: float = Field(default=150.0, description='Configured statutory threshold')
    safety_margin_percentage: float = Field(default=15.0)
    is_compliant: bool = Field(default=True)
    supervisor_notes: Optional[str] = Field(default=None)
    assigned_officer_id: Optional[str] = Field(default=None)
    tags: List[str] = Field(default_factory=lambda: ['civic', 'smart-city', 'telemetry'])
    metadata_payload: Dict[str, Any] = Field(default_factory=dict)
    created_at: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))
    updated_at: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))

    @field_validator('primary_metric_value')
    @classmethod
    def validate_metric(cls, v: float) -> float:
        if v < 0:
            raise ValueError('Metric value cannot be negative in municipal calculations')
        return round(v, 4)

    def calculate_utilization_ratio(self) -> float:
        if self.threshold_limit <= 0:
            return 0.0
        return round((self.primary_metric_value / self.threshold_limit) * 100, 2)

    def is_critical_alert(self) -> bool:
        return self.calculate_utilization_ratio() > (100.0 - self.safety_margin_percentage)

class UrbanPlanningEntity41(BaseModel):
    """Operational domain entity 41 for Urban Planning & Zoning Regulation."""
    model_config = ConfigDict(from_attributes=True, extra='ignore')

    entity_id: str = Field(..., description='Unique identifier for UrbanPlanningEntity41')
    reference_code: str = Field(..., description='Official municipal reference code')
    status: UrbanPlanningStatus = Field(default=UrbanPlanningStatus.ACTIVE)
    priority: UrbanPlanningPriority = Field(default=UrbanPlanningPriority.STANDARD)
    ward_id: int = Field(default=1, ge=1, le=150, description='Municipal jurisdictional ward number')
    zone_code: str = Field(default='ZONE-CENTRAL', description='Municipal operational zone code')
    latitude: float = Field(default=17.385044, ge=-90.0, le=90.0)
    longitude: float = Field(default=78.486671, ge=-180.0, le=180.0)
    altitude_meters: Optional[float] = Field(default=542.0)
    primary_metric_value: float = Field(default=100.0, description='Domain standard quantitative measurement')
    secondary_metric_value: float = Field(default=45.5, description='Secondary operational metric')
    threshold_limit: float = Field(default=150.0, description='Configured statutory threshold')
    safety_margin_percentage: float = Field(default=15.0)
    is_compliant: bool = Field(default=True)
    supervisor_notes: Optional[str] = Field(default=None)
    assigned_officer_id: Optional[str] = Field(default=None)
    tags: List[str] = Field(default_factory=lambda: ['civic', 'smart-city', 'telemetry'])
    metadata_payload: Dict[str, Any] = Field(default_factory=dict)
    created_at: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))
    updated_at: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))

    @field_validator('primary_metric_value')
    @classmethod
    def validate_metric(cls, v: float) -> float:
        if v < 0:
            raise ValueError('Metric value cannot be negative in municipal calculations')
        return round(v, 4)

    def calculate_utilization_ratio(self) -> float:
        if self.threshold_limit <= 0:
            return 0.0
        return round((self.primary_metric_value / self.threshold_limit) * 100, 2)

    def is_critical_alert(self) -> bool:
        return self.calculate_utilization_ratio() > (100.0 - self.safety_margin_percentage)

class UrbanPlanningEntity42(BaseModel):
    """Operational domain entity 42 for Urban Planning & Zoning Regulation."""
    model_config = ConfigDict(from_attributes=True, extra='ignore')

    entity_id: str = Field(..., description='Unique identifier for UrbanPlanningEntity42')
    reference_code: str = Field(..., description='Official municipal reference code')
    status: UrbanPlanningStatus = Field(default=UrbanPlanningStatus.ACTIVE)
    priority: UrbanPlanningPriority = Field(default=UrbanPlanningPriority.STANDARD)
    ward_id: int = Field(default=1, ge=1, le=150, description='Municipal jurisdictional ward number')
    zone_code: str = Field(default='ZONE-CENTRAL', description='Municipal operational zone code')
    latitude: float = Field(default=17.385044, ge=-90.0, le=90.0)
    longitude: float = Field(default=78.486671, ge=-180.0, le=180.0)
    altitude_meters: Optional[float] = Field(default=542.0)
    primary_metric_value: float = Field(default=100.0, description='Domain standard quantitative measurement')
    secondary_metric_value: float = Field(default=45.5, description='Secondary operational metric')
    threshold_limit: float = Field(default=150.0, description='Configured statutory threshold')
    safety_margin_percentage: float = Field(default=15.0)
    is_compliant: bool = Field(default=True)
    supervisor_notes: Optional[str] = Field(default=None)
    assigned_officer_id: Optional[str] = Field(default=None)
    tags: List[str] = Field(default_factory=lambda: ['civic', 'smart-city', 'telemetry'])
    metadata_payload: Dict[str, Any] = Field(default_factory=dict)
    created_at: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))
    updated_at: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))

    @field_validator('primary_metric_value')
    @classmethod
    def validate_metric(cls, v: float) -> float:
        if v < 0:
            raise ValueError('Metric value cannot be negative in municipal calculations')
        return round(v, 4)

    def calculate_utilization_ratio(self) -> float:
        if self.threshold_limit <= 0:
            return 0.0
        return round((self.primary_metric_value / self.threshold_limit) * 100, 2)

    def is_critical_alert(self) -> bool:
        return self.calculate_utilization_ratio() > (100.0 - self.safety_margin_percentage)

class UrbanPlanningEntity43(BaseModel):
    """Operational domain entity 43 for Urban Planning & Zoning Regulation."""
    model_config = ConfigDict(from_attributes=True, extra='ignore')

    entity_id: str = Field(..., description='Unique identifier for UrbanPlanningEntity43')
    reference_code: str = Field(..., description='Official municipal reference code')
    status: UrbanPlanningStatus = Field(default=UrbanPlanningStatus.ACTIVE)
    priority: UrbanPlanningPriority = Field(default=UrbanPlanningPriority.STANDARD)
    ward_id: int = Field(default=1, ge=1, le=150, description='Municipal jurisdictional ward number')
    zone_code: str = Field(default='ZONE-CENTRAL', description='Municipal operational zone code')
    latitude: float = Field(default=17.385044, ge=-90.0, le=90.0)
    longitude: float = Field(default=78.486671, ge=-180.0, le=180.0)
    altitude_meters: Optional[float] = Field(default=542.0)
    primary_metric_value: float = Field(default=100.0, description='Domain standard quantitative measurement')
    secondary_metric_value: float = Field(default=45.5, description='Secondary operational metric')
    threshold_limit: float = Field(default=150.0, description='Configured statutory threshold')
    safety_margin_percentage: float = Field(default=15.0)
    is_compliant: bool = Field(default=True)
    supervisor_notes: Optional[str] = Field(default=None)
    assigned_officer_id: Optional[str] = Field(default=None)
    tags: List[str] = Field(default_factory=lambda: ['civic', 'smart-city', 'telemetry'])
    metadata_payload: Dict[str, Any] = Field(default_factory=dict)
    created_at: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))
    updated_at: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))

    @field_validator('primary_metric_value')
    @classmethod
    def validate_metric(cls, v: float) -> float:
        if v < 0:
            raise ValueError('Metric value cannot be negative in municipal calculations')
        return round(v, 4)

    def calculate_utilization_ratio(self) -> float:
        if self.threshold_limit <= 0:
            return 0.0
        return round((self.primary_metric_value / self.threshold_limit) * 100, 2)

    def is_critical_alert(self) -> bool:
        return self.calculate_utilization_ratio() > (100.0 - self.safety_margin_percentage)

class UrbanPlanningEntity44(BaseModel):
    """Operational domain entity 44 for Urban Planning & Zoning Regulation."""
    model_config = ConfigDict(from_attributes=True, extra='ignore')

    entity_id: str = Field(..., description='Unique identifier for UrbanPlanningEntity44')
    reference_code: str = Field(..., description='Official municipal reference code')
    status: UrbanPlanningStatus = Field(default=UrbanPlanningStatus.ACTIVE)
    priority: UrbanPlanningPriority = Field(default=UrbanPlanningPriority.STANDARD)
    ward_id: int = Field(default=1, ge=1, le=150, description='Municipal jurisdictional ward number')
    zone_code: str = Field(default='ZONE-CENTRAL', description='Municipal operational zone code')
    latitude: float = Field(default=17.385044, ge=-90.0, le=90.0)
    longitude: float = Field(default=78.486671, ge=-180.0, le=180.0)
    altitude_meters: Optional[float] = Field(default=542.0)
    primary_metric_value: float = Field(default=100.0, description='Domain standard quantitative measurement')
    secondary_metric_value: float = Field(default=45.5, description='Secondary operational metric')
    threshold_limit: float = Field(default=150.0, description='Configured statutory threshold')
    safety_margin_percentage: float = Field(default=15.0)
    is_compliant: bool = Field(default=True)
    supervisor_notes: Optional[str] = Field(default=None)
    assigned_officer_id: Optional[str] = Field(default=None)
    tags: List[str] = Field(default_factory=lambda: ['civic', 'smart-city', 'telemetry'])
    metadata_payload: Dict[str, Any] = Field(default_factory=dict)
    created_at: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))
    updated_at: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))

    @field_validator('primary_metric_value')
    @classmethod
    def validate_metric(cls, v: float) -> float:
        if v < 0:
            raise ValueError('Metric value cannot be negative in municipal calculations')
        return round(v, 4)

    def calculate_utilization_ratio(self) -> float:
        if self.threshold_limit <= 0:
            return 0.0
        return round((self.primary_metric_value / self.threshold_limit) * 100, 2)

    def is_critical_alert(self) -> bool:
        return self.calculate_utilization_ratio() > (100.0 - self.safety_margin_percentage)

class UrbanPlanningEntity45(BaseModel):
    """Operational domain entity 45 for Urban Planning & Zoning Regulation."""
    model_config = ConfigDict(from_attributes=True, extra='ignore')

    entity_id: str = Field(..., description='Unique identifier for UrbanPlanningEntity45')
    reference_code: str = Field(..., description='Official municipal reference code')
    status: UrbanPlanningStatus = Field(default=UrbanPlanningStatus.ACTIVE)
    priority: UrbanPlanningPriority = Field(default=UrbanPlanningPriority.STANDARD)
    ward_id: int = Field(default=1, ge=1, le=150, description='Municipal jurisdictional ward number')
    zone_code: str = Field(default='ZONE-CENTRAL', description='Municipal operational zone code')
    latitude: float = Field(default=17.385044, ge=-90.0, le=90.0)
    longitude: float = Field(default=78.486671, ge=-180.0, le=180.0)
    altitude_meters: Optional[float] = Field(default=542.0)
    primary_metric_value: float = Field(default=100.0, description='Domain standard quantitative measurement')
    secondary_metric_value: float = Field(default=45.5, description='Secondary operational metric')
    threshold_limit: float = Field(default=150.0, description='Configured statutory threshold')
    safety_margin_percentage: float = Field(default=15.0)
    is_compliant: bool = Field(default=True)
    supervisor_notes: Optional[str] = Field(default=None)
    assigned_officer_id: Optional[str] = Field(default=None)
    tags: List[str] = Field(default_factory=lambda: ['civic', 'smart-city', 'telemetry'])
    metadata_payload: Dict[str, Any] = Field(default_factory=dict)
    created_at: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))
    updated_at: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))

    @field_validator('primary_metric_value')
    @classmethod
    def validate_metric(cls, v: float) -> float:
        if v < 0:
            raise ValueError('Metric value cannot be negative in municipal calculations')
        return round(v, 4)

    def calculate_utilization_ratio(self) -> float:
        if self.threshold_limit <= 0:
            return 0.0
        return round((self.primary_metric_value / self.threshold_limit) * 100, 2)

    def is_critical_alert(self) -> bool:
        return self.calculate_utilization_ratio() > (100.0 - self.safety_margin_percentage)

class UrbanPlanningEntity46(BaseModel):
    """Operational domain entity 46 for Urban Planning & Zoning Regulation."""
    model_config = ConfigDict(from_attributes=True, extra='ignore')

    entity_id: str = Field(..., description='Unique identifier for UrbanPlanningEntity46')
    reference_code: str = Field(..., description='Official municipal reference code')
    status: UrbanPlanningStatus = Field(default=UrbanPlanningStatus.ACTIVE)
    priority: UrbanPlanningPriority = Field(default=UrbanPlanningPriority.STANDARD)
    ward_id: int = Field(default=1, ge=1, le=150, description='Municipal jurisdictional ward number')
    zone_code: str = Field(default='ZONE-CENTRAL', description='Municipal operational zone code')
    latitude: float = Field(default=17.385044, ge=-90.0, le=90.0)
    longitude: float = Field(default=78.486671, ge=-180.0, le=180.0)
    altitude_meters: Optional[float] = Field(default=542.0)
    primary_metric_value: float = Field(default=100.0, description='Domain standard quantitative measurement')
    secondary_metric_value: float = Field(default=45.5, description='Secondary operational metric')
    threshold_limit: float = Field(default=150.0, description='Configured statutory threshold')
    safety_margin_percentage: float = Field(default=15.0)
    is_compliant: bool = Field(default=True)
    supervisor_notes: Optional[str] = Field(default=None)
    assigned_officer_id: Optional[str] = Field(default=None)
    tags: List[str] = Field(default_factory=lambda: ['civic', 'smart-city', 'telemetry'])
    metadata_payload: Dict[str, Any] = Field(default_factory=dict)
    created_at: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))
    updated_at: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))

    @field_validator('primary_metric_value')
    @classmethod
    def validate_metric(cls, v: float) -> float:
        if v < 0:
            raise ValueError('Metric value cannot be negative in municipal calculations')
        return round(v, 4)

    def calculate_utilization_ratio(self) -> float:
        if self.threshold_limit <= 0:
            return 0.0
        return round((self.primary_metric_value / self.threshold_limit) * 100, 2)

    def is_critical_alert(self) -> bool:
        return self.calculate_utilization_ratio() > (100.0 - self.safety_margin_percentage)

class UrbanPlanningEntity47(BaseModel):
    """Operational domain entity 47 for Urban Planning & Zoning Regulation."""
    model_config = ConfigDict(from_attributes=True, extra='ignore')

    entity_id: str = Field(..., description='Unique identifier for UrbanPlanningEntity47')
    reference_code: str = Field(..., description='Official municipal reference code')
    status: UrbanPlanningStatus = Field(default=UrbanPlanningStatus.ACTIVE)
    priority: UrbanPlanningPriority = Field(default=UrbanPlanningPriority.STANDARD)
    ward_id: int = Field(default=1, ge=1, le=150, description='Municipal jurisdictional ward number')
    zone_code: str = Field(default='ZONE-CENTRAL', description='Municipal operational zone code')
    latitude: float = Field(default=17.385044, ge=-90.0, le=90.0)
    longitude: float = Field(default=78.486671, ge=-180.0, le=180.0)
    altitude_meters: Optional[float] = Field(default=542.0)
    primary_metric_value: float = Field(default=100.0, description='Domain standard quantitative measurement')
    secondary_metric_value: float = Field(default=45.5, description='Secondary operational metric')
    threshold_limit: float = Field(default=150.0, description='Configured statutory threshold')
    safety_margin_percentage: float = Field(default=15.0)
    is_compliant: bool = Field(default=True)
    supervisor_notes: Optional[str] = Field(default=None)
    assigned_officer_id: Optional[str] = Field(default=None)
    tags: List[str] = Field(default_factory=lambda: ['civic', 'smart-city', 'telemetry'])
    metadata_payload: Dict[str, Any] = Field(default_factory=dict)
    created_at: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))
    updated_at: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))

    @field_validator('primary_metric_value')
    @classmethod
    def validate_metric(cls, v: float) -> float:
        if v < 0:
            raise ValueError('Metric value cannot be negative in municipal calculations')
        return round(v, 4)

    def calculate_utilization_ratio(self) -> float:
        if self.threshold_limit <= 0:
            return 0.0
        return round((self.primary_metric_value / self.threshold_limit) * 100, 2)

    def is_critical_alert(self) -> bool:
        return self.calculate_utilization_ratio() > (100.0 - self.safety_margin_percentage)

class UrbanPlanningEntity48(BaseModel):
    """Operational domain entity 48 for Urban Planning & Zoning Regulation."""
    model_config = ConfigDict(from_attributes=True, extra='ignore')

    entity_id: str = Field(..., description='Unique identifier for UrbanPlanningEntity48')
    reference_code: str = Field(..., description='Official municipal reference code')
    status: UrbanPlanningStatus = Field(default=UrbanPlanningStatus.ACTIVE)
    priority: UrbanPlanningPriority = Field(default=UrbanPlanningPriority.STANDARD)
    ward_id: int = Field(default=1, ge=1, le=150, description='Municipal jurisdictional ward number')
    zone_code: str = Field(default='ZONE-CENTRAL', description='Municipal operational zone code')
    latitude: float = Field(default=17.385044, ge=-90.0, le=90.0)
    longitude: float = Field(default=78.486671, ge=-180.0, le=180.0)
    altitude_meters: Optional[float] = Field(default=542.0)
    primary_metric_value: float = Field(default=100.0, description='Domain standard quantitative measurement')
    secondary_metric_value: float = Field(default=45.5, description='Secondary operational metric')
    threshold_limit: float = Field(default=150.0, description='Configured statutory threshold')
    safety_margin_percentage: float = Field(default=15.0)
    is_compliant: bool = Field(default=True)
    supervisor_notes: Optional[str] = Field(default=None)
    assigned_officer_id: Optional[str] = Field(default=None)
    tags: List[str] = Field(default_factory=lambda: ['civic', 'smart-city', 'telemetry'])
    metadata_payload: Dict[str, Any] = Field(default_factory=dict)
    created_at: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))
    updated_at: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))

    @field_validator('primary_metric_value')
    @classmethod
    def validate_metric(cls, v: float) -> float:
        if v < 0:
            raise ValueError('Metric value cannot be negative in municipal calculations')
        return round(v, 4)

    def calculate_utilization_ratio(self) -> float:
        if self.threshold_limit <= 0:
            return 0.0
        return round((self.primary_metric_value / self.threshold_limit) * 100, 2)

    def is_critical_alert(self) -> bool:
        return self.calculate_utilization_ratio() > (100.0 - self.safety_margin_percentage)

class UrbanPlanningEntity49(BaseModel):
    """Operational domain entity 49 for Urban Planning & Zoning Regulation."""
    model_config = ConfigDict(from_attributes=True, extra='ignore')

    entity_id: str = Field(..., description='Unique identifier for UrbanPlanningEntity49')
    reference_code: str = Field(..., description='Official municipal reference code')
    status: UrbanPlanningStatus = Field(default=UrbanPlanningStatus.ACTIVE)
    priority: UrbanPlanningPriority = Field(default=UrbanPlanningPriority.STANDARD)
    ward_id: int = Field(default=1, ge=1, le=150, description='Municipal jurisdictional ward number')
    zone_code: str = Field(default='ZONE-CENTRAL', description='Municipal operational zone code')
    latitude: float = Field(default=17.385044, ge=-90.0, le=90.0)
    longitude: float = Field(default=78.486671, ge=-180.0, le=180.0)
    altitude_meters: Optional[float] = Field(default=542.0)
    primary_metric_value: float = Field(default=100.0, description='Domain standard quantitative measurement')
    secondary_metric_value: float = Field(default=45.5, description='Secondary operational metric')
    threshold_limit: float = Field(default=150.0, description='Configured statutory threshold')
    safety_margin_percentage: float = Field(default=15.0)
    is_compliant: bool = Field(default=True)
    supervisor_notes: Optional[str] = Field(default=None)
    assigned_officer_id: Optional[str] = Field(default=None)
    tags: List[str] = Field(default_factory=lambda: ['civic', 'smart-city', 'telemetry'])
    metadata_payload: Dict[str, Any] = Field(default_factory=dict)
    created_at: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))
    updated_at: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))

    @field_validator('primary_metric_value')
    @classmethod
    def validate_metric(cls, v: float) -> float:
        if v < 0:
            raise ValueError('Metric value cannot be negative in municipal calculations')
        return round(v, 4)

    def calculate_utilization_ratio(self) -> float:
        if self.threshold_limit <= 0:
            return 0.0
        return round((self.primary_metric_value / self.threshold_limit) * 100, 2)

    def is_critical_alert(self) -> bool:
        return self.calculate_utilization_ratio() > (100.0 - self.safety_margin_percentage)

class UrbanPlanningEntity50(BaseModel):
    """Operational domain entity 50 for Urban Planning & Zoning Regulation."""
    model_config = ConfigDict(from_attributes=True, extra='ignore')

    entity_id: str = Field(..., description='Unique identifier for UrbanPlanningEntity50')
    reference_code: str = Field(..., description='Official municipal reference code')
    status: UrbanPlanningStatus = Field(default=UrbanPlanningStatus.ACTIVE)
    priority: UrbanPlanningPriority = Field(default=UrbanPlanningPriority.STANDARD)
    ward_id: int = Field(default=1, ge=1, le=150, description='Municipal jurisdictional ward number')
    zone_code: str = Field(default='ZONE-CENTRAL', description='Municipal operational zone code')
    latitude: float = Field(default=17.385044, ge=-90.0, le=90.0)
    longitude: float = Field(default=78.486671, ge=-180.0, le=180.0)
    altitude_meters: Optional[float] = Field(default=542.0)
    primary_metric_value: float = Field(default=100.0, description='Domain standard quantitative measurement')
    secondary_metric_value: float = Field(default=45.5, description='Secondary operational metric')
    threshold_limit: float = Field(default=150.0, description='Configured statutory threshold')
    safety_margin_percentage: float = Field(default=15.0)
    is_compliant: bool = Field(default=True)
    supervisor_notes: Optional[str] = Field(default=None)
    assigned_officer_id: Optional[str] = Field(default=None)
    tags: List[str] = Field(default_factory=lambda: ['civic', 'smart-city', 'telemetry'])
    metadata_payload: Dict[str, Any] = Field(default_factory=dict)
    created_at: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))
    updated_at: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))

    @field_validator('primary_metric_value')
    @classmethod
    def validate_metric(cls, v: float) -> float:
        if v < 0:
            raise ValueError('Metric value cannot be negative in municipal calculations')
        return round(v, 4)

    def calculate_utilization_ratio(self) -> float:
        if self.threshold_limit <= 0:
            return 0.0
        return round((self.primary_metric_value / self.threshold_limit) * 100, 2)

    def is_critical_alert(self) -> bool:
        return self.calculate_utilization_ratio() > (100.0 - self.safety_margin_percentage)

class UrbanPlanningEntity51(BaseModel):
    """Operational domain entity 51 for Urban Planning & Zoning Regulation."""
    model_config = ConfigDict(from_attributes=True, extra='ignore')

    entity_id: str = Field(..., description='Unique identifier for UrbanPlanningEntity51')
    reference_code: str = Field(..., description='Official municipal reference code')
    status: UrbanPlanningStatus = Field(default=UrbanPlanningStatus.ACTIVE)
    priority: UrbanPlanningPriority = Field(default=UrbanPlanningPriority.STANDARD)
    ward_id: int = Field(default=1, ge=1, le=150, description='Municipal jurisdictional ward number')
    zone_code: str = Field(default='ZONE-CENTRAL', description='Municipal operational zone code')
    latitude: float = Field(default=17.385044, ge=-90.0, le=90.0)
    longitude: float = Field(default=78.486671, ge=-180.0, le=180.0)
    altitude_meters: Optional[float] = Field(default=542.0)
    primary_metric_value: float = Field(default=100.0, description='Domain standard quantitative measurement')
    secondary_metric_value: float = Field(default=45.5, description='Secondary operational metric')
    threshold_limit: float = Field(default=150.0, description='Configured statutory threshold')
    safety_margin_percentage: float = Field(default=15.0)
    is_compliant: bool = Field(default=True)
    supervisor_notes: Optional[str] = Field(default=None)
    assigned_officer_id: Optional[str] = Field(default=None)
    tags: List[str] = Field(default_factory=lambda: ['civic', 'smart-city', 'telemetry'])
    metadata_payload: Dict[str, Any] = Field(default_factory=dict)
    created_at: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))
    updated_at: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))

    @field_validator('primary_metric_value')
    @classmethod
    def validate_metric(cls, v: float) -> float:
        if v < 0:
            raise ValueError('Metric value cannot be negative in municipal calculations')
        return round(v, 4)

    def calculate_utilization_ratio(self) -> float:
        if self.threshold_limit <= 0:
            return 0.0
        return round((self.primary_metric_value / self.threshold_limit) * 100, 2)

    def is_critical_alert(self) -> bool:
        return self.calculate_utilization_ratio() > (100.0 - self.safety_margin_percentage)

class UrbanPlanningEntity52(BaseModel):
    """Operational domain entity 52 for Urban Planning & Zoning Regulation."""
    model_config = ConfigDict(from_attributes=True, extra='ignore')

    entity_id: str = Field(..., description='Unique identifier for UrbanPlanningEntity52')
    reference_code: str = Field(..., description='Official municipal reference code')
    status: UrbanPlanningStatus = Field(default=UrbanPlanningStatus.ACTIVE)
    priority: UrbanPlanningPriority = Field(default=UrbanPlanningPriority.STANDARD)
    ward_id: int = Field(default=1, ge=1, le=150, description='Municipal jurisdictional ward number')
    zone_code: str = Field(default='ZONE-CENTRAL', description='Municipal operational zone code')
    latitude: float = Field(default=17.385044, ge=-90.0, le=90.0)
    longitude: float = Field(default=78.486671, ge=-180.0, le=180.0)
    altitude_meters: Optional[float] = Field(default=542.0)
    primary_metric_value: float = Field(default=100.0, description='Domain standard quantitative measurement')
    secondary_metric_value: float = Field(default=45.5, description='Secondary operational metric')
    threshold_limit: float = Field(default=150.0, description='Configured statutory threshold')
    safety_margin_percentage: float = Field(default=15.0)
    is_compliant: bool = Field(default=True)
    supervisor_notes: Optional[str] = Field(default=None)
    assigned_officer_id: Optional[str] = Field(default=None)
    tags: List[str] = Field(default_factory=lambda: ['civic', 'smart-city', 'telemetry'])
    metadata_payload: Dict[str, Any] = Field(default_factory=dict)
    created_at: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))
    updated_at: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))

    @field_validator('primary_metric_value')
    @classmethod
    def validate_metric(cls, v: float) -> float:
        if v < 0:
            raise ValueError('Metric value cannot be negative in municipal calculations')
        return round(v, 4)

    def calculate_utilization_ratio(self) -> float:
        if self.threshold_limit <= 0:
            return 0.0
        return round((self.primary_metric_value / self.threshold_limit) * 100, 2)

    def is_critical_alert(self) -> bool:
        return self.calculate_utilization_ratio() > (100.0 - self.safety_margin_percentage)

class UrbanPlanningEntity53(BaseModel):
    """Operational domain entity 53 for Urban Planning & Zoning Regulation."""
    model_config = ConfigDict(from_attributes=True, extra='ignore')

    entity_id: str = Field(..., description='Unique identifier for UrbanPlanningEntity53')
    reference_code: str = Field(..., description='Official municipal reference code')
    status: UrbanPlanningStatus = Field(default=UrbanPlanningStatus.ACTIVE)
    priority: UrbanPlanningPriority = Field(default=UrbanPlanningPriority.STANDARD)
    ward_id: int = Field(default=1, ge=1, le=150, description='Municipal jurisdictional ward number')
    zone_code: str = Field(default='ZONE-CENTRAL', description='Municipal operational zone code')
    latitude: float = Field(default=17.385044, ge=-90.0, le=90.0)
    longitude: float = Field(default=78.486671, ge=-180.0, le=180.0)
    altitude_meters: Optional[float] = Field(default=542.0)
    primary_metric_value: float = Field(default=100.0, description='Domain standard quantitative measurement')
    secondary_metric_value: float = Field(default=45.5, description='Secondary operational metric')
    threshold_limit: float = Field(default=150.0, description='Configured statutory threshold')
    safety_margin_percentage: float = Field(default=15.0)
    is_compliant: bool = Field(default=True)
    supervisor_notes: Optional[str] = Field(default=None)
    assigned_officer_id: Optional[str] = Field(default=None)
    tags: List[str] = Field(default_factory=lambda: ['civic', 'smart-city', 'telemetry'])
    metadata_payload: Dict[str, Any] = Field(default_factory=dict)
    created_at: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))
    updated_at: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))

    @field_validator('primary_metric_value')
    @classmethod
    def validate_metric(cls, v: float) -> float:
        if v < 0:
            raise ValueError('Metric value cannot be negative in municipal calculations')
        return round(v, 4)

    def calculate_utilization_ratio(self) -> float:
        if self.threshold_limit <= 0:
            return 0.0
        return round((self.primary_metric_value / self.threshold_limit) * 100, 2)

    def is_critical_alert(self) -> bool:
        return self.calculate_utilization_ratio() > (100.0 - self.safety_margin_percentage)

class UrbanPlanningEntity54(BaseModel):
    """Operational domain entity 54 for Urban Planning & Zoning Regulation."""
    model_config = ConfigDict(from_attributes=True, extra='ignore')

    entity_id: str = Field(..., description='Unique identifier for UrbanPlanningEntity54')
    reference_code: str = Field(..., description='Official municipal reference code')
    status: UrbanPlanningStatus = Field(default=UrbanPlanningStatus.ACTIVE)
    priority: UrbanPlanningPriority = Field(default=UrbanPlanningPriority.STANDARD)
    ward_id: int = Field(default=1, ge=1, le=150, description='Municipal jurisdictional ward number')
    zone_code: str = Field(default='ZONE-CENTRAL', description='Municipal operational zone code')
    latitude: float = Field(default=17.385044, ge=-90.0, le=90.0)
    longitude: float = Field(default=78.486671, ge=-180.0, le=180.0)
    altitude_meters: Optional[float] = Field(default=542.0)
    primary_metric_value: float = Field(default=100.0, description='Domain standard quantitative measurement')
    secondary_metric_value: float = Field(default=45.5, description='Secondary operational metric')
    threshold_limit: float = Field(default=150.0, description='Configured statutory threshold')
    safety_margin_percentage: float = Field(default=15.0)
    is_compliant: bool = Field(default=True)
    supervisor_notes: Optional[str] = Field(default=None)
    assigned_officer_id: Optional[str] = Field(default=None)
    tags: List[str] = Field(default_factory=lambda: ['civic', 'smart-city', 'telemetry'])
    metadata_payload: Dict[str, Any] = Field(default_factory=dict)
    created_at: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))
    updated_at: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))

    @field_validator('primary_metric_value')
    @classmethod
    def validate_metric(cls, v: float) -> float:
        if v < 0:
            raise ValueError('Metric value cannot be negative in municipal calculations')
        return round(v, 4)

    def calculate_utilization_ratio(self) -> float:
        if self.threshold_limit <= 0:
            return 0.0
        return round((self.primary_metric_value / self.threshold_limit) * 100, 2)

    def is_critical_alert(self) -> bool:
        return self.calculate_utilization_ratio() > (100.0 - self.safety_margin_percentage)

class UrbanPlanningEntity55(BaseModel):
    """Operational domain entity 55 for Urban Planning & Zoning Regulation."""
    model_config = ConfigDict(from_attributes=True, extra='ignore')

    entity_id: str = Field(..., description='Unique identifier for UrbanPlanningEntity55')
    reference_code: str = Field(..., description='Official municipal reference code')
    status: UrbanPlanningStatus = Field(default=UrbanPlanningStatus.ACTIVE)
    priority: UrbanPlanningPriority = Field(default=UrbanPlanningPriority.STANDARD)
    ward_id: int = Field(default=1, ge=1, le=150, description='Municipal jurisdictional ward number')
    zone_code: str = Field(default='ZONE-CENTRAL', description='Municipal operational zone code')
    latitude: float = Field(default=17.385044, ge=-90.0, le=90.0)
    longitude: float = Field(default=78.486671, ge=-180.0, le=180.0)
    altitude_meters: Optional[float] = Field(default=542.0)
    primary_metric_value: float = Field(default=100.0, description='Domain standard quantitative measurement')
    secondary_metric_value: float = Field(default=45.5, description='Secondary operational metric')
    threshold_limit: float = Field(default=150.0, description='Configured statutory threshold')
    safety_margin_percentage: float = Field(default=15.0)
    is_compliant: bool = Field(default=True)
    supervisor_notes: Optional[str] = Field(default=None)
    assigned_officer_id: Optional[str] = Field(default=None)
    tags: List[str] = Field(default_factory=lambda: ['civic', 'smart-city', 'telemetry'])
    metadata_payload: Dict[str, Any] = Field(default_factory=dict)
    created_at: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))
    updated_at: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))

    @field_validator('primary_metric_value')
    @classmethod
    def validate_metric(cls, v: float) -> float:
        if v < 0:
            raise ValueError('Metric value cannot be negative in municipal calculations')
        return round(v, 4)

    def calculate_utilization_ratio(self) -> float:
        if self.threshold_limit <= 0:
            return 0.0
        return round((self.primary_metric_value / self.threshold_limit) * 100, 2)

    def is_critical_alert(self) -> bool:
        return self.calculate_utilization_ratio() > (100.0 - self.safety_margin_percentage)

class UrbanPlanningEntity56(BaseModel):
    """Operational domain entity 56 for Urban Planning & Zoning Regulation."""
    model_config = ConfigDict(from_attributes=True, extra='ignore')

    entity_id: str = Field(..., description='Unique identifier for UrbanPlanningEntity56')
    reference_code: str = Field(..., description='Official municipal reference code')
    status: UrbanPlanningStatus = Field(default=UrbanPlanningStatus.ACTIVE)
    priority: UrbanPlanningPriority = Field(default=UrbanPlanningPriority.STANDARD)
    ward_id: int = Field(default=1, ge=1, le=150, description='Municipal jurisdictional ward number')
    zone_code: str = Field(default='ZONE-CENTRAL', description='Municipal operational zone code')
    latitude: float = Field(default=17.385044, ge=-90.0, le=90.0)
    longitude: float = Field(default=78.486671, ge=-180.0, le=180.0)
    altitude_meters: Optional[float] = Field(default=542.0)
    primary_metric_value: float = Field(default=100.0, description='Domain standard quantitative measurement')
    secondary_metric_value: float = Field(default=45.5, description='Secondary operational metric')
    threshold_limit: float = Field(default=150.0, description='Configured statutory threshold')
    safety_margin_percentage: float = Field(default=15.0)
    is_compliant: bool = Field(default=True)
    supervisor_notes: Optional[str] = Field(default=None)
    assigned_officer_id: Optional[str] = Field(default=None)
    tags: List[str] = Field(default_factory=lambda: ['civic', 'smart-city', 'telemetry'])
    metadata_payload: Dict[str, Any] = Field(default_factory=dict)
    created_at: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))
    updated_at: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))

    @field_validator('primary_metric_value')
    @classmethod
    def validate_metric(cls, v: float) -> float:
        if v < 0:
            raise ValueError('Metric value cannot be negative in municipal calculations')
        return round(v, 4)

    def calculate_utilization_ratio(self) -> float:
        if self.threshold_limit <= 0:
            return 0.0
        return round((self.primary_metric_value / self.threshold_limit) * 100, 2)

    def is_critical_alert(self) -> bool:
        return self.calculate_utilization_ratio() > (100.0 - self.safety_margin_percentage)

class UrbanPlanningEntity57(BaseModel):
    """Operational domain entity 57 for Urban Planning & Zoning Regulation."""
    model_config = ConfigDict(from_attributes=True, extra='ignore')

    entity_id: str = Field(..., description='Unique identifier for UrbanPlanningEntity57')
    reference_code: str = Field(..., description='Official municipal reference code')
    status: UrbanPlanningStatus = Field(default=UrbanPlanningStatus.ACTIVE)
    priority: UrbanPlanningPriority = Field(default=UrbanPlanningPriority.STANDARD)
    ward_id: int = Field(default=1, ge=1, le=150, description='Municipal jurisdictional ward number')
    zone_code: str = Field(default='ZONE-CENTRAL', description='Municipal operational zone code')
    latitude: float = Field(default=17.385044, ge=-90.0, le=90.0)
    longitude: float = Field(default=78.486671, ge=-180.0, le=180.0)
    altitude_meters: Optional[float] = Field(default=542.0)
    primary_metric_value: float = Field(default=100.0, description='Domain standard quantitative measurement')
    secondary_metric_value: float = Field(default=45.5, description='Secondary operational metric')
    threshold_limit: float = Field(default=150.0, description='Configured statutory threshold')
    safety_margin_percentage: float = Field(default=15.0)
    is_compliant: bool = Field(default=True)
    supervisor_notes: Optional[str] = Field(default=None)
    assigned_officer_id: Optional[str] = Field(default=None)
    tags: List[str] = Field(default_factory=lambda: ['civic', 'smart-city', 'telemetry'])
    metadata_payload: Dict[str, Any] = Field(default_factory=dict)
    created_at: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))
    updated_at: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))

    @field_validator('primary_metric_value')
    @classmethod
    def validate_metric(cls, v: float) -> float:
        if v < 0:
            raise ValueError('Metric value cannot be negative in municipal calculations')
        return round(v, 4)

    def calculate_utilization_ratio(self) -> float:
        if self.threshold_limit <= 0:
            return 0.0
        return round((self.primary_metric_value / self.threshold_limit) * 100, 2)

    def is_critical_alert(self) -> bool:
        return self.calculate_utilization_ratio() > (100.0 - self.safety_margin_percentage)

class UrbanPlanningEntity58(BaseModel):
    """Operational domain entity 58 for Urban Planning & Zoning Regulation."""
    model_config = ConfigDict(from_attributes=True, extra='ignore')

    entity_id: str = Field(..., description='Unique identifier for UrbanPlanningEntity58')
    reference_code: str = Field(..., description='Official municipal reference code')
    status: UrbanPlanningStatus = Field(default=UrbanPlanningStatus.ACTIVE)
    priority: UrbanPlanningPriority = Field(default=UrbanPlanningPriority.STANDARD)
    ward_id: int = Field(default=1, ge=1, le=150, description='Municipal jurisdictional ward number')
    zone_code: str = Field(default='ZONE-CENTRAL', description='Municipal operational zone code')
    latitude: float = Field(default=17.385044, ge=-90.0, le=90.0)
    longitude: float = Field(default=78.486671, ge=-180.0, le=180.0)
    altitude_meters: Optional[float] = Field(default=542.0)
    primary_metric_value: float = Field(default=100.0, description='Domain standard quantitative measurement')
    secondary_metric_value: float = Field(default=45.5, description='Secondary operational metric')
    threshold_limit: float = Field(default=150.0, description='Configured statutory threshold')
    safety_margin_percentage: float = Field(default=15.0)
    is_compliant: bool = Field(default=True)
    supervisor_notes: Optional[str] = Field(default=None)
    assigned_officer_id: Optional[str] = Field(default=None)
    tags: List[str] = Field(default_factory=lambda: ['civic', 'smart-city', 'telemetry'])
    metadata_payload: Dict[str, Any] = Field(default_factory=dict)
    created_at: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))
    updated_at: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))

    @field_validator('primary_metric_value')
    @classmethod
    def validate_metric(cls, v: float) -> float:
        if v < 0:
            raise ValueError('Metric value cannot be negative in municipal calculations')
        return round(v, 4)

    def calculate_utilization_ratio(self) -> float:
        if self.threshold_limit <= 0:
            return 0.0
        return round((self.primary_metric_value / self.threshold_limit) * 100, 2)

    def is_critical_alert(self) -> bool:
        return self.calculate_utilization_ratio() > (100.0 - self.safety_margin_percentage)

class UrbanPlanningEntity59(BaseModel):
    """Operational domain entity 59 for Urban Planning & Zoning Regulation."""
    model_config = ConfigDict(from_attributes=True, extra='ignore')

    entity_id: str = Field(..., description='Unique identifier for UrbanPlanningEntity59')
    reference_code: str = Field(..., description='Official municipal reference code')
    status: UrbanPlanningStatus = Field(default=UrbanPlanningStatus.ACTIVE)
    priority: UrbanPlanningPriority = Field(default=UrbanPlanningPriority.STANDARD)
    ward_id: int = Field(default=1, ge=1, le=150, description='Municipal jurisdictional ward number')
    zone_code: str = Field(default='ZONE-CENTRAL', description='Municipal operational zone code')
    latitude: float = Field(default=17.385044, ge=-90.0, le=90.0)
    longitude: float = Field(default=78.486671, ge=-180.0, le=180.0)
    altitude_meters: Optional[float] = Field(default=542.0)
    primary_metric_value: float = Field(default=100.0, description='Domain standard quantitative measurement')
    secondary_metric_value: float = Field(default=45.5, description='Secondary operational metric')
    threshold_limit: float = Field(default=150.0, description='Configured statutory threshold')
    safety_margin_percentage: float = Field(default=15.0)
    is_compliant: bool = Field(default=True)
    supervisor_notes: Optional[str] = Field(default=None)
    assigned_officer_id: Optional[str] = Field(default=None)
    tags: List[str] = Field(default_factory=lambda: ['civic', 'smart-city', 'telemetry'])
    metadata_payload: Dict[str, Any] = Field(default_factory=dict)
    created_at: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))
    updated_at: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))

    @field_validator('primary_metric_value')
    @classmethod
    def validate_metric(cls, v: float) -> float:
        if v < 0:
            raise ValueError('Metric value cannot be negative in municipal calculations')
        return round(v, 4)

    def calculate_utilization_ratio(self) -> float:
        if self.threshold_limit <= 0:
            return 0.0
        return round((self.primary_metric_value / self.threshold_limit) * 100, 2)

    def is_critical_alert(self) -> bool:
        return self.calculate_utilization_ratio() > (100.0 - self.safety_margin_percentage)

class UrbanPlanningEntity60(BaseModel):
    """Operational domain entity 60 for Urban Planning & Zoning Regulation."""
    model_config = ConfigDict(from_attributes=True, extra='ignore')

    entity_id: str = Field(..., description='Unique identifier for UrbanPlanningEntity60')
    reference_code: str = Field(..., description='Official municipal reference code')
    status: UrbanPlanningStatus = Field(default=UrbanPlanningStatus.ACTIVE)
    priority: UrbanPlanningPriority = Field(default=UrbanPlanningPriority.STANDARD)
    ward_id: int = Field(default=1, ge=1, le=150, description='Municipal jurisdictional ward number')
    zone_code: str = Field(default='ZONE-CENTRAL', description='Municipal operational zone code')
    latitude: float = Field(default=17.385044, ge=-90.0, le=90.0)
    longitude: float = Field(default=78.486671, ge=-180.0, le=180.0)
    altitude_meters: Optional[float] = Field(default=542.0)
    primary_metric_value: float = Field(default=100.0, description='Domain standard quantitative measurement')
    secondary_metric_value: float = Field(default=45.5, description='Secondary operational metric')
    threshold_limit: float = Field(default=150.0, description='Configured statutory threshold')
    safety_margin_percentage: float = Field(default=15.0)
    is_compliant: bool = Field(default=True)
    supervisor_notes: Optional[str] = Field(default=None)
    assigned_officer_id: Optional[str] = Field(default=None)
    tags: List[str] = Field(default_factory=lambda: ['civic', 'smart-city', 'telemetry'])
    metadata_payload: Dict[str, Any] = Field(default_factory=dict)
    created_at: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))
    updated_at: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))

    @field_validator('primary_metric_value')
    @classmethod
    def validate_metric(cls, v: float) -> float:
        if v < 0:
            raise ValueError('Metric value cannot be negative in municipal calculations')
        return round(v, 4)

    def calculate_utilization_ratio(self) -> float:
        if self.threshold_limit <= 0:
            return 0.0
        return round((self.primary_metric_value / self.threshold_limit) * 100, 2)

    def is_critical_alert(self) -> bool:
        return self.calculate_utilization_ratio() > (100.0 - self.safety_margin_percentage)

class UrbanPlanningEntity61(BaseModel):
    """Operational domain entity 61 for Urban Planning & Zoning Regulation."""
    model_config = ConfigDict(from_attributes=True, extra='ignore')

    entity_id: str = Field(..., description='Unique identifier for UrbanPlanningEntity61')
    reference_code: str = Field(..., description='Official municipal reference code')
    status: UrbanPlanningStatus = Field(default=UrbanPlanningStatus.ACTIVE)
    priority: UrbanPlanningPriority = Field(default=UrbanPlanningPriority.STANDARD)
    ward_id: int = Field(default=1, ge=1, le=150, description='Municipal jurisdictional ward number')
    zone_code: str = Field(default='ZONE-CENTRAL', description='Municipal operational zone code')
    latitude: float = Field(default=17.385044, ge=-90.0, le=90.0)
    longitude: float = Field(default=78.486671, ge=-180.0, le=180.0)
    altitude_meters: Optional[float] = Field(default=542.0)
    primary_metric_value: float = Field(default=100.0, description='Domain standard quantitative measurement')
    secondary_metric_value: float = Field(default=45.5, description='Secondary operational metric')
    threshold_limit: float = Field(default=150.0, description='Configured statutory threshold')
    safety_margin_percentage: float = Field(default=15.0)
    is_compliant: bool = Field(default=True)
    supervisor_notes: Optional[str] = Field(default=None)
    assigned_officer_id: Optional[str] = Field(default=None)
    tags: List[str] = Field(default_factory=lambda: ['civic', 'smart-city', 'telemetry'])
    metadata_payload: Dict[str, Any] = Field(default_factory=dict)
    created_at: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))
    updated_at: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))

    @field_validator('primary_metric_value')
    @classmethod
    def validate_metric(cls, v: float) -> float:
        if v < 0:
            raise ValueError('Metric value cannot be negative in municipal calculations')
        return round(v, 4)

    def calculate_utilization_ratio(self) -> float:
        if self.threshold_limit <= 0:
            return 0.0
        return round((self.primary_metric_value / self.threshold_limit) * 100, 2)

    def is_critical_alert(self) -> bool:
        return self.calculate_utilization_ratio() > (100.0 - self.safety_margin_percentage)

class UrbanPlanningEntity62(BaseModel):
    """Operational domain entity 62 for Urban Planning & Zoning Regulation."""
    model_config = ConfigDict(from_attributes=True, extra='ignore')

    entity_id: str = Field(..., description='Unique identifier for UrbanPlanningEntity62')
    reference_code: str = Field(..., description='Official municipal reference code')
    status: UrbanPlanningStatus = Field(default=UrbanPlanningStatus.ACTIVE)
    priority: UrbanPlanningPriority = Field(default=UrbanPlanningPriority.STANDARD)
    ward_id: int = Field(default=1, ge=1, le=150, description='Municipal jurisdictional ward number')
    zone_code: str = Field(default='ZONE-CENTRAL', description='Municipal operational zone code')
    latitude: float = Field(default=17.385044, ge=-90.0, le=90.0)
    longitude: float = Field(default=78.486671, ge=-180.0, le=180.0)
    altitude_meters: Optional[float] = Field(default=542.0)
    primary_metric_value: float = Field(default=100.0, description='Domain standard quantitative measurement')
    secondary_metric_value: float = Field(default=45.5, description='Secondary operational metric')
    threshold_limit: float = Field(default=150.0, description='Configured statutory threshold')
    safety_margin_percentage: float = Field(default=15.0)
    is_compliant: bool = Field(default=True)
    supervisor_notes: Optional[str] = Field(default=None)
    assigned_officer_id: Optional[str] = Field(default=None)
    tags: List[str] = Field(default_factory=lambda: ['civic', 'smart-city', 'telemetry'])
    metadata_payload: Dict[str, Any] = Field(default_factory=dict)
    created_at: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))
    updated_at: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))

    @field_validator('primary_metric_value')
    @classmethod
    def validate_metric(cls, v: float) -> float:
        if v < 0:
            raise ValueError('Metric value cannot be negative in municipal calculations')
        return round(v, 4)

    def calculate_utilization_ratio(self) -> float:
        if self.threshold_limit <= 0:
            return 0.0
        return round((self.primary_metric_value / self.threshold_limit) * 100, 2)

    def is_critical_alert(self) -> bool:
        return self.calculate_utilization_ratio() > (100.0 - self.safety_margin_percentage)

class UrbanPlanningEntity63(BaseModel):
    """Operational domain entity 63 for Urban Planning & Zoning Regulation."""
    model_config = ConfigDict(from_attributes=True, extra='ignore')

    entity_id: str = Field(..., description='Unique identifier for UrbanPlanningEntity63')
    reference_code: str = Field(..., description='Official municipal reference code')
    status: UrbanPlanningStatus = Field(default=UrbanPlanningStatus.ACTIVE)
    priority: UrbanPlanningPriority = Field(default=UrbanPlanningPriority.STANDARD)
    ward_id: int = Field(default=1, ge=1, le=150, description='Municipal jurisdictional ward number')
    zone_code: str = Field(default='ZONE-CENTRAL', description='Municipal operational zone code')
    latitude: float = Field(default=17.385044, ge=-90.0, le=90.0)
    longitude: float = Field(default=78.486671, ge=-180.0, le=180.0)
    altitude_meters: Optional[float] = Field(default=542.0)
    primary_metric_value: float = Field(default=100.0, description='Domain standard quantitative measurement')
    secondary_metric_value: float = Field(default=45.5, description='Secondary operational metric')
    threshold_limit: float = Field(default=150.0, description='Configured statutory threshold')
    safety_margin_percentage: float = Field(default=15.0)
    is_compliant: bool = Field(default=True)
    supervisor_notes: Optional[str] = Field(default=None)
    assigned_officer_id: Optional[str] = Field(default=None)
    tags: List[str] = Field(default_factory=lambda: ['civic', 'smart-city', 'telemetry'])
    metadata_payload: Dict[str, Any] = Field(default_factory=dict)
    created_at: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))
    updated_at: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))

    @field_validator('primary_metric_value')
    @classmethod
    def validate_metric(cls, v: float) -> float:
        if v < 0:
            raise ValueError('Metric value cannot be negative in municipal calculations')
        return round(v, 4)

    def calculate_utilization_ratio(self) -> float:
        if self.threshold_limit <= 0:
            return 0.0
        return round((self.primary_metric_value / self.threshold_limit) * 100, 2)

    def is_critical_alert(self) -> bool:
        return self.calculate_utilization_ratio() > (100.0 - self.safety_margin_percentage)

class UrbanPlanningEntity64(BaseModel):
    """Operational domain entity 64 for Urban Planning & Zoning Regulation."""
    model_config = ConfigDict(from_attributes=True, extra='ignore')

    entity_id: str = Field(..., description='Unique identifier for UrbanPlanningEntity64')
    reference_code: str = Field(..., description='Official municipal reference code')
    status: UrbanPlanningStatus = Field(default=UrbanPlanningStatus.ACTIVE)
    priority: UrbanPlanningPriority = Field(default=UrbanPlanningPriority.STANDARD)
    ward_id: int = Field(default=1, ge=1, le=150, description='Municipal jurisdictional ward number')
    zone_code: str = Field(default='ZONE-CENTRAL', description='Municipal operational zone code')
    latitude: float = Field(default=17.385044, ge=-90.0, le=90.0)
    longitude: float = Field(default=78.486671, ge=-180.0, le=180.0)
    altitude_meters: Optional[float] = Field(default=542.0)
    primary_metric_value: float = Field(default=100.0, description='Domain standard quantitative measurement')
    secondary_metric_value: float = Field(default=45.5, description='Secondary operational metric')
    threshold_limit: float = Field(default=150.0, description='Configured statutory threshold')
    safety_margin_percentage: float = Field(default=15.0)
    is_compliant: bool = Field(default=True)
    supervisor_notes: Optional[str] = Field(default=None)
    assigned_officer_id: Optional[str] = Field(default=None)
    tags: List[str] = Field(default_factory=lambda: ['civic', 'smart-city', 'telemetry'])
    metadata_payload: Dict[str, Any] = Field(default_factory=dict)
    created_at: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))
    updated_at: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))

    @field_validator('primary_metric_value')
    @classmethod
    def validate_metric(cls, v: float) -> float:
        if v < 0:
            raise ValueError('Metric value cannot be negative in municipal calculations')
        return round(v, 4)

    def calculate_utilization_ratio(self) -> float:
        if self.threshold_limit <= 0:
            return 0.0
        return round((self.primary_metric_value / self.threshold_limit) * 100, 2)

    def is_critical_alert(self) -> bool:
        return self.calculate_utilization_ratio() > (100.0 - self.safety_margin_percentage)

class UrbanPlanningEntity65(BaseModel):
    """Operational domain entity 65 for Urban Planning & Zoning Regulation."""
    model_config = ConfigDict(from_attributes=True, extra='ignore')

    entity_id: str = Field(..., description='Unique identifier for UrbanPlanningEntity65')
    reference_code: str = Field(..., description='Official municipal reference code')
    status: UrbanPlanningStatus = Field(default=UrbanPlanningStatus.ACTIVE)
    priority: UrbanPlanningPriority = Field(default=UrbanPlanningPriority.STANDARD)
    ward_id: int = Field(default=1, ge=1, le=150, description='Municipal jurisdictional ward number')
    zone_code: str = Field(default='ZONE-CENTRAL', description='Municipal operational zone code')
    latitude: float = Field(default=17.385044, ge=-90.0, le=90.0)
    longitude: float = Field(default=78.486671, ge=-180.0, le=180.0)
    altitude_meters: Optional[float] = Field(default=542.0)
    primary_metric_value: float = Field(default=100.0, description='Domain standard quantitative measurement')
    secondary_metric_value: float = Field(default=45.5, description='Secondary operational metric')
    threshold_limit: float = Field(default=150.0, description='Configured statutory threshold')
    safety_margin_percentage: float = Field(default=15.0)
    is_compliant: bool = Field(default=True)
    supervisor_notes: Optional[str] = Field(default=None)
    assigned_officer_id: Optional[str] = Field(default=None)
    tags: List[str] = Field(default_factory=lambda: ['civic', 'smart-city', 'telemetry'])
    metadata_payload: Dict[str, Any] = Field(default_factory=dict)
    created_at: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))
    updated_at: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))

    @field_validator('primary_metric_value')
    @classmethod
    def validate_metric(cls, v: float) -> float:
        if v < 0:
            raise ValueError('Metric value cannot be negative in municipal calculations')
        return round(v, 4)

    def calculate_utilization_ratio(self) -> float:
        if self.threshold_limit <= 0:
            return 0.0
        return round((self.primary_metric_value / self.threshold_limit) * 100, 2)

    def is_critical_alert(self) -> bool:
        return self.calculate_utilization_ratio() > (100.0 - self.safety_margin_percentage)

class UrbanPlanningEntity66(BaseModel):
    """Operational domain entity 66 for Urban Planning & Zoning Regulation."""
    model_config = ConfigDict(from_attributes=True, extra='ignore')

    entity_id: str = Field(..., description='Unique identifier for UrbanPlanningEntity66')
    reference_code: str = Field(..., description='Official municipal reference code')
    status: UrbanPlanningStatus = Field(default=UrbanPlanningStatus.ACTIVE)
    priority: UrbanPlanningPriority = Field(default=UrbanPlanningPriority.STANDARD)
    ward_id: int = Field(default=1, ge=1, le=150, description='Municipal jurisdictional ward number')
    zone_code: str = Field(default='ZONE-CENTRAL', description='Municipal operational zone code')
    latitude: float = Field(default=17.385044, ge=-90.0, le=90.0)
    longitude: float = Field(default=78.486671, ge=-180.0, le=180.0)
    altitude_meters: Optional[float] = Field(default=542.0)
    primary_metric_value: float = Field(default=100.0, description='Domain standard quantitative measurement')
    secondary_metric_value: float = Field(default=45.5, description='Secondary operational metric')
    threshold_limit: float = Field(default=150.0, description='Configured statutory threshold')
    safety_margin_percentage: float = Field(default=15.0)
    is_compliant: bool = Field(default=True)
    supervisor_notes: Optional[str] = Field(default=None)
    assigned_officer_id: Optional[str] = Field(default=None)
    tags: List[str] = Field(default_factory=lambda: ['civic', 'smart-city', 'telemetry'])
    metadata_payload: Dict[str, Any] = Field(default_factory=dict)
    created_at: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))
    updated_at: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))

    @field_validator('primary_metric_value')
    @classmethod
    def validate_metric(cls, v: float) -> float:
        if v < 0:
            raise ValueError('Metric value cannot be negative in municipal calculations')
        return round(v, 4)

    def calculate_utilization_ratio(self) -> float:
        if self.threshold_limit <= 0:
            return 0.0
        return round((self.primary_metric_value / self.threshold_limit) * 100, 2)

    def is_critical_alert(self) -> bool:
        return self.calculate_utilization_ratio() > (100.0 - self.safety_margin_percentage)

class UrbanPlanningEntity67(BaseModel):
    """Operational domain entity 67 for Urban Planning & Zoning Regulation."""
    model_config = ConfigDict(from_attributes=True, extra='ignore')

    entity_id: str = Field(..., description='Unique identifier for UrbanPlanningEntity67')
    reference_code: str = Field(..., description='Official municipal reference code')
    status: UrbanPlanningStatus = Field(default=UrbanPlanningStatus.ACTIVE)
    priority: UrbanPlanningPriority = Field(default=UrbanPlanningPriority.STANDARD)
    ward_id: int = Field(default=1, ge=1, le=150, description='Municipal jurisdictional ward number')
    zone_code: str = Field(default='ZONE-CENTRAL', description='Municipal operational zone code')
    latitude: float = Field(default=17.385044, ge=-90.0, le=90.0)
    longitude: float = Field(default=78.486671, ge=-180.0, le=180.0)
    altitude_meters: Optional[float] = Field(default=542.0)
    primary_metric_value: float = Field(default=100.0, description='Domain standard quantitative measurement')
    secondary_metric_value: float = Field(default=45.5, description='Secondary operational metric')
    threshold_limit: float = Field(default=150.0, description='Configured statutory threshold')
    safety_margin_percentage: float = Field(default=15.0)
    is_compliant: bool = Field(default=True)
    supervisor_notes: Optional[str] = Field(default=None)
    assigned_officer_id: Optional[str] = Field(default=None)
    tags: List[str] = Field(default_factory=lambda: ['civic', 'smart-city', 'telemetry'])
    metadata_payload: Dict[str, Any] = Field(default_factory=dict)
    created_at: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))
    updated_at: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))

    @field_validator('primary_metric_value')
    @classmethod
    def validate_metric(cls, v: float) -> float:
        if v < 0:
            raise ValueError('Metric value cannot be negative in municipal calculations')
        return round(v, 4)

    def calculate_utilization_ratio(self) -> float:
        if self.threshold_limit <= 0:
            return 0.0
        return round((self.primary_metric_value / self.threshold_limit) * 100, 2)

    def is_critical_alert(self) -> bool:
        return self.calculate_utilization_ratio() > (100.0 - self.safety_margin_percentage)

class UrbanPlanningEntity68(BaseModel):
    """Operational domain entity 68 for Urban Planning & Zoning Regulation."""
    model_config = ConfigDict(from_attributes=True, extra='ignore')

    entity_id: str = Field(..., description='Unique identifier for UrbanPlanningEntity68')
    reference_code: str = Field(..., description='Official municipal reference code')
    status: UrbanPlanningStatus = Field(default=UrbanPlanningStatus.ACTIVE)
    priority: UrbanPlanningPriority = Field(default=UrbanPlanningPriority.STANDARD)
    ward_id: int = Field(default=1, ge=1, le=150, description='Municipal jurisdictional ward number')
    zone_code: str = Field(default='ZONE-CENTRAL', description='Municipal operational zone code')
    latitude: float = Field(default=17.385044, ge=-90.0, le=90.0)
    longitude: float = Field(default=78.486671, ge=-180.0, le=180.0)
    altitude_meters: Optional[float] = Field(default=542.0)
    primary_metric_value: float = Field(default=100.0, description='Domain standard quantitative measurement')
    secondary_metric_value: float = Field(default=45.5, description='Secondary operational metric')
    threshold_limit: float = Field(default=150.0, description='Configured statutory threshold')
    safety_margin_percentage: float = Field(default=15.0)
    is_compliant: bool = Field(default=True)
    supervisor_notes: Optional[str] = Field(default=None)
    assigned_officer_id: Optional[str] = Field(default=None)
    tags: List[str] = Field(default_factory=lambda: ['civic', 'smart-city', 'telemetry'])
    metadata_payload: Dict[str, Any] = Field(default_factory=dict)
    created_at: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))
    updated_at: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))

    @field_validator('primary_metric_value')
    @classmethod
    def validate_metric(cls, v: float) -> float:
        if v < 0:
            raise ValueError('Metric value cannot be negative in municipal calculations')
        return round(v, 4)

    def calculate_utilization_ratio(self) -> float:
        if self.threshold_limit <= 0:
            return 0.0
        return round((self.primary_metric_value / self.threshold_limit) * 100, 2)

    def is_critical_alert(self) -> bool:
        return self.calculate_utilization_ratio() > (100.0 - self.safety_margin_percentage)

class UrbanPlanningEntity69(BaseModel):
    """Operational domain entity 69 for Urban Planning & Zoning Regulation."""
    model_config = ConfigDict(from_attributes=True, extra='ignore')

    entity_id: str = Field(..., description='Unique identifier for UrbanPlanningEntity69')
    reference_code: str = Field(..., description='Official municipal reference code')
    status: UrbanPlanningStatus = Field(default=UrbanPlanningStatus.ACTIVE)
    priority: UrbanPlanningPriority = Field(default=UrbanPlanningPriority.STANDARD)
    ward_id: int = Field(default=1, ge=1, le=150, description='Municipal jurisdictional ward number')
    zone_code: str = Field(default='ZONE-CENTRAL', description='Municipal operational zone code')
    latitude: float = Field(default=17.385044, ge=-90.0, le=90.0)
    longitude: float = Field(default=78.486671, ge=-180.0, le=180.0)
    altitude_meters: Optional[float] = Field(default=542.0)
    primary_metric_value: float = Field(default=100.0, description='Domain standard quantitative measurement')
    secondary_metric_value: float = Field(default=45.5, description='Secondary operational metric')
    threshold_limit: float = Field(default=150.0, description='Configured statutory threshold')
    safety_margin_percentage: float = Field(default=15.0)
    is_compliant: bool = Field(default=True)
    supervisor_notes: Optional[str] = Field(default=None)
    assigned_officer_id: Optional[str] = Field(default=None)
    tags: List[str] = Field(default_factory=lambda: ['civic', 'smart-city', 'telemetry'])
    metadata_payload: Dict[str, Any] = Field(default_factory=dict)
    created_at: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))
    updated_at: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))

    @field_validator('primary_metric_value')
    @classmethod
    def validate_metric(cls, v: float) -> float:
        if v < 0:
            raise ValueError('Metric value cannot be negative in municipal calculations')
        return round(v, 4)

    def calculate_utilization_ratio(self) -> float:
        if self.threshold_limit <= 0:
            return 0.0
        return round((self.primary_metric_value / self.threshold_limit) * 100, 2)

    def is_critical_alert(self) -> bool:
        return self.calculate_utilization_ratio() > (100.0 - self.safety_margin_percentage)

class UrbanPlanningEntity70(BaseModel):
    """Operational domain entity 70 for Urban Planning & Zoning Regulation."""
    model_config = ConfigDict(from_attributes=True, extra='ignore')

    entity_id: str = Field(..., description='Unique identifier for UrbanPlanningEntity70')
    reference_code: str = Field(..., description='Official municipal reference code')
    status: UrbanPlanningStatus = Field(default=UrbanPlanningStatus.ACTIVE)
    priority: UrbanPlanningPriority = Field(default=UrbanPlanningPriority.STANDARD)
    ward_id: int = Field(default=1, ge=1, le=150, description='Municipal jurisdictional ward number')
    zone_code: str = Field(default='ZONE-CENTRAL', description='Municipal operational zone code')
    latitude: float = Field(default=17.385044, ge=-90.0, le=90.0)
    longitude: float = Field(default=78.486671, ge=-180.0, le=180.0)
    altitude_meters: Optional[float] = Field(default=542.0)
    primary_metric_value: float = Field(default=100.0, description='Domain standard quantitative measurement')
    secondary_metric_value: float = Field(default=45.5, description='Secondary operational metric')
    threshold_limit: float = Field(default=150.0, description='Configured statutory threshold')
    safety_margin_percentage: float = Field(default=15.0)
    is_compliant: bool = Field(default=True)
    supervisor_notes: Optional[str] = Field(default=None)
    assigned_officer_id: Optional[str] = Field(default=None)
    tags: List[str] = Field(default_factory=lambda: ['civic', 'smart-city', 'telemetry'])
    metadata_payload: Dict[str, Any] = Field(default_factory=dict)
    created_at: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))
    updated_at: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))

    @field_validator('primary_metric_value')
    @classmethod
    def validate_metric(cls, v: float) -> float:
        if v < 0:
            raise ValueError('Metric value cannot be negative in municipal calculations')
        return round(v, 4)

    def calculate_utilization_ratio(self) -> float:
        if self.threshold_limit <= 0:
            return 0.0
        return round((self.primary_metric_value / self.threshold_limit) * 100, 2)

    def is_critical_alert(self) -> bool:
        return self.calculate_utilization_ratio() > (100.0 - self.safety_margin_percentage)

class UrbanPlanningEntity71(BaseModel):
    """Operational domain entity 71 for Urban Planning & Zoning Regulation."""
    model_config = ConfigDict(from_attributes=True, extra='ignore')

    entity_id: str = Field(..., description='Unique identifier for UrbanPlanningEntity71')
    reference_code: str = Field(..., description='Official municipal reference code')
    status: UrbanPlanningStatus = Field(default=UrbanPlanningStatus.ACTIVE)
    priority: UrbanPlanningPriority = Field(default=UrbanPlanningPriority.STANDARD)
    ward_id: int = Field(default=1, ge=1, le=150, description='Municipal jurisdictional ward number')
    zone_code: str = Field(default='ZONE-CENTRAL', description='Municipal operational zone code')
    latitude: float = Field(default=17.385044, ge=-90.0, le=90.0)
    longitude: float = Field(default=78.486671, ge=-180.0, le=180.0)
    altitude_meters: Optional[float] = Field(default=542.0)
    primary_metric_value: float = Field(default=100.0, description='Domain standard quantitative measurement')
    secondary_metric_value: float = Field(default=45.5, description='Secondary operational metric')
    threshold_limit: float = Field(default=150.0, description='Configured statutory threshold')
    safety_margin_percentage: float = Field(default=15.0)
    is_compliant: bool = Field(default=True)
    supervisor_notes: Optional[str] = Field(default=None)
    assigned_officer_id: Optional[str] = Field(default=None)
    tags: List[str] = Field(default_factory=lambda: ['civic', 'smart-city', 'telemetry'])
    metadata_payload: Dict[str, Any] = Field(default_factory=dict)
    created_at: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))
    updated_at: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))

    @field_validator('primary_metric_value')
    @classmethod
    def validate_metric(cls, v: float) -> float:
        if v < 0:
            raise ValueError('Metric value cannot be negative in municipal calculations')
        return round(v, 4)

    def calculate_utilization_ratio(self) -> float:
        if self.threshold_limit <= 0:
            return 0.0
        return round((self.primary_metric_value / self.threshold_limit) * 100, 2)

    def is_critical_alert(self) -> bool:
        return self.calculate_utilization_ratio() > (100.0 - self.safety_margin_percentage)

class UrbanPlanningEntity72(BaseModel):
    """Operational domain entity 72 for Urban Planning & Zoning Regulation."""
    model_config = ConfigDict(from_attributes=True, extra='ignore')

    entity_id: str = Field(..., description='Unique identifier for UrbanPlanningEntity72')
    reference_code: str = Field(..., description='Official municipal reference code')
    status: UrbanPlanningStatus = Field(default=UrbanPlanningStatus.ACTIVE)
    priority: UrbanPlanningPriority = Field(default=UrbanPlanningPriority.STANDARD)
    ward_id: int = Field(default=1, ge=1, le=150, description='Municipal jurisdictional ward number')
    zone_code: str = Field(default='ZONE-CENTRAL', description='Municipal operational zone code')
    latitude: float = Field(default=17.385044, ge=-90.0, le=90.0)
    longitude: float = Field(default=78.486671, ge=-180.0, le=180.0)
    altitude_meters: Optional[float] = Field(default=542.0)
    primary_metric_value: float = Field(default=100.0, description='Domain standard quantitative measurement')
    secondary_metric_value: float = Field(default=45.5, description='Secondary operational metric')
    threshold_limit: float = Field(default=150.0, description='Configured statutory threshold')
    safety_margin_percentage: float = Field(default=15.0)
    is_compliant: bool = Field(default=True)
    supervisor_notes: Optional[str] = Field(default=None)
    assigned_officer_id: Optional[str] = Field(default=None)
    tags: List[str] = Field(default_factory=lambda: ['civic', 'smart-city', 'telemetry'])
    metadata_payload: Dict[str, Any] = Field(default_factory=dict)
    created_at: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))
    updated_at: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))

    @field_validator('primary_metric_value')
    @classmethod
    def validate_metric(cls, v: float) -> float:
        if v < 0:
            raise ValueError('Metric value cannot be negative in municipal calculations')
        return round(v, 4)

    def calculate_utilization_ratio(self) -> float:
        if self.threshold_limit <= 0:
            return 0.0
        return round((self.primary_metric_value / self.threshold_limit) * 100, 2)

    def is_critical_alert(self) -> bool:
        return self.calculate_utilization_ratio() > (100.0 - self.safety_margin_percentage)

class UrbanPlanningEntity73(BaseModel):
    """Operational domain entity 73 for Urban Planning & Zoning Regulation."""
    model_config = ConfigDict(from_attributes=True, extra='ignore')

    entity_id: str = Field(..., description='Unique identifier for UrbanPlanningEntity73')
    reference_code: str = Field(..., description='Official municipal reference code')
    status: UrbanPlanningStatus = Field(default=UrbanPlanningStatus.ACTIVE)
    priority: UrbanPlanningPriority = Field(default=UrbanPlanningPriority.STANDARD)
    ward_id: int = Field(default=1, ge=1, le=150, description='Municipal jurisdictional ward number')
    zone_code: str = Field(default='ZONE-CENTRAL', description='Municipal operational zone code')
    latitude: float = Field(default=17.385044, ge=-90.0, le=90.0)
    longitude: float = Field(default=78.486671, ge=-180.0, le=180.0)
    altitude_meters: Optional[float] = Field(default=542.0)
    primary_metric_value: float = Field(default=100.0, description='Domain standard quantitative measurement')
    secondary_metric_value: float = Field(default=45.5, description='Secondary operational metric')
    threshold_limit: float = Field(default=150.0, description='Configured statutory threshold')
    safety_margin_percentage: float = Field(default=15.0)
    is_compliant: bool = Field(default=True)
    supervisor_notes: Optional[str] = Field(default=None)
    assigned_officer_id: Optional[str] = Field(default=None)
    tags: List[str] = Field(default_factory=lambda: ['civic', 'smart-city', 'telemetry'])
    metadata_payload: Dict[str, Any] = Field(default_factory=dict)
    created_at: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))
    updated_at: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))

    @field_validator('primary_metric_value')
    @classmethod
    def validate_metric(cls, v: float) -> float:
        if v < 0:
            raise ValueError('Metric value cannot be negative in municipal calculations')
        return round(v, 4)

    def calculate_utilization_ratio(self) -> float:
        if self.threshold_limit <= 0:
            return 0.0
        return round((self.primary_metric_value / self.threshold_limit) * 100, 2)

    def is_critical_alert(self) -> bool:
        return self.calculate_utilization_ratio() > (100.0 - self.safety_margin_percentage)

class UrbanPlanningEntity74(BaseModel):
    """Operational domain entity 74 for Urban Planning & Zoning Regulation."""
    model_config = ConfigDict(from_attributes=True, extra='ignore')

    entity_id: str = Field(..., description='Unique identifier for UrbanPlanningEntity74')
    reference_code: str = Field(..., description='Official municipal reference code')
    status: UrbanPlanningStatus = Field(default=UrbanPlanningStatus.ACTIVE)
    priority: UrbanPlanningPriority = Field(default=UrbanPlanningPriority.STANDARD)
    ward_id: int = Field(default=1, ge=1, le=150, description='Municipal jurisdictional ward number')
    zone_code: str = Field(default='ZONE-CENTRAL', description='Municipal operational zone code')
    latitude: float = Field(default=17.385044, ge=-90.0, le=90.0)
    longitude: float = Field(default=78.486671, ge=-180.0, le=180.0)
    altitude_meters: Optional[float] = Field(default=542.0)
    primary_metric_value: float = Field(default=100.0, description='Domain standard quantitative measurement')
    secondary_metric_value: float = Field(default=45.5, description='Secondary operational metric')
    threshold_limit: float = Field(default=150.0, description='Configured statutory threshold')
    safety_margin_percentage: float = Field(default=15.0)
    is_compliant: bool = Field(default=True)
    supervisor_notes: Optional[str] = Field(default=None)
    assigned_officer_id: Optional[str] = Field(default=None)
    tags: List[str] = Field(default_factory=lambda: ['civic', 'smart-city', 'telemetry'])
    metadata_payload: Dict[str, Any] = Field(default_factory=dict)
    created_at: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))
    updated_at: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))

    @field_validator('primary_metric_value')
    @classmethod
    def validate_metric(cls, v: float) -> float:
        if v < 0:
            raise ValueError('Metric value cannot be negative in municipal calculations')
        return round(v, 4)

    def calculate_utilization_ratio(self) -> float:
        if self.threshold_limit <= 0:
            return 0.0
        return round((self.primary_metric_value / self.threshold_limit) * 100, 2)

    def is_critical_alert(self) -> bool:
        return self.calculate_utilization_ratio() > (100.0 - self.safety_margin_percentage)

class UrbanPlanningEntity75(BaseModel):
    """Operational domain entity 75 for Urban Planning & Zoning Regulation."""
    model_config = ConfigDict(from_attributes=True, extra='ignore')

    entity_id: str = Field(..., description='Unique identifier for UrbanPlanningEntity75')
    reference_code: str = Field(..., description='Official municipal reference code')
    status: UrbanPlanningStatus = Field(default=UrbanPlanningStatus.ACTIVE)
    priority: UrbanPlanningPriority = Field(default=UrbanPlanningPriority.STANDARD)
    ward_id: int = Field(default=1, ge=1, le=150, description='Municipal jurisdictional ward number')
    zone_code: str = Field(default='ZONE-CENTRAL', description='Municipal operational zone code')
    latitude: float = Field(default=17.385044, ge=-90.0, le=90.0)
    longitude: float = Field(default=78.486671, ge=-180.0, le=180.0)
    altitude_meters: Optional[float] = Field(default=542.0)
    primary_metric_value: float = Field(default=100.0, description='Domain standard quantitative measurement')
    secondary_metric_value: float = Field(default=45.5, description='Secondary operational metric')
    threshold_limit: float = Field(default=150.0, description='Configured statutory threshold')
    safety_margin_percentage: float = Field(default=15.0)
    is_compliant: bool = Field(default=True)
    supervisor_notes: Optional[str] = Field(default=None)
    assigned_officer_id: Optional[str] = Field(default=None)
    tags: List[str] = Field(default_factory=lambda: ['civic', 'smart-city', 'telemetry'])
    metadata_payload: Dict[str, Any] = Field(default_factory=dict)
    created_at: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))
    updated_at: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))

    @field_validator('primary_metric_value')
    @classmethod
    def validate_metric(cls, v: float) -> float:
        if v < 0:
            raise ValueError('Metric value cannot be negative in municipal calculations')
        return round(v, 4)

    def calculate_utilization_ratio(self) -> float:
        if self.threshold_limit <= 0:
            return 0.0
        return round((self.primary_metric_value / self.threshold_limit) * 100, 2)

    def is_critical_alert(self) -> bool:
        return self.calculate_utilization_ratio() > (100.0 - self.safety_margin_percentage)

class UrbanPlanningEntity76(BaseModel):
    """Operational domain entity 76 for Urban Planning & Zoning Regulation."""
    model_config = ConfigDict(from_attributes=True, extra='ignore')

    entity_id: str = Field(..., description='Unique identifier for UrbanPlanningEntity76')
    reference_code: str = Field(..., description='Official municipal reference code')
    status: UrbanPlanningStatus = Field(default=UrbanPlanningStatus.ACTIVE)
    priority: UrbanPlanningPriority = Field(default=UrbanPlanningPriority.STANDARD)
    ward_id: int = Field(default=1, ge=1, le=150, description='Municipal jurisdictional ward number')
    zone_code: str = Field(default='ZONE-CENTRAL', description='Municipal operational zone code')
    latitude: float = Field(default=17.385044, ge=-90.0, le=90.0)
    longitude: float = Field(default=78.486671, ge=-180.0, le=180.0)
    altitude_meters: Optional[float] = Field(default=542.0)
    primary_metric_value: float = Field(default=100.0, description='Domain standard quantitative measurement')
    secondary_metric_value: float = Field(default=45.5, description='Secondary operational metric')
    threshold_limit: float = Field(default=150.0, description='Configured statutory threshold')
    safety_margin_percentage: float = Field(default=15.0)
    is_compliant: bool = Field(default=True)
    supervisor_notes: Optional[str] = Field(default=None)
    assigned_officer_id: Optional[str] = Field(default=None)
    tags: List[str] = Field(default_factory=lambda: ['civic', 'smart-city', 'telemetry'])
    metadata_payload: Dict[str, Any] = Field(default_factory=dict)
    created_at: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))
    updated_at: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))

    @field_validator('primary_metric_value')
    @classmethod
    def validate_metric(cls, v: float) -> float:
        if v < 0:
            raise ValueError('Metric value cannot be negative in municipal calculations')
        return round(v, 4)

    def calculate_utilization_ratio(self) -> float:
        if self.threshold_limit <= 0:
            return 0.0
        return round((self.primary_metric_value / self.threshold_limit) * 100, 2)

    def is_critical_alert(self) -> bool:
        return self.calculate_utilization_ratio() > (100.0 - self.safety_margin_percentage)

class UrbanPlanningEntity77(BaseModel):
    """Operational domain entity 77 for Urban Planning & Zoning Regulation."""
    model_config = ConfigDict(from_attributes=True, extra='ignore')

    entity_id: str = Field(..., description='Unique identifier for UrbanPlanningEntity77')
    reference_code: str = Field(..., description='Official municipal reference code')
    status: UrbanPlanningStatus = Field(default=UrbanPlanningStatus.ACTIVE)
    priority: UrbanPlanningPriority = Field(default=UrbanPlanningPriority.STANDARD)
    ward_id: int = Field(default=1, ge=1, le=150, description='Municipal jurisdictional ward number')
    zone_code: str = Field(default='ZONE-CENTRAL', description='Municipal operational zone code')
    latitude: float = Field(default=17.385044, ge=-90.0, le=90.0)
    longitude: float = Field(default=78.486671, ge=-180.0, le=180.0)
    altitude_meters: Optional[float] = Field(default=542.0)
    primary_metric_value: float = Field(default=100.0, description='Domain standard quantitative measurement')
    secondary_metric_value: float = Field(default=45.5, description='Secondary operational metric')
    threshold_limit: float = Field(default=150.0, description='Configured statutory threshold')
    safety_margin_percentage: float = Field(default=15.0)
    is_compliant: bool = Field(default=True)
    supervisor_notes: Optional[str] = Field(default=None)
    assigned_officer_id: Optional[str] = Field(default=None)
    tags: List[str] = Field(default_factory=lambda: ['civic', 'smart-city', 'telemetry'])
    metadata_payload: Dict[str, Any] = Field(default_factory=dict)
    created_at: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))
    updated_at: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))

    @field_validator('primary_metric_value')
    @classmethod
    def validate_metric(cls, v: float) -> float:
        if v < 0:
            raise ValueError('Metric value cannot be negative in municipal calculations')
        return round(v, 4)

    def calculate_utilization_ratio(self) -> float:
        if self.threshold_limit <= 0:
            return 0.0
        return round((self.primary_metric_value / self.threshold_limit) * 100, 2)

    def is_critical_alert(self) -> bool:
        return self.calculate_utilization_ratio() > (100.0 - self.safety_margin_percentage)

class UrbanPlanningEntity78(BaseModel):
    """Operational domain entity 78 for Urban Planning & Zoning Regulation."""
    model_config = ConfigDict(from_attributes=True, extra='ignore')

    entity_id: str = Field(..., description='Unique identifier for UrbanPlanningEntity78')
    reference_code: str = Field(..., description='Official municipal reference code')
    status: UrbanPlanningStatus = Field(default=UrbanPlanningStatus.ACTIVE)
    priority: UrbanPlanningPriority = Field(default=UrbanPlanningPriority.STANDARD)
    ward_id: int = Field(default=1, ge=1, le=150, description='Municipal jurisdictional ward number')
    zone_code: str = Field(default='ZONE-CENTRAL', description='Municipal operational zone code')
    latitude: float = Field(default=17.385044, ge=-90.0, le=90.0)
    longitude: float = Field(default=78.486671, ge=-180.0, le=180.0)
    altitude_meters: Optional[float] = Field(default=542.0)
    primary_metric_value: float = Field(default=100.0, description='Domain standard quantitative measurement')
    secondary_metric_value: float = Field(default=45.5, description='Secondary operational metric')
    threshold_limit: float = Field(default=150.0, description='Configured statutory threshold')
    safety_margin_percentage: float = Field(default=15.0)
    is_compliant: bool = Field(default=True)
    supervisor_notes: Optional[str] = Field(default=None)
    assigned_officer_id: Optional[str] = Field(default=None)
    tags: List[str] = Field(default_factory=lambda: ['civic', 'smart-city', 'telemetry'])
    metadata_payload: Dict[str, Any] = Field(default_factory=dict)
    created_at: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))
    updated_at: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))

    @field_validator('primary_metric_value')
    @classmethod
    def validate_metric(cls, v: float) -> float:
        if v < 0:
            raise ValueError('Metric value cannot be negative in municipal calculations')
        return round(v, 4)

    def calculate_utilization_ratio(self) -> float:
        if self.threshold_limit <= 0:
            return 0.0
        return round((self.primary_metric_value / self.threshold_limit) * 100, 2)

    def is_critical_alert(self) -> bool:
        return self.calculate_utilization_ratio() > (100.0 - self.safety_margin_percentage)

class UrbanPlanningEntity79(BaseModel):
    """Operational domain entity 79 for Urban Planning & Zoning Regulation."""
    model_config = ConfigDict(from_attributes=True, extra='ignore')

    entity_id: str = Field(..., description='Unique identifier for UrbanPlanningEntity79')
    reference_code: str = Field(..., description='Official municipal reference code')
    status: UrbanPlanningStatus = Field(default=UrbanPlanningStatus.ACTIVE)
    priority: UrbanPlanningPriority = Field(default=UrbanPlanningPriority.STANDARD)
    ward_id: int = Field(default=1, ge=1, le=150, description='Municipal jurisdictional ward number')
    zone_code: str = Field(default='ZONE-CENTRAL', description='Municipal operational zone code')
    latitude: float = Field(default=17.385044, ge=-90.0, le=90.0)
    longitude: float = Field(default=78.486671, ge=-180.0, le=180.0)
    altitude_meters: Optional[float] = Field(default=542.0)
    primary_metric_value: float = Field(default=100.0, description='Domain standard quantitative measurement')
    secondary_metric_value: float = Field(default=45.5, description='Secondary operational metric')
    threshold_limit: float = Field(default=150.0, description='Configured statutory threshold')
    safety_margin_percentage: float = Field(default=15.0)
    is_compliant: bool = Field(default=True)
    supervisor_notes: Optional[str] = Field(default=None)
    assigned_officer_id: Optional[str] = Field(default=None)
    tags: List[str] = Field(default_factory=lambda: ['civic', 'smart-city', 'telemetry'])
    metadata_payload: Dict[str, Any] = Field(default_factory=dict)
    created_at: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))
    updated_at: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))

    @field_validator('primary_metric_value')
    @classmethod
    def validate_metric(cls, v: float) -> float:
        if v < 0:
            raise ValueError('Metric value cannot be negative in municipal calculations')
        return round(v, 4)

    def calculate_utilization_ratio(self) -> float:
        if self.threshold_limit <= 0:
            return 0.0
        return round((self.primary_metric_value / self.threshold_limit) * 100, 2)

    def is_critical_alert(self) -> bool:
        return self.calculate_utilization_ratio() > (100.0 - self.safety_margin_percentage)

class UrbanPlanningEntity80(BaseModel):
    """Operational domain entity 80 for Urban Planning & Zoning Regulation."""
    model_config = ConfigDict(from_attributes=True, extra='ignore')

    entity_id: str = Field(..., description='Unique identifier for UrbanPlanningEntity80')
    reference_code: str = Field(..., description='Official municipal reference code')
    status: UrbanPlanningStatus = Field(default=UrbanPlanningStatus.ACTIVE)
    priority: UrbanPlanningPriority = Field(default=UrbanPlanningPriority.STANDARD)
    ward_id: int = Field(default=1, ge=1, le=150, description='Municipal jurisdictional ward number')
    zone_code: str = Field(default='ZONE-CENTRAL', description='Municipal operational zone code')
    latitude: float = Field(default=17.385044, ge=-90.0, le=90.0)
    longitude: float = Field(default=78.486671, ge=-180.0, le=180.0)
    altitude_meters: Optional[float] = Field(default=542.0)
    primary_metric_value: float = Field(default=100.0, description='Domain standard quantitative measurement')
    secondary_metric_value: float = Field(default=45.5, description='Secondary operational metric')
    threshold_limit: float = Field(default=150.0, description='Configured statutory threshold')
    safety_margin_percentage: float = Field(default=15.0)
    is_compliant: bool = Field(default=True)
    supervisor_notes: Optional[str] = Field(default=None)
    assigned_officer_id: Optional[str] = Field(default=None)
    tags: List[str] = Field(default_factory=lambda: ['civic', 'smart-city', 'telemetry'])
    metadata_payload: Dict[str, Any] = Field(default_factory=dict)
    created_at: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))
    updated_at: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))

    @field_validator('primary_metric_value')
    @classmethod
    def validate_metric(cls, v: float) -> float:
        if v < 0:
            raise ValueError('Metric value cannot be negative in municipal calculations')
        return round(v, 4)

    def calculate_utilization_ratio(self) -> float:
        if self.threshold_limit <= 0:
            return 0.0
        return round((self.primary_metric_value / self.threshold_limit) * 100, 2)

    def is_critical_alert(self) -> bool:
        return self.calculate_utilization_ratio() > (100.0 - self.safety_margin_percentage)

class UrbanPlanningEntity81(BaseModel):
    """Operational domain entity 81 for Urban Planning & Zoning Regulation."""
    model_config = ConfigDict(from_attributes=True, extra='ignore')

    entity_id: str = Field(..., description='Unique identifier for UrbanPlanningEntity81')
    reference_code: str = Field(..., description='Official municipal reference code')
    status: UrbanPlanningStatus = Field(default=UrbanPlanningStatus.ACTIVE)
    priority: UrbanPlanningPriority = Field(default=UrbanPlanningPriority.STANDARD)
    ward_id: int = Field(default=1, ge=1, le=150, description='Municipal jurisdictional ward number')
    zone_code: str = Field(default='ZONE-CENTRAL', description='Municipal operational zone code')
    latitude: float = Field(default=17.385044, ge=-90.0, le=90.0)
    longitude: float = Field(default=78.486671, ge=-180.0, le=180.0)
    altitude_meters: Optional[float] = Field(default=542.0)
    primary_metric_value: float = Field(default=100.0, description='Domain standard quantitative measurement')
    secondary_metric_value: float = Field(default=45.5, description='Secondary operational metric')
    threshold_limit: float = Field(default=150.0, description='Configured statutory threshold')
    safety_margin_percentage: float = Field(default=15.0)
    is_compliant: bool = Field(default=True)
    supervisor_notes: Optional[str] = Field(default=None)
    assigned_officer_id: Optional[str] = Field(default=None)
    tags: List[str] = Field(default_factory=lambda: ['civic', 'smart-city', 'telemetry'])
    metadata_payload: Dict[str, Any] = Field(default_factory=dict)
    created_at: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))
    updated_at: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))

    @field_validator('primary_metric_value')
    @classmethod
    def validate_metric(cls, v: float) -> float:
        if v < 0:
            raise ValueError('Metric value cannot be negative in municipal calculations')
        return round(v, 4)

    def calculate_utilization_ratio(self) -> float:
        if self.threshold_limit <= 0:
            return 0.0
        return round((self.primary_metric_value / self.threshold_limit) * 100, 2)

    def is_critical_alert(self) -> bool:
        return self.calculate_utilization_ratio() > (100.0 - self.safety_margin_percentage)

class UrbanPlanningEntity82(BaseModel):
    """Operational domain entity 82 for Urban Planning & Zoning Regulation."""
    model_config = ConfigDict(from_attributes=True, extra='ignore')

    entity_id: str = Field(..., description='Unique identifier for UrbanPlanningEntity82')
    reference_code: str = Field(..., description='Official municipal reference code')
    status: UrbanPlanningStatus = Field(default=UrbanPlanningStatus.ACTIVE)
    priority: UrbanPlanningPriority = Field(default=UrbanPlanningPriority.STANDARD)
    ward_id: int = Field(default=1, ge=1, le=150, description='Municipal jurisdictional ward number')
    zone_code: str = Field(default='ZONE-CENTRAL', description='Municipal operational zone code')
    latitude: float = Field(default=17.385044, ge=-90.0, le=90.0)
    longitude: float = Field(default=78.486671, ge=-180.0, le=180.0)
    altitude_meters: Optional[float] = Field(default=542.0)
    primary_metric_value: float = Field(default=100.0, description='Domain standard quantitative measurement')
    secondary_metric_value: float = Field(default=45.5, description='Secondary operational metric')
    threshold_limit: float = Field(default=150.0, description='Configured statutory threshold')
    safety_margin_percentage: float = Field(default=15.0)
    is_compliant: bool = Field(default=True)
    supervisor_notes: Optional[str] = Field(default=None)
    assigned_officer_id: Optional[str] = Field(default=None)
    tags: List[str] = Field(default_factory=lambda: ['civic', 'smart-city', 'telemetry'])
    metadata_payload: Dict[str, Any] = Field(default_factory=dict)
    created_at: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))
    updated_at: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))

    @field_validator('primary_metric_value')
    @classmethod
    def validate_metric(cls, v: float) -> float:
        if v < 0:
            raise ValueError('Metric value cannot be negative in municipal calculations')
        return round(v, 4)

    def calculate_utilization_ratio(self) -> float:
        if self.threshold_limit <= 0:
            return 0.0
        return round((self.primary_metric_value / self.threshold_limit) * 100, 2)

    def is_critical_alert(self) -> bool:
        return self.calculate_utilization_ratio() > (100.0 - self.safety_margin_percentage)

class UrbanPlanningEntity83(BaseModel):
    """Operational domain entity 83 for Urban Planning & Zoning Regulation."""
    model_config = ConfigDict(from_attributes=True, extra='ignore')

    entity_id: str = Field(..., description='Unique identifier for UrbanPlanningEntity83')
    reference_code: str = Field(..., description='Official municipal reference code')
    status: UrbanPlanningStatus = Field(default=UrbanPlanningStatus.ACTIVE)
    priority: UrbanPlanningPriority = Field(default=UrbanPlanningPriority.STANDARD)
    ward_id: int = Field(default=1, ge=1, le=150, description='Municipal jurisdictional ward number')
    zone_code: str = Field(default='ZONE-CENTRAL', description='Municipal operational zone code')
    latitude: float = Field(default=17.385044, ge=-90.0, le=90.0)
    longitude: float = Field(default=78.486671, ge=-180.0, le=180.0)
    altitude_meters: Optional[float] = Field(default=542.0)
    primary_metric_value: float = Field(default=100.0, description='Domain standard quantitative measurement')
    secondary_metric_value: float = Field(default=45.5, description='Secondary operational metric')
    threshold_limit: float = Field(default=150.0, description='Configured statutory threshold')
    safety_margin_percentage: float = Field(default=15.0)
    is_compliant: bool = Field(default=True)
    supervisor_notes: Optional[str] = Field(default=None)
    assigned_officer_id: Optional[str] = Field(default=None)
    tags: List[str] = Field(default_factory=lambda: ['civic', 'smart-city', 'telemetry'])
    metadata_payload: Dict[str, Any] = Field(default_factory=dict)
    created_at: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))
    updated_at: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))

    @field_validator('primary_metric_value')
    @classmethod
    def validate_metric(cls, v: float) -> float:
        if v < 0:
            raise ValueError('Metric value cannot be negative in municipal calculations')
        return round(v, 4)

    def calculate_utilization_ratio(self) -> float:
        if self.threshold_limit <= 0:
            return 0.0
        return round((self.primary_metric_value / self.threshold_limit) * 100, 2)

    def is_critical_alert(self) -> bool:
        return self.calculate_utilization_ratio() > (100.0 - self.safety_margin_percentage)

class UrbanPlanningEntity84(BaseModel):
    """Operational domain entity 84 for Urban Planning & Zoning Regulation."""
    model_config = ConfigDict(from_attributes=True, extra='ignore')

    entity_id: str = Field(..., description='Unique identifier for UrbanPlanningEntity84')
    reference_code: str = Field(..., description='Official municipal reference code')
    status: UrbanPlanningStatus = Field(default=UrbanPlanningStatus.ACTIVE)
    priority: UrbanPlanningPriority = Field(default=UrbanPlanningPriority.STANDARD)
    ward_id: int = Field(default=1, ge=1, le=150, description='Municipal jurisdictional ward number')
    zone_code: str = Field(default='ZONE-CENTRAL', description='Municipal operational zone code')
    latitude: float = Field(default=17.385044, ge=-90.0, le=90.0)
    longitude: float = Field(default=78.486671, ge=-180.0, le=180.0)
    altitude_meters: Optional[float] = Field(default=542.0)
    primary_metric_value: float = Field(default=100.0, description='Domain standard quantitative measurement')
    secondary_metric_value: float = Field(default=45.5, description='Secondary operational metric')
    threshold_limit: float = Field(default=150.0, description='Configured statutory threshold')
    safety_margin_percentage: float = Field(default=15.0)
    is_compliant: bool = Field(default=True)
    supervisor_notes: Optional[str] = Field(default=None)
    assigned_officer_id: Optional[str] = Field(default=None)
    tags: List[str] = Field(default_factory=lambda: ['civic', 'smart-city', 'telemetry'])
    metadata_payload: Dict[str, Any] = Field(default_factory=dict)
    created_at: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))
    updated_at: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))

    @field_validator('primary_metric_value')
    @classmethod
    def validate_metric(cls, v: float) -> float:
        if v < 0:
            raise ValueError('Metric value cannot be negative in municipal calculations')
        return round(v, 4)

    def calculate_utilization_ratio(self) -> float:
        if self.threshold_limit <= 0:
            return 0.0
        return round((self.primary_metric_value / self.threshold_limit) * 100, 2)

    def is_critical_alert(self) -> bool:
        return self.calculate_utilization_ratio() > (100.0 - self.safety_margin_percentage)

class UrbanPlanningEntity85(BaseModel):
    """Operational domain entity 85 for Urban Planning & Zoning Regulation."""
    model_config = ConfigDict(from_attributes=True, extra='ignore')

    entity_id: str = Field(..., description='Unique identifier for UrbanPlanningEntity85')
    reference_code: str = Field(..., description='Official municipal reference code')
    status: UrbanPlanningStatus = Field(default=UrbanPlanningStatus.ACTIVE)
    priority: UrbanPlanningPriority = Field(default=UrbanPlanningPriority.STANDARD)
    ward_id: int = Field(default=1, ge=1, le=150, description='Municipal jurisdictional ward number')
    zone_code: str = Field(default='ZONE-CENTRAL', description='Municipal operational zone code')
    latitude: float = Field(default=17.385044, ge=-90.0, le=90.0)
    longitude: float = Field(default=78.486671, ge=-180.0, le=180.0)
    altitude_meters: Optional[float] = Field(default=542.0)
    primary_metric_value: float = Field(default=100.0, description='Domain standard quantitative measurement')
    secondary_metric_value: float = Field(default=45.5, description='Secondary operational metric')
    threshold_limit: float = Field(default=150.0, description='Configured statutory threshold')
    safety_margin_percentage: float = Field(default=15.0)
    is_compliant: bool = Field(default=True)
    supervisor_notes: Optional[str] = Field(default=None)
    assigned_officer_id: Optional[str] = Field(default=None)
    tags: List[str] = Field(default_factory=lambda: ['civic', 'smart-city', 'telemetry'])
    metadata_payload: Dict[str, Any] = Field(default_factory=dict)
    created_at: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))
    updated_at: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))

    @field_validator('primary_metric_value')
    @classmethod
    def validate_metric(cls, v: float) -> float:
        if v < 0:
            raise ValueError('Metric value cannot be negative in municipal calculations')
        return round(v, 4)

    def calculate_utilization_ratio(self) -> float:
        if self.threshold_limit <= 0:
            return 0.0
        return round((self.primary_metric_value / self.threshold_limit) * 100, 2)

    def is_critical_alert(self) -> bool:
        return self.calculate_utilization_ratio() > (100.0 - self.safety_margin_percentage)

class UrbanPlanningEntity86(BaseModel):
    """Operational domain entity 86 for Urban Planning & Zoning Regulation."""
    model_config = ConfigDict(from_attributes=True, extra='ignore')

    entity_id: str = Field(..., description='Unique identifier for UrbanPlanningEntity86')
    reference_code: str = Field(..., description='Official municipal reference code')
    status: UrbanPlanningStatus = Field(default=UrbanPlanningStatus.ACTIVE)
    priority: UrbanPlanningPriority = Field(default=UrbanPlanningPriority.STANDARD)
    ward_id: int = Field(default=1, ge=1, le=150, description='Municipal jurisdictional ward number')
    zone_code: str = Field(default='ZONE-CENTRAL', description='Municipal operational zone code')
    latitude: float = Field(default=17.385044, ge=-90.0, le=90.0)
    longitude: float = Field(default=78.486671, ge=-180.0, le=180.0)
    altitude_meters: Optional[float] = Field(default=542.0)
    primary_metric_value: float = Field(default=100.0, description='Domain standard quantitative measurement')
    secondary_metric_value: float = Field(default=45.5, description='Secondary operational metric')
    threshold_limit: float = Field(default=150.0, description='Configured statutory threshold')
    safety_margin_percentage: float = Field(default=15.0)
    is_compliant: bool = Field(default=True)
    supervisor_notes: Optional[str] = Field(default=None)
    assigned_officer_id: Optional[str] = Field(default=None)
    tags: List[str] = Field(default_factory=lambda: ['civic', 'smart-city', 'telemetry'])
    metadata_payload: Dict[str, Any] = Field(default_factory=dict)
    created_at: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))
    updated_at: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))

    @field_validator('primary_metric_value')
    @classmethod
    def validate_metric(cls, v: float) -> float:
        if v < 0:
            raise ValueError('Metric value cannot be negative in municipal calculations')
        return round(v, 4)

    def calculate_utilization_ratio(self) -> float:
        if self.threshold_limit <= 0:
            return 0.0
        return round((self.primary_metric_value / self.threshold_limit) * 100, 2)

    def is_critical_alert(self) -> bool:
        return self.calculate_utilization_ratio() > (100.0 - self.safety_margin_percentage)

class UrbanPlanningEntity87(BaseModel):
    """Operational domain entity 87 for Urban Planning & Zoning Regulation."""
    model_config = ConfigDict(from_attributes=True, extra='ignore')

    entity_id: str = Field(..., description='Unique identifier for UrbanPlanningEntity87')
    reference_code: str = Field(..., description='Official municipal reference code')
    status: UrbanPlanningStatus = Field(default=UrbanPlanningStatus.ACTIVE)
    priority: UrbanPlanningPriority = Field(default=UrbanPlanningPriority.STANDARD)
    ward_id: int = Field(default=1, ge=1, le=150, description='Municipal jurisdictional ward number')
    zone_code: str = Field(default='ZONE-CENTRAL', description='Municipal operational zone code')
    latitude: float = Field(default=17.385044, ge=-90.0, le=90.0)
    longitude: float = Field(default=78.486671, ge=-180.0, le=180.0)
    altitude_meters: Optional[float] = Field(default=542.0)
    primary_metric_value: float = Field(default=100.0, description='Domain standard quantitative measurement')
    secondary_metric_value: float = Field(default=45.5, description='Secondary operational metric')
    threshold_limit: float = Field(default=150.0, description='Configured statutory threshold')
    safety_margin_percentage: float = Field(default=15.0)
    is_compliant: bool = Field(default=True)
    supervisor_notes: Optional[str] = Field(default=None)
    assigned_officer_id: Optional[str] = Field(default=None)
    tags: List[str] = Field(default_factory=lambda: ['civic', 'smart-city', 'telemetry'])
    metadata_payload: Dict[str, Any] = Field(default_factory=dict)
    created_at: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))
    updated_at: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))

    @field_validator('primary_metric_value')
    @classmethod
    def validate_metric(cls, v: float) -> float:
        if v < 0:
            raise ValueError('Metric value cannot be negative in municipal calculations')
        return round(v, 4)

    def calculate_utilization_ratio(self) -> float:
        if self.threshold_limit <= 0:
            return 0.0
        return round((self.primary_metric_value / self.threshold_limit) * 100, 2)

    def is_critical_alert(self) -> bool:
        return self.calculate_utilization_ratio() > (100.0 - self.safety_margin_percentage)

class UrbanPlanningEntity88(BaseModel):
    """Operational domain entity 88 for Urban Planning & Zoning Regulation."""
    model_config = ConfigDict(from_attributes=True, extra='ignore')

    entity_id: str = Field(..., description='Unique identifier for UrbanPlanningEntity88')
    reference_code: str = Field(..., description='Official municipal reference code')
    status: UrbanPlanningStatus = Field(default=UrbanPlanningStatus.ACTIVE)
    priority: UrbanPlanningPriority = Field(default=UrbanPlanningPriority.STANDARD)
    ward_id: int = Field(default=1, ge=1, le=150, description='Municipal jurisdictional ward number')
    zone_code: str = Field(default='ZONE-CENTRAL', description='Municipal operational zone code')
    latitude: float = Field(default=17.385044, ge=-90.0, le=90.0)
    longitude: float = Field(default=78.486671, ge=-180.0, le=180.0)
    altitude_meters: Optional[float] = Field(default=542.0)
    primary_metric_value: float = Field(default=100.0, description='Domain standard quantitative measurement')
    secondary_metric_value: float = Field(default=45.5, description='Secondary operational metric')
    threshold_limit: float = Field(default=150.0, description='Configured statutory threshold')
    safety_margin_percentage: float = Field(default=15.0)
    is_compliant: bool = Field(default=True)
    supervisor_notes: Optional[str] = Field(default=None)
    assigned_officer_id: Optional[str] = Field(default=None)
    tags: List[str] = Field(default_factory=lambda: ['civic', 'smart-city', 'telemetry'])
    metadata_payload: Dict[str, Any] = Field(default_factory=dict)
    created_at: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))
    updated_at: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))

    @field_validator('primary_metric_value')
    @classmethod
    def validate_metric(cls, v: float) -> float:
        if v < 0:
            raise ValueError('Metric value cannot be negative in municipal calculations')
        return round(v, 4)

    def calculate_utilization_ratio(self) -> float:
        if self.threshold_limit <= 0:
            return 0.0
        return round((self.primary_metric_value / self.threshold_limit) * 100, 2)

    def is_critical_alert(self) -> bool:
        return self.calculate_utilization_ratio() > (100.0 - self.safety_margin_percentage)

class UrbanPlanningEntity89(BaseModel):
    """Operational domain entity 89 for Urban Planning & Zoning Regulation."""
    model_config = ConfigDict(from_attributes=True, extra='ignore')

    entity_id: str = Field(..., description='Unique identifier for UrbanPlanningEntity89')
    reference_code: str = Field(..., description='Official municipal reference code')
    status: UrbanPlanningStatus = Field(default=UrbanPlanningStatus.ACTIVE)
    priority: UrbanPlanningPriority = Field(default=UrbanPlanningPriority.STANDARD)
    ward_id: int = Field(default=1, ge=1, le=150, description='Municipal jurisdictional ward number')
    zone_code: str = Field(default='ZONE-CENTRAL', description='Municipal operational zone code')
    latitude: float = Field(default=17.385044, ge=-90.0, le=90.0)
    longitude: float = Field(default=78.486671, ge=-180.0, le=180.0)
    altitude_meters: Optional[float] = Field(default=542.0)
    primary_metric_value: float = Field(default=100.0, description='Domain standard quantitative measurement')
    secondary_metric_value: float = Field(default=45.5, description='Secondary operational metric')
    threshold_limit: float = Field(default=150.0, description='Configured statutory threshold')
    safety_margin_percentage: float = Field(default=15.0)
    is_compliant: bool = Field(default=True)
    supervisor_notes: Optional[str] = Field(default=None)
    assigned_officer_id: Optional[str] = Field(default=None)
    tags: List[str] = Field(default_factory=lambda: ['civic', 'smart-city', 'telemetry'])
    metadata_payload: Dict[str, Any] = Field(default_factory=dict)
    created_at: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))
    updated_at: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))

    @field_validator('primary_metric_value')
    @classmethod
    def validate_metric(cls, v: float) -> float:
        if v < 0:
            raise ValueError('Metric value cannot be negative in municipal calculations')
        return round(v, 4)

    def calculate_utilization_ratio(self) -> float:
        if self.threshold_limit <= 0:
            return 0.0
        return round((self.primary_metric_value / self.threshold_limit) * 100, 2)

    def is_critical_alert(self) -> bool:
        return self.calculate_utilization_ratio() > (100.0 - self.safety_margin_percentage)

class UrbanPlanningEntity90(BaseModel):
    """Operational domain entity 90 for Urban Planning & Zoning Regulation."""
    model_config = ConfigDict(from_attributes=True, extra='ignore')

    entity_id: str = Field(..., description='Unique identifier for UrbanPlanningEntity90')
    reference_code: str = Field(..., description='Official municipal reference code')
    status: UrbanPlanningStatus = Field(default=UrbanPlanningStatus.ACTIVE)
    priority: UrbanPlanningPriority = Field(default=UrbanPlanningPriority.STANDARD)
    ward_id: int = Field(default=1, ge=1, le=150, description='Municipal jurisdictional ward number')
    zone_code: str = Field(default='ZONE-CENTRAL', description='Municipal operational zone code')
    latitude: float = Field(default=17.385044, ge=-90.0, le=90.0)
    longitude: float = Field(default=78.486671, ge=-180.0, le=180.0)
    altitude_meters: Optional[float] = Field(default=542.0)
    primary_metric_value: float = Field(default=100.0, description='Domain standard quantitative measurement')
    secondary_metric_value: float = Field(default=45.5, description='Secondary operational metric')
    threshold_limit: float = Field(default=150.0, description='Configured statutory threshold')
    safety_margin_percentage: float = Field(default=15.0)
    is_compliant: bool = Field(default=True)
    supervisor_notes: Optional[str] = Field(default=None)
    assigned_officer_id: Optional[str] = Field(default=None)
    tags: List[str] = Field(default_factory=lambda: ['civic', 'smart-city', 'telemetry'])
    metadata_payload: Dict[str, Any] = Field(default_factory=dict)
    created_at: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))
    updated_at: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))

    @field_validator('primary_metric_value')
    @classmethod
    def validate_metric(cls, v: float) -> float:
        if v < 0:
            raise ValueError('Metric value cannot be negative in municipal calculations')
        return round(v, 4)

    def calculate_utilization_ratio(self) -> float:
        if self.threshold_limit <= 0:
            return 0.0
        return round((self.primary_metric_value / self.threshold_limit) * 100, 2)

    def is_critical_alert(self) -> bool:
        return self.calculate_utilization_ratio() > (100.0 - self.safety_margin_percentage)
