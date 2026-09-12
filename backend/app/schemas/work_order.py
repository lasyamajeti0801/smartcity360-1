"""
SmartCity360 - Work Order Pydantic Schemas (Pydantic v2)
"""

from datetime import datetime
from typing import List, Optional
from pydantic import BaseModel, ConfigDict, Field

class WorkOrderTaskResponse(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: str
    title: str
    is_completed: bool
    order_index: int
    completed_at: Optional[datetime] = None

class WorkOrderEvidenceResponse(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: str
    evidence_type: str
    file_url: str
    caption: Optional[str] = None
    created_at: datetime

class WorkOrderResponse(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: str
    order_number: str
    complaint_id: Optional[str] = None
    department_id: str
    assigned_technician_id: Optional[str] = None
    title: str
    description: str
    priority: str
    status: str
    completion_percentage: int
    field_notes: Optional[str] = None
    latitude: float
    longitude: float
    location_address: str
    due_date: Optional[datetime] = None
    completed_at: Optional[datetime] = None
    verified_at: Optional[datetime] = None
    created_at: datetime
    tasks: List[WorkOrderTaskResponse] = []
    evidence: List[WorkOrderEvidenceResponse] = []

class WorkOrderCreateRequest(BaseModel):
    complaint_id: Optional[str] = None
    department_id: str
    assigned_technician_id: Optional[str] = None
    title: str = Field(min_length=5, max_length=255)
    description: str
    priority: str = "MEDIUM"
    latitude: float
    longitude: float
    location_address: str
    due_date: Optional[datetime] = None
    task_titles: List[str] = []

class WorkOrderStatusUpdateRequest(BaseModel):
    status: str
    completion_percentage: Optional[int] = Field(None, ge=0, le=100)
    field_notes: Optional[str] = None

class WorkOrderEvidenceCreateRequest(BaseModel):
    evidence_type: str = Field(default="PHOTO", pattern="^(BEFORE|AFTER|RECEIPT|PERMIT|INSPECTION|PHOTO)$")
    file_url: str = Field(min_length=5, max_length=512)
    caption: Optional[str] = Field(None, max_length=255)

class WorkOrderAssignRequest(BaseModel):
    assigned_technician_id: str
    supervisor_id: Optional[str] = None

class WorkOrderVerifyRequest(BaseModel):
    is_approved: bool
    notes: Optional[str] = None

