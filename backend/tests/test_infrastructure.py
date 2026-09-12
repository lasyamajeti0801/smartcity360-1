"""
SmartCity360 - Urban Infrastructure, Utilities & Asset Inspection Test Suite
Verifies asset registration, condition grading, health score scoring, streetlight repair, and waste requests.
"""

import uuid
from datetime import datetime, timezone
import pytest
from httpx import AsyncClient
from sqlalchemy import select
from backend.app.core.database import AsyncSessionLocal
from backend.app.models.infrastructure import StreetlightAsset, WasteZone

@pytest.mark.asyncio
async def test_infrastructure_asset_and_inspection_lifecycle(async_client: AsyncClient):
    # 1. Register & login a municipal inspector
    unique_email = f"inspector.{uuid.uuid4().hex[:8]}@example.com"
    await async_client.post("/api/v1/auth/register", json={
        "email": unique_email,
        "password": "Password123!",
        "full_name": "City Asset Inspector",
        "phone_number": "+1-555-019-7777",
        "address_line": "Municipal Public Works Yard"
    })
    login_res = await async_client.post("/api/v1/auth/login", json={
        "email": unique_email,
        "password": "Password123!"
    })
    token = login_res.json()["access_token"]
    headers = {"Authorization": f"Bearer {token}"}

    # 2. Get department
    dept_res = await async_client.get("/api/v1/departments")
    dept_id = dept_res.json()[0]["id"]

    # 3. Create an infrastructure asset (e.g. flyover bridge)
    asset_payload = {
        "name": "North Flyover Expansion Joint #4",
        "asset_type": "BRIDGE",
        "department_id": dept_id,
        "latitude": 12.9716,
        "longitude": 77.5946,
        "location_description": "Outer Ring Road Milepost 14.2",
        "ward_number": 3,
        "condition_status": "GOOD",
        "health_score": 100
    }
    create_res = await async_client.post("/api/v1/infrastructure/assets", json=asset_payload)
    assert create_res.status_code == 201
    asset_data = create_res.json()
    asset_id = asset_data["id"]
    assert asset_data["asset_tag"].startswith("AST-BRID-")
    assert asset_data["health_score"] == 100

    # 4. Perform inspection finding wear and tear -> condition POOR
    insp_payload = {
        "condition_found": "POOR",
        "notes": "Severe rubber seal degradation and 4cm vertical settlement detected.",
        "defects_observed": "Joint leakage onto lower roadway and vehicle vibration thump.",
        "recommended_action": "Resurface approach slab and replace elastomeric joint seal."
    }
    insp_res = await async_client.post(
        f"/api/v1/infrastructure/assets/{asset_id}/inspections",
        json=insp_payload,
        headers=headers
    )
    assert insp_res.status_code == 200
    updated_asset = insp_res.json()
    assert updated_asset["condition_status"] == "POOR"
    assert updated_asset["health_score"] == 40
    assert len(updated_asset["inspections"]) == 1

@pytest.mark.asyncio
async def test_streetlight_repair_and_waste_collection(async_client: AsyncClient):
    # 1. Login citizen
    unique_email = f"resident.{uuid.uuid4().hex[:8]}@example.com"
    await async_client.post("/api/v1/auth/register", json={
        "email": unique_email,
        "password": "Password123!",
        "full_name": "Civic Resident",
        "phone_number": "+1-555-019-3333",
        "address_line": "74 Blossom Ridge"
    })
    login_res = await async_client.post("/api/v1/auth/login", json={
        "email": unique_email,
        "password": "Password123!"
    })
    token = login_res.json()["access_token"]
    headers = {"Authorization": f"Bearer {token}"}
    # Ensure streetlight and waste zone exist
    async with AsyncSessionLocal() as session:
        sl = (await session.execute(select(StreetlightAsset))).scalars().first()
        if not sl:
            session.add(StreetlightAsset(
                pole_number="SL-POLE-401",
                latitude=12.9716,
                longitude=77.5946,
                street_name="MG Road Junction",
                luminaire_type="LED-60W",
                wattage=60,
                is_operational=True
            ))
        wz = (await session.execute(select(WasteZone))).scalars().first()
        if not wz:
            session.add(WasteZone(
                zone_code="WZ-CENTRAL",
                name="Central Urban Core Zone",
                collection_frequency="DAILY",
                daily_tonnage_capacity=25.0
            ))
        await session.commit()

    # 2. Check streetlights
    sl_res = await async_client.get("/api/v1/infrastructure/streetlights")
    assert sl_res.status_code == 200
    streetlights = sl_res.json()
    if len(streetlights) > 0:
        pole = streetlights[0]["pole_number"]
        # Update status
        up_res = await async_client.patch(
            f"/api/v1/infrastructure/streetlights/{pole}",
            json={"is_operational": True, "replace_bulb": True}
        )
        assert up_res.status_code == 200
        assert up_res.json()["is_operational"] is True
        assert up_res.json()["last_bulb_replacement"] is not None

    # 3. Schedule bulk waste collection
    zones_res = await async_client.get("/api/v1/infrastructure/waste/zones")
    assert zones_res.status_code == 200
    zones = zones_res.json()
    assert len(zones) > 0
    zone_id = zones[0]["id"]

    waste_payload = {
        "zone_id": zone_id,
        "waste_type": "BULK",
        "preferred_date": datetime.now(timezone.utc).isoformat(),
        "pickup_address": "74 Blossom Ridge, Driveway",
        "notes": "Old sofa and broken wooden dining table."
    }
    wst_res = await async_client.post(
        "/api/v1/infrastructure/waste/requests",
        json=waste_payload,
        headers=headers
    )
    assert wst_res.status_code == 201
    w_data = wst_res.json()
    assert w_data["request_number"].startswith("WST-")
    assert w_data["status"] == "SCHEDULED"
