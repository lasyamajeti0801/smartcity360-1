"""
SmartCity360 - Complaint Management Pydantic Schemas (Pydantic v2)
"""

from datetime import datetime
from typing import List, Optional
from pydantic import BaseModel, ConfigDict, Field

class ComplaintCategoryResponse(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: str
    code: str
    name: str
    default_department_code: str
    default_sla_hours: int
    icon_name: str
    description: Optional[str] = None

class ComplaintCommentResponse(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: str
    comment: str
    is_internal: bool
    created_at: datetime
    author_id: Optional[str] = None

class ComplaintStatusHistoryResponse(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: str
    from_status: str
    to_status: str
    reason: Optional[str] = None
    created_at: datetime

class ComplaintResponse(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: str
    ticket_number: str
    citizen_id: str
    category_id: str
    department_id: str
    assigned_staff_id: Optional[str] = None
    title: str
    description: str
    priority: str
    status: str
    latitude: float
    longitude: float
    location_address: str
    ward_number: Optional[int] = None
    sla_due_at: Optional[datetime] = None
    is_escalated: bool
    escalated_at: Optional[datetime] = None
    resolved_at: Optional[datetime] = None
    citizen_rating: Optional[int] = None
    citizen_feedback: Optional[str] = None
    evidence_image_url: Optional[str] = None
    resolution_image_url: Optional[str] = None
    created_at: datetime
    updated_at: datetime
    comments: List[ComplaintCommentResponse] = []
    status_history: List[ComplaintStatusHistoryResponse] = []

class ComplaintCreateRequest(BaseModel):
    category_id: str
    title: str = Field(min_length=5, max_length=255)
    description: str = Field(min_length=10)
    latitude: float = Field(ge=-90.0, le=90.0)
    longitude: float = Field(ge=-180.0, le=180.0)
    location_address: str = Field(min_length=3, max_length=255)
    ward_number: Optional[int] = None
    evidence_image_url: Optional[str] = None

class ComplaintStatusUpdateRequest(BaseModel):
    status: str
    reason: Optional[str] = None
    assigned_staff_id: Optional[str] = None
    resolution_image_url: Optional[str] = None

class ComplaintCommentCreateRequest(BaseModel):
    comment: str = Field(min_length=1)
    is_internal: bool = False

class CitizenFeedbackRequest(BaseModel):
    rating: int = Field(ge=1, le=5)
    feedback: Optional[str] = None
