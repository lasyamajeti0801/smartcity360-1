import pytest

@pytest.mark.asyncio
async def test_health_check(async_client):
    response = await async_client.get("/health")
    assert response.status_code == 200
    data = response.json()
    assert data["status"] == "HEALTHY"
    assert data["platform"] == "SmartCity360"

@pytest.mark.asyncio
async def test_liveness_probe(async_client):
    response = await async_client.get("/health/live")
    assert response.status_code == 200
    assert response.json() == {"status": "ALIVE"}

@pytest.mark.asyncio
async def test_readiness_probe(async_client):
    response = await async_client.get("/health/ready")
    assert response.status_code == 200
    data = response.json()
    assert data["status"] == "READY"
    assert data["database"] == "CONNECTED"
