"""
SmartCity360 - Emergency Services & Public Facility Endpoints
"""

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
    FacilityResponse,
    EmergencyDispatchCreateRequest,
    EmergencyResolveRequest
)
from backend.app.services.emergency_service import EmergencyService

router = APIRouter(prefix="/emergency", tags=["Emergency & Public Safety"])

@router.get("/incidents", response_model=List[EmergencyIncidentResponse], summary="List emergency incidents with filter")
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

@router.get("/incidents/{incident_id}", response_model=EmergencyIncidentResponse, summary="Get emergency incident by ID")
async def get_emergency_incident(incident_id: str, db: AsyncSession = Depends(get_db)):
    service = EmergencyService(db)
    inc = await service.get_incident(incident_id)
    return EmergencyIncidentResponse.model_validate(inc)

@router.post("/incidents", response_model=EmergencyIncidentResponse, status_code=status.HTTP_201_CREATED, summary="Create emergency incident")
async def create_emergency_incident(
    req: EmergencyIncidentCreateRequest,
    db: AsyncSession = Depends(get_db)
):
    service = EmergencyService(db)
    inc = await service.create_incident(req)
    return EmergencyIncidentResponse.model_validate(inc)

@router.post("/incidents/{incident_id}/dispatch", response_model=EmergencyIncidentResponse, summary="Dispatch response unit squad")
async def dispatch_response_team(
    incident_id: str,
    req: EmergencyDispatchCreateRequest,
    db: AsyncSession = Depends(get_db)
):
    service = EmergencyService(db)
    inc = await service.dispatch_team(incident_id, req)
    return EmergencyIncidentResponse.model_validate(inc)

@router.post("/incidents/{incident_id}/arrive", response_model=EmergencyIncidentResponse, summary="Mark squad arrival on scene")
async def mark_team_arrival(
    incident_id: str,
    team_id: str = Query(...),
    db: AsyncSession = Depends(get_db)
):
    service = EmergencyService(db)
    inc = await service.mark_arrived(incident_id, team_id)
    return EmergencyIncidentResponse.model_validate(inc)

@router.post("/incidents/{incident_id}/contain", response_model=EmergencyIncidentResponse, summary="Mark incident contained")
async def mark_incident_contained(
    incident_id: str,
    db: AsyncSession = Depends(get_db)
):
    service = EmergencyService(db)
    inc = await service.mark_contained(incident_id)
    return EmergencyIncidentResponse.model_validate(inc)

@router.post("/incidents/{incident_id}/resolve", response_model=EmergencyIncidentResponse, summary="Resolve incident and release units")
async def resolve_emergency_incident(
    incident_id: str,
    req: EmergencyResolveRequest,
    db: AsyncSession = Depends(get_db)
):
    service = EmergencyService(db)
    inc = await service.resolve_incident(incident_id, req)
    return EmergencyIncidentResponse.model_validate(inc)

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
