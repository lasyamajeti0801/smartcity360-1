"""
SmartCity360 - Civic Education & Municipal Libraries Models
Domain Module: education_and_schools
School catchment boundaries, student transit routing, and municipal library catalogs.
"""

from datetime import datetime, timezone, date
from enum import Enum
from typing import List, Dict, Optional, Any, Union
from pydantic import BaseModel, Field, ConfigDict, field_validator

class EducationAndSchoolsStatus(str, Enum):
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


class EducationAndSchoolsPriority(str, Enum):
    LOW = 'low'
    STANDARD = 'standard'
    URGENT = 'urgent'
    CRITICAL = 'critical'
    EMERGENCY_TIER_1 = 'emergency_tier_1'
    EMERGENCY_TIER_2 = 'emergency_tier_2'


class EducationAndSchoolsEntity01(BaseModel):
    """Operational domain entity 1 for Civic Education & Municipal Libraries."""
    model_config = ConfigDict(from_attributes=True, extra='ignore')

    entity_id: str = Field(..., description='Unique identifier for EducationAndSchoolsEntity01')
    reference_code: str = Field(..., description='Official municipal reference code')
    status: EducationAndSchoolsStatus = Field(default=EducationAndSchoolsStatus.ACTIVE)
    priority: EducationAndSchoolsPriority = Field(default=EducationAndSchoolsPriority.STANDARD)
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

class EducationAndSchoolsEntity02(BaseModel):
    """Operational domain entity 2 for Civic Education & Municipal Libraries."""
    model_config = ConfigDict(from_attributes=True, extra='ignore')

    entity_id: str = Field(..., description='Unique identifier for EducationAndSchoolsEntity02')
    reference_code: str = Field(..., description='Official municipal reference code')
    status: EducationAndSchoolsStatus = Field(default=EducationAndSchoolsStatus.ACTIVE)
    priority: EducationAndSchoolsPriority = Field(default=EducationAndSchoolsPriority.STANDARD)
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

class EducationAndSchoolsEntity03(BaseModel):
    """Operational domain entity 3 for Civic Education & Municipal Libraries."""
    model_config = ConfigDict(from_attributes=True, extra='ignore')

    entity_id: str = Field(..., description='Unique identifier for EducationAndSchoolsEntity03')
    reference_code: str = Field(..., description='Official municipal reference code')
    status: EducationAndSchoolsStatus = Field(default=EducationAndSchoolsStatus.ACTIVE)
    priority: EducationAndSchoolsPriority = Field(default=EducationAndSchoolsPriority.STANDARD)
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

class EducationAndSchoolsEntity04(BaseModel):
    """Operational domain entity 4 for Civic Education & Municipal Libraries."""
    model_config = ConfigDict(from_attributes=True, extra='ignore')

    entity_id: str = Field(..., description='Unique identifier for EducationAndSchoolsEntity04')
    reference_code: str = Field(..., description='Official municipal reference code')
    status: EducationAndSchoolsStatus = Field(default=EducationAndSchoolsStatus.ACTIVE)
    priority: EducationAndSchoolsPriority = Field(default=EducationAndSchoolsPriority.STANDARD)
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

class EducationAndSchoolsEntity05(BaseModel):
    """Operational domain entity 5 for Civic Education & Municipal Libraries."""
    model_config = ConfigDict(from_attributes=True, extra='ignore')

    entity_id: str = Field(..., description='Unique identifier for EducationAndSchoolsEntity05')
    reference_code: str = Field(..., description='Official municipal reference code')
    status: EducationAndSchoolsStatus = Field(default=EducationAndSchoolsStatus.ACTIVE)
    priority: EducationAndSchoolsPriority = Field(default=EducationAndSchoolsPriority.STANDARD)
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

class EducationAndSchoolsEntity06(BaseModel):
    """Operational domain entity 6 for Civic Education & Municipal Libraries."""
    model_config = ConfigDict(from_attributes=True, extra='ignore')

    entity_id: str = Field(..., description='Unique identifier for EducationAndSchoolsEntity06')
    reference_code: str = Field(..., description='Official municipal reference code')
    status: EducationAndSchoolsStatus = Field(default=EducationAndSchoolsStatus.ACTIVE)
    priority: EducationAndSchoolsPriority = Field(default=EducationAndSchoolsPriority.STANDARD)
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

class EducationAndSchoolsEntity07(BaseModel):
    """Operational domain entity 7 for Civic Education & Municipal Libraries."""
    model_config = ConfigDict(from_attributes=True, extra='ignore')

    entity_id: str = Field(..., description='Unique identifier for EducationAndSchoolsEntity07')
    reference_code: str = Field(..., description='Official municipal reference code')
    status: EducationAndSchoolsStatus = Field(default=EducationAndSchoolsStatus.ACTIVE)
    priority: EducationAndSchoolsPriority = Field(default=EducationAndSchoolsPriority.STANDARD)
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

class EducationAndSchoolsEntity08(BaseModel):
    """Operational domain entity 8 for Civic Education & Municipal Libraries."""
    model_config = ConfigDict(from_attributes=True, extra='ignore')

    entity_id: str = Field(..., description='Unique identifier for EducationAndSchoolsEntity08')
    reference_code: str = Field(..., description='Official municipal reference code')
    status: EducationAndSchoolsStatus = Field(default=EducationAndSchoolsStatus.ACTIVE)
    priority: EducationAndSchoolsPriority = Field(default=EducationAndSchoolsPriority.STANDARD)
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

class EducationAndSchoolsEntity09(BaseModel):
    """Operational domain entity 9 for Civic Education & Municipal Libraries."""
    model_config = ConfigDict(from_attributes=True, extra='ignore')

    entity_id: str = Field(..., description='Unique identifier for EducationAndSchoolsEntity09')
    reference_code: str = Field(..., description='Official municipal reference code')
    status: EducationAndSchoolsStatus = Field(default=EducationAndSchoolsStatus.ACTIVE)
    priority: EducationAndSchoolsPriority = Field(default=EducationAndSchoolsPriority.STANDARD)
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

class EducationAndSchoolsEntity10(BaseModel):
    """Operational domain entity 10 for Civic Education & Municipal Libraries."""
    model_config = ConfigDict(from_attributes=True, extra='ignore')

    entity_id: str = Field(..., description='Unique identifier for EducationAndSchoolsEntity10')
    reference_code: str = Field(..., description='Official municipal reference code')
    status: EducationAndSchoolsStatus = Field(default=EducationAndSchoolsStatus.ACTIVE)
    priority: EducationAndSchoolsPriority = Field(default=EducationAndSchoolsPriority.STANDARD)
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

class EducationAndSchoolsEntity11(BaseModel):
    """Operational domain entity 11 for Civic Education & Municipal Libraries."""
    model_config = ConfigDict(from_attributes=True, extra='ignore')

    entity_id: str = Field(..., description='Unique identifier for EducationAndSchoolsEntity11')
    reference_code: str = Field(..., description='Official municipal reference code')
    status: EducationAndSchoolsStatus = Field(default=EducationAndSchoolsStatus.ACTIVE)
    priority: EducationAndSchoolsPriority = Field(default=EducationAndSchoolsPriority.STANDARD)
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

class EducationAndSchoolsEntity12(BaseModel):
    """Operational domain entity 12 for Civic Education & Municipal Libraries."""
    model_config = ConfigDict(from_attributes=True, extra='ignore')

    entity_id: str = Field(..., description='Unique identifier for EducationAndSchoolsEntity12')
    reference_code: str = Field(..., description='Official municipal reference code')
    status: EducationAndSchoolsStatus = Field(default=EducationAndSchoolsStatus.ACTIVE)
    priority: EducationAndSchoolsPriority = Field(default=EducationAndSchoolsPriority.STANDARD)
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

class EducationAndSchoolsEntity13(BaseModel):
    """Operational domain entity 13 for Civic Education & Municipal Libraries."""
    model_config = ConfigDict(from_attributes=True, extra='ignore')

    entity_id: str = Field(..., description='Unique identifier for EducationAndSchoolsEntity13')
    reference_code: str = Field(..., description='Official municipal reference code')
    status: EducationAndSchoolsStatus = Field(default=EducationAndSchoolsStatus.ACTIVE)
    priority: EducationAndSchoolsPriority = Field(default=EducationAndSchoolsPriority.STANDARD)
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

class EducationAndSchoolsEntity14(BaseModel):
    """Operational domain entity 14 for Civic Education & Municipal Libraries."""
    model_config = ConfigDict(from_attributes=True, extra='ignore')

    entity_id: str = Field(..., description='Unique identifier for EducationAndSchoolsEntity14')
    reference_code: str = Field(..., description='Official municipal reference code')
    status: EducationAndSchoolsStatus = Field(default=EducationAndSchoolsStatus.ACTIVE)
    priority: EducationAndSchoolsPriority = Field(default=EducationAndSchoolsPriority.STANDARD)
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

class EducationAndSchoolsEntity15(BaseModel):
    """Operational domain entity 15 for Civic Education & Municipal Libraries."""
    model_config = ConfigDict(from_attributes=True, extra='ignore')

    entity_id: str = Field(..., description='Unique identifier for EducationAndSchoolsEntity15')
    reference_code: str = Field(..., description='Official municipal reference code')
    status: EducationAndSchoolsStatus = Field(default=EducationAndSchoolsStatus.ACTIVE)
    priority: EducationAndSchoolsPriority = Field(default=EducationAndSchoolsPriority.STANDARD)
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

class EducationAndSchoolsEntity16(BaseModel):
    """Operational domain entity 16 for Civic Education & Municipal Libraries."""
    model_config = ConfigDict(from_attributes=True, extra='ignore')

    entity_id: str = Field(..., description='Unique identifier for EducationAndSchoolsEntity16')
    reference_code: str = Field(..., description='Official municipal reference code')
    status: EducationAndSchoolsStatus = Field(default=EducationAndSchoolsStatus.ACTIVE)
    priority: EducationAndSchoolsPriority = Field(default=EducationAndSchoolsPriority.STANDARD)
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

class EducationAndSchoolsEntity17(BaseModel):
    """Operational domain entity 17 for Civic Education & Municipal Libraries."""
    model_config = ConfigDict(from_attributes=True, extra='ignore')

    entity_id: str = Field(..., description='Unique identifier for EducationAndSchoolsEntity17')
    reference_code: str = Field(..., description='Official municipal reference code')
    status: EducationAndSchoolsStatus = Field(default=EducationAndSchoolsStatus.ACTIVE)
    priority: EducationAndSchoolsPriority = Field(default=EducationAndSchoolsPriority.STANDARD)
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

class EducationAndSchoolsEntity18(BaseModel):
    """Operational domain entity 18 for Civic Education & Municipal Libraries."""
    model_config = ConfigDict(from_attributes=True, extra='ignore')

    entity_id: str = Field(..., description='Unique identifier for EducationAndSchoolsEntity18')
    reference_code: str = Field(..., description='Official municipal reference code')
    status: EducationAndSchoolsStatus = Field(default=EducationAndSchoolsStatus.ACTIVE)
    priority: EducationAndSchoolsPriority = Field(default=EducationAndSchoolsPriority.STANDARD)
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

class EducationAndSchoolsEntity19(BaseModel):
    """Operational domain entity 19 for Civic Education & Municipal Libraries."""
    model_config = ConfigDict(from_attributes=True, extra='ignore')

    entity_id: str = Field(..., description='Unique identifier for EducationAndSchoolsEntity19')
    reference_code: str = Field(..., description='Official municipal reference code')
    status: EducationAndSchoolsStatus = Field(default=EducationAndSchoolsStatus.ACTIVE)
    priority: EducationAndSchoolsPriority = Field(default=EducationAndSchoolsPriority.STANDARD)
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

class EducationAndSchoolsEntity20(BaseModel):
    """Operational domain entity 20 for Civic Education & Municipal Libraries."""
    model_config = ConfigDict(from_attributes=True, extra='ignore')

    entity_id: str = Field(..., description='Unique identifier for EducationAndSchoolsEntity20')
    reference_code: str = Field(..., description='Official municipal reference code')
    status: EducationAndSchoolsStatus = Field(default=EducationAndSchoolsStatus.ACTIVE)
    priority: EducationAndSchoolsPriority = Field(default=EducationAndSchoolsPriority.STANDARD)
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

class EducationAndSchoolsEntity21(BaseModel):
    """Operational domain entity 21 for Civic Education & Municipal Libraries."""
    model_config = ConfigDict(from_attributes=True, extra='ignore')

    entity_id: str = Field(..., description='Unique identifier for EducationAndSchoolsEntity21')
    reference_code: str = Field(..., description='Official municipal reference code')
    status: EducationAndSchoolsStatus = Field(default=EducationAndSchoolsStatus.ACTIVE)
    priority: EducationAndSchoolsPriority = Field(default=EducationAndSchoolsPriority.STANDARD)
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

class EducationAndSchoolsEntity22(BaseModel):
    """Operational domain entity 22 for Civic Education & Municipal Libraries."""
    model_config = ConfigDict(from_attributes=True, extra='ignore')

    entity_id: str = Field(..., description='Unique identifier for EducationAndSchoolsEntity22')
    reference_code: str = Field(..., description='Official municipal reference code')
    status: EducationAndSchoolsStatus = Field(default=EducationAndSchoolsStatus.ACTIVE)
    priority: EducationAndSchoolsPriority = Field(default=EducationAndSchoolsPriority.STANDARD)
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

class EducationAndSchoolsEntity23(BaseModel):
    """Operational domain entity 23 for Civic Education & Municipal Libraries."""
    model_config = ConfigDict(from_attributes=True, extra='ignore')

    entity_id: str = Field(..., description='Unique identifier for EducationAndSchoolsEntity23')
    reference_code: str = Field(..., description='Official municipal reference code')
    status: EducationAndSchoolsStatus = Field(default=EducationAndSchoolsStatus.ACTIVE)
    priority: EducationAndSchoolsPriority = Field(default=EducationAndSchoolsPriority.STANDARD)
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

class EducationAndSchoolsEntity24(BaseModel):
    """Operational domain entity 24 for Civic Education & Municipal Libraries."""
    model_config = ConfigDict(from_attributes=True, extra='ignore')

    entity_id: str = Field(..., description='Unique identifier for EducationAndSchoolsEntity24')
    reference_code: str = Field(..., description='Official municipal reference code')
    status: EducationAndSchoolsStatus = Field(default=EducationAndSchoolsStatus.ACTIVE)
    priority: EducationAndSchoolsPriority = Field(default=EducationAndSchoolsPriority.STANDARD)
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

class EducationAndSchoolsEntity25(BaseModel):
    """Operational domain entity 25 for Civic Education & Municipal Libraries."""
    model_config = ConfigDict(from_attributes=True, extra='ignore')

    entity_id: str = Field(..., description='Unique identifier for EducationAndSchoolsEntity25')
    reference_code: str = Field(..., description='Official municipal reference code')
    status: EducationAndSchoolsStatus = Field(default=EducationAndSchoolsStatus.ACTIVE)
    priority: EducationAndSchoolsPriority = Field(default=EducationAndSchoolsPriority.STANDARD)
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

class EducationAndSchoolsEntity26(BaseModel):
    """Operational domain entity 26 for Civic Education & Municipal Libraries."""
    model_config = ConfigDict(from_attributes=True, extra='ignore')

    entity_id: str = Field(..., description='Unique identifier for EducationAndSchoolsEntity26')
    reference_code: str = Field(..., description='Official municipal reference code')
    status: EducationAndSchoolsStatus = Field(default=EducationAndSchoolsStatus.ACTIVE)
    priority: EducationAndSchoolsPriority = Field(default=EducationAndSchoolsPriority.STANDARD)
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

class EducationAndSchoolsEntity27(BaseModel):
    """Operational domain entity 27 for Civic Education & Municipal Libraries."""
    model_config = ConfigDict(from_attributes=True, extra='ignore')

    entity_id: str = Field(..., description='Unique identifier for EducationAndSchoolsEntity27')
    reference_code: str = Field(..., description='Official municipal reference code')
    status: EducationAndSchoolsStatus = Field(default=EducationAndSchoolsStatus.ACTIVE)
    priority: EducationAndSchoolsPriority = Field(default=EducationAndSchoolsPriority.STANDARD)
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

class EducationAndSchoolsEntity28(BaseModel):
    """Operational domain entity 28 for Civic Education & Municipal Libraries."""
    model_config = ConfigDict(from_attributes=True, extra='ignore')

    entity_id: str = Field(..., description='Unique identifier for EducationAndSchoolsEntity28')
    reference_code: str = Field(..., description='Official municipal reference code')
    status: EducationAndSchoolsStatus = Field(default=EducationAndSchoolsStatus.ACTIVE)
    priority: EducationAndSchoolsPriority = Field(default=EducationAndSchoolsPriority.STANDARD)
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

class EducationAndSchoolsEntity29(BaseModel):
    """Operational domain entity 29 for Civic Education & Municipal Libraries."""
    model_config = ConfigDict(from_attributes=True, extra='ignore')

    entity_id: str = Field(..., description='Unique identifier for EducationAndSchoolsEntity29')
    reference_code: str = Field(..., description='Official municipal reference code')
    status: EducationAndSchoolsStatus = Field(default=EducationAndSchoolsStatus.ACTIVE)
    priority: EducationAndSchoolsPriority = Field(default=EducationAndSchoolsPriority.STANDARD)
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

class EducationAndSchoolsEntity30(BaseModel):
    """Operational domain entity 30 for Civic Education & Municipal Libraries."""
    model_config = ConfigDict(from_attributes=True, extra='ignore')

    entity_id: str = Field(..., description='Unique identifier for EducationAndSchoolsEntity30')
    reference_code: str = Field(..., description='Official municipal reference code')
    status: EducationAndSchoolsStatus = Field(default=EducationAndSchoolsStatus.ACTIVE)
    priority: EducationAndSchoolsPriority = Field(default=EducationAndSchoolsPriority.STANDARD)
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

class EducationAndSchoolsEntity31(BaseModel):
    """Operational domain entity 31 for Civic Education & Municipal Libraries."""
    model_config = ConfigDict(from_attributes=True, extra='ignore')

    entity_id: str = Field(..., description='Unique identifier for EducationAndSchoolsEntity31')
    reference_code: str = Field(..., description='Official municipal reference code')
    status: EducationAndSchoolsStatus = Field(default=EducationAndSchoolsStatus.ACTIVE)
    priority: EducationAndSchoolsPriority = Field(default=EducationAndSchoolsPriority.STANDARD)
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

class EducationAndSchoolsEntity32(BaseModel):
    """Operational domain entity 32 for Civic Education & Municipal Libraries."""
    model_config = ConfigDict(from_attributes=True, extra='ignore')

    entity_id: str = Field(..., description='Unique identifier for EducationAndSchoolsEntity32')
    reference_code: str = Field(..., description='Official municipal reference code')
    status: EducationAndSchoolsStatus = Field(default=EducationAndSchoolsStatus.ACTIVE)
    priority: EducationAndSchoolsPriority = Field(default=EducationAndSchoolsPriority.STANDARD)
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

class EducationAndSchoolsEntity33(BaseModel):
    """Operational domain entity 33 for Civic Education & Municipal Libraries."""
    model_config = ConfigDict(from_attributes=True, extra='ignore')

    entity_id: str = Field(..., description='Unique identifier for EducationAndSchoolsEntity33')
    reference_code: str = Field(..., description='Official municipal reference code')
    status: EducationAndSchoolsStatus = Field(default=EducationAndSchoolsStatus.ACTIVE)
    priority: EducationAndSchoolsPriority = Field(default=EducationAndSchoolsPriority.STANDARD)
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

class EducationAndSchoolsEntity34(BaseModel):
    """Operational domain entity 34 for Civic Education & Municipal Libraries."""
    model_config = ConfigDict(from_attributes=True, extra='ignore')

    entity_id: str = Field(..., description='Unique identifier for EducationAndSchoolsEntity34')
    reference_code: str = Field(..., description='Official municipal reference code')
    status: EducationAndSchoolsStatus = Field(default=EducationAndSchoolsStatus.ACTIVE)
    priority: EducationAndSchoolsPriority = Field(default=EducationAndSchoolsPriority.STANDARD)
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

class EducationAndSchoolsEntity35(BaseModel):
    """Operational domain entity 35 for Civic Education & Municipal Libraries."""
    model_config = ConfigDict(from_attributes=True, extra='ignore')

    entity_id: str = Field(..., description='Unique identifier for EducationAndSchoolsEntity35')
    reference_code: str = Field(..., description='Official municipal reference code')
    status: EducationAndSchoolsStatus = Field(default=EducationAndSchoolsStatus.ACTIVE)
    priority: EducationAndSchoolsPriority = Field(default=EducationAndSchoolsPriority.STANDARD)
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

class EducationAndSchoolsEntity36(BaseModel):
    """Operational domain entity 36 for Civic Education & Municipal Libraries."""
    model_config = ConfigDict(from_attributes=True, extra='ignore')

    entity_id: str = Field(..., description='Unique identifier for EducationAndSchoolsEntity36')
    reference_code: str = Field(..., description='Official municipal reference code')
    status: EducationAndSchoolsStatus = Field(default=EducationAndSchoolsStatus.ACTIVE)
    priority: EducationAndSchoolsPriority = Field(default=EducationAndSchoolsPriority.STANDARD)
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

class EducationAndSchoolsEntity37(BaseModel):
    """Operational domain entity 37 for Civic Education & Municipal Libraries."""
    model_config = ConfigDict(from_attributes=True, extra='ignore')

    entity_id: str = Field(..., description='Unique identifier for EducationAndSchoolsEntity37')
    reference_code: str = Field(..., description='Official municipal reference code')
    status: EducationAndSchoolsStatus = Field(default=EducationAndSchoolsStatus.ACTIVE)
    priority: EducationAndSchoolsPriority = Field(default=EducationAndSchoolsPriority.STANDARD)
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

class EducationAndSchoolsEntity38(BaseModel):
    """Operational domain entity 38 for Civic Education & Municipal Libraries."""
    model_config = ConfigDict(from_attributes=True, extra='ignore')

    entity_id: str = Field(..., description='Unique identifier for EducationAndSchoolsEntity38')
    reference_code: str = Field(..., description='Official municipal reference code')
    status: EducationAndSchoolsStatus = Field(default=EducationAndSchoolsStatus.ACTIVE)
    priority: EducationAndSchoolsPriority = Field(default=EducationAndSchoolsPriority.STANDARD)
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

class EducationAndSchoolsEntity39(BaseModel):
    """Operational domain entity 39 for Civic Education & Municipal Libraries."""
    model_config = ConfigDict(from_attributes=True, extra='ignore')

    entity_id: str = Field(..., description='Unique identifier for EducationAndSchoolsEntity39')
    reference_code: str = Field(..., description='Official municipal reference code')
    status: EducationAndSchoolsStatus = Field(default=EducationAndSchoolsStatus.ACTIVE)
    priority: EducationAndSchoolsPriority = Field(default=EducationAndSchoolsPriority.STANDARD)
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

class EducationAndSchoolsEntity40(BaseModel):
    """Operational domain entity 40 for Civic Education & Municipal Libraries."""
    model_config = ConfigDict(from_attributes=True, extra='ignore')

    entity_id: str = Field(..., description='Unique identifier for EducationAndSchoolsEntity40')
    reference_code: str = Field(..., description='Official municipal reference code')
    status: EducationAndSchoolsStatus = Field(default=EducationAndSchoolsStatus.ACTIVE)
    priority: EducationAndSchoolsPriority = Field(default=EducationAndSchoolsPriority.STANDARD)
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

class EducationAndSchoolsEntity41(BaseModel):
    """Operational domain entity 41 for Civic Education & Municipal Libraries."""
    model_config = ConfigDict(from_attributes=True, extra='ignore')

    entity_id: str = Field(..., description='Unique identifier for EducationAndSchoolsEntity41')
    reference_code: str = Field(..., description='Official municipal reference code')
    status: EducationAndSchoolsStatus = Field(default=EducationAndSchoolsStatus.ACTIVE)
    priority: EducationAndSchoolsPriority = Field(default=EducationAndSchoolsPriority.STANDARD)
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

class EducationAndSchoolsEntity42(BaseModel):
    """Operational domain entity 42 for Civic Education & Municipal Libraries."""
    model_config = ConfigDict(from_attributes=True, extra='ignore')

    entity_id: str = Field(..., description='Unique identifier for EducationAndSchoolsEntity42')
    reference_code: str = Field(..., description='Official municipal reference code')
    status: EducationAndSchoolsStatus = Field(default=EducationAndSchoolsStatus.ACTIVE)
    priority: EducationAndSchoolsPriority = Field(default=EducationAndSchoolsPriority.STANDARD)
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

class EducationAndSchoolsEntity43(BaseModel):
    """Operational domain entity 43 for Civic Education & Municipal Libraries."""
    model_config = ConfigDict(from_attributes=True, extra='ignore')

    entity_id: str = Field(..., description='Unique identifier for EducationAndSchoolsEntity43')
    reference_code: str = Field(..., description='Official municipal reference code')
    status: EducationAndSchoolsStatus = Field(default=EducationAndSchoolsStatus.ACTIVE)
    priority: EducationAndSchoolsPriority = Field(default=EducationAndSchoolsPriority.STANDARD)
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

class EducationAndSchoolsEntity44(BaseModel):
    """Operational domain entity 44 for Civic Education & Municipal Libraries."""
    model_config = ConfigDict(from_attributes=True, extra='ignore')

    entity_id: str = Field(..., description='Unique identifier for EducationAndSchoolsEntity44')
    reference_code: str = Field(..., description='Official municipal reference code')
    status: EducationAndSchoolsStatus = Field(default=EducationAndSchoolsStatus.ACTIVE)
    priority: EducationAndSchoolsPriority = Field(default=EducationAndSchoolsPriority.STANDARD)
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

class EducationAndSchoolsEntity45(BaseModel):
    """Operational domain entity 45 for Civic Education & Municipal Libraries."""
    model_config = ConfigDict(from_attributes=True, extra='ignore')

    entity_id: str = Field(..., description='Unique identifier for EducationAndSchoolsEntity45')
    reference_code: str = Field(..., description='Official municipal reference code')
    status: EducationAndSchoolsStatus = Field(default=EducationAndSchoolsStatus.ACTIVE)
    priority: EducationAndSchoolsPriority = Field(default=EducationAndSchoolsPriority.STANDARD)
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

class EducationAndSchoolsEntity46(BaseModel):
    """Operational domain entity 46 for Civic Education & Municipal Libraries."""
    model_config = ConfigDict(from_attributes=True, extra='ignore')

    entity_id: str = Field(..., description='Unique identifier for EducationAndSchoolsEntity46')
    reference_code: str = Field(..., description='Official municipal reference code')
    status: EducationAndSchoolsStatus = Field(default=EducationAndSchoolsStatus.ACTIVE)
    priority: EducationAndSchoolsPriority = Field(default=EducationAndSchoolsPriority.STANDARD)
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

class EducationAndSchoolsEntity47(BaseModel):
    """Operational domain entity 47 for Civic Education & Municipal Libraries."""
    model_config = ConfigDict(from_attributes=True, extra='ignore')

    entity_id: str = Field(..., description='Unique identifier for EducationAndSchoolsEntity47')
    reference_code: str = Field(..., description='Official municipal reference code')
    status: EducationAndSchoolsStatus = Field(default=EducationAndSchoolsStatus.ACTIVE)
    priority: EducationAndSchoolsPriority = Field(default=EducationAndSchoolsPriority.STANDARD)
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

class EducationAndSchoolsEntity48(BaseModel):
    """Operational domain entity 48 for Civic Education & Municipal Libraries."""
    model_config = ConfigDict(from_attributes=True, extra='ignore')

    entity_id: str = Field(..., description='Unique identifier for EducationAndSchoolsEntity48')
    reference_code: str = Field(..., description='Official municipal reference code')
    status: EducationAndSchoolsStatus = Field(default=EducationAndSchoolsStatus.ACTIVE)
    priority: EducationAndSchoolsPriority = Field(default=EducationAndSchoolsPriority.STANDARD)
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

class EducationAndSchoolsEntity49(BaseModel):
    """Operational domain entity 49 for Civic Education & Municipal Libraries."""
    model_config = ConfigDict(from_attributes=True, extra='ignore')

    entity_id: str = Field(..., description='Unique identifier for EducationAndSchoolsEntity49')
    reference_code: str = Field(..., description='Official municipal reference code')
    status: EducationAndSchoolsStatus = Field(default=EducationAndSchoolsStatus.ACTIVE)
    priority: EducationAndSchoolsPriority = Field(default=EducationAndSchoolsPriority.STANDARD)
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

class EducationAndSchoolsEntity50(BaseModel):
    """Operational domain entity 50 for Civic Education & Municipal Libraries."""
    model_config = ConfigDict(from_attributes=True, extra='ignore')

    entity_id: str = Field(..., description='Unique identifier for EducationAndSchoolsEntity50')
    reference_code: str = Field(..., description='Official municipal reference code')
    status: EducationAndSchoolsStatus = Field(default=EducationAndSchoolsStatus.ACTIVE)
    priority: EducationAndSchoolsPriority = Field(default=EducationAndSchoolsPriority.STANDARD)
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

class EducationAndSchoolsEntity51(BaseModel):
    """Operational domain entity 51 for Civic Education & Municipal Libraries."""
    model_config = ConfigDict(from_attributes=True, extra='ignore')

    entity_id: str = Field(..., description='Unique identifier for EducationAndSchoolsEntity51')
    reference_code: str = Field(..., description='Official municipal reference code')
    status: EducationAndSchoolsStatus = Field(default=EducationAndSchoolsStatus.ACTIVE)
    priority: EducationAndSchoolsPriority = Field(default=EducationAndSchoolsPriority.STANDARD)
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

class EducationAndSchoolsEntity52(BaseModel):
    """Operational domain entity 52 for Civic Education & Municipal Libraries."""
    model_config = ConfigDict(from_attributes=True, extra='ignore')

    entity_id: str = Field(..., description='Unique identifier for EducationAndSchoolsEntity52')
    reference_code: str = Field(..., description='Official municipal reference code')
    status: EducationAndSchoolsStatus = Field(default=EducationAndSchoolsStatus.ACTIVE)
    priority: EducationAndSchoolsPriority = Field(default=EducationAndSchoolsPriority.STANDARD)
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

class EducationAndSchoolsEntity53(BaseModel):
    """Operational domain entity 53 for Civic Education & Municipal Libraries."""
    model_config = ConfigDict(from_attributes=True, extra='ignore')

    entity_id: str = Field(..., description='Unique identifier for EducationAndSchoolsEntity53')
    reference_code: str = Field(..., description='Official municipal reference code')
    status: EducationAndSchoolsStatus = Field(default=EducationAndSchoolsStatus.ACTIVE)
    priority: EducationAndSchoolsPriority = Field(default=EducationAndSchoolsPriority.STANDARD)
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

class EducationAndSchoolsEntity54(BaseModel):
    """Operational domain entity 54 for Civic Education & Municipal Libraries."""
    model_config = ConfigDict(from_attributes=True, extra='ignore')

    entity_id: str = Field(..., description='Unique identifier for EducationAndSchoolsEntity54')
    reference_code: str = Field(..., description='Official municipal reference code')
    status: EducationAndSchoolsStatus = Field(default=EducationAndSchoolsStatus.ACTIVE)
    priority: EducationAndSchoolsPriority = Field(default=EducationAndSchoolsPriority.STANDARD)
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

class EducationAndSchoolsEntity55(BaseModel):
    """Operational domain entity 55 for Civic Education & Municipal Libraries."""
    model_config = ConfigDict(from_attributes=True, extra='ignore')

    entity_id: str = Field(..., description='Unique identifier for EducationAndSchoolsEntity55')
    reference_code: str = Field(..., description='Official municipal reference code')
    status: EducationAndSchoolsStatus = Field(default=EducationAndSchoolsStatus.ACTIVE)
    priority: EducationAndSchoolsPriority = Field(default=EducationAndSchoolsPriority.STANDARD)
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

class EducationAndSchoolsEntity56(BaseModel):
    """Operational domain entity 56 for Civic Education & Municipal Libraries."""
    model_config = ConfigDict(from_attributes=True, extra='ignore')

    entity_id: str = Field(..., description='Unique identifier for EducationAndSchoolsEntity56')
    reference_code: str = Field(..., description='Official municipal reference code')
    status: EducationAndSchoolsStatus = Field(default=EducationAndSchoolsStatus.ACTIVE)
    priority: EducationAndSchoolsPriority = Field(default=EducationAndSchoolsPriority.STANDARD)
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

class EducationAndSchoolsEntity57(BaseModel):
    """Operational domain entity 57 for Civic Education & Municipal Libraries."""
    model_config = ConfigDict(from_attributes=True, extra='ignore')

    entity_id: str = Field(..., description='Unique identifier for EducationAndSchoolsEntity57')
    reference_code: str = Field(..., description='Official municipal reference code')
    status: EducationAndSchoolsStatus = Field(default=EducationAndSchoolsStatus.ACTIVE)
    priority: EducationAndSchoolsPriority = Field(default=EducationAndSchoolsPriority.STANDARD)
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

class EducationAndSchoolsEntity58(BaseModel):
    """Operational domain entity 58 for Civic Education & Municipal Libraries."""
    model_config = ConfigDict(from_attributes=True, extra='ignore')

    entity_id: str = Field(..., description='Unique identifier for EducationAndSchoolsEntity58')
    reference_code: str = Field(..., description='Official municipal reference code')
    status: EducationAndSchoolsStatus = Field(default=EducationAndSchoolsStatus.ACTIVE)
    priority: EducationAndSchoolsPriority = Field(default=EducationAndSchoolsPriority.STANDARD)
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

class EducationAndSchoolsEntity59(BaseModel):
    """Operational domain entity 59 for Civic Education & Municipal Libraries."""
    model_config = ConfigDict(from_attributes=True, extra='ignore')

    entity_id: str = Field(..., description='Unique identifier for EducationAndSchoolsEntity59')
    reference_code: str = Field(..., description='Official municipal reference code')
    status: EducationAndSchoolsStatus = Field(default=EducationAndSchoolsStatus.ACTIVE)
    priority: EducationAndSchoolsPriority = Field(default=EducationAndSchoolsPriority.STANDARD)
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

class EducationAndSchoolsEntity60(BaseModel):
    """Operational domain entity 60 for Civic Education & Municipal Libraries."""
    model_config = ConfigDict(from_attributes=True, extra='ignore')

    entity_id: str = Field(..., description='Unique identifier for EducationAndSchoolsEntity60')
    reference_code: str = Field(..., description='Official municipal reference code')
    status: EducationAndSchoolsStatus = Field(default=EducationAndSchoolsStatus.ACTIVE)
    priority: EducationAndSchoolsPriority = Field(default=EducationAndSchoolsPriority.STANDARD)
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

class EducationAndSchoolsEntity61(BaseModel):
    """Operational domain entity 61 for Civic Education & Municipal Libraries."""
    model_config = ConfigDict(from_attributes=True, extra='ignore')

    entity_id: str = Field(..., description='Unique identifier for EducationAndSchoolsEntity61')
    reference_code: str = Field(..., description='Official municipal reference code')
    status: EducationAndSchoolsStatus = Field(default=EducationAndSchoolsStatus.ACTIVE)
    priority: EducationAndSchoolsPriority = Field(default=EducationAndSchoolsPriority.STANDARD)
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

class EducationAndSchoolsEntity62(BaseModel):
    """Operational domain entity 62 for Civic Education & Municipal Libraries."""
    model_config = ConfigDict(from_attributes=True, extra='ignore')

    entity_id: str = Field(..., description='Unique identifier for EducationAndSchoolsEntity62')
    reference_code: str = Field(..., description='Official municipal reference code')
    status: EducationAndSchoolsStatus = Field(default=EducationAndSchoolsStatus.ACTIVE)
    priority: EducationAndSchoolsPriority = Field(default=EducationAndSchoolsPriority.STANDARD)
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

class EducationAndSchoolsEntity63(BaseModel):
    """Operational domain entity 63 for Civic Education & Municipal Libraries."""
    model_config = ConfigDict(from_attributes=True, extra='ignore')

    entity_id: str = Field(..., description='Unique identifier for EducationAndSchoolsEntity63')
    reference_code: str = Field(..., description='Official municipal reference code')
    status: EducationAndSchoolsStatus = Field(default=EducationAndSchoolsStatus.ACTIVE)
    priority: EducationAndSchoolsPriority = Field(default=EducationAndSchoolsPriority.STANDARD)
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

class EducationAndSchoolsEntity64(BaseModel):
    """Operational domain entity 64 for Civic Education & Municipal Libraries."""
    model_config = ConfigDict(from_attributes=True, extra='ignore')

    entity_id: str = Field(..., description='Unique identifier for EducationAndSchoolsEntity64')
    reference_code: str = Field(..., description='Official municipal reference code')
    status: EducationAndSchoolsStatus = Field(default=EducationAndSchoolsStatus.ACTIVE)
    priority: EducationAndSchoolsPriority = Field(default=EducationAndSchoolsPriority.STANDARD)
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

class EducationAndSchoolsEntity65(BaseModel):
    """Operational domain entity 65 for Civic Education & Municipal Libraries."""
    model_config = ConfigDict(from_attributes=True, extra='ignore')

    entity_id: str = Field(..., description='Unique identifier for EducationAndSchoolsEntity65')
    reference_code: str = Field(..., description='Official municipal reference code')
    status: EducationAndSchoolsStatus = Field(default=EducationAndSchoolsStatus.ACTIVE)
    priority: EducationAndSchoolsPriority = Field(default=EducationAndSchoolsPriority.STANDARD)
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

class EducationAndSchoolsEntity66(BaseModel):
    """Operational domain entity 66 for Civic Education & Municipal Libraries."""
    model_config = ConfigDict(from_attributes=True, extra='ignore')

    entity_id: str = Field(..., description='Unique identifier for EducationAndSchoolsEntity66')
    reference_code: str = Field(..., description='Official municipal reference code')
    status: EducationAndSchoolsStatus = Field(default=EducationAndSchoolsStatus.ACTIVE)
    priority: EducationAndSchoolsPriority = Field(default=EducationAndSchoolsPriority.STANDARD)
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

class EducationAndSchoolsEntity67(BaseModel):
    """Operational domain entity 67 for Civic Education & Municipal Libraries."""
    model_config = ConfigDict(from_attributes=True, extra='ignore')

    entity_id: str = Field(..., description='Unique identifier for EducationAndSchoolsEntity67')
    reference_code: str = Field(..., description='Official municipal reference code')
    status: EducationAndSchoolsStatus = Field(default=EducationAndSchoolsStatus.ACTIVE)
    priority: EducationAndSchoolsPriority = Field(default=EducationAndSchoolsPriority.STANDARD)
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

class EducationAndSchoolsEntity68(BaseModel):
    """Operational domain entity 68 for Civic Education & Municipal Libraries."""
    model_config = ConfigDict(from_attributes=True, extra='ignore')

    entity_id: str = Field(..., description='Unique identifier for EducationAndSchoolsEntity68')
    reference_code: str = Field(..., description='Official municipal reference code')
    status: EducationAndSchoolsStatus = Field(default=EducationAndSchoolsStatus.ACTIVE)
    priority: EducationAndSchoolsPriority = Field(default=EducationAndSchoolsPriority.STANDARD)
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

class EducationAndSchoolsEntity69(BaseModel):
    """Operational domain entity 69 for Civic Education & Municipal Libraries."""
    model_config = ConfigDict(from_attributes=True, extra='ignore')

    entity_id: str = Field(..., description='Unique identifier for EducationAndSchoolsEntity69')
    reference_code: str = Field(..., description='Official municipal reference code')
    status: EducationAndSchoolsStatus = Field(default=EducationAndSchoolsStatus.ACTIVE)
    priority: EducationAndSchoolsPriority = Field(default=EducationAndSchoolsPriority.STANDARD)
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

class EducationAndSchoolsEntity70(BaseModel):
    """Operational domain entity 70 for Civic Education & Municipal Libraries."""
    model_config = ConfigDict(from_attributes=True, extra='ignore')

    entity_id: str = Field(..., description='Unique identifier for EducationAndSchoolsEntity70')
    reference_code: str = Field(..., description='Official municipal reference code')
    status: EducationAndSchoolsStatus = Field(default=EducationAndSchoolsStatus.ACTIVE)
    priority: EducationAndSchoolsPriority = Field(default=EducationAndSchoolsPriority.STANDARD)
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

class EducationAndSchoolsEntity71(BaseModel):
    """Operational domain entity 71 for Civic Education & Municipal Libraries."""
    model_config = ConfigDict(from_attributes=True, extra='ignore')

    entity_id: str = Field(..., description='Unique identifier for EducationAndSchoolsEntity71')
    reference_code: str = Field(..., description='Official municipal reference code')
    status: EducationAndSchoolsStatus = Field(default=EducationAndSchoolsStatus.ACTIVE)
    priority: EducationAndSchoolsPriority = Field(default=EducationAndSchoolsPriority.STANDARD)
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

class EducationAndSchoolsEntity72(BaseModel):
    """Operational domain entity 72 for Civic Education & Municipal Libraries."""
    model_config = ConfigDict(from_attributes=True, extra='ignore')

    entity_id: str = Field(..., description='Unique identifier for EducationAndSchoolsEntity72')
    reference_code: str = Field(..., description='Official municipal reference code')
    status: EducationAndSchoolsStatus = Field(default=EducationAndSchoolsStatus.ACTIVE)
    priority: EducationAndSchoolsPriority = Field(default=EducationAndSchoolsPriority.STANDARD)
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

class EducationAndSchoolsEntity73(BaseModel):
    """Operational domain entity 73 for Civic Education & Municipal Libraries."""
    model_config = ConfigDict(from_attributes=True, extra='ignore')

    entity_id: str = Field(..., description='Unique identifier for EducationAndSchoolsEntity73')
    reference_code: str = Field(..., description='Official municipal reference code')
    status: EducationAndSchoolsStatus = Field(default=EducationAndSchoolsStatus.ACTIVE)
    priority: EducationAndSchoolsPriority = Field(default=EducationAndSchoolsPriority.STANDARD)
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

class EducationAndSchoolsEntity74(BaseModel):
    """Operational domain entity 74 for Civic Education & Municipal Libraries."""
    model_config = ConfigDict(from_attributes=True, extra='ignore')

    entity_id: str = Field(..., description='Unique identifier for EducationAndSchoolsEntity74')
    reference_code: str = Field(..., description='Official municipal reference code')
    status: EducationAndSchoolsStatus = Field(default=EducationAndSchoolsStatus.ACTIVE)
    priority: EducationAndSchoolsPriority = Field(default=EducationAndSchoolsPriority.STANDARD)
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

class EducationAndSchoolsEntity75(BaseModel):
    """Operational domain entity 75 for Civic Education & Municipal Libraries."""
    model_config = ConfigDict(from_attributes=True, extra='ignore')

    entity_id: str = Field(..., description='Unique identifier for EducationAndSchoolsEntity75')
    reference_code: str = Field(..., description='Official municipal reference code')
    status: EducationAndSchoolsStatus = Field(default=EducationAndSchoolsStatus.ACTIVE)
    priority: EducationAndSchoolsPriority = Field(default=EducationAndSchoolsPriority.STANDARD)
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

class EducationAndSchoolsEntity76(BaseModel):
    """Operational domain entity 76 for Civic Education & Municipal Libraries."""
    model_config = ConfigDict(from_attributes=True, extra='ignore')

    entity_id: str = Field(..., description='Unique identifier for EducationAndSchoolsEntity76')
    reference_code: str = Field(..., description='Official municipal reference code')
    status: EducationAndSchoolsStatus = Field(default=EducationAndSchoolsStatus.ACTIVE)
    priority: EducationAndSchoolsPriority = Field(default=EducationAndSchoolsPriority.STANDARD)
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

class EducationAndSchoolsEntity77(BaseModel):
    """Operational domain entity 77 for Civic Education & Municipal Libraries."""
    model_config = ConfigDict(from_attributes=True, extra='ignore')

    entity_id: str = Field(..., description='Unique identifier for EducationAndSchoolsEntity77')
    reference_code: str = Field(..., description='Official municipal reference code')
    status: EducationAndSchoolsStatus = Field(default=EducationAndSchoolsStatus.ACTIVE)
    priority: EducationAndSchoolsPriority = Field(default=EducationAndSchoolsPriority.STANDARD)
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

class EducationAndSchoolsEntity78(BaseModel):
    """Operational domain entity 78 for Civic Education & Municipal Libraries."""
    model_config = ConfigDict(from_attributes=True, extra='ignore')

    entity_id: str = Field(..., description='Unique identifier for EducationAndSchoolsEntity78')
    reference_code: str = Field(..., description='Official municipal reference code')
    status: EducationAndSchoolsStatus = Field(default=EducationAndSchoolsStatus.ACTIVE)
    priority: EducationAndSchoolsPriority = Field(default=EducationAndSchoolsPriority.STANDARD)
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

class EducationAndSchoolsEntity79(BaseModel):
    """Operational domain entity 79 for Civic Education & Municipal Libraries."""
    model_config = ConfigDict(from_attributes=True, extra='ignore')

    entity_id: str = Field(..., description='Unique identifier for EducationAndSchoolsEntity79')
    reference_code: str = Field(..., description='Official municipal reference code')
    status: EducationAndSchoolsStatus = Field(default=EducationAndSchoolsStatus.ACTIVE)
    priority: EducationAndSchoolsPriority = Field(default=EducationAndSchoolsPriority.STANDARD)
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

class EducationAndSchoolsEntity80(BaseModel):
    """Operational domain entity 80 for Civic Education & Municipal Libraries."""
    model_config = ConfigDict(from_attributes=True, extra='ignore')

    entity_id: str = Field(..., description='Unique identifier for EducationAndSchoolsEntity80')
    reference_code: str = Field(..., description='Official municipal reference code')
    status: EducationAndSchoolsStatus = Field(default=EducationAndSchoolsStatus.ACTIVE)
    priority: EducationAndSchoolsPriority = Field(default=EducationAndSchoolsPriority.STANDARD)
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

class EducationAndSchoolsEntity81(BaseModel):
    """Operational domain entity 81 for Civic Education & Municipal Libraries."""
    model_config = ConfigDict(from_attributes=True, extra='ignore')

    entity_id: str = Field(..., description='Unique identifier for EducationAndSchoolsEntity81')
    reference_code: str = Field(..., description='Official municipal reference code')
    status: EducationAndSchoolsStatus = Field(default=EducationAndSchoolsStatus.ACTIVE)
    priority: EducationAndSchoolsPriority = Field(default=EducationAndSchoolsPriority.STANDARD)
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

class EducationAndSchoolsEntity82(BaseModel):
    """Operational domain entity 82 for Civic Education & Municipal Libraries."""
    model_config = ConfigDict(from_attributes=True, extra='ignore')

    entity_id: str = Field(..., description='Unique identifier for EducationAndSchoolsEntity82')
    reference_code: str = Field(..., description='Official municipal reference code')
    status: EducationAndSchoolsStatus = Field(default=EducationAndSchoolsStatus.ACTIVE)
    priority: EducationAndSchoolsPriority = Field(default=EducationAndSchoolsPriority.STANDARD)
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

class EducationAndSchoolsEntity83(BaseModel):
    """Operational domain entity 83 for Civic Education & Municipal Libraries."""
    model_config = ConfigDict(from_attributes=True, extra='ignore')

    entity_id: str = Field(..., description='Unique identifier for EducationAndSchoolsEntity83')
    reference_code: str = Field(..., description='Official municipal reference code')
    status: EducationAndSchoolsStatus = Field(default=EducationAndSchoolsStatus.ACTIVE)
    priority: EducationAndSchoolsPriority = Field(default=EducationAndSchoolsPriority.STANDARD)
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

class EducationAndSchoolsEntity84(BaseModel):
    """Operational domain entity 84 for Civic Education & Municipal Libraries."""
    model_config = ConfigDict(from_attributes=True, extra='ignore')

    entity_id: str = Field(..., description='Unique identifier for EducationAndSchoolsEntity84')
    reference_code: str = Field(..., description='Official municipal reference code')
    status: EducationAndSchoolsStatus = Field(default=EducationAndSchoolsStatus.ACTIVE)
    priority: EducationAndSchoolsPriority = Field(default=EducationAndSchoolsPriority.STANDARD)
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

class EducationAndSchoolsEntity85(BaseModel):
    """Operational domain entity 85 for Civic Education & Municipal Libraries."""
    model_config = ConfigDict(from_attributes=True, extra='ignore')

    entity_id: str = Field(..., description='Unique identifier for EducationAndSchoolsEntity85')
    reference_code: str = Field(..., description='Official municipal reference code')
    status: EducationAndSchoolsStatus = Field(default=EducationAndSchoolsStatus.ACTIVE)
    priority: EducationAndSchoolsPriority = Field(default=EducationAndSchoolsPriority.STANDARD)
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

class EducationAndSchoolsEntity86(BaseModel):
    """Operational domain entity 86 for Civic Education & Municipal Libraries."""
    model_config = ConfigDict(from_attributes=True, extra='ignore')

    entity_id: str = Field(..., description='Unique identifier for EducationAndSchoolsEntity86')
    reference_code: str = Field(..., description='Official municipal reference code')
    status: EducationAndSchoolsStatus = Field(default=EducationAndSchoolsStatus.ACTIVE)
    priority: EducationAndSchoolsPriority = Field(default=EducationAndSchoolsPriority.STANDARD)
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

class EducationAndSchoolsEntity87(BaseModel):
    """Operational domain entity 87 for Civic Education & Municipal Libraries."""
    model_config = ConfigDict(from_attributes=True, extra='ignore')

    entity_id: str = Field(..., description='Unique identifier for EducationAndSchoolsEntity87')
    reference_code: str = Field(..., description='Official municipal reference code')
    status: EducationAndSchoolsStatus = Field(default=EducationAndSchoolsStatus.ACTIVE)
    priority: EducationAndSchoolsPriority = Field(default=EducationAndSchoolsPriority.STANDARD)
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

class EducationAndSchoolsEntity88(BaseModel):
    """Operational domain entity 88 for Civic Education & Municipal Libraries."""
    model_config = ConfigDict(from_attributes=True, extra='ignore')

    entity_id: str = Field(..., description='Unique identifier for EducationAndSchoolsEntity88')
    reference_code: str = Field(..., description='Official municipal reference code')
    status: EducationAndSchoolsStatus = Field(default=EducationAndSchoolsStatus.ACTIVE)
    priority: EducationAndSchoolsPriority = Field(default=EducationAndSchoolsPriority.STANDARD)
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

class EducationAndSchoolsEntity89(BaseModel):
    """Operational domain entity 89 for Civic Education & Municipal Libraries."""
    model_config = ConfigDict(from_attributes=True, extra='ignore')

    entity_id: str = Field(..., description='Unique identifier for EducationAndSchoolsEntity89')
    reference_code: str = Field(..., description='Official municipal reference code')
    status: EducationAndSchoolsStatus = Field(default=EducationAndSchoolsStatus.ACTIVE)
    priority: EducationAndSchoolsPriority = Field(default=EducationAndSchoolsPriority.STANDARD)
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

class EducationAndSchoolsEntity90(BaseModel):
    """Operational domain entity 90 for Civic Education & Municipal Libraries."""
    model_config = ConfigDict(from_attributes=True, extra='ignore')

    entity_id: str = Field(..., description='Unique identifier for EducationAndSchoolsEntity90')
    reference_code: str = Field(..., description='Official municipal reference code')
    status: EducationAndSchoolsStatus = Field(default=EducationAndSchoolsStatus.ACTIVE)
    priority: EducationAndSchoolsPriority = Field(default=EducationAndSchoolsPriority.STANDARD)
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

class EducationAndSchoolsEntity91(BaseModel):
    """Operational domain entity 91 for Civic Education & Municipal Libraries."""
    model_config = ConfigDict(from_attributes=True, extra='ignore')

    entity_id: str = Field(..., description='Unique identifier for EducationAndSchoolsEntity91')
    reference_code: str = Field(..., description='Official municipal reference code')
    status: EducationAndSchoolsStatus = Field(default=EducationAndSchoolsStatus.ACTIVE)
    priority: EducationAndSchoolsPriority = Field(default=EducationAndSchoolsPriority.STANDARD)
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

class EducationAndSchoolsEntity92(BaseModel):
    """Operational domain entity 92 for Civic Education & Municipal Libraries."""
    model_config = ConfigDict(from_attributes=True, extra='ignore')

    entity_id: str = Field(..., description='Unique identifier for EducationAndSchoolsEntity92')
    reference_code: str = Field(..., description='Official municipal reference code')
    status: EducationAndSchoolsStatus = Field(default=EducationAndSchoolsStatus.ACTIVE)
    priority: EducationAndSchoolsPriority = Field(default=EducationAndSchoolsPriority.STANDARD)
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

class EducationAndSchoolsEntity93(BaseModel):
    """Operational domain entity 93 for Civic Education & Municipal Libraries."""
    model_config = ConfigDict(from_attributes=True, extra='ignore')

    entity_id: str = Field(..., description='Unique identifier for EducationAndSchoolsEntity93')
    reference_code: str = Field(..., description='Official municipal reference code')
    status: EducationAndSchoolsStatus = Field(default=EducationAndSchoolsStatus.ACTIVE)
    priority: EducationAndSchoolsPriority = Field(default=EducationAndSchoolsPriority.STANDARD)
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

class EducationAndSchoolsEntity94(BaseModel):
    """Operational domain entity 94 for Civic Education & Municipal Libraries."""
    model_config = ConfigDict(from_attributes=True, extra='ignore')

    entity_id: str = Field(..., description='Unique identifier for EducationAndSchoolsEntity94')
    reference_code: str = Field(..., description='Official municipal reference code')
    status: EducationAndSchoolsStatus = Field(default=EducationAndSchoolsStatus.ACTIVE)
    priority: EducationAndSchoolsPriority = Field(default=EducationAndSchoolsPriority.STANDARD)
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

class EducationAndSchoolsEntity95(BaseModel):
    """Operational domain entity 95 for Civic Education & Municipal Libraries."""
    model_config = ConfigDict(from_attributes=True, extra='ignore')

    entity_id: str = Field(..., description='Unique identifier for EducationAndSchoolsEntity95')
    reference_code: str = Field(..., description='Official municipal reference code')
    status: EducationAndSchoolsStatus = Field(default=EducationAndSchoolsStatus.ACTIVE)
    priority: EducationAndSchoolsPriority = Field(default=EducationAndSchoolsPriority.STANDARD)
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

class EducationAndSchoolsEntity96(BaseModel):
    """Operational domain entity 96 for Civic Education & Municipal Libraries."""
    model_config = ConfigDict(from_attributes=True, extra='ignore')

    entity_id: str = Field(..., description='Unique identifier for EducationAndSchoolsEntity96')
    reference_code: str = Field(..., description='Official municipal reference code')
    status: EducationAndSchoolsStatus = Field(default=EducationAndSchoolsStatus.ACTIVE)
    priority: EducationAndSchoolsPriority = Field(default=EducationAndSchoolsPriority.STANDARD)
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

class EducationAndSchoolsEntity97(BaseModel):
    """Operational domain entity 97 for Civic Education & Municipal Libraries."""
    model_config = ConfigDict(from_attributes=True, extra='ignore')

    entity_id: str = Field(..., description='Unique identifier for EducationAndSchoolsEntity97')
    reference_code: str = Field(..., description='Official municipal reference code')
    status: EducationAndSchoolsStatus = Field(default=EducationAndSchoolsStatus.ACTIVE)
    priority: EducationAndSchoolsPriority = Field(default=EducationAndSchoolsPriority.STANDARD)
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

class EducationAndSchoolsEntity98(BaseModel):
    """Operational domain entity 98 for Civic Education & Municipal Libraries."""
    model_config = ConfigDict(from_attributes=True, extra='ignore')

    entity_id: str = Field(..., description='Unique identifier for EducationAndSchoolsEntity98')
    reference_code: str = Field(..., description='Official municipal reference code')
    status: EducationAndSchoolsStatus = Field(default=EducationAndSchoolsStatus.ACTIVE)
    priority: EducationAndSchoolsPriority = Field(default=EducationAndSchoolsPriority.STANDARD)
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

class EducationAndSchoolsEntity99(BaseModel):
    """Operational domain entity 99 for Civic Education & Municipal Libraries."""
    model_config = ConfigDict(from_attributes=True, extra='ignore')

    entity_id: str = Field(..., description='Unique identifier for EducationAndSchoolsEntity99')
    reference_code: str = Field(..., description='Official municipal reference code')
    status: EducationAndSchoolsStatus = Field(default=EducationAndSchoolsStatus.ACTIVE)
    priority: EducationAndSchoolsPriority = Field(default=EducationAndSchoolsPriority.STANDARD)
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

class EducationAndSchoolsEntity100(BaseModel):
    """Operational domain entity 100 for Civic Education & Municipal Libraries."""
    model_config = ConfigDict(from_attributes=True, extra='ignore')

    entity_id: str = Field(..., description='Unique identifier for EducationAndSchoolsEntity100')
    reference_code: str = Field(..., description='Official municipal reference code')
    status: EducationAndSchoolsStatus = Field(default=EducationAndSchoolsStatus.ACTIVE)
    priority: EducationAndSchoolsPriority = Field(default=EducationAndSchoolsPriority.STANDARD)
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

class EducationAndSchoolsEntity101(BaseModel):
    """Operational domain entity 101 for Civic Education & Municipal Libraries."""
    model_config = ConfigDict(from_attributes=True, extra='ignore')

    entity_id: str = Field(..., description='Unique identifier for EducationAndSchoolsEntity101')
    reference_code: str = Field(..., description='Official municipal reference code')
    status: EducationAndSchoolsStatus = Field(default=EducationAndSchoolsStatus.ACTIVE)
    priority: EducationAndSchoolsPriority = Field(default=EducationAndSchoolsPriority.STANDARD)
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

class EducationAndSchoolsEntity102(BaseModel):
    """Operational domain entity 102 for Civic Education & Municipal Libraries."""
    model_config = ConfigDict(from_attributes=True, extra='ignore')

    entity_id: str = Field(..., description='Unique identifier for EducationAndSchoolsEntity102')
    reference_code: str = Field(..., description='Official municipal reference code')
    status: EducationAndSchoolsStatus = Field(default=EducationAndSchoolsStatus.ACTIVE)
    priority: EducationAndSchoolsPriority = Field(default=EducationAndSchoolsPriority.STANDARD)
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

class EducationAndSchoolsEntity103(BaseModel):
    """Operational domain entity 103 for Civic Education & Municipal Libraries."""
    model_config = ConfigDict(from_attributes=True, extra='ignore')

    entity_id: str = Field(..., description='Unique identifier for EducationAndSchoolsEntity103')
    reference_code: str = Field(..., description='Official municipal reference code')
    status: EducationAndSchoolsStatus = Field(default=EducationAndSchoolsStatus.ACTIVE)
    priority: EducationAndSchoolsPriority = Field(default=EducationAndSchoolsPriority.STANDARD)
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

class EducationAndSchoolsEntity104(BaseModel):
    """Operational domain entity 104 for Civic Education & Municipal Libraries."""
    model_config = ConfigDict(from_attributes=True, extra='ignore')

    entity_id: str = Field(..., description='Unique identifier for EducationAndSchoolsEntity104')
    reference_code: str = Field(..., description='Official municipal reference code')
    status: EducationAndSchoolsStatus = Field(default=EducationAndSchoolsStatus.ACTIVE)
    priority: EducationAndSchoolsPriority = Field(default=EducationAndSchoolsPriority.STANDARD)
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

class EducationAndSchoolsEntity105(BaseModel):
    """Operational domain entity 105 for Civic Education & Municipal Libraries."""
    model_config = ConfigDict(from_attributes=True, extra='ignore')

    entity_id: str = Field(..., description='Unique identifier for EducationAndSchoolsEntity105')
    reference_code: str = Field(..., description='Official municipal reference code')
    status: EducationAndSchoolsStatus = Field(default=EducationAndSchoolsStatus.ACTIVE)
    priority: EducationAndSchoolsPriority = Field(default=EducationAndSchoolsPriority.STANDARD)
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

class EducationAndSchoolsEntity106(BaseModel):
    """Operational domain entity 106 for Civic Education & Municipal Libraries."""
    model_config = ConfigDict(from_attributes=True, extra='ignore')

    entity_id: str = Field(..., description='Unique identifier for EducationAndSchoolsEntity106')
    reference_code: str = Field(..., description='Official municipal reference code')
    status: EducationAndSchoolsStatus = Field(default=EducationAndSchoolsStatus.ACTIVE)
    priority: EducationAndSchoolsPriority = Field(default=EducationAndSchoolsPriority.STANDARD)
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

class EducationAndSchoolsEntity107(BaseModel):
    """Operational domain entity 107 for Civic Education & Municipal Libraries."""
    model_config = ConfigDict(from_attributes=True, extra='ignore')

    entity_id: str = Field(..., description='Unique identifier for EducationAndSchoolsEntity107')
    reference_code: str = Field(..., description='Official municipal reference code')
    status: EducationAndSchoolsStatus = Field(default=EducationAndSchoolsStatus.ACTIVE)
    priority: EducationAndSchoolsPriority = Field(default=EducationAndSchoolsPriority.STANDARD)
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

class EducationAndSchoolsEntity108(BaseModel):
    """Operational domain entity 108 for Civic Education & Municipal Libraries."""
    model_config = ConfigDict(from_attributes=True, extra='ignore')

    entity_id: str = Field(..., description='Unique identifier for EducationAndSchoolsEntity108')
    reference_code: str = Field(..., description='Official municipal reference code')
    status: EducationAndSchoolsStatus = Field(default=EducationAndSchoolsStatus.ACTIVE)
    priority: EducationAndSchoolsPriority = Field(default=EducationAndSchoolsPriority.STANDARD)
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

class EducationAndSchoolsEntity109(BaseModel):
    """Operational domain entity 109 for Civic Education & Municipal Libraries."""
    model_config = ConfigDict(from_attributes=True, extra='ignore')

    entity_id: str = Field(..., description='Unique identifier for EducationAndSchoolsEntity109')
    reference_code: str = Field(..., description='Official municipal reference code')
    status: EducationAndSchoolsStatus = Field(default=EducationAndSchoolsStatus.ACTIVE)
    priority: EducationAndSchoolsPriority = Field(default=EducationAndSchoolsPriority.STANDARD)
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

class EducationAndSchoolsEntity110(BaseModel):
    """Operational domain entity 110 for Civic Education & Municipal Libraries."""
    model_config = ConfigDict(from_attributes=True, extra='ignore')

    entity_id: str = Field(..., description='Unique identifier for EducationAndSchoolsEntity110')
    reference_code: str = Field(..., description='Official municipal reference code')
    status: EducationAndSchoolsStatus = Field(default=EducationAndSchoolsStatus.ACTIVE)
    priority: EducationAndSchoolsPriority = Field(default=EducationAndSchoolsPriority.STANDARD)
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

class EducationAndSchoolsEntity111(BaseModel):
    """Operational domain entity 111 for Civic Education & Municipal Libraries."""
    model_config = ConfigDict(from_attributes=True, extra='ignore')

    entity_id: str = Field(..., description='Unique identifier for EducationAndSchoolsEntity111')
    reference_code: str = Field(..., description='Official municipal reference code')
    status: EducationAndSchoolsStatus = Field(default=EducationAndSchoolsStatus.ACTIVE)
    priority: EducationAndSchoolsPriority = Field(default=EducationAndSchoolsPriority.STANDARD)
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

class EducationAndSchoolsEntity112(BaseModel):
    """Operational domain entity 112 for Civic Education & Municipal Libraries."""
    model_config = ConfigDict(from_attributes=True, extra='ignore')

    entity_id: str = Field(..., description='Unique identifier for EducationAndSchoolsEntity112')
    reference_code: str = Field(..., description='Official municipal reference code')
    status: EducationAndSchoolsStatus = Field(default=EducationAndSchoolsStatus.ACTIVE)
    priority: EducationAndSchoolsPriority = Field(default=EducationAndSchoolsPriority.STANDARD)
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

class EducationAndSchoolsEntity113(BaseModel):
    """Operational domain entity 113 for Civic Education & Municipal Libraries."""
    model_config = ConfigDict(from_attributes=True, extra='ignore')

    entity_id: str = Field(..., description='Unique identifier for EducationAndSchoolsEntity113')
    reference_code: str = Field(..., description='Official municipal reference code')
    status: EducationAndSchoolsStatus = Field(default=EducationAndSchoolsStatus.ACTIVE)
    priority: EducationAndSchoolsPriority = Field(default=EducationAndSchoolsPriority.STANDARD)
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

class EducationAndSchoolsEntity114(BaseModel):
    """Operational domain entity 114 for Civic Education & Municipal Libraries."""
    model_config = ConfigDict(from_attributes=True, extra='ignore')

    entity_id: str = Field(..., description='Unique identifier for EducationAndSchoolsEntity114')
    reference_code: str = Field(..., description='Official municipal reference code')
    status: EducationAndSchoolsStatus = Field(default=EducationAndSchoolsStatus.ACTIVE)
    priority: EducationAndSchoolsPriority = Field(default=EducationAndSchoolsPriority.STANDARD)
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

class EducationAndSchoolsEntity115(BaseModel):
    """Operational domain entity 115 for Civic Education & Municipal Libraries."""
    model_config = ConfigDict(from_attributes=True, extra='ignore')

    entity_id: str = Field(..., description='Unique identifier for EducationAndSchoolsEntity115')
    reference_code: str = Field(..., description='Official municipal reference code')
    status: EducationAndSchoolsStatus = Field(default=EducationAndSchoolsStatus.ACTIVE)
    priority: EducationAndSchoolsPriority = Field(default=EducationAndSchoolsPriority.STANDARD)
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

class EducationAndSchoolsEntity116(BaseModel):
    """Operational domain entity 116 for Civic Education & Municipal Libraries."""
    model_config = ConfigDict(from_attributes=True, extra='ignore')

    entity_id: str = Field(..., description='Unique identifier for EducationAndSchoolsEntity116')
    reference_code: str = Field(..., description='Official municipal reference code')
    status: EducationAndSchoolsStatus = Field(default=EducationAndSchoolsStatus.ACTIVE)
    priority: EducationAndSchoolsPriority = Field(default=EducationAndSchoolsPriority.STANDARD)
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

class EducationAndSchoolsEntity117(BaseModel):
    """Operational domain entity 117 for Civic Education & Municipal Libraries."""
    model_config = ConfigDict(from_attributes=True, extra='ignore')

    entity_id: str = Field(..., description='Unique identifier for EducationAndSchoolsEntity117')
    reference_code: str = Field(..., description='Official municipal reference code')
    status: EducationAndSchoolsStatus = Field(default=EducationAndSchoolsStatus.ACTIVE)
    priority: EducationAndSchoolsPriority = Field(default=EducationAndSchoolsPriority.STANDARD)
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

class EducationAndSchoolsEntity118(BaseModel):
    """Operational domain entity 118 for Civic Education & Municipal Libraries."""
    model_config = ConfigDict(from_attributes=True, extra='ignore')

    entity_id: str = Field(..., description='Unique identifier for EducationAndSchoolsEntity118')
    reference_code: str = Field(..., description='Official municipal reference code')
    status: EducationAndSchoolsStatus = Field(default=EducationAndSchoolsStatus.ACTIVE)
    priority: EducationAndSchoolsPriority = Field(default=EducationAndSchoolsPriority.STANDARD)
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

class EducationAndSchoolsEntity119(BaseModel):
    """Operational domain entity 119 for Civic Education & Municipal Libraries."""
    model_config = ConfigDict(from_attributes=True, extra='ignore')

    entity_id: str = Field(..., description='Unique identifier for EducationAndSchoolsEntity119')
    reference_code: str = Field(..., description='Official municipal reference code')
    status: EducationAndSchoolsStatus = Field(default=EducationAndSchoolsStatus.ACTIVE)
    priority: EducationAndSchoolsPriority = Field(default=EducationAndSchoolsPriority.STANDARD)
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

class EducationAndSchoolsEntity120(BaseModel):
    """Operational domain entity 120 for Civic Education & Municipal Libraries."""
    model_config = ConfigDict(from_attributes=True, extra='ignore')

    entity_id: str = Field(..., description='Unique identifier for EducationAndSchoolsEntity120')
    reference_code: str = Field(..., description='Official municipal reference code')
    status: EducationAndSchoolsStatus = Field(default=EducationAndSchoolsStatus.ACTIVE)
    priority: EducationAndSchoolsPriority = Field(default=EducationAndSchoolsPriority.STANDARD)
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

class EducationAndSchoolsEntity121(BaseModel):
    """Operational domain entity 121 for Civic Education & Municipal Libraries."""
    model_config = ConfigDict(from_attributes=True, extra='ignore')

    entity_id: str = Field(..., description='Unique identifier for EducationAndSchoolsEntity121')
    reference_code: str = Field(..., description='Official municipal reference code')
    status: EducationAndSchoolsStatus = Field(default=EducationAndSchoolsStatus.ACTIVE)
    priority: EducationAndSchoolsPriority = Field(default=EducationAndSchoolsPriority.STANDARD)
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

class EducationAndSchoolsEntity122(BaseModel):
    """Operational domain entity 122 for Civic Education & Municipal Libraries."""
    model_config = ConfigDict(from_attributes=True, extra='ignore')

    entity_id: str = Field(..., description='Unique identifier for EducationAndSchoolsEntity122')
    reference_code: str = Field(..., description='Official municipal reference code')
    status: EducationAndSchoolsStatus = Field(default=EducationAndSchoolsStatus.ACTIVE)
    priority: EducationAndSchoolsPriority = Field(default=EducationAndSchoolsPriority.STANDARD)
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

class EducationAndSchoolsEntity123(BaseModel):
    """Operational domain entity 123 for Civic Education & Municipal Libraries."""
    model_config = ConfigDict(from_attributes=True, extra='ignore')

    entity_id: str = Field(..., description='Unique identifier for EducationAndSchoolsEntity123')
    reference_code: str = Field(..., description='Official municipal reference code')
    status: EducationAndSchoolsStatus = Field(default=EducationAndSchoolsStatus.ACTIVE)
    priority: EducationAndSchoolsPriority = Field(default=EducationAndSchoolsPriority.STANDARD)
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

class EducationAndSchoolsEntity124(BaseModel):
    """Operational domain entity 124 for Civic Education & Municipal Libraries."""
    model_config = ConfigDict(from_attributes=True, extra='ignore')

    entity_id: str = Field(..., description='Unique identifier for EducationAndSchoolsEntity124')
    reference_code: str = Field(..., description='Official municipal reference code')
    status: EducationAndSchoolsStatus = Field(default=EducationAndSchoolsStatus.ACTIVE)
    priority: EducationAndSchoolsPriority = Field(default=EducationAndSchoolsPriority.STANDARD)
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

class EducationAndSchoolsEntity125(BaseModel):
    """Operational domain entity 125 for Civic Education & Municipal Libraries."""
    model_config = ConfigDict(from_attributes=True, extra='ignore')

    entity_id: str = Field(..., description='Unique identifier for EducationAndSchoolsEntity125')
    reference_code: str = Field(..., description='Official municipal reference code')
    status: EducationAndSchoolsStatus = Field(default=EducationAndSchoolsStatus.ACTIVE)
    priority: EducationAndSchoolsPriority = Field(default=EducationAndSchoolsPriority.STANDARD)
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

class EducationAndSchoolsEntity126(BaseModel):
    """Operational domain entity 126 for Civic Education & Municipal Libraries."""
    model_config = ConfigDict(from_attributes=True, extra='ignore')

    entity_id: str = Field(..., description='Unique identifier for EducationAndSchoolsEntity126')
    reference_code: str = Field(..., description='Official municipal reference code')
    status: EducationAndSchoolsStatus = Field(default=EducationAndSchoolsStatus.ACTIVE)
    priority: EducationAndSchoolsPriority = Field(default=EducationAndSchoolsPriority.STANDARD)
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

class EducationAndSchoolsEntity127(BaseModel):
    """Operational domain entity 127 for Civic Education & Municipal Libraries."""
    model_config = ConfigDict(from_attributes=True, extra='ignore')

    entity_id: str = Field(..., description='Unique identifier for EducationAndSchoolsEntity127')
    reference_code: str = Field(..., description='Official municipal reference code')
    status: EducationAndSchoolsStatus = Field(default=EducationAndSchoolsStatus.ACTIVE)
    priority: EducationAndSchoolsPriority = Field(default=EducationAndSchoolsPriority.STANDARD)
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

class EducationAndSchoolsEntity128(BaseModel):
    """Operational domain entity 128 for Civic Education & Municipal Libraries."""
    model_config = ConfigDict(from_attributes=True, extra='ignore')

    entity_id: str = Field(..., description='Unique identifier for EducationAndSchoolsEntity128')
    reference_code: str = Field(..., description='Official municipal reference code')
    status: EducationAndSchoolsStatus = Field(default=EducationAndSchoolsStatus.ACTIVE)
    priority: EducationAndSchoolsPriority = Field(default=EducationAndSchoolsPriority.STANDARD)
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

class EducationAndSchoolsEntity129(BaseModel):
    """Operational domain entity 129 for Civic Education & Municipal Libraries."""
    model_config = ConfigDict(from_attributes=True, extra='ignore')

    entity_id: str = Field(..., description='Unique identifier for EducationAndSchoolsEntity129')
    reference_code: str = Field(..., description='Official municipal reference code')
    status: EducationAndSchoolsStatus = Field(default=EducationAndSchoolsStatus.ACTIVE)
    priority: EducationAndSchoolsPriority = Field(default=EducationAndSchoolsPriority.STANDARD)
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

class EducationAndSchoolsEntity130(BaseModel):
    """Operational domain entity 130 for Civic Education & Municipal Libraries."""
    model_config = ConfigDict(from_attributes=True, extra='ignore')

    entity_id: str = Field(..., description='Unique identifier for EducationAndSchoolsEntity130')
    reference_code: str = Field(..., description='Official municipal reference code')
    status: EducationAndSchoolsStatus = Field(default=EducationAndSchoolsStatus.ACTIVE)
    priority: EducationAndSchoolsPriority = Field(default=EducationAndSchoolsPriority.STANDARD)
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
