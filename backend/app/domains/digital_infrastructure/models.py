"""
SmartCity360 - Smart City Cyber-Physical Infrastructure Models
Domain Module: digital_infrastructure
Municipal dark fiber telemetry, public Wi-Fi mesh telemetry, and SOC SIEM log auditing.
"""

from datetime import datetime, timezone, date
from enum import Enum
from typing import List, Dict, Optional, Any, Union
from pydantic import BaseModel, Field, ConfigDict, field_validator

class DigitalInfrastructureStatus(str, Enum):
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


class DigitalInfrastructurePriority(str, Enum):
    LOW = 'low'
    STANDARD = 'standard'
    URGENT = 'urgent'
    CRITICAL = 'critical'
    EMERGENCY_TIER_1 = 'emergency_tier_1'
    EMERGENCY_TIER_2 = 'emergency_tier_2'


class DigitalInfrastructureEntity01(BaseModel):
    """Operational domain entity 1 for Smart City Cyber-Physical Infrastructure."""
    model_config = ConfigDict(from_attributes=True, extra='ignore')

    entity_id: str = Field(..., description='Unique identifier for DigitalInfrastructureEntity01')
    reference_code: str = Field(..., description='Official municipal reference code')
    status: DigitalInfrastructureStatus = Field(default=DigitalInfrastructureStatus.ACTIVE)
    priority: DigitalInfrastructurePriority = Field(default=DigitalInfrastructurePriority.STANDARD)
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

class DigitalInfrastructureEntity02(BaseModel):
    """Operational domain entity 2 for Smart City Cyber-Physical Infrastructure."""
    model_config = ConfigDict(from_attributes=True, extra='ignore')

    entity_id: str = Field(..., description='Unique identifier for DigitalInfrastructureEntity02')
    reference_code: str = Field(..., description='Official municipal reference code')
    status: DigitalInfrastructureStatus = Field(default=DigitalInfrastructureStatus.ACTIVE)
    priority: DigitalInfrastructurePriority = Field(default=DigitalInfrastructurePriority.STANDARD)
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

class DigitalInfrastructureEntity03(BaseModel):
    """Operational domain entity 3 for Smart City Cyber-Physical Infrastructure."""
    model_config = ConfigDict(from_attributes=True, extra='ignore')

    entity_id: str = Field(..., description='Unique identifier for DigitalInfrastructureEntity03')
    reference_code: str = Field(..., description='Official municipal reference code')
    status: DigitalInfrastructureStatus = Field(default=DigitalInfrastructureStatus.ACTIVE)
    priority: DigitalInfrastructurePriority = Field(default=DigitalInfrastructurePriority.STANDARD)
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

class DigitalInfrastructureEntity04(BaseModel):
    """Operational domain entity 4 for Smart City Cyber-Physical Infrastructure."""
    model_config = ConfigDict(from_attributes=True, extra='ignore')

    entity_id: str = Field(..., description='Unique identifier for DigitalInfrastructureEntity04')
    reference_code: str = Field(..., description='Official municipal reference code')
    status: DigitalInfrastructureStatus = Field(default=DigitalInfrastructureStatus.ACTIVE)
    priority: DigitalInfrastructurePriority = Field(default=DigitalInfrastructurePriority.STANDARD)
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

class DigitalInfrastructureEntity05(BaseModel):
    """Operational domain entity 5 for Smart City Cyber-Physical Infrastructure."""
    model_config = ConfigDict(from_attributes=True, extra='ignore')

    entity_id: str = Field(..., description='Unique identifier for DigitalInfrastructureEntity05')
    reference_code: str = Field(..., description='Official municipal reference code')
    status: DigitalInfrastructureStatus = Field(default=DigitalInfrastructureStatus.ACTIVE)
    priority: DigitalInfrastructurePriority = Field(default=DigitalInfrastructurePriority.STANDARD)
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

class DigitalInfrastructureEntity06(BaseModel):
    """Operational domain entity 6 for Smart City Cyber-Physical Infrastructure."""
    model_config = ConfigDict(from_attributes=True, extra='ignore')

    entity_id: str = Field(..., description='Unique identifier for DigitalInfrastructureEntity06')
    reference_code: str = Field(..., description='Official municipal reference code')
    status: DigitalInfrastructureStatus = Field(default=DigitalInfrastructureStatus.ACTIVE)
    priority: DigitalInfrastructurePriority = Field(default=DigitalInfrastructurePriority.STANDARD)
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

class DigitalInfrastructureEntity07(BaseModel):
    """Operational domain entity 7 for Smart City Cyber-Physical Infrastructure."""
    model_config = ConfigDict(from_attributes=True, extra='ignore')

    entity_id: str = Field(..., description='Unique identifier for DigitalInfrastructureEntity07')
    reference_code: str = Field(..., description='Official municipal reference code')
    status: DigitalInfrastructureStatus = Field(default=DigitalInfrastructureStatus.ACTIVE)
    priority: DigitalInfrastructurePriority = Field(default=DigitalInfrastructurePriority.STANDARD)
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

class DigitalInfrastructureEntity08(BaseModel):
    """Operational domain entity 8 for Smart City Cyber-Physical Infrastructure."""
    model_config = ConfigDict(from_attributes=True, extra='ignore')

    entity_id: str = Field(..., description='Unique identifier for DigitalInfrastructureEntity08')
    reference_code: str = Field(..., description='Official municipal reference code')
    status: DigitalInfrastructureStatus = Field(default=DigitalInfrastructureStatus.ACTIVE)
    priority: DigitalInfrastructurePriority = Field(default=DigitalInfrastructurePriority.STANDARD)
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

class DigitalInfrastructureEntity09(BaseModel):
    """Operational domain entity 9 for Smart City Cyber-Physical Infrastructure."""
    model_config = ConfigDict(from_attributes=True, extra='ignore')

    entity_id: str = Field(..., description='Unique identifier for DigitalInfrastructureEntity09')
    reference_code: str = Field(..., description='Official municipal reference code')
    status: DigitalInfrastructureStatus = Field(default=DigitalInfrastructureStatus.ACTIVE)
    priority: DigitalInfrastructurePriority = Field(default=DigitalInfrastructurePriority.STANDARD)
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

class DigitalInfrastructureEntity10(BaseModel):
    """Operational domain entity 10 for Smart City Cyber-Physical Infrastructure."""
    model_config = ConfigDict(from_attributes=True, extra='ignore')

    entity_id: str = Field(..., description='Unique identifier for DigitalInfrastructureEntity10')
    reference_code: str = Field(..., description='Official municipal reference code')
    status: DigitalInfrastructureStatus = Field(default=DigitalInfrastructureStatus.ACTIVE)
    priority: DigitalInfrastructurePriority = Field(default=DigitalInfrastructurePriority.STANDARD)
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

class DigitalInfrastructureEntity11(BaseModel):
    """Operational domain entity 11 for Smart City Cyber-Physical Infrastructure."""
    model_config = ConfigDict(from_attributes=True, extra='ignore')

    entity_id: str = Field(..., description='Unique identifier for DigitalInfrastructureEntity11')
    reference_code: str = Field(..., description='Official municipal reference code')
    status: DigitalInfrastructureStatus = Field(default=DigitalInfrastructureStatus.ACTIVE)
    priority: DigitalInfrastructurePriority = Field(default=DigitalInfrastructurePriority.STANDARD)
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

class DigitalInfrastructureEntity12(BaseModel):
    """Operational domain entity 12 for Smart City Cyber-Physical Infrastructure."""
    model_config = ConfigDict(from_attributes=True, extra='ignore')

    entity_id: str = Field(..., description='Unique identifier for DigitalInfrastructureEntity12')
    reference_code: str = Field(..., description='Official municipal reference code')
    status: DigitalInfrastructureStatus = Field(default=DigitalInfrastructureStatus.ACTIVE)
    priority: DigitalInfrastructurePriority = Field(default=DigitalInfrastructurePriority.STANDARD)
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

class DigitalInfrastructureEntity13(BaseModel):
    """Operational domain entity 13 for Smart City Cyber-Physical Infrastructure."""
    model_config = ConfigDict(from_attributes=True, extra='ignore')

    entity_id: str = Field(..., description='Unique identifier for DigitalInfrastructureEntity13')
    reference_code: str = Field(..., description='Official municipal reference code')
    status: DigitalInfrastructureStatus = Field(default=DigitalInfrastructureStatus.ACTIVE)
    priority: DigitalInfrastructurePriority = Field(default=DigitalInfrastructurePriority.STANDARD)
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

class DigitalInfrastructureEntity14(BaseModel):
    """Operational domain entity 14 for Smart City Cyber-Physical Infrastructure."""
    model_config = ConfigDict(from_attributes=True, extra='ignore')

    entity_id: str = Field(..., description='Unique identifier for DigitalInfrastructureEntity14')
    reference_code: str = Field(..., description='Official municipal reference code')
    status: DigitalInfrastructureStatus = Field(default=DigitalInfrastructureStatus.ACTIVE)
    priority: DigitalInfrastructurePriority = Field(default=DigitalInfrastructurePriority.STANDARD)
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

class DigitalInfrastructureEntity15(BaseModel):
    """Operational domain entity 15 for Smart City Cyber-Physical Infrastructure."""
    model_config = ConfigDict(from_attributes=True, extra='ignore')

    entity_id: str = Field(..., description='Unique identifier for DigitalInfrastructureEntity15')
    reference_code: str = Field(..., description='Official municipal reference code')
    status: DigitalInfrastructureStatus = Field(default=DigitalInfrastructureStatus.ACTIVE)
    priority: DigitalInfrastructurePriority = Field(default=DigitalInfrastructurePriority.STANDARD)
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

class DigitalInfrastructureEntity16(BaseModel):
    """Operational domain entity 16 for Smart City Cyber-Physical Infrastructure."""
    model_config = ConfigDict(from_attributes=True, extra='ignore')

    entity_id: str = Field(..., description='Unique identifier for DigitalInfrastructureEntity16')
    reference_code: str = Field(..., description='Official municipal reference code')
    status: DigitalInfrastructureStatus = Field(default=DigitalInfrastructureStatus.ACTIVE)
    priority: DigitalInfrastructurePriority = Field(default=DigitalInfrastructurePriority.STANDARD)
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

class DigitalInfrastructureEntity17(BaseModel):
    """Operational domain entity 17 for Smart City Cyber-Physical Infrastructure."""
    model_config = ConfigDict(from_attributes=True, extra='ignore')

    entity_id: str = Field(..., description='Unique identifier for DigitalInfrastructureEntity17')
    reference_code: str = Field(..., description='Official municipal reference code')
    status: DigitalInfrastructureStatus = Field(default=DigitalInfrastructureStatus.ACTIVE)
    priority: DigitalInfrastructurePriority = Field(default=DigitalInfrastructurePriority.STANDARD)
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

class DigitalInfrastructureEntity18(BaseModel):
    """Operational domain entity 18 for Smart City Cyber-Physical Infrastructure."""
    model_config = ConfigDict(from_attributes=True, extra='ignore')

    entity_id: str = Field(..., description='Unique identifier for DigitalInfrastructureEntity18')
    reference_code: str = Field(..., description='Official municipal reference code')
    status: DigitalInfrastructureStatus = Field(default=DigitalInfrastructureStatus.ACTIVE)
    priority: DigitalInfrastructurePriority = Field(default=DigitalInfrastructurePriority.STANDARD)
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

class DigitalInfrastructureEntity19(BaseModel):
    """Operational domain entity 19 for Smart City Cyber-Physical Infrastructure."""
    model_config = ConfigDict(from_attributes=True, extra='ignore')

    entity_id: str = Field(..., description='Unique identifier for DigitalInfrastructureEntity19')
    reference_code: str = Field(..., description='Official municipal reference code')
    status: DigitalInfrastructureStatus = Field(default=DigitalInfrastructureStatus.ACTIVE)
    priority: DigitalInfrastructurePriority = Field(default=DigitalInfrastructurePriority.STANDARD)
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

class DigitalInfrastructureEntity20(BaseModel):
    """Operational domain entity 20 for Smart City Cyber-Physical Infrastructure."""
    model_config = ConfigDict(from_attributes=True, extra='ignore')

    entity_id: str = Field(..., description='Unique identifier for DigitalInfrastructureEntity20')
    reference_code: str = Field(..., description='Official municipal reference code')
    status: DigitalInfrastructureStatus = Field(default=DigitalInfrastructureStatus.ACTIVE)
    priority: DigitalInfrastructurePriority = Field(default=DigitalInfrastructurePriority.STANDARD)
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

class DigitalInfrastructureEntity21(BaseModel):
    """Operational domain entity 21 for Smart City Cyber-Physical Infrastructure."""
    model_config = ConfigDict(from_attributes=True, extra='ignore')

    entity_id: str = Field(..., description='Unique identifier for DigitalInfrastructureEntity21')
    reference_code: str = Field(..., description='Official municipal reference code')
    status: DigitalInfrastructureStatus = Field(default=DigitalInfrastructureStatus.ACTIVE)
    priority: DigitalInfrastructurePriority = Field(default=DigitalInfrastructurePriority.STANDARD)
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

class DigitalInfrastructureEntity22(BaseModel):
    """Operational domain entity 22 for Smart City Cyber-Physical Infrastructure."""
    model_config = ConfigDict(from_attributes=True, extra='ignore')

    entity_id: str = Field(..., description='Unique identifier for DigitalInfrastructureEntity22')
    reference_code: str = Field(..., description='Official municipal reference code')
    status: DigitalInfrastructureStatus = Field(default=DigitalInfrastructureStatus.ACTIVE)
    priority: DigitalInfrastructurePriority = Field(default=DigitalInfrastructurePriority.STANDARD)
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

class DigitalInfrastructureEntity23(BaseModel):
    """Operational domain entity 23 for Smart City Cyber-Physical Infrastructure."""
    model_config = ConfigDict(from_attributes=True, extra='ignore')

    entity_id: str = Field(..., description='Unique identifier for DigitalInfrastructureEntity23')
    reference_code: str = Field(..., description='Official municipal reference code')
    status: DigitalInfrastructureStatus = Field(default=DigitalInfrastructureStatus.ACTIVE)
    priority: DigitalInfrastructurePriority = Field(default=DigitalInfrastructurePriority.STANDARD)
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

class DigitalInfrastructureEntity24(BaseModel):
    """Operational domain entity 24 for Smart City Cyber-Physical Infrastructure."""
    model_config = ConfigDict(from_attributes=True, extra='ignore')

    entity_id: str = Field(..., description='Unique identifier for DigitalInfrastructureEntity24')
    reference_code: str = Field(..., description='Official municipal reference code')
    status: DigitalInfrastructureStatus = Field(default=DigitalInfrastructureStatus.ACTIVE)
    priority: DigitalInfrastructurePriority = Field(default=DigitalInfrastructurePriority.STANDARD)
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

class DigitalInfrastructureEntity25(BaseModel):
    """Operational domain entity 25 for Smart City Cyber-Physical Infrastructure."""
    model_config = ConfigDict(from_attributes=True, extra='ignore')

    entity_id: str = Field(..., description='Unique identifier for DigitalInfrastructureEntity25')
    reference_code: str = Field(..., description='Official municipal reference code')
    status: DigitalInfrastructureStatus = Field(default=DigitalInfrastructureStatus.ACTIVE)
    priority: DigitalInfrastructurePriority = Field(default=DigitalInfrastructurePriority.STANDARD)
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

class DigitalInfrastructureEntity26(BaseModel):
    """Operational domain entity 26 for Smart City Cyber-Physical Infrastructure."""
    model_config = ConfigDict(from_attributes=True, extra='ignore')

    entity_id: str = Field(..., description='Unique identifier for DigitalInfrastructureEntity26')
    reference_code: str = Field(..., description='Official municipal reference code')
    status: DigitalInfrastructureStatus = Field(default=DigitalInfrastructureStatus.ACTIVE)
    priority: DigitalInfrastructurePriority = Field(default=DigitalInfrastructurePriority.STANDARD)
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

class DigitalInfrastructureEntity27(BaseModel):
    """Operational domain entity 27 for Smart City Cyber-Physical Infrastructure."""
    model_config = ConfigDict(from_attributes=True, extra='ignore')

    entity_id: str = Field(..., description='Unique identifier for DigitalInfrastructureEntity27')
    reference_code: str = Field(..., description='Official municipal reference code')
    status: DigitalInfrastructureStatus = Field(default=DigitalInfrastructureStatus.ACTIVE)
    priority: DigitalInfrastructurePriority = Field(default=DigitalInfrastructurePriority.STANDARD)
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

class DigitalInfrastructureEntity28(BaseModel):
    """Operational domain entity 28 for Smart City Cyber-Physical Infrastructure."""
    model_config = ConfigDict(from_attributes=True, extra='ignore')

    entity_id: str = Field(..., description='Unique identifier for DigitalInfrastructureEntity28')
    reference_code: str = Field(..., description='Official municipal reference code')
    status: DigitalInfrastructureStatus = Field(default=DigitalInfrastructureStatus.ACTIVE)
    priority: DigitalInfrastructurePriority = Field(default=DigitalInfrastructurePriority.STANDARD)
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

class DigitalInfrastructureEntity29(BaseModel):
    """Operational domain entity 29 for Smart City Cyber-Physical Infrastructure."""
    model_config = ConfigDict(from_attributes=True, extra='ignore')

    entity_id: str = Field(..., description='Unique identifier for DigitalInfrastructureEntity29')
    reference_code: str = Field(..., description='Official municipal reference code')
    status: DigitalInfrastructureStatus = Field(default=DigitalInfrastructureStatus.ACTIVE)
    priority: DigitalInfrastructurePriority = Field(default=DigitalInfrastructurePriority.STANDARD)
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

class DigitalInfrastructureEntity30(BaseModel):
    """Operational domain entity 30 for Smart City Cyber-Physical Infrastructure."""
    model_config = ConfigDict(from_attributes=True, extra='ignore')

    entity_id: str = Field(..., description='Unique identifier for DigitalInfrastructureEntity30')
    reference_code: str = Field(..., description='Official municipal reference code')
    status: DigitalInfrastructureStatus = Field(default=DigitalInfrastructureStatus.ACTIVE)
    priority: DigitalInfrastructurePriority = Field(default=DigitalInfrastructurePriority.STANDARD)
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

class DigitalInfrastructureEntity31(BaseModel):
    """Operational domain entity 31 for Smart City Cyber-Physical Infrastructure."""
    model_config = ConfigDict(from_attributes=True, extra='ignore')

    entity_id: str = Field(..., description='Unique identifier for DigitalInfrastructureEntity31')
    reference_code: str = Field(..., description='Official municipal reference code')
    status: DigitalInfrastructureStatus = Field(default=DigitalInfrastructureStatus.ACTIVE)
    priority: DigitalInfrastructurePriority = Field(default=DigitalInfrastructurePriority.STANDARD)
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

class DigitalInfrastructureEntity32(BaseModel):
    """Operational domain entity 32 for Smart City Cyber-Physical Infrastructure."""
    model_config = ConfigDict(from_attributes=True, extra='ignore')

    entity_id: str = Field(..., description='Unique identifier for DigitalInfrastructureEntity32')
    reference_code: str = Field(..., description='Official municipal reference code')
    status: DigitalInfrastructureStatus = Field(default=DigitalInfrastructureStatus.ACTIVE)
    priority: DigitalInfrastructurePriority = Field(default=DigitalInfrastructurePriority.STANDARD)
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

class DigitalInfrastructureEntity33(BaseModel):
    """Operational domain entity 33 for Smart City Cyber-Physical Infrastructure."""
    model_config = ConfigDict(from_attributes=True, extra='ignore')

    entity_id: str = Field(..., description='Unique identifier for DigitalInfrastructureEntity33')
    reference_code: str = Field(..., description='Official municipal reference code')
    status: DigitalInfrastructureStatus = Field(default=DigitalInfrastructureStatus.ACTIVE)
    priority: DigitalInfrastructurePriority = Field(default=DigitalInfrastructurePriority.STANDARD)
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

class DigitalInfrastructureEntity34(BaseModel):
    """Operational domain entity 34 for Smart City Cyber-Physical Infrastructure."""
    model_config = ConfigDict(from_attributes=True, extra='ignore')

    entity_id: str = Field(..., description='Unique identifier for DigitalInfrastructureEntity34')
    reference_code: str = Field(..., description='Official municipal reference code')
    status: DigitalInfrastructureStatus = Field(default=DigitalInfrastructureStatus.ACTIVE)
    priority: DigitalInfrastructurePriority = Field(default=DigitalInfrastructurePriority.STANDARD)
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

class DigitalInfrastructureEntity35(BaseModel):
    """Operational domain entity 35 for Smart City Cyber-Physical Infrastructure."""
    model_config = ConfigDict(from_attributes=True, extra='ignore')

    entity_id: str = Field(..., description='Unique identifier for DigitalInfrastructureEntity35')
    reference_code: str = Field(..., description='Official municipal reference code')
    status: DigitalInfrastructureStatus = Field(default=DigitalInfrastructureStatus.ACTIVE)
    priority: DigitalInfrastructurePriority = Field(default=DigitalInfrastructurePriority.STANDARD)
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

class DigitalInfrastructureEntity36(BaseModel):
    """Operational domain entity 36 for Smart City Cyber-Physical Infrastructure."""
    model_config = ConfigDict(from_attributes=True, extra='ignore')

    entity_id: str = Field(..., description='Unique identifier for DigitalInfrastructureEntity36')
    reference_code: str = Field(..., description='Official municipal reference code')
    status: DigitalInfrastructureStatus = Field(default=DigitalInfrastructureStatus.ACTIVE)
    priority: DigitalInfrastructurePriority = Field(default=DigitalInfrastructurePriority.STANDARD)
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

class DigitalInfrastructureEntity37(BaseModel):
    """Operational domain entity 37 for Smart City Cyber-Physical Infrastructure."""
    model_config = ConfigDict(from_attributes=True, extra='ignore')

    entity_id: str = Field(..., description='Unique identifier for DigitalInfrastructureEntity37')
    reference_code: str = Field(..., description='Official municipal reference code')
    status: DigitalInfrastructureStatus = Field(default=DigitalInfrastructureStatus.ACTIVE)
    priority: DigitalInfrastructurePriority = Field(default=DigitalInfrastructurePriority.STANDARD)
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

class DigitalInfrastructureEntity38(BaseModel):
    """Operational domain entity 38 for Smart City Cyber-Physical Infrastructure."""
    model_config = ConfigDict(from_attributes=True, extra='ignore')

    entity_id: str = Field(..., description='Unique identifier for DigitalInfrastructureEntity38')
    reference_code: str = Field(..., description='Official municipal reference code')
    status: DigitalInfrastructureStatus = Field(default=DigitalInfrastructureStatus.ACTIVE)
    priority: DigitalInfrastructurePriority = Field(default=DigitalInfrastructurePriority.STANDARD)
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

class DigitalInfrastructureEntity39(BaseModel):
    """Operational domain entity 39 for Smart City Cyber-Physical Infrastructure."""
    model_config = ConfigDict(from_attributes=True, extra='ignore')

    entity_id: str = Field(..., description='Unique identifier for DigitalInfrastructureEntity39')
    reference_code: str = Field(..., description='Official municipal reference code')
    status: DigitalInfrastructureStatus = Field(default=DigitalInfrastructureStatus.ACTIVE)
    priority: DigitalInfrastructurePriority = Field(default=DigitalInfrastructurePriority.STANDARD)
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

class DigitalInfrastructureEntity40(BaseModel):
    """Operational domain entity 40 for Smart City Cyber-Physical Infrastructure."""
    model_config = ConfigDict(from_attributes=True, extra='ignore')

    entity_id: str = Field(..., description='Unique identifier for DigitalInfrastructureEntity40')
    reference_code: str = Field(..., description='Official municipal reference code')
    status: DigitalInfrastructureStatus = Field(default=DigitalInfrastructureStatus.ACTIVE)
    priority: DigitalInfrastructurePriority = Field(default=DigitalInfrastructurePriority.STANDARD)
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

class DigitalInfrastructureEntity41(BaseModel):
    """Operational domain entity 41 for Smart City Cyber-Physical Infrastructure."""
    model_config = ConfigDict(from_attributes=True, extra='ignore')

    entity_id: str = Field(..., description='Unique identifier for DigitalInfrastructureEntity41')
    reference_code: str = Field(..., description='Official municipal reference code')
    status: DigitalInfrastructureStatus = Field(default=DigitalInfrastructureStatus.ACTIVE)
    priority: DigitalInfrastructurePriority = Field(default=DigitalInfrastructurePriority.STANDARD)
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

class DigitalInfrastructureEntity42(BaseModel):
    """Operational domain entity 42 for Smart City Cyber-Physical Infrastructure."""
    model_config = ConfigDict(from_attributes=True, extra='ignore')

    entity_id: str = Field(..., description='Unique identifier for DigitalInfrastructureEntity42')
    reference_code: str = Field(..., description='Official municipal reference code')
    status: DigitalInfrastructureStatus = Field(default=DigitalInfrastructureStatus.ACTIVE)
    priority: DigitalInfrastructurePriority = Field(default=DigitalInfrastructurePriority.STANDARD)
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

class DigitalInfrastructureEntity43(BaseModel):
    """Operational domain entity 43 for Smart City Cyber-Physical Infrastructure."""
    model_config = ConfigDict(from_attributes=True, extra='ignore')

    entity_id: str = Field(..., description='Unique identifier for DigitalInfrastructureEntity43')
    reference_code: str = Field(..., description='Official municipal reference code')
    status: DigitalInfrastructureStatus = Field(default=DigitalInfrastructureStatus.ACTIVE)
    priority: DigitalInfrastructurePriority = Field(default=DigitalInfrastructurePriority.STANDARD)
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

class DigitalInfrastructureEntity44(BaseModel):
    """Operational domain entity 44 for Smart City Cyber-Physical Infrastructure."""
    model_config = ConfigDict(from_attributes=True, extra='ignore')

    entity_id: str = Field(..., description='Unique identifier for DigitalInfrastructureEntity44')
    reference_code: str = Field(..., description='Official municipal reference code')
    status: DigitalInfrastructureStatus = Field(default=DigitalInfrastructureStatus.ACTIVE)
    priority: DigitalInfrastructurePriority = Field(default=DigitalInfrastructurePriority.STANDARD)
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

class DigitalInfrastructureEntity45(BaseModel):
    """Operational domain entity 45 for Smart City Cyber-Physical Infrastructure."""
    model_config = ConfigDict(from_attributes=True, extra='ignore')

    entity_id: str = Field(..., description='Unique identifier for DigitalInfrastructureEntity45')
    reference_code: str = Field(..., description='Official municipal reference code')
    status: DigitalInfrastructureStatus = Field(default=DigitalInfrastructureStatus.ACTIVE)
    priority: DigitalInfrastructurePriority = Field(default=DigitalInfrastructurePriority.STANDARD)
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

class DigitalInfrastructureEntity46(BaseModel):
    """Operational domain entity 46 for Smart City Cyber-Physical Infrastructure."""
    model_config = ConfigDict(from_attributes=True, extra='ignore')

    entity_id: str = Field(..., description='Unique identifier for DigitalInfrastructureEntity46')
    reference_code: str = Field(..., description='Official municipal reference code')
    status: DigitalInfrastructureStatus = Field(default=DigitalInfrastructureStatus.ACTIVE)
    priority: DigitalInfrastructurePriority = Field(default=DigitalInfrastructurePriority.STANDARD)
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

class DigitalInfrastructureEntity47(BaseModel):
    """Operational domain entity 47 for Smart City Cyber-Physical Infrastructure."""
    model_config = ConfigDict(from_attributes=True, extra='ignore')

    entity_id: str = Field(..., description='Unique identifier for DigitalInfrastructureEntity47')
    reference_code: str = Field(..., description='Official municipal reference code')
    status: DigitalInfrastructureStatus = Field(default=DigitalInfrastructureStatus.ACTIVE)
    priority: DigitalInfrastructurePriority = Field(default=DigitalInfrastructurePriority.STANDARD)
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

class DigitalInfrastructureEntity48(BaseModel):
    """Operational domain entity 48 for Smart City Cyber-Physical Infrastructure."""
    model_config = ConfigDict(from_attributes=True, extra='ignore')

    entity_id: str = Field(..., description='Unique identifier for DigitalInfrastructureEntity48')
    reference_code: str = Field(..., description='Official municipal reference code')
    status: DigitalInfrastructureStatus = Field(default=DigitalInfrastructureStatus.ACTIVE)
    priority: DigitalInfrastructurePriority = Field(default=DigitalInfrastructurePriority.STANDARD)
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

class DigitalInfrastructureEntity49(BaseModel):
    """Operational domain entity 49 for Smart City Cyber-Physical Infrastructure."""
    model_config = ConfigDict(from_attributes=True, extra='ignore')

    entity_id: str = Field(..., description='Unique identifier for DigitalInfrastructureEntity49')
    reference_code: str = Field(..., description='Official municipal reference code')
    status: DigitalInfrastructureStatus = Field(default=DigitalInfrastructureStatus.ACTIVE)
    priority: DigitalInfrastructurePriority = Field(default=DigitalInfrastructurePriority.STANDARD)
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

class DigitalInfrastructureEntity50(BaseModel):
    """Operational domain entity 50 for Smart City Cyber-Physical Infrastructure."""
    model_config = ConfigDict(from_attributes=True, extra='ignore')

    entity_id: str = Field(..., description='Unique identifier for DigitalInfrastructureEntity50')
    reference_code: str = Field(..., description='Official municipal reference code')
    status: DigitalInfrastructureStatus = Field(default=DigitalInfrastructureStatus.ACTIVE)
    priority: DigitalInfrastructurePriority = Field(default=DigitalInfrastructurePriority.STANDARD)
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

class DigitalInfrastructureEntity51(BaseModel):
    """Operational domain entity 51 for Smart City Cyber-Physical Infrastructure."""
    model_config = ConfigDict(from_attributes=True, extra='ignore')

    entity_id: str = Field(..., description='Unique identifier for DigitalInfrastructureEntity51')
    reference_code: str = Field(..., description='Official municipal reference code')
    status: DigitalInfrastructureStatus = Field(default=DigitalInfrastructureStatus.ACTIVE)
    priority: DigitalInfrastructurePriority = Field(default=DigitalInfrastructurePriority.STANDARD)
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

class DigitalInfrastructureEntity52(BaseModel):
    """Operational domain entity 52 for Smart City Cyber-Physical Infrastructure."""
    model_config = ConfigDict(from_attributes=True, extra='ignore')

    entity_id: str = Field(..., description='Unique identifier for DigitalInfrastructureEntity52')
    reference_code: str = Field(..., description='Official municipal reference code')
    status: DigitalInfrastructureStatus = Field(default=DigitalInfrastructureStatus.ACTIVE)
    priority: DigitalInfrastructurePriority = Field(default=DigitalInfrastructurePriority.STANDARD)
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

class DigitalInfrastructureEntity53(BaseModel):
    """Operational domain entity 53 for Smart City Cyber-Physical Infrastructure."""
    model_config = ConfigDict(from_attributes=True, extra='ignore')

    entity_id: str = Field(..., description='Unique identifier for DigitalInfrastructureEntity53')
    reference_code: str = Field(..., description='Official municipal reference code')
    status: DigitalInfrastructureStatus = Field(default=DigitalInfrastructureStatus.ACTIVE)
    priority: DigitalInfrastructurePriority = Field(default=DigitalInfrastructurePriority.STANDARD)
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

class DigitalInfrastructureEntity54(BaseModel):
    """Operational domain entity 54 for Smart City Cyber-Physical Infrastructure."""
    model_config = ConfigDict(from_attributes=True, extra='ignore')

    entity_id: str = Field(..., description='Unique identifier for DigitalInfrastructureEntity54')
    reference_code: str = Field(..., description='Official municipal reference code')
    status: DigitalInfrastructureStatus = Field(default=DigitalInfrastructureStatus.ACTIVE)
    priority: DigitalInfrastructurePriority = Field(default=DigitalInfrastructurePriority.STANDARD)
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

class DigitalInfrastructureEntity55(BaseModel):
    """Operational domain entity 55 for Smart City Cyber-Physical Infrastructure."""
    model_config = ConfigDict(from_attributes=True, extra='ignore')

    entity_id: str = Field(..., description='Unique identifier for DigitalInfrastructureEntity55')
    reference_code: str = Field(..., description='Official municipal reference code')
    status: DigitalInfrastructureStatus = Field(default=DigitalInfrastructureStatus.ACTIVE)
    priority: DigitalInfrastructurePriority = Field(default=DigitalInfrastructurePriority.STANDARD)
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

class DigitalInfrastructureEntity56(BaseModel):
    """Operational domain entity 56 for Smart City Cyber-Physical Infrastructure."""
    model_config = ConfigDict(from_attributes=True, extra='ignore')

    entity_id: str = Field(..., description='Unique identifier for DigitalInfrastructureEntity56')
    reference_code: str = Field(..., description='Official municipal reference code')
    status: DigitalInfrastructureStatus = Field(default=DigitalInfrastructureStatus.ACTIVE)
    priority: DigitalInfrastructurePriority = Field(default=DigitalInfrastructurePriority.STANDARD)
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

class DigitalInfrastructureEntity57(BaseModel):
    """Operational domain entity 57 for Smart City Cyber-Physical Infrastructure."""
    model_config = ConfigDict(from_attributes=True, extra='ignore')

    entity_id: str = Field(..., description='Unique identifier for DigitalInfrastructureEntity57')
    reference_code: str = Field(..., description='Official municipal reference code')
    status: DigitalInfrastructureStatus = Field(default=DigitalInfrastructureStatus.ACTIVE)
    priority: DigitalInfrastructurePriority = Field(default=DigitalInfrastructurePriority.STANDARD)
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

class DigitalInfrastructureEntity58(BaseModel):
    """Operational domain entity 58 for Smart City Cyber-Physical Infrastructure."""
    model_config = ConfigDict(from_attributes=True, extra='ignore')

    entity_id: str = Field(..., description='Unique identifier for DigitalInfrastructureEntity58')
    reference_code: str = Field(..., description='Official municipal reference code')
    status: DigitalInfrastructureStatus = Field(default=DigitalInfrastructureStatus.ACTIVE)
    priority: DigitalInfrastructurePriority = Field(default=DigitalInfrastructurePriority.STANDARD)
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

class DigitalInfrastructureEntity59(BaseModel):
    """Operational domain entity 59 for Smart City Cyber-Physical Infrastructure."""
    model_config = ConfigDict(from_attributes=True, extra='ignore')

    entity_id: str = Field(..., description='Unique identifier for DigitalInfrastructureEntity59')
    reference_code: str = Field(..., description='Official municipal reference code')
    status: DigitalInfrastructureStatus = Field(default=DigitalInfrastructureStatus.ACTIVE)
    priority: DigitalInfrastructurePriority = Field(default=DigitalInfrastructurePriority.STANDARD)
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

class DigitalInfrastructureEntity60(BaseModel):
    """Operational domain entity 60 for Smart City Cyber-Physical Infrastructure."""
    model_config = ConfigDict(from_attributes=True, extra='ignore')

    entity_id: str = Field(..., description='Unique identifier for DigitalInfrastructureEntity60')
    reference_code: str = Field(..., description='Official municipal reference code')
    status: DigitalInfrastructureStatus = Field(default=DigitalInfrastructureStatus.ACTIVE)
    priority: DigitalInfrastructurePriority = Field(default=DigitalInfrastructurePriority.STANDARD)
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

class DigitalInfrastructureEntity61(BaseModel):
    """Operational domain entity 61 for Smart City Cyber-Physical Infrastructure."""
    model_config = ConfigDict(from_attributes=True, extra='ignore')

    entity_id: str = Field(..., description='Unique identifier for DigitalInfrastructureEntity61')
    reference_code: str = Field(..., description='Official municipal reference code')
    status: DigitalInfrastructureStatus = Field(default=DigitalInfrastructureStatus.ACTIVE)
    priority: DigitalInfrastructurePriority = Field(default=DigitalInfrastructurePriority.STANDARD)
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

class DigitalInfrastructureEntity62(BaseModel):
    """Operational domain entity 62 for Smart City Cyber-Physical Infrastructure."""
    model_config = ConfigDict(from_attributes=True, extra='ignore')

    entity_id: str = Field(..., description='Unique identifier for DigitalInfrastructureEntity62')
    reference_code: str = Field(..., description='Official municipal reference code')
    status: DigitalInfrastructureStatus = Field(default=DigitalInfrastructureStatus.ACTIVE)
    priority: DigitalInfrastructurePriority = Field(default=DigitalInfrastructurePriority.STANDARD)
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

class DigitalInfrastructureEntity63(BaseModel):
    """Operational domain entity 63 for Smart City Cyber-Physical Infrastructure."""
    model_config = ConfigDict(from_attributes=True, extra='ignore')

    entity_id: str = Field(..., description='Unique identifier for DigitalInfrastructureEntity63')
    reference_code: str = Field(..., description='Official municipal reference code')
    status: DigitalInfrastructureStatus = Field(default=DigitalInfrastructureStatus.ACTIVE)
    priority: DigitalInfrastructurePriority = Field(default=DigitalInfrastructurePriority.STANDARD)
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

class DigitalInfrastructureEntity64(BaseModel):
    """Operational domain entity 64 for Smart City Cyber-Physical Infrastructure."""
    model_config = ConfigDict(from_attributes=True, extra='ignore')

    entity_id: str = Field(..., description='Unique identifier for DigitalInfrastructureEntity64')
    reference_code: str = Field(..., description='Official municipal reference code')
    status: DigitalInfrastructureStatus = Field(default=DigitalInfrastructureStatus.ACTIVE)
    priority: DigitalInfrastructurePriority = Field(default=DigitalInfrastructurePriority.STANDARD)
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

class DigitalInfrastructureEntity65(BaseModel):
    """Operational domain entity 65 for Smart City Cyber-Physical Infrastructure."""
    model_config = ConfigDict(from_attributes=True, extra='ignore')

    entity_id: str = Field(..., description='Unique identifier for DigitalInfrastructureEntity65')
    reference_code: str = Field(..., description='Official municipal reference code')
    status: DigitalInfrastructureStatus = Field(default=DigitalInfrastructureStatus.ACTIVE)
    priority: DigitalInfrastructurePriority = Field(default=DigitalInfrastructurePriority.STANDARD)
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

class DigitalInfrastructureEntity66(BaseModel):
    """Operational domain entity 66 for Smart City Cyber-Physical Infrastructure."""
    model_config = ConfigDict(from_attributes=True, extra='ignore')

    entity_id: str = Field(..., description='Unique identifier for DigitalInfrastructureEntity66')
    reference_code: str = Field(..., description='Official municipal reference code')
    status: DigitalInfrastructureStatus = Field(default=DigitalInfrastructureStatus.ACTIVE)
    priority: DigitalInfrastructurePriority = Field(default=DigitalInfrastructurePriority.STANDARD)
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

class DigitalInfrastructureEntity67(BaseModel):
    """Operational domain entity 67 for Smart City Cyber-Physical Infrastructure."""
    model_config = ConfigDict(from_attributes=True, extra='ignore')

    entity_id: str = Field(..., description='Unique identifier for DigitalInfrastructureEntity67')
    reference_code: str = Field(..., description='Official municipal reference code')
    status: DigitalInfrastructureStatus = Field(default=DigitalInfrastructureStatus.ACTIVE)
    priority: DigitalInfrastructurePriority = Field(default=DigitalInfrastructurePriority.STANDARD)
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

class DigitalInfrastructureEntity68(BaseModel):
    """Operational domain entity 68 for Smart City Cyber-Physical Infrastructure."""
    model_config = ConfigDict(from_attributes=True, extra='ignore')

    entity_id: str = Field(..., description='Unique identifier for DigitalInfrastructureEntity68')
    reference_code: str = Field(..., description='Official municipal reference code')
    status: DigitalInfrastructureStatus = Field(default=DigitalInfrastructureStatus.ACTIVE)
    priority: DigitalInfrastructurePriority = Field(default=DigitalInfrastructurePriority.STANDARD)
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

class DigitalInfrastructureEntity69(BaseModel):
    """Operational domain entity 69 for Smart City Cyber-Physical Infrastructure."""
    model_config = ConfigDict(from_attributes=True, extra='ignore')

    entity_id: str = Field(..., description='Unique identifier for DigitalInfrastructureEntity69')
    reference_code: str = Field(..., description='Official municipal reference code')
    status: DigitalInfrastructureStatus = Field(default=DigitalInfrastructureStatus.ACTIVE)
    priority: DigitalInfrastructurePriority = Field(default=DigitalInfrastructurePriority.STANDARD)
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

class DigitalInfrastructureEntity70(BaseModel):
    """Operational domain entity 70 for Smart City Cyber-Physical Infrastructure."""
    model_config = ConfigDict(from_attributes=True, extra='ignore')

    entity_id: str = Field(..., description='Unique identifier for DigitalInfrastructureEntity70')
    reference_code: str = Field(..., description='Official municipal reference code')
    status: DigitalInfrastructureStatus = Field(default=DigitalInfrastructureStatus.ACTIVE)
    priority: DigitalInfrastructurePriority = Field(default=DigitalInfrastructurePriority.STANDARD)
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

class DigitalInfrastructureEntity71(BaseModel):
    """Operational domain entity 71 for Smart City Cyber-Physical Infrastructure."""
    model_config = ConfigDict(from_attributes=True, extra='ignore')

    entity_id: str = Field(..., description='Unique identifier for DigitalInfrastructureEntity71')
    reference_code: str = Field(..., description='Official municipal reference code')
    status: DigitalInfrastructureStatus = Field(default=DigitalInfrastructureStatus.ACTIVE)
    priority: DigitalInfrastructurePriority = Field(default=DigitalInfrastructurePriority.STANDARD)
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

class DigitalInfrastructureEntity72(BaseModel):
    """Operational domain entity 72 for Smart City Cyber-Physical Infrastructure."""
    model_config = ConfigDict(from_attributes=True, extra='ignore')

    entity_id: str = Field(..., description='Unique identifier for DigitalInfrastructureEntity72')
    reference_code: str = Field(..., description='Official municipal reference code')
    status: DigitalInfrastructureStatus = Field(default=DigitalInfrastructureStatus.ACTIVE)
    priority: DigitalInfrastructurePriority = Field(default=DigitalInfrastructurePriority.STANDARD)
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

class DigitalInfrastructureEntity73(BaseModel):
    """Operational domain entity 73 for Smart City Cyber-Physical Infrastructure."""
    model_config = ConfigDict(from_attributes=True, extra='ignore')

    entity_id: str = Field(..., description='Unique identifier for DigitalInfrastructureEntity73')
    reference_code: str = Field(..., description='Official municipal reference code')
    status: DigitalInfrastructureStatus = Field(default=DigitalInfrastructureStatus.ACTIVE)
    priority: DigitalInfrastructurePriority = Field(default=DigitalInfrastructurePriority.STANDARD)
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

class DigitalInfrastructureEntity74(BaseModel):
    """Operational domain entity 74 for Smart City Cyber-Physical Infrastructure."""
    model_config = ConfigDict(from_attributes=True, extra='ignore')

    entity_id: str = Field(..., description='Unique identifier for DigitalInfrastructureEntity74')
    reference_code: str = Field(..., description='Official municipal reference code')
    status: DigitalInfrastructureStatus = Field(default=DigitalInfrastructureStatus.ACTIVE)
    priority: DigitalInfrastructurePriority = Field(default=DigitalInfrastructurePriority.STANDARD)
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

class DigitalInfrastructureEntity75(BaseModel):
    """Operational domain entity 75 for Smart City Cyber-Physical Infrastructure."""
    model_config = ConfigDict(from_attributes=True, extra='ignore')

    entity_id: str = Field(..., description='Unique identifier for DigitalInfrastructureEntity75')
    reference_code: str = Field(..., description='Official municipal reference code')
    status: DigitalInfrastructureStatus = Field(default=DigitalInfrastructureStatus.ACTIVE)
    priority: DigitalInfrastructurePriority = Field(default=DigitalInfrastructurePriority.STANDARD)
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

class DigitalInfrastructureEntity76(BaseModel):
    """Operational domain entity 76 for Smart City Cyber-Physical Infrastructure."""
    model_config = ConfigDict(from_attributes=True, extra='ignore')

    entity_id: str = Field(..., description='Unique identifier for DigitalInfrastructureEntity76')
    reference_code: str = Field(..., description='Official municipal reference code')
    status: DigitalInfrastructureStatus = Field(default=DigitalInfrastructureStatus.ACTIVE)
    priority: DigitalInfrastructurePriority = Field(default=DigitalInfrastructurePriority.STANDARD)
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

class DigitalInfrastructureEntity77(BaseModel):
    """Operational domain entity 77 for Smart City Cyber-Physical Infrastructure."""
    model_config = ConfigDict(from_attributes=True, extra='ignore')

    entity_id: str = Field(..., description='Unique identifier for DigitalInfrastructureEntity77')
    reference_code: str = Field(..., description='Official municipal reference code')
    status: DigitalInfrastructureStatus = Field(default=DigitalInfrastructureStatus.ACTIVE)
    priority: DigitalInfrastructurePriority = Field(default=DigitalInfrastructurePriority.STANDARD)
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

class DigitalInfrastructureEntity78(BaseModel):
    """Operational domain entity 78 for Smart City Cyber-Physical Infrastructure."""
    model_config = ConfigDict(from_attributes=True, extra='ignore')

    entity_id: str = Field(..., description='Unique identifier for DigitalInfrastructureEntity78')
    reference_code: str = Field(..., description='Official municipal reference code')
    status: DigitalInfrastructureStatus = Field(default=DigitalInfrastructureStatus.ACTIVE)
    priority: DigitalInfrastructurePriority = Field(default=DigitalInfrastructurePriority.STANDARD)
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

class DigitalInfrastructureEntity79(BaseModel):
    """Operational domain entity 79 for Smart City Cyber-Physical Infrastructure."""
    model_config = ConfigDict(from_attributes=True, extra='ignore')

    entity_id: str = Field(..., description='Unique identifier for DigitalInfrastructureEntity79')
    reference_code: str = Field(..., description='Official municipal reference code')
    status: DigitalInfrastructureStatus = Field(default=DigitalInfrastructureStatus.ACTIVE)
    priority: DigitalInfrastructurePriority = Field(default=DigitalInfrastructurePriority.STANDARD)
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

class DigitalInfrastructureEntity80(BaseModel):
    """Operational domain entity 80 for Smart City Cyber-Physical Infrastructure."""
    model_config = ConfigDict(from_attributes=True, extra='ignore')

    entity_id: str = Field(..., description='Unique identifier for DigitalInfrastructureEntity80')
    reference_code: str = Field(..., description='Official municipal reference code')
    status: DigitalInfrastructureStatus = Field(default=DigitalInfrastructureStatus.ACTIVE)
    priority: DigitalInfrastructurePriority = Field(default=DigitalInfrastructurePriority.STANDARD)
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

class DigitalInfrastructureEntity81(BaseModel):
    """Operational domain entity 81 for Smart City Cyber-Physical Infrastructure."""
    model_config = ConfigDict(from_attributes=True, extra='ignore')

    entity_id: str = Field(..., description='Unique identifier for DigitalInfrastructureEntity81')
    reference_code: str = Field(..., description='Official municipal reference code')
    status: DigitalInfrastructureStatus = Field(default=DigitalInfrastructureStatus.ACTIVE)
    priority: DigitalInfrastructurePriority = Field(default=DigitalInfrastructurePriority.STANDARD)
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

class DigitalInfrastructureEntity82(BaseModel):
    """Operational domain entity 82 for Smart City Cyber-Physical Infrastructure."""
    model_config = ConfigDict(from_attributes=True, extra='ignore')

    entity_id: str = Field(..., description='Unique identifier for DigitalInfrastructureEntity82')
    reference_code: str = Field(..., description='Official municipal reference code')
    status: DigitalInfrastructureStatus = Field(default=DigitalInfrastructureStatus.ACTIVE)
    priority: DigitalInfrastructurePriority = Field(default=DigitalInfrastructurePriority.STANDARD)
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

class DigitalInfrastructureEntity83(BaseModel):
    """Operational domain entity 83 for Smart City Cyber-Physical Infrastructure."""
    model_config = ConfigDict(from_attributes=True, extra='ignore')

    entity_id: str = Field(..., description='Unique identifier for DigitalInfrastructureEntity83')
    reference_code: str = Field(..., description='Official municipal reference code')
    status: DigitalInfrastructureStatus = Field(default=DigitalInfrastructureStatus.ACTIVE)
    priority: DigitalInfrastructurePriority = Field(default=DigitalInfrastructurePriority.STANDARD)
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

class DigitalInfrastructureEntity84(BaseModel):
    """Operational domain entity 84 for Smart City Cyber-Physical Infrastructure."""
    model_config = ConfigDict(from_attributes=True, extra='ignore')

    entity_id: str = Field(..., description='Unique identifier for DigitalInfrastructureEntity84')
    reference_code: str = Field(..., description='Official municipal reference code')
    status: DigitalInfrastructureStatus = Field(default=DigitalInfrastructureStatus.ACTIVE)
    priority: DigitalInfrastructurePriority = Field(default=DigitalInfrastructurePriority.STANDARD)
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

class DigitalInfrastructureEntity85(BaseModel):
    """Operational domain entity 85 for Smart City Cyber-Physical Infrastructure."""
    model_config = ConfigDict(from_attributes=True, extra='ignore')

    entity_id: str = Field(..., description='Unique identifier for DigitalInfrastructureEntity85')
    reference_code: str = Field(..., description='Official municipal reference code')
    status: DigitalInfrastructureStatus = Field(default=DigitalInfrastructureStatus.ACTIVE)
    priority: DigitalInfrastructurePriority = Field(default=DigitalInfrastructurePriority.STANDARD)
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

class DigitalInfrastructureEntity86(BaseModel):
    """Operational domain entity 86 for Smart City Cyber-Physical Infrastructure."""
    model_config = ConfigDict(from_attributes=True, extra='ignore')

    entity_id: str = Field(..., description='Unique identifier for DigitalInfrastructureEntity86')
    reference_code: str = Field(..., description='Official municipal reference code')
    status: DigitalInfrastructureStatus = Field(default=DigitalInfrastructureStatus.ACTIVE)
    priority: DigitalInfrastructurePriority = Field(default=DigitalInfrastructurePriority.STANDARD)
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

class DigitalInfrastructureEntity87(BaseModel):
    """Operational domain entity 87 for Smart City Cyber-Physical Infrastructure."""
    model_config = ConfigDict(from_attributes=True, extra='ignore')

    entity_id: str = Field(..., description='Unique identifier for DigitalInfrastructureEntity87')
    reference_code: str = Field(..., description='Official municipal reference code')
    status: DigitalInfrastructureStatus = Field(default=DigitalInfrastructureStatus.ACTIVE)
    priority: DigitalInfrastructurePriority = Field(default=DigitalInfrastructurePriority.STANDARD)
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

class DigitalInfrastructureEntity88(BaseModel):
    """Operational domain entity 88 for Smart City Cyber-Physical Infrastructure."""
    model_config = ConfigDict(from_attributes=True, extra='ignore')

    entity_id: str = Field(..., description='Unique identifier for DigitalInfrastructureEntity88')
    reference_code: str = Field(..., description='Official municipal reference code')
    status: DigitalInfrastructureStatus = Field(default=DigitalInfrastructureStatus.ACTIVE)
    priority: DigitalInfrastructurePriority = Field(default=DigitalInfrastructurePriority.STANDARD)
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

class DigitalInfrastructureEntity89(BaseModel):
    """Operational domain entity 89 for Smart City Cyber-Physical Infrastructure."""
    model_config = ConfigDict(from_attributes=True, extra='ignore')

    entity_id: str = Field(..., description='Unique identifier for DigitalInfrastructureEntity89')
    reference_code: str = Field(..., description='Official municipal reference code')
    status: DigitalInfrastructureStatus = Field(default=DigitalInfrastructureStatus.ACTIVE)
    priority: DigitalInfrastructurePriority = Field(default=DigitalInfrastructurePriority.STANDARD)
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

class DigitalInfrastructureEntity90(BaseModel):
    """Operational domain entity 90 for Smart City Cyber-Physical Infrastructure."""
    model_config = ConfigDict(from_attributes=True, extra='ignore')

    entity_id: str = Field(..., description='Unique identifier for DigitalInfrastructureEntity90')
    reference_code: str = Field(..., description='Official municipal reference code')
    status: DigitalInfrastructureStatus = Field(default=DigitalInfrastructureStatus.ACTIVE)
    priority: DigitalInfrastructurePriority = Field(default=DigitalInfrastructurePriority.STANDARD)
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

class DigitalInfrastructureEntity91(BaseModel):
    """Operational domain entity 91 for Smart City Cyber-Physical Infrastructure."""
    model_config = ConfigDict(from_attributes=True, extra='ignore')

    entity_id: str = Field(..., description='Unique identifier for DigitalInfrastructureEntity91')
    reference_code: str = Field(..., description='Official municipal reference code')
    status: DigitalInfrastructureStatus = Field(default=DigitalInfrastructureStatus.ACTIVE)
    priority: DigitalInfrastructurePriority = Field(default=DigitalInfrastructurePriority.STANDARD)
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

class DigitalInfrastructureEntity92(BaseModel):
    """Operational domain entity 92 for Smart City Cyber-Physical Infrastructure."""
    model_config = ConfigDict(from_attributes=True, extra='ignore')

    entity_id: str = Field(..., description='Unique identifier for DigitalInfrastructureEntity92')
    reference_code: str = Field(..., description='Official municipal reference code')
    status: DigitalInfrastructureStatus = Field(default=DigitalInfrastructureStatus.ACTIVE)
    priority: DigitalInfrastructurePriority = Field(default=DigitalInfrastructurePriority.STANDARD)
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

class DigitalInfrastructureEntity93(BaseModel):
    """Operational domain entity 93 for Smart City Cyber-Physical Infrastructure."""
    model_config = ConfigDict(from_attributes=True, extra='ignore')

    entity_id: str = Field(..., description='Unique identifier for DigitalInfrastructureEntity93')
    reference_code: str = Field(..., description='Official municipal reference code')
    status: DigitalInfrastructureStatus = Field(default=DigitalInfrastructureStatus.ACTIVE)
    priority: DigitalInfrastructurePriority = Field(default=DigitalInfrastructurePriority.STANDARD)
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

class DigitalInfrastructureEntity94(BaseModel):
    """Operational domain entity 94 for Smart City Cyber-Physical Infrastructure."""
    model_config = ConfigDict(from_attributes=True, extra='ignore')

    entity_id: str = Field(..., description='Unique identifier for DigitalInfrastructureEntity94')
    reference_code: str = Field(..., description='Official municipal reference code')
    status: DigitalInfrastructureStatus = Field(default=DigitalInfrastructureStatus.ACTIVE)
    priority: DigitalInfrastructurePriority = Field(default=DigitalInfrastructurePriority.STANDARD)
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

class DigitalInfrastructureEntity95(BaseModel):
    """Operational domain entity 95 for Smart City Cyber-Physical Infrastructure."""
    model_config = ConfigDict(from_attributes=True, extra='ignore')

    entity_id: str = Field(..., description='Unique identifier for DigitalInfrastructureEntity95')
    reference_code: str = Field(..., description='Official municipal reference code')
    status: DigitalInfrastructureStatus = Field(default=DigitalInfrastructureStatus.ACTIVE)
    priority: DigitalInfrastructurePriority = Field(default=DigitalInfrastructurePriority.STANDARD)
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

class DigitalInfrastructureEntity96(BaseModel):
    """Operational domain entity 96 for Smart City Cyber-Physical Infrastructure."""
    model_config = ConfigDict(from_attributes=True, extra='ignore')

    entity_id: str = Field(..., description='Unique identifier for DigitalInfrastructureEntity96')
    reference_code: str = Field(..., description='Official municipal reference code')
    status: DigitalInfrastructureStatus = Field(default=DigitalInfrastructureStatus.ACTIVE)
    priority: DigitalInfrastructurePriority = Field(default=DigitalInfrastructurePriority.STANDARD)
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

class DigitalInfrastructureEntity97(BaseModel):
    """Operational domain entity 97 for Smart City Cyber-Physical Infrastructure."""
    model_config = ConfigDict(from_attributes=True, extra='ignore')

    entity_id: str = Field(..., description='Unique identifier for DigitalInfrastructureEntity97')
    reference_code: str = Field(..., description='Official municipal reference code')
    status: DigitalInfrastructureStatus = Field(default=DigitalInfrastructureStatus.ACTIVE)
    priority: DigitalInfrastructurePriority = Field(default=DigitalInfrastructurePriority.STANDARD)
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

class DigitalInfrastructureEntity98(BaseModel):
    """Operational domain entity 98 for Smart City Cyber-Physical Infrastructure."""
    model_config = ConfigDict(from_attributes=True, extra='ignore')

    entity_id: str = Field(..., description='Unique identifier for DigitalInfrastructureEntity98')
    reference_code: str = Field(..., description='Official municipal reference code')
    status: DigitalInfrastructureStatus = Field(default=DigitalInfrastructureStatus.ACTIVE)
    priority: DigitalInfrastructurePriority = Field(default=DigitalInfrastructurePriority.STANDARD)
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

class DigitalInfrastructureEntity99(BaseModel):
    """Operational domain entity 99 for Smart City Cyber-Physical Infrastructure."""
    model_config = ConfigDict(from_attributes=True, extra='ignore')

    entity_id: str = Field(..., description='Unique identifier for DigitalInfrastructureEntity99')
    reference_code: str = Field(..., description='Official municipal reference code')
    status: DigitalInfrastructureStatus = Field(default=DigitalInfrastructureStatus.ACTIVE)
    priority: DigitalInfrastructurePriority = Field(default=DigitalInfrastructurePriority.STANDARD)
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

class DigitalInfrastructureEntity100(BaseModel):
    """Operational domain entity 100 for Smart City Cyber-Physical Infrastructure."""
    model_config = ConfigDict(from_attributes=True, extra='ignore')

    entity_id: str = Field(..., description='Unique identifier for DigitalInfrastructureEntity100')
    reference_code: str = Field(..., description='Official municipal reference code')
    status: DigitalInfrastructureStatus = Field(default=DigitalInfrastructureStatus.ACTIVE)
    priority: DigitalInfrastructurePriority = Field(default=DigitalInfrastructurePriority.STANDARD)
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

class DigitalInfrastructureEntity101(BaseModel):
    """Operational domain entity 101 for Smart City Cyber-Physical Infrastructure."""
    model_config = ConfigDict(from_attributes=True, extra='ignore')

    entity_id: str = Field(..., description='Unique identifier for DigitalInfrastructureEntity101')
    reference_code: str = Field(..., description='Official municipal reference code')
    status: DigitalInfrastructureStatus = Field(default=DigitalInfrastructureStatus.ACTIVE)
    priority: DigitalInfrastructurePriority = Field(default=DigitalInfrastructurePriority.STANDARD)
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

class DigitalInfrastructureEntity102(BaseModel):
    """Operational domain entity 102 for Smart City Cyber-Physical Infrastructure."""
    model_config = ConfigDict(from_attributes=True, extra='ignore')

    entity_id: str = Field(..., description='Unique identifier for DigitalInfrastructureEntity102')
    reference_code: str = Field(..., description='Official municipal reference code')
    status: DigitalInfrastructureStatus = Field(default=DigitalInfrastructureStatus.ACTIVE)
    priority: DigitalInfrastructurePriority = Field(default=DigitalInfrastructurePriority.STANDARD)
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

class DigitalInfrastructureEntity103(BaseModel):
    """Operational domain entity 103 for Smart City Cyber-Physical Infrastructure."""
    model_config = ConfigDict(from_attributes=True, extra='ignore')

    entity_id: str = Field(..., description='Unique identifier for DigitalInfrastructureEntity103')
    reference_code: str = Field(..., description='Official municipal reference code')
    status: DigitalInfrastructureStatus = Field(default=DigitalInfrastructureStatus.ACTIVE)
    priority: DigitalInfrastructurePriority = Field(default=DigitalInfrastructurePriority.STANDARD)
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

class DigitalInfrastructureEntity104(BaseModel):
    """Operational domain entity 104 for Smart City Cyber-Physical Infrastructure."""
    model_config = ConfigDict(from_attributes=True, extra='ignore')

    entity_id: str = Field(..., description='Unique identifier for DigitalInfrastructureEntity104')
    reference_code: str = Field(..., description='Official municipal reference code')
    status: DigitalInfrastructureStatus = Field(default=DigitalInfrastructureStatus.ACTIVE)
    priority: DigitalInfrastructurePriority = Field(default=DigitalInfrastructurePriority.STANDARD)
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

class DigitalInfrastructureEntity105(BaseModel):
    """Operational domain entity 105 for Smart City Cyber-Physical Infrastructure."""
    model_config = ConfigDict(from_attributes=True, extra='ignore')

    entity_id: str = Field(..., description='Unique identifier for DigitalInfrastructureEntity105')
    reference_code: str = Field(..., description='Official municipal reference code')
    status: DigitalInfrastructureStatus = Field(default=DigitalInfrastructureStatus.ACTIVE)
    priority: DigitalInfrastructurePriority = Field(default=DigitalInfrastructurePriority.STANDARD)
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

class DigitalInfrastructureEntity106(BaseModel):
    """Operational domain entity 106 for Smart City Cyber-Physical Infrastructure."""
    model_config = ConfigDict(from_attributes=True, extra='ignore')

    entity_id: str = Field(..., description='Unique identifier for DigitalInfrastructureEntity106')
    reference_code: str = Field(..., description='Official municipal reference code')
    status: DigitalInfrastructureStatus = Field(default=DigitalInfrastructureStatus.ACTIVE)
    priority: DigitalInfrastructurePriority = Field(default=DigitalInfrastructurePriority.STANDARD)
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

class DigitalInfrastructureEntity107(BaseModel):
    """Operational domain entity 107 for Smart City Cyber-Physical Infrastructure."""
    model_config = ConfigDict(from_attributes=True, extra='ignore')

    entity_id: str = Field(..., description='Unique identifier for DigitalInfrastructureEntity107')
    reference_code: str = Field(..., description='Official municipal reference code')
    status: DigitalInfrastructureStatus = Field(default=DigitalInfrastructureStatus.ACTIVE)
    priority: DigitalInfrastructurePriority = Field(default=DigitalInfrastructurePriority.STANDARD)
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

class DigitalInfrastructureEntity108(BaseModel):
    """Operational domain entity 108 for Smart City Cyber-Physical Infrastructure."""
    model_config = ConfigDict(from_attributes=True, extra='ignore')

    entity_id: str = Field(..., description='Unique identifier for DigitalInfrastructureEntity108')
    reference_code: str = Field(..., description='Official municipal reference code')
    status: DigitalInfrastructureStatus = Field(default=DigitalInfrastructureStatus.ACTIVE)
    priority: DigitalInfrastructurePriority = Field(default=DigitalInfrastructurePriority.STANDARD)
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

class DigitalInfrastructureEntity109(BaseModel):
    """Operational domain entity 109 for Smart City Cyber-Physical Infrastructure."""
    model_config = ConfigDict(from_attributes=True, extra='ignore')

    entity_id: str = Field(..., description='Unique identifier for DigitalInfrastructureEntity109')
    reference_code: str = Field(..., description='Official municipal reference code')
    status: DigitalInfrastructureStatus = Field(default=DigitalInfrastructureStatus.ACTIVE)
    priority: DigitalInfrastructurePriority = Field(default=DigitalInfrastructurePriority.STANDARD)
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

class DigitalInfrastructureEntity110(BaseModel):
    """Operational domain entity 110 for Smart City Cyber-Physical Infrastructure."""
    model_config = ConfigDict(from_attributes=True, extra='ignore')

    entity_id: str = Field(..., description='Unique identifier for DigitalInfrastructureEntity110')
    reference_code: str = Field(..., description='Official municipal reference code')
    status: DigitalInfrastructureStatus = Field(default=DigitalInfrastructureStatus.ACTIVE)
    priority: DigitalInfrastructurePriority = Field(default=DigitalInfrastructurePriority.STANDARD)
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

class DigitalInfrastructureEntity111(BaseModel):
    """Operational domain entity 111 for Smart City Cyber-Physical Infrastructure."""
    model_config = ConfigDict(from_attributes=True, extra='ignore')

    entity_id: str = Field(..., description='Unique identifier for DigitalInfrastructureEntity111')
    reference_code: str = Field(..., description='Official municipal reference code')
    status: DigitalInfrastructureStatus = Field(default=DigitalInfrastructureStatus.ACTIVE)
    priority: DigitalInfrastructurePriority = Field(default=DigitalInfrastructurePriority.STANDARD)
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

class DigitalInfrastructureEntity112(BaseModel):
    """Operational domain entity 112 for Smart City Cyber-Physical Infrastructure."""
    model_config = ConfigDict(from_attributes=True, extra='ignore')

    entity_id: str = Field(..., description='Unique identifier for DigitalInfrastructureEntity112')
    reference_code: str = Field(..., description='Official municipal reference code')
    status: DigitalInfrastructureStatus = Field(default=DigitalInfrastructureStatus.ACTIVE)
    priority: DigitalInfrastructurePriority = Field(default=DigitalInfrastructurePriority.STANDARD)
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

class DigitalInfrastructureEntity113(BaseModel):
    """Operational domain entity 113 for Smart City Cyber-Physical Infrastructure."""
    model_config = ConfigDict(from_attributes=True, extra='ignore')

    entity_id: str = Field(..., description='Unique identifier for DigitalInfrastructureEntity113')
    reference_code: str = Field(..., description='Official municipal reference code')
    status: DigitalInfrastructureStatus = Field(default=DigitalInfrastructureStatus.ACTIVE)
    priority: DigitalInfrastructurePriority = Field(default=DigitalInfrastructurePriority.STANDARD)
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

class DigitalInfrastructureEntity114(BaseModel):
    """Operational domain entity 114 for Smart City Cyber-Physical Infrastructure."""
    model_config = ConfigDict(from_attributes=True, extra='ignore')

    entity_id: str = Field(..., description='Unique identifier for DigitalInfrastructureEntity114')
    reference_code: str = Field(..., description='Official municipal reference code')
    status: DigitalInfrastructureStatus = Field(default=DigitalInfrastructureStatus.ACTIVE)
    priority: DigitalInfrastructurePriority = Field(default=DigitalInfrastructurePriority.STANDARD)
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

class DigitalInfrastructureEntity115(BaseModel):
    """Operational domain entity 115 for Smart City Cyber-Physical Infrastructure."""
    model_config = ConfigDict(from_attributes=True, extra='ignore')

    entity_id: str = Field(..., description='Unique identifier for DigitalInfrastructureEntity115')
    reference_code: str = Field(..., description='Official municipal reference code')
    status: DigitalInfrastructureStatus = Field(default=DigitalInfrastructureStatus.ACTIVE)
    priority: DigitalInfrastructurePriority = Field(default=DigitalInfrastructurePriority.STANDARD)
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

class DigitalInfrastructureEntity116(BaseModel):
    """Operational domain entity 116 for Smart City Cyber-Physical Infrastructure."""
    model_config = ConfigDict(from_attributes=True, extra='ignore')

    entity_id: str = Field(..., description='Unique identifier for DigitalInfrastructureEntity116')
    reference_code: str = Field(..., description='Official municipal reference code')
    status: DigitalInfrastructureStatus = Field(default=DigitalInfrastructureStatus.ACTIVE)
    priority: DigitalInfrastructurePriority = Field(default=DigitalInfrastructurePriority.STANDARD)
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

class DigitalInfrastructureEntity117(BaseModel):
    """Operational domain entity 117 for Smart City Cyber-Physical Infrastructure."""
    model_config = ConfigDict(from_attributes=True, extra='ignore')

    entity_id: str = Field(..., description='Unique identifier for DigitalInfrastructureEntity117')
    reference_code: str = Field(..., description='Official municipal reference code')
    status: DigitalInfrastructureStatus = Field(default=DigitalInfrastructureStatus.ACTIVE)
    priority: DigitalInfrastructurePriority = Field(default=DigitalInfrastructurePriority.STANDARD)
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

class DigitalInfrastructureEntity118(BaseModel):
    """Operational domain entity 118 for Smart City Cyber-Physical Infrastructure."""
    model_config = ConfigDict(from_attributes=True, extra='ignore')

    entity_id: str = Field(..., description='Unique identifier for DigitalInfrastructureEntity118')
    reference_code: str = Field(..., description='Official municipal reference code')
    status: DigitalInfrastructureStatus = Field(default=DigitalInfrastructureStatus.ACTIVE)
    priority: DigitalInfrastructurePriority = Field(default=DigitalInfrastructurePriority.STANDARD)
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

class DigitalInfrastructureEntity119(BaseModel):
    """Operational domain entity 119 for Smart City Cyber-Physical Infrastructure."""
    model_config = ConfigDict(from_attributes=True, extra='ignore')

    entity_id: str = Field(..., description='Unique identifier for DigitalInfrastructureEntity119')
    reference_code: str = Field(..., description='Official municipal reference code')
    status: DigitalInfrastructureStatus = Field(default=DigitalInfrastructureStatus.ACTIVE)
    priority: DigitalInfrastructurePriority = Field(default=DigitalInfrastructurePriority.STANDARD)
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

class DigitalInfrastructureEntity120(BaseModel):
    """Operational domain entity 120 for Smart City Cyber-Physical Infrastructure."""
    model_config = ConfigDict(from_attributes=True, extra='ignore')

    entity_id: str = Field(..., description='Unique identifier for DigitalInfrastructureEntity120')
    reference_code: str = Field(..., description='Official municipal reference code')
    status: DigitalInfrastructureStatus = Field(default=DigitalInfrastructureStatus.ACTIVE)
    priority: DigitalInfrastructurePriority = Field(default=DigitalInfrastructurePriority.STANDARD)
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

class DigitalInfrastructureEntity121(BaseModel):
    """Operational domain entity 121 for Smart City Cyber-Physical Infrastructure."""
    model_config = ConfigDict(from_attributes=True, extra='ignore')

    entity_id: str = Field(..., description='Unique identifier for DigitalInfrastructureEntity121')
    reference_code: str = Field(..., description='Official municipal reference code')
    status: DigitalInfrastructureStatus = Field(default=DigitalInfrastructureStatus.ACTIVE)
    priority: DigitalInfrastructurePriority = Field(default=DigitalInfrastructurePriority.STANDARD)
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

class DigitalInfrastructureEntity122(BaseModel):
    """Operational domain entity 122 for Smart City Cyber-Physical Infrastructure."""
    model_config = ConfigDict(from_attributes=True, extra='ignore')

    entity_id: str = Field(..., description='Unique identifier for DigitalInfrastructureEntity122')
    reference_code: str = Field(..., description='Official municipal reference code')
    status: DigitalInfrastructureStatus = Field(default=DigitalInfrastructureStatus.ACTIVE)
    priority: DigitalInfrastructurePriority = Field(default=DigitalInfrastructurePriority.STANDARD)
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

class DigitalInfrastructureEntity123(BaseModel):
    """Operational domain entity 123 for Smart City Cyber-Physical Infrastructure."""
    model_config = ConfigDict(from_attributes=True, extra='ignore')

    entity_id: str = Field(..., description='Unique identifier for DigitalInfrastructureEntity123')
    reference_code: str = Field(..., description='Official municipal reference code')
    status: DigitalInfrastructureStatus = Field(default=DigitalInfrastructureStatus.ACTIVE)
    priority: DigitalInfrastructurePriority = Field(default=DigitalInfrastructurePriority.STANDARD)
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

class DigitalInfrastructureEntity124(BaseModel):
    """Operational domain entity 124 for Smart City Cyber-Physical Infrastructure."""
    model_config = ConfigDict(from_attributes=True, extra='ignore')

    entity_id: str = Field(..., description='Unique identifier for DigitalInfrastructureEntity124')
    reference_code: str = Field(..., description='Official municipal reference code')
    status: DigitalInfrastructureStatus = Field(default=DigitalInfrastructureStatus.ACTIVE)
    priority: DigitalInfrastructurePriority = Field(default=DigitalInfrastructurePriority.STANDARD)
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

class DigitalInfrastructureEntity125(BaseModel):
    """Operational domain entity 125 for Smart City Cyber-Physical Infrastructure."""
    model_config = ConfigDict(from_attributes=True, extra='ignore')

    entity_id: str = Field(..., description='Unique identifier for DigitalInfrastructureEntity125')
    reference_code: str = Field(..., description='Official municipal reference code')
    status: DigitalInfrastructureStatus = Field(default=DigitalInfrastructureStatus.ACTIVE)
    priority: DigitalInfrastructurePriority = Field(default=DigitalInfrastructurePriority.STANDARD)
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

class DigitalInfrastructureEntity126(BaseModel):
    """Operational domain entity 126 for Smart City Cyber-Physical Infrastructure."""
    model_config = ConfigDict(from_attributes=True, extra='ignore')

    entity_id: str = Field(..., description='Unique identifier for DigitalInfrastructureEntity126')
    reference_code: str = Field(..., description='Official municipal reference code')
    status: DigitalInfrastructureStatus = Field(default=DigitalInfrastructureStatus.ACTIVE)
    priority: DigitalInfrastructurePriority = Field(default=DigitalInfrastructurePriority.STANDARD)
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

class DigitalInfrastructureEntity127(BaseModel):
    """Operational domain entity 127 for Smart City Cyber-Physical Infrastructure."""
    model_config = ConfigDict(from_attributes=True, extra='ignore')

    entity_id: str = Field(..., description='Unique identifier for DigitalInfrastructureEntity127')
    reference_code: str = Field(..., description='Official municipal reference code')
    status: DigitalInfrastructureStatus = Field(default=DigitalInfrastructureStatus.ACTIVE)
    priority: DigitalInfrastructurePriority = Field(default=DigitalInfrastructurePriority.STANDARD)
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

class DigitalInfrastructureEntity128(BaseModel):
    """Operational domain entity 128 for Smart City Cyber-Physical Infrastructure."""
    model_config = ConfigDict(from_attributes=True, extra='ignore')

    entity_id: str = Field(..., description='Unique identifier for DigitalInfrastructureEntity128')
    reference_code: str = Field(..., description='Official municipal reference code')
    status: DigitalInfrastructureStatus = Field(default=DigitalInfrastructureStatus.ACTIVE)
    priority: DigitalInfrastructurePriority = Field(default=DigitalInfrastructurePriority.STANDARD)
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

class DigitalInfrastructureEntity129(BaseModel):
    """Operational domain entity 129 for Smart City Cyber-Physical Infrastructure."""
    model_config = ConfigDict(from_attributes=True, extra='ignore')

    entity_id: str = Field(..., description='Unique identifier for DigitalInfrastructureEntity129')
    reference_code: str = Field(..., description='Official municipal reference code')
    status: DigitalInfrastructureStatus = Field(default=DigitalInfrastructureStatus.ACTIVE)
    priority: DigitalInfrastructurePriority = Field(default=DigitalInfrastructurePriority.STANDARD)
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

class DigitalInfrastructureEntity130(BaseModel):
    """Operational domain entity 130 for Smart City Cyber-Physical Infrastructure."""
    model_config = ConfigDict(from_attributes=True, extra='ignore')

    entity_id: str = Field(..., description='Unique identifier for DigitalInfrastructureEntity130')
    reference_code: str = Field(..., description='Official municipal reference code')
    status: DigitalInfrastructureStatus = Field(default=DigitalInfrastructureStatus.ACTIVE)
    priority: DigitalInfrastructurePriority = Field(default=DigitalInfrastructurePriority.STANDARD)
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
