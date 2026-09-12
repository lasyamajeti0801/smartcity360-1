"""
SmartCity360 - Urban Infrastructure, Utilities & Asset Lifecycle Service
Manages city asset registries, health scoring, condition inspections,
streetlight network maintenance, and residential waste collection bookings.
"""

from datetime import datetime, timezone
import uuid
from typing import List, Optional
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import selectinload
from backend.app.core.exceptions import (
    EntityNotFoundException,
    SmartCityException
)
from backend.app.models.infrastructure import (
    InfrastructureAsset,
    AssetInspection,
    StreetlightAsset,
    WaterAsset,
    WasteZone,
    WasteCollectionRequest,
    CONDITION_GOOD,
    CONDITION_FAIR,
    CONDITION_POOR,
    CONDITION_CRITICAL
)
from backend.app.schemas.infrastructure import (
    InfrastructureAssetCreateRequest,
    AssetInspectionCreateRequest,
    StreetlightStatusUpdateRequest,
    WasteCollectionCreateRequest
)

HEALTH_SCORE_DEFAULTS = {
    CONDITION_GOOD: 95,
    CONDITION_FAIR: 70,
    CONDITION_POOR: 40,
    CONDITION_CRITICAL: 15
}

class InfrastructureService:
    def __init__(self, session: AsyncSession):
        self.session = session

    def _generate_tag(self, prefix: str) -> str:
        date_str = datetime.now(timezone.utc).strftime("%Y%m%d")
        rand_suffix = uuid.uuid4().hex[:6].upper()
        return f"{prefix}-{date_str}-{rand_suffix}"

    async def get_asset(self, asset_id: str) -> InfrastructureAsset:
        query = (
            select(InfrastructureAsset)
            .where(InfrastructureAsset.id == asset_id, InfrastructureAsset.is_deleted == False)
            .options(selectinload(InfrastructureAsset.inspections))
        )
        res = await self.session.execute(query)
        asset = res.scalars().first()
        if not asset:
            raise EntityNotFoundException("InfrastructureAsset", asset_id)
        return asset

    async def create_asset(self, req: InfrastructureAssetCreateRequest) -> InfrastructureAsset:
        tag = self._generate_tag(f"AST-{req.asset_type[:4].upper()}")
        asset = InfrastructureAsset(
            asset_tag=tag,
            name=req.name,
            asset_type=req.asset_type.upper(),
            department_id=req.department_id,
            latitude=req.latitude,
            longitude=req.longitude,
            location_description=req.location_description,
            ward_number=req.ward_number,
            condition_status=req.condition_status.upper(),
            health_score=req.health_score,
            installation_date=datetime.now(timezone.utc)
        )
        self.session.add(asset)
        await self.session.flush()
        await self.session.refresh(asset, ["inspections"])
        return asset

    async def add_inspection(
        self,
        asset_id: str,
        inspector_id: Optional[str],
        req: AssetInspectionCreateRequest
    ) -> InfrastructureAsset:
        asset = await self.get_asset(asset_id)
        now = datetime.now(timezone.utc)

        inspection = AssetInspection(
            asset_id=asset.id,
            inspector_id=inspector_id,
            inspection_date=now,
            condition_found=req.condition_found,
            notes=req.notes,
            defects_observed=req.defects_observed,
            recommended_action=req.recommended_action
        )
        self.session.add(inspection)

        # Update asset condition & health score
        asset.condition_status = req.condition_found
        asset.last_inspection_date = now
        if req.health_score_adjustment is not None:
            asset.health_score = req.health_score_adjustment
        else:
            asset.health_score = HEALTH_SCORE_DEFAULTS.get(req.condition_found, 50)

        await self.session.flush()
        await self.session.refresh(asset, ["inspections"])
        return asset

    async def update_streetlight(
        self,
        pole_number: str,
        req: StreetlightStatusUpdateRequest
    ) -> StreetlightAsset:
        query = select(StreetlightAsset).where(
            StreetlightAsset.pole_number == pole_number,
            StreetlightAsset.is_deleted == False
        )
        res = await self.session.execute(query)
        sl = res.scalars().first()
        if not sl:
            raise EntityNotFoundException("StreetlightAsset", pole_number)

        sl.is_operational = req.is_operational
        if req.replace_bulb:
            sl.last_bulb_replacement = datetime.now(timezone.utc)
            sl.is_operational = True

        await self.session.flush()
        return sl

    async def create_waste_request(
        self,
        citizen_id: str,
        req: WasteCollectionCreateRequest
    ) -> WasteCollectionRequest:
        # Validate zone
        z_query = select(WasteZone).where(WasteZone.id == req.zone_id, WasteZone.is_deleted == False)
        z_res = await self.session.execute(z_query)
        zone = z_res.scalars().first()
        if not zone:
            raise EntityNotFoundException("WasteZone", req.zone_id)

        req_num = self._generate_tag("WST")
        wc = WasteCollectionRequest(
            request_number=req_num,
            citizen_id=citizen_id,
            zone_id=zone.id,
            waste_type=req.waste_type,
            status="SCHEDULED",
            preferred_date=req.preferred_date,
            pickup_address=req.pickup_address,
            notes=req.notes
        )
        self.session.add(wc)
        await self.session.flush()
        return wc
