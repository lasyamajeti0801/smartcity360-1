"""
SmartCity360 - Emergency Services & 911 Operations Command Business Service
Manages public safety incidents, rapid response unit dispatches, on-scene coordination,
and facility proximity queries.
"""

from datetime import datetime, timezone
import uuid
from typing import List, Optional
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import selectinload
from backend.app.core.exceptions import (
    EntityNotFoundException,
    InvalidStateTransitionException,
    SmartCityException
)
from backend.app.models.emergency import (
    EmergencyIncident,
    EmergencyResponseTeam,
    EmergencyDispatch,
    Facility,
    EMERGENCY_STATUS_REPORTED,
    EMERGENCY_STATUS_DISPATCHED,
    EMERGENCY_STATUS_RESPONDING,
    EMERGENCY_STATUS_CONTAINED,
    EMERGENCY_STATUS_RESOLVED,
    EMERGENCY_STATUS_CLOSED
)
from backend.app.schemas.emergency import (
    EmergencyIncidentCreateRequest,
    EmergencyDispatchCreateRequest,
    EmergencyResolveRequest
)

class EmergencyService:
    def __init__(self, session: AsyncSession):
        self.session = session

    def _generate_incident_number(self) -> str:
        date_str = datetime.now(timezone.utc).strftime("%Y%m%d")
        rand_suffix = uuid.uuid4().hex[:6].upper()
        return f"EMG-{date_str}-{rand_suffix}"

    async def get_incident(self, incident_id: str) -> EmergencyIncident:
        query = (
            select(EmergencyIncident)
            .where(EmergencyIncident.id == incident_id, EmergencyIncident.is_deleted == False)
            .options(selectinload(EmergencyIncident.dispatches))
        )
        res = await self.session.execute(query)
        inc = res.scalars().first()
        if not inc:
            raise EntityNotFoundException("EmergencyIncident", incident_id)
        return inc

    async def create_incident(self, req: EmergencyIncidentCreateRequest) -> EmergencyIncident:
        inc_num = self._generate_incident_number()

        inc = EmergencyIncident(
            incident_number=inc_num,
            incident_type=req.incident_type,
            severity=req.severity,
            status=EMERGENCY_STATUS_REPORTED,
            title=req.title,
            description=req.description,
            latitude=req.latitude,
            longitude=req.longitude,
            location_address=req.location_address,
            caller_name=req.caller_name,
            caller_phone=req.caller_phone
        )
        self.session.add(inc)
        await self.session.flush()
        await self.session.refresh(inc, ["dispatches"])
        return inc

    async def dispatch_team(self, incident_id: str, req: EmergencyDispatchCreateRequest) -> EmergencyIncident:
        inc = await self.get_incident(incident_id)

        # Check team availability
        t_query = select(EmergencyResponseTeam).where(
            EmergencyResponseTeam.id == req.team_id,
            EmergencyResponseTeam.is_deleted == False
        )
        t_res = await self.session.execute(t_query)
        team = t_res.scalars().first()
        if not team:
            raise EntityNotFoundException("EmergencyResponseTeam", req.team_id)

        now = datetime.now(timezone.utc)
        dispatch = EmergencyDispatch(
            incident_id=inc.id,
            team_id=team.id,
            dispatched_at=now,
            dispatch_notes=req.dispatch_notes
        )
        self.session.add(dispatch)

        # Update team state
        team.is_available = False

        # Update incident state
        inc.status = EMERGENCY_STATUS_DISPATCHED
        if not inc.dispatched_at:
            inc.dispatched_at = now

        await self.session.flush()
        await self.session.refresh(inc, ["dispatches"])
        return inc

    async def mark_arrived(self, incident_id: str, team_id: str) -> EmergencyIncident:
        inc = await self.get_incident(incident_id)
        now = datetime.now(timezone.utc)

        # Update specific dispatch
        for d in inc.dispatches:
            if d.team_id == team_id and not d.arrival_time:
                d.arrival_time = now

        inc.status = EMERGENCY_STATUS_RESPONDING
        if not inc.arrived_at:
            inc.arrived_at = now

        await self.session.flush()
        await self.session.refresh(inc, ["dispatches"])
        return inc

    async def mark_contained(self, incident_id: str) -> EmergencyIncident:
        inc = await self.get_incident(incident_id)
        inc.status = EMERGENCY_STATUS_CONTAINED
        await self.session.flush()
        await self.session.refresh(inc, ["dispatches"])
        return inc

    async def resolve_incident(self, incident_id: str, req: EmergencyResolveRequest) -> EmergencyIncident:
        inc = await self.get_incident(incident_id)
        now = datetime.now(timezone.utc)

        inc.status = EMERGENCY_STATUS_RESOLVED
        inc.resolved_at = now

        # Release all dispatched teams and record departure
        for d in inc.dispatches:
            if not d.departure_time:
                d.departure_time = now

            # Find team to set available
            t_query = select(EmergencyResponseTeam).where(EmergencyResponseTeam.id == d.team_id)
            t_res = await self.session.execute(t_query)
            team = t_res.scalars().first()
            if team:
                team.is_available = True

        await self.session.flush()
        await self.session.refresh(inc, ["dispatches"])
        return inc
