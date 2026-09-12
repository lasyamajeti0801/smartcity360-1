"""
SmartCity360 - Department & Service Catalog Pydantic Schemas (Pydantic v2)
"""

from typing import List, Optional
from pydantic import BaseModel, ConfigDict, Field

class ServiceCategoryResponse(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: str
    code: str
    name: str
    description: Optional[str] = None
    icon_name: str
    display_order: int

class MunicipalServiceResponse(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: str
    department_id: str
    category_id: str
    code: str
    title: str
    description: str
    eligibility_criteria: str
    fee_amount: float
    sla_turnaround_days: int
    required_documents: str
    is_online_submission: bool

class DepartmentResponse(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: str
    code: str
    name: str
    description: str
    contact_email: str
    contact_phone: str
    head_official: Optional[str] = None
    is_active: bool
    services: List[MunicipalServiceResponse] = []

class DepartmentCreateRequest(BaseModel):
    code: str = Field(min_length=2, max_length=32)
    name: str = Field(min_length=3, max_length=128)
    description: str
    contact_email: str
    contact_phone: str
    head_official: Optional[str] = None
