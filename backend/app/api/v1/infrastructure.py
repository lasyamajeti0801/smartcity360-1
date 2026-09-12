"""
SmartCity360 - Infrastructure, Streetlights, Water, Waste, Traffic & Parking Endpoints
"""

from typing import List, Optional
from fastapi import APIRouter, Depends, Query
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
from backend.app.core.database import get_db
from backend.app.models.infrastructure import (
    InfrastructureAsset,
    StreetlightAsset,
    WaterAsset,
    WasteZone
)
from backend.app.models.mobility import TrafficIncident, ParkingLocation
from backend.app.schemas.infrastructure import (
    InfrastructureAssetResponse,
    StreetlightAssetResponse,
    WaterAssetResponse,
    WasteZoneResponse,
    TrafficIncidentResponse,
    ParkingLocationResponse
)

router = APIRouter(prefix="/infrastructure", tags=["Urban Infrastructure & Utilities"])

@router.get("/assets", response_model=List[InfrastructureAssetResponse], summary="List infrastructure assets")
async def list_assets(
    condition: Optional[str] = Query(None),
    asset_type: Optional[str] = Query(None),
    db: AsyncSession = Depends(get_db)
):
    query = select(InfrastructureAsset).where(InfrastructureAsset.is_deleted == False)
    if condition:
        query = query.where(InfrastructureAsset.condition_status == condition)
    if asset_type:
        query = query.where(InfrastructureAsset.asset_type == asset_type)
    res = await db.execute(query)
    return [InfrastructureAssetResponse.model_validate(a) for a in res.scalars().all()]

@router.get("/streetlights", response_model=List[StreetlightAssetResponse], summary="List streetlight inventory")
async def list_streetlights(
    operational_only: Optional[bool] = Query(None),
    db: AsyncSession = Depends(get_db)
):
    query = select(StreetlightAsset).where(StreetlightAsset.is_deleted == False)
    if operational_only is not None:
        query = query.where(StreetlightAsset.is_operational == operational_only)
    res = await db.execute(query)
    return [StreetlightAssetResponse.model_validate(s) for s in res.scalars().all()]

@router.get("/water", response_model=List[WaterAssetResponse], summary="List water distribution network nodes")
async def list_water_assets(db: AsyncSession = Depends(get_db)):
    query = select(WaterAsset).where(WaterAsset.is_deleted == False)
    res = await db.execute(query)
    return [WaterAssetResponse.model_validate(w) for w in res.scalars().all()]

@router.get("/waste/zones", response_model=List[WasteZoneResponse], summary="List municipal waste collection sectors")
async def list_waste_zones(db: AsyncSession = Depends(get_db)):
    query = select(WasteZone).where(WasteZone.is_deleted == False)
    res = await db.execute(query)
    return [WasteZoneResponse.model_validate(z) for z in res.scalars().all()]

@router.get("/traffic", response_model=List[TrafficIncidentResponse], summary="List traffic incidents and road conditions")
async def list_traffic_incidents(
    status: Optional[str] = Query(None),
    db: AsyncSession = Depends(get_db)
):
    query = select(TrafficIncident).where(TrafficIncident.is_deleted == False)
    if status:
        query = query.where(TrafficIncident.status == status)
    res = await db.execute(query)
    return [TrafficIncidentResponse.model_validate(t) for t in res.scalars().all()]

@router.get("/parking", response_model=List[ParkingLocationResponse], summary="List parking facilities & live occupancy")
async def list_parking_lots(db: AsyncSession = Depends(get_db)):
    query = select(ParkingLocation).where(ParkingLocation.is_deleted == False)
    res = await db.execute(query)
    return [ParkingLocationResponse.model_validate(p) for p in res.scalars().all()]
