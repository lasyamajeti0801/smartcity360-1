import pytest
import uuid

@pytest.mark.asyncio
async def test_complaint_lifecycle(async_client):
    # 1. Register & login a citizen
    unique_email = f"citizen.{uuid.uuid4().hex[:8]}@example.com"
    await async_client.post("/api/v1/auth/register", json={
        "email": unique_email,
        "password": "Password123!",
        "full_name": "Complaint Reporter",
        "address_line": "45 Park Way",
        "ward_number": 2
    })
    login_res = await async_client.post("/api/v1/auth/login", json={
        "email": unique_email,
        "password": "Password123!"
    })
    token = login_res.json()["access_token"]
    headers = {"Authorization": f"Bearer {token}"}

    # 2. Fetch categories
    cats_res = await async_client.get("/api/v1/complaints/categories")
    assert cats_res.status_code == 200
    categories = cats_res.json()
    assert len(categories) > 0
    category_id = categories[0]["id"]

    # 3. Create complaint
    create_payload = {
        "category_id": category_id,
        "title": "Broken storm drain grate causing hazard",
        "description": "The metal storm drain grate is displaced and broken, exposing a deep hole in the sidewalk.",
        "latitude": 12.9716,
        "longitude": 77.5946,
        "location_address": "Corner of 5th Ave and Maple St",
        "ward_number": 2
    }
    c_res = await async_client.post("/api/v1/complaints", json=create_payload, headers=headers)
    assert c_res.status_code == 201
    c_data = c_res.json()
    assert c_data["status"] == "NEW"
    assert c_data["ticket_number"].startswith("CMP-")
    complaint_id = c_data["id"]
    ticket_number = c_data["ticket_number"]

    # 4. Fetch complaint by ticket number
    get_res = await async_client.get(f"/api/v1/complaints/{ticket_number}")
    assert get_res.status_code == 200
    assert get_res.json()["ticket_number"] == ticket_number

    # 5. Add a comment
    cmt_res = await async_client.post(
        f"/api/v1/complaints/{complaint_id}/comments",
        json={"comment": "Adding note: pedestrian walked by and nearly tripped.", "is_internal": False},
        headers=headers
    )
    assert cmt_res.status_code == 200
    assert cmt_res.json()["comment"] == "Adding note: pedestrian walked by and nearly tripped."

    # 6. Status update: NEW -> UNDER_REVIEW
    status_res = await async_client.patch(
        f"/api/v1/complaints/{complaint_id}/status",
        json={"status": "UNDER_REVIEW", "reason": "Department supervisor assigned ticket for inspection"},
        headers=headers
    )
    assert status_res.status_code == 200
    assert status_res.json()["status"] == "UNDER_REVIEW"

@pytest.mark.asyncio
async def test_invalid_status_transition(async_client):
    # Register & login
    unique_email = f"citizen.{uuid.uuid4().hex[:8]}@example.com"
    await async_client.post("/api/v1/auth/register", json={
        "email": unique_email,
        "password": "Password123!",
        "full_name": "Tester",
        "address_line": "123 St",
    })
    token = (await async_client.post("/api/v1/auth/login", json={"email": unique_email, "password": "Password123!"})).json()["access_token"]
    headers = {"Authorization": f"Bearer {token}"}

    cats = (await async_client.get("/api/v1/complaints/categories")).json()
    c_data = (await async_client.post("/api/v1/complaints", json={
        "category_id": cats[0]["id"],
        "title": "Road pothole test",
        "description": "Testing invalid transition from NEW directly to CLOSED",
        "latitude": 12.97,
        "longitude": 77.59,
        "location_address": "Test Road"
    }, headers=headers)).json()

    # Attempt illegal transition: NEW -> CLOSED (must go through review/resolved)
    bad_transition = await async_client.patch(
        f"/api/v1/complaints/{c_data['id']}/status",
        json={"status": "CLOSED"},
        headers=headers
    )
    assert bad_transition.status_code == 422
    assert bad_transition.json()["error"]["code"] == "INVALID_STATE_TRANSITION"
