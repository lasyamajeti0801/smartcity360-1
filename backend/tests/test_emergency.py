"""
SmartCity360 - Emergency 911 Operations Command Test Suite
Verifies emergency incident reporting, squad dispatch, on-scene arrival, and team release.
"""

import pytest
from httpx import AsyncClient

@pytest.mark.asyncio
async def test_emergency_dispatch_and_resolution_cycle(async_client: AsyncClient):
    # 1. Report emergency
    report_payload = {
        "incident_type": "FIRE_RESCUE",
        "severity": "CRITICAL",
        "title": "Commercial High-Rise Fire Alarm Triggered",
        "description": "Dense black smoke observed on 4th floor balcony. Sprinkler system activated.",
        "latitude": 12.9735,
        "longitude": 77.5955,
        "location_address": "88 Tower Road, Financial District",
        "caller_name": "Security Dispatch Desk",
        "caller_phone": "+1-555-019-9110"
    }
    rep_res = await async_client.post("/api/v1/emergency/incidents", json=report_payload)
    assert rep_res.status_code == 201
    inc_data = rep_res.json()
    inc_id = inc_data["id"]
    assert inc_data["status"] == "REPORTED"
    assert inc_data["incident_number"].startswith("EMG-")

    # 2. Find an available team
    teams_res = await async_client.get("/api/v1/emergency/teams?is_available=true")
    assert teams_res.status_code == 200
    teams = teams_res.json()
    assert len(teams) > 0
    team_id = teams[0]["id"]

    # 3. Dispatch team
    dispatch_payload = {
        "team_id": team_id,
        "dispatch_notes": "Engine 4 and ladder squad dispatched under Code 3 sirens."
    }
    disp_res = await async_client.post(f"/api/v1/emergency/incidents/{inc_id}/dispatch", json=dispatch_payload)
    assert disp_res.status_code == 200
    disp_data = disp_res.json()
    assert disp_data["status"] == "DISPATCHED"
    assert len(disp_data["dispatches"]) == 1

    # Check team availability is now false
    check_team_res = await async_client.get(f"/api/v1/emergency/teams")
    matched = next((t for t in check_team_res.json() if t["id"] == team_id), None)
    assert matched is not None
    assert matched["is_available"] is False

    # 4. Mark team arrived
    arrive_res = await async_client.post(f"/api/v1/emergency/incidents/{inc_id}/arrive?team_id={team_id}")
    assert arrive_res.status_code == 200
    assert arrive_res.json()["status"] == "RESPONDING"

    # 5. Containment
    contain_res = await async_client.post(f"/api/v1/emergency/incidents/{inc_id}/contain")
    assert contain_res.status_code == 200
    assert contain_res.json()["status"] == "CONTAINED"

    # 6. Resolution & Team release
    resolve_payload = {
        "notes": "Fire extinguished. Thermal imaging scan clear. Scene handed over to building warden."
    }
    res_res = await async_client.post(f"/api/v1/emergency/incidents/{inc_id}/resolve", json=resolve_payload)
    assert res_res.status_code == 200
    res_data = res_res.json()
    assert res_data["status"] == "RESOLVED"
    assert res_data["resolved_at"] is not None

    # Check team availability restored
    check_restored = await async_client.get(f"/api/v1/emergency/teams")
    matched_restored = next((t for t in check_restored.json() if t["id"] == team_id), None)
    assert matched_restored is not None
    assert matched_restored["is_available"] is True

@pytest.mark.asyncio
async def test_facility_directory_listing(async_client: AsyncClient):
    fac_res = await async_client.get("/api/v1/emergency/facilities")
    assert fac_res.status_code == 200
    facilities = fac_res.json()
    assert len(facilities) > 0
    assert all("facility_code" in f for f in facilities)
