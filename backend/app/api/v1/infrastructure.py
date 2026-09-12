"""
SmartCity360 - Infrastructure, Streetlights, Water, Waste, Traffic & Parking Endpoints
"""

from typing import List, Optional
from fastapi import APIRouter, Depends, Query, status
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
from sqlalchemy.orm import selectinload
from backend.app.core.database import get_db
from backend.app.core.security import decode_token, oauth2_scheme
from backend.app.models.infrastructure import (
    InfrastructureAsset,
    StreetlightAsset,
    WaterAsset,
    WasteZone
)
from backend.app.models.mobility import TrafficIncident, ParkingLocation
from backend.app.schemas.infrastructure import (
    InfrastructureAssetResponse,
    InfrastructureAssetCreateRequest,
    AssetInspectionCreateRequest,
    StreetlightAssetResponse,
    StreetlightStatusUpdateRequest,
    WaterAssetResponse,
    WasteZoneResponse,
    WasteCollectionCreateRequest,
    WasteCollectionResponse,
    TrafficIncidentResponse,
    ParkingLocationResponse
)
from backend.app.services.infrastructure_service import InfrastructureService

router = APIRouter(prefix="/infrastructure", tags=["Urban Infrastructure & Utilities"])

@router.get("/assets", response_model=List[InfrastructureAssetResponse], summary="List infrastructure assets")
async def list_assets(
    condition: Optional[str] = Query(None),
    asset_type: Optional[str] = Query(None),
    db: AsyncSession = Depends(get_db)
):
    query = (
        select(InfrastructureAsset)
        .where(InfrastructureAsset.is_deleted == False)
        .options(selectinload(InfrastructureAsset.inspections))
    )
    if condition:
        query = query.where(InfrastructureAsset.condition_status == condition)
    if asset_type:
        query = query.where(InfrastructureAsset.asset_type == asset_type)
    res = await db.execute(query)
    return [InfrastructureAssetResponse.model_validate(a) for a in res.scalars().all()]

@router.get("/assets/{asset_id}", response_model=InfrastructureAssetResponse, summary="Get infrastructure asset by ID")
async def get_asset(asset_id: str, db: AsyncSession = Depends(get_db)):
    service = InfrastructureService(db)
    asset = await service.get_asset(asset_id)
    return InfrastructureAssetResponse.model_validate(asset)

@router.post("/assets", response_model=InfrastructureAssetResponse, status_code=status.HTTP_201_CREATED, summary="Register infrastructure asset")
async def create_asset(
    req: InfrastructureAssetCreateRequest,
    db: AsyncSession = Depends(get_db)
):
    service = InfrastructureService(db)
    asset = await service.create_asset(req)
    return InfrastructureAssetResponse.model_validate(asset)

@router.post("/assets/{asset_id}/inspections", response_model=InfrastructureAssetResponse, summary="Log asset condition inspection")
async def record_asset_inspection(
    asset_id: str,
    req: AssetInspectionCreateRequest,
    token: str = Depends(oauth2_scheme),
    db: AsyncSession = Depends(get_db)
):
    payload = decode_token(token)
    inspector_id = payload.get("sub")
    service = InfrastructureService(db)
    asset = await service.add_inspection(asset_id, inspector_id, req)
    return InfrastructureAssetResponse.model_validate(asset)

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

@router.patch("/streetlights/{pole_number}", response_model=StreetlightAssetResponse, summary="Update streetlight operational status")
async def update_streetlight_status(
    pole_number: str,
    req: StreetlightStatusUpdateRequest,
    db: AsyncSession = Depends(get_db)
):
    service = InfrastructureService(db)
    sl = await service.update_streetlight(pole_number, req)
    return StreetlightAssetResponse.model_validate(sl)

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

@router.post("/waste/requests", response_model=WasteCollectionResponse, status_code=status.HTTP_201_CREATED, summary="Schedule bulk waste collection")
async def schedule_waste_pickup(
    req: WasteCollectionCreateRequest,
    token: str = Depends(oauth2_scheme),
    db: AsyncSession = Depends(get_db)
):
    payload = decode_token(token)
    citizen_id = payload.get("sub")
    service = InfrastructureService(db)
    wc = await service.create_waste_request(citizen_id, req)
    return WasteCollectionResponse.model_validate(wc)

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
