"""
SmartCity360 - Emergency Services & Public Facility Endpoints
"""

from datetime import datetime, timezone
import uuid
from typing import List, Optional
from fastapi import APIRouter, Depends, Query, status
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
from sqlalchemy.orm import selectinload
from backend.app.core.database import get_db
from backend.app.models.emergency import EmergencyIncident, EmergencyResponseTeam, Facility
from backend.app.schemas.emergency import (
    EmergencyIncidentCreateRequest,
    EmergencyIncidentResponse,
    EmergencyResponseTeamResponse,
    FacilityResponse
)

router = APIRouter(prefix="/emergency", tags=["Emergency & Public Safety"])

@router.get("/incidents", response_model=List[EmergencyIncidentResponse], summary="List emergency incidents")
async def list_emergency_incidents(
    status: Optional[str] = Query(None),
    severity: Optional[str] = Query(None),
    db: AsyncSession = Depends(get_db)
):
    query = (
        select(EmergencyIncident)
        .where(EmergencyIncident.is_deleted == False)
        .options(selectinload(EmergencyIncident.dispatches))
    )
    if status:
        query = query.where(EmergencyIncident.status == status)
    if severity:
        query = query.where(EmergencyIncident.severity == severity)
    query = query.order_by(EmergencyIncident.created_at.desc())
    res = await db.execute(query)
    incidents = res.scalars().all()
    return [EmergencyIncidentResponse.model_validate(i) for i in incidents]

@router.post("/incidents", response_model=EmergencyIncidentResponse, status_code=status.HTTP_201_CREATED, summary="Create emergency incident")
async def create_emergency_incident(
    req: EmergencyIncidentCreateRequest,
    db: AsyncSession = Depends(get_db)
):
    date_str = datetime.now(timezone.utc).strftime("%Y%m%d")
    rand_suffix = uuid.uuid4().hex[:6].upper()
    inc_num = f"EMG-{date_str}-{rand_suffix}"

    inc = EmergencyIncident(
        incident_number=inc_num,
        incident_type=req.incident_type,
        severity=req.severity,
        status="REPORTED",
        title=req.title,
        description=req.description,
        latitude=req.latitude,
        longitude=req.longitude,
        location_address=req.location_address,
        caller_name=req.caller_name,
        caller_phone=req.caller_phone
    )
    db.add(inc)
    await db.flush()

    q = select(EmergencyIncident).where(EmergencyIncident.id == inc.id).options(selectinload(EmergencyIncident.dispatches))
    res = await db.execute(q)
    return EmergencyIncidentResponse.model_validate(res.scalars().first())

@router.get("/teams", response_model=List[EmergencyResponseTeamResponse], summary="List emergency squads & response teams")
async def list_response_teams(
    is_available: Optional[bool] = Query(None),
    service_type: Optional[str] = Query(None),
    db: AsyncSession = Depends(get_db)
):
    query = select(EmergencyResponseTeam).where(EmergencyResponseTeam.is_deleted == False)
    if is_available is not None:
        query = query.where(EmergencyResponseTeam.is_available == is_available)
    if service_type:
        query = query.where(EmergencyResponseTeam.service_type == service_type)
    res = await db.execute(query)
    teams = res.scalars().all()
    return [EmergencyResponseTeamResponse.model_validate(t) for t in teams]

@router.get("/facilities", response_model=List[FacilityResponse], summary="List municipal facilities (hospitals, fire, police)")
async def list_facilities(
    category: Optional[str] = Query(None),
    db: AsyncSession = Depends(get_db)
):
    query = select(Facility).where(Facility.is_deleted == False)
    if category:
        query = query.where(Facility.category == category)
    query = query.order_by(Facility.name.asc())
    res = await db.execute(query)
    facilities = res.scalars().all()
    return [FacilityResponse.model_validate(f) for f in facilities]
