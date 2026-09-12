"""
SmartCity360 - Work Order Field Execution Test Suite
Verifies task checklist toggling, percentage calculation, evidence attachment, and supervisor verification.
"""

import uuid
import pytest
from httpx import AsyncClient

@pytest.mark.asyncio
async def test_work_order_full_lifecycle(async_client: AsyncClient):
    # 1. First register a user and get auth token
    unique_email = f"tech.{uuid.uuid4().hex[:8]}@example.com"
    user_payload = {
        "email": unique_email,
        "password": "SecurePassword123!",
        "full_name": "Senior Field Technician",
        "phone_number": "+1-555-019-4444",
        "address_line": "12 Field HQ Road"
    }
    reg_res = await async_client.post("/api/v1/auth/register", json=user_payload)
    assert reg_res.status_code == 201
    login_res = await async_client.post(
        "/api/v1/auth/login",
        json={"email": unique_email, "password": "SecurePassword123!"}
    )
    assert login_res.status_code == 200
    token = login_res.json()["access_token"]
    headers = {"Authorization": f"Bearer {token}"}

    # 2. Get department
    dept_res = await async_client.get("/api/v1/departments")
    depts = dept_res.json()
    assert len(depts) > 0
    dept_id = depts[0]["id"]

    # 3. Create a work order with 2 tasks
    wo_payload = {
        "department_id": dept_id,
        "title": "Repair severed traffic light cable conduit",
        "description": "Exposed high voltage underground conduit damaged during excavation",
        "priority": "HIGH",
        "latitude": 12.9716,
        "longitude": 77.5946,
        "location_address": "MG Road & 4th Cross",
        "task_titles": [
            "Cut power at sub-station feeder 4",
            "Splice multi-core copper signal wiring and heat shrink"
        ]
    }
    create_res = await async_client.post("/api/v1/work-orders", json=wo_payload, headers=headers)
    assert create_res.status_code == 201
    wo_data = create_res.json()
    wo_id = wo_data["id"]
    assert wo_data["status"] == "CREATED"
    assert wo_data["completion_percentage"] == 0
    assert len(wo_data["tasks"]) == 2

    # 4. Toggle first task
    task1_id = wo_data["tasks"][0]["id"]
    toggle_res1 = await async_client.post(f"/api/v1/work-orders/{wo_id}/tasks/{task1_id}/toggle")
    assert toggle_res1.status_code == 200
    t1_data = toggle_res1.json()
    assert t1_data["completion_percentage"] == 50

    # 5. Attach evidence photo
    ev_payload = {
        "evidence_type": "PHOTO",
        "file_url": "https://storage.smartcity360.local/evidence/cable_repaired.jpg",
        "caption": "Repaired conduit and weather-tight seal inspection"
    }
    ev_res = await async_client.post(f"/api/v1/work-orders/{wo_id}/evidence", json=ev_payload, headers=headers)
    assert ev_res.status_code == 200
    ev_data = ev_res.json()
    assert len(ev_data["evidence"]) == 1

    # 6. Toggle second task -> 100% completion
    task2_id = wo_data["tasks"][1]["id"]
    toggle_res2 = await async_client.post(f"/api/v1/work-orders/{wo_id}/tasks/{task2_id}/toggle")
    assert toggle_res2.status_code == 200
    t2_data = toggle_res2.json()
    assert t2_data["completion_percentage"] == 100

    # 7. Supervisor Verification
    verify_payload = {
        "is_approved": True,
        "notes": "Field inspection verified by Chief Electrical Engineer. Cable test passed."
    }
    verify_res = await async_client.post(f"/api/v1/work-orders/{wo_id}/verify", json=verify_payload)
    assert verify_res.status_code == 200
    v_data = verify_res.json()
    assert v_data["status"] == "COMPLETED"
    assert v_data["verified_at"] is not None
