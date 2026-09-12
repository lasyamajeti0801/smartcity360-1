"""
SmartCity360 - Authentication & User Pydantic Schemas (Pydantic v2)
"""

from datetime import datetime
from typing import List, Optional
from pydantic import BaseModel, ConfigDict, Field

class PermissionResponse(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    code: str
    name: str
    module: str
    description: Optional[str] = None

class RoleResponse(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: str
    name: str
    description: str
    permissions: List[PermissionResponse] = []

class CitizenProfileResponse(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    address_line: str
    ward_number: Optional[int] = None
    zone_name: Optional[str] = None
    preferred_language: str
    emergency_contact: Optional[str] = None

class DepartmentStaffResponse(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    department_id: str
    employee_badge: str
    designation: str
    is_field_responder: bool
    is_available: bool

class UserResponse(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: str
    email: str
    full_name: str
    phone_number: Optional[str] = None
    is_active: bool
    is_verified: bool
    roles: List[RoleResponse] = []
    citizen_profile: Optional[CitizenProfileResponse] = None
    staff_profile: Optional[DepartmentStaffResponse] = None
    created_at: datetime

class CitizenRegisterRequest(BaseModel):
    email: str = Field(min_length=3, max_length=255)
    password: str = Field(min_length=8, max_length=128)
    full_name: str = Field(min_length=2, max_length=255)
    phone_number: Optional[str] = Field(None, max_length=32)
    address_line: str = Field(min_length=5, max_length=255)
    ward_number: Optional[int] = None
    preferred_language: str = Field(default="en", max_length=10)

class LoginRequest(BaseModel):
    email: str
    password: str

class TokenResponse(BaseModel):
    access_token: str
    token_type: str = "bearer"
    expires_in_seconds: int
    user: UserResponse
