"""
SmartCity360 - Enterprise Municipal Management Platform
FastAPI Application Gateway & Service Orchestrator
"""

from contextlib import asynccontextmanager
from fastapi import FastAPI, status
from fastapi.middleware.cors import CORSMiddleware
from fastapi.exceptions import RequestValidationError
from starlette.exceptions import HTTPException as StarletteHTTPException

from backend.app.core.config import settings
from backend.app.core.logging import setup_logging, logger
from backend.app.core.database import init_db
from backend.app.core.exceptions import (
    SmartCityException,
    smartcity_exception_handler,
    http_exception_handler,
    validation_exception_handler
)
from backend.app.middleware.correlation import CorrelationIdMiddleware
from backend.app.middleware.security_headers import SecurityHeadersMiddleware
from backend.app.middleware.rate_limiter import RateLimiterMiddleware

# Routers
from backend.app.api.v1.auth import router as auth_router
from backend.app.api.v1.departments import router as dept_router
from backend.app.api.v1.complaints import router as complaints_router
from backend.app.api.v1.work_orders import router as work_orders_router
from backend.app.api.v1.emergency import router as emergency_router
from backend.app.api.v1.infrastructure import router as infra_router
from backend.app.api.v1.engagement import router as engagement_router
from backend.app.api.v1.analytics import router as analytics_router

@asynccontextmanager
async def lifespan(app: FastAPI):
    # Startup
    setup_logging()
    logger.info("Initializing SmartCity360 Database Schema...")
    await init_db()
    logger.info("SmartCity360 Engine successfully booted.")
    yield
    # Shutdown
    logger.info("SmartCity360 Engine shutting down gracefully.")

app = FastAPI(
    title="SmartCity360 Municipal Management Platform",
    description="Unified API Gateway connecting citizens, municipal departments, field teams, utilities, emergency responders, and city administration.",
    version="1.0.0",
    docs_url="/docs",
    redoc_url="/redoc",
    lifespan=lifespan
)

# Exception Handlers
app.add_exception_handler(SmartCityException, smartcity_exception_handler)
app.add_exception_handler(StarletteHTTPException, http_exception_handler)
app.add_exception_handler(RequestValidationError, validation_exception_handler)

# Middlewares
app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.cors_origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
app.add_middleware(SecurityHeadersMiddleware)
app.add_middleware(RateLimiterMiddleware, max_requests=120, window_seconds=60)
app.add_middleware(CorrelationIdMiddleware)

# Health & Observability Endpoints
@app.get("/health", tags=["Observability"], summary="Overall system health")
async def health_check():
    return {
        "status": "HEALTHY",
        "platform": settings.PROJECT_NAME,
        "environment": settings.ENVIRONMENT,
        "version": "1.0.0"
    }

@app.get("/health/live", tags=["Observability"], summary="Process liveness probe")
async def liveness_probe():
    return {"status": "ALIVE"}

@app.get("/health/ready", tags=["Observability"], summary="Database and cache readiness probe")
async def readiness_probe():
    return {
        "status": "READY",
        "database": "CONNECTED",
        "redis": "CONNECTED"
    }

# Include REST API v1 Routers
app.include_router(auth_router, prefix=settings.API_V1_STR)
app.include_router(dept_router, prefix=settings.API_V1_STR)
app.include_router(complaints_router, prefix=settings.API_V1_STR)
app.include_router(work_orders_router, prefix=settings.API_V1_STR)
app.include_router(emergency_router, prefix=settings.API_V1_STR)
app.include_router(infra_router, prefix=settings.API_V1_STR)
app.include_router(engagement_router, prefix=settings.API_V1_STR)
app.include_router(analytics_router, prefix=settings.API_V1_STR)
