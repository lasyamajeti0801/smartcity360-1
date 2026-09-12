import pytest
import uuid

@pytest.mark.asyncio
async def test_citizen_registration_and_login(async_client):
    unique_email = f"citizen.{uuid.uuid4().hex[:8]}@example.com"
    register_payload = {
        "email": unique_email,
        "password": "SecurePassword123!",
        "full_name": "Test Resident",
        "phone_number": "+1-555-019-9999",
        "address_line": "123 Civic Boulevard",
        "ward_number": 4,
        "preferred_language": "en"
    }

    # 1. Register citizen
    reg_response = await async_client.post("/api/v1/auth/register", json=register_payload)
    assert reg_response.status_code == 201
    reg_data = reg_response.json()
    assert reg_data["email"] == unique_email
    assert reg_data["full_name"] == "Test Resident"

    # 2. Login with valid credentials
    login_payload = {
        "email": unique_email,
        "password": "SecurePassword123!"
    }
    login_response = await async_client.post("/api/v1/auth/login", json=login_payload)
    assert login_response.status_code == 200
    token_data = login_response.json()
    assert "access_token" in token_data
    assert token_data["token_type"] == "bearer"
    token = token_data["access_token"]

    # 3. Authenticated /me profile check
    headers = {"Authorization": f"Bearer {token}"}
    me_response = await async_client.get("/api/v1/auth/me", headers=headers)
    assert me_response.status_code == 200
    me_data = me_response.json()
    assert me_data["email"] == unique_email

@pytest.mark.asyncio
async def test_login_invalid_password(async_client):
    login_payload = {
        "email": "admin@smartcity360.local",
        "password": "WrongPassword!"
    }
    response = await async_client.post("/api/v1/auth/login", json=login_payload)
    assert response.status_code == 401
    data = response.json()
    assert data["success"] is False
    assert data["error"]["code"] == "INVALID_CREDENTIALS"
