"""
Pytest configuration and shared async fixtures for SmartCity360.
"""

import sys
from pathlib import Path
import pytest
import pytest_asyncio
from httpx import AsyncClient, ASGITransport

# Ensure repository root is in sys.path
root_dir = Path(__file__).resolve().parent.parent.parent
sys.path.insert(0, str(root_dir))

from backend.app.main import app
from backend.app.core.database import init_db

@pytest_asyncio.fixture(scope="session", autouse=True)
async def setup_test_database():
    """Ensure all database tables are initialized prior to test execution."""
    await init_db()
    yield

@pytest_asyncio.fixture
async def async_client():
    """Provides an isolated AsyncClient instance for FastAPI endpoint testing."""
    transport = ASGITransport(app=app)
    async with AsyncClient(transport=transport, base_url="http://testserver") as client:
        yield client
