"""
SmartCity360 - AI/ML Decision Support Test Suite
Verifies priority classification, departmental routing, confidence scores, and API endpoints.
"""

import pytest
from httpx import AsyncClient
from backend.app.services.ml_service import ml_service

def test_ml_service_direct_priority_inference():
    """Verify priority classifier predicts appropriate severity for critical vs normal issues."""
    # Critical road hazard
    crit_result = ml_service.predict_priority(
        title="Severe pavement collapse and crater",
        description="Massive sinkhole in center lane creating lethal hazard"
    )
    assert crit_result["priority"] in ["CRITICAL", "HIGH"]
    assert crit_result["confidence"] > 0.0

    # Low priority issue
    low_result = ml_service.predict_priority(
        title="Small gravel depression on the shoulder",
        description="Minor cosmetic wear on street curb"
    )
    assert low_result["priority"] in ["LOW", "MEDIUM"]
    assert "model_version" in low_result

def test_ml_service_direct_department_inference():
    """Verify department router correctly assigns civic issues to competent agencies."""
    # Water leak -> WATER
    water_res = ml_service.predict_department(
        title="Major drinking water pipeline burst",
        description="Continuous clean water leakage flooding roadway"
    )
    assert water_res["department"] == "WATER"

    # Electrical outage -> ELECTRICAL
    elec_res = ml_service.predict_department(
        title="Cluster of 5 streetlights completely dark",
        description="Exposed electrical wiring at base of public light pole"
    )
    assert elec_res["department"] == "ELECTRICAL"

    # Garbage overflow -> SANITATION
    san_res = ml_service.predict_department(
        title="Overflowing municipal garbage container",
        description="Rotting organic waste pile emitting severe odor"
    )
    assert san_res["department"] == "SANITATION"

@pytest.mark.asyncio
async def test_ai_triage_api_endpoint(async_client: AsyncClient):
    """Test /api/v1/complaints/ai-triage REST endpoint."""
    payload = {
        "title": "Major water pipe burst flooding intersection",
        "description": "Clean drinking water rushing into street and basements"
    }
    response = await async_client.post("/api/v1/complaints/ai-triage", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "predicted_priority" in data
    assert "predicted_department" in data
    assert "priority_confidence" in data
    assert "recommended_sla_hours" in data
    assert data["predicted_department"] == "WATER"

@pytest.mark.asyncio
async def test_model_registry_api_endpoint(async_client: AsyncClient):
    """Test /api/v1/complaints/models/registry endpoint."""
    response = await async_client.get("/api/v1/complaints/models/registry")
    assert response.status_code == 200
    data = response.json()
    assert "registered_models" in data
    model_names = [m["name"] for m in data["registered_models"]]
    assert "complaint_priority_classifier" in model_names
    assert "department_routing_classifier" in model_names
