"""
SmartCity360 - Central Configuration Settings
Reads from environment variables and provides typed settings with defaults.
"""

from typing import List, Optional, Union
from pydantic import AnyHttpUrl, field_validator
from pydantic_settings import BaseSettings, SettingsConfigDict
import os

class Settings(BaseSettings):
    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        case_sensitive=True,
        extra="ignore"
    )

    # Core Environment
    PROJECT_NAME: str = "SmartCity360"
    ENVIRONMENT: str = "development"
    DEBUG: bool = True
    API_V1_STR: str = "/api/v1"
    
    # Server Binding
    BACKEND_HOST: str = "0.0.0.0"
    BACKEND_PORT: int = 8000
    
    # Cryptographic Security
    SECRET_KEY: str = "development-insecure-secret-key-change-in-production-min-32-chars"
    ALGORITHM: str = "HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 60 * 24  # 24 hours
    REFRESH_TOKEN_EXPIRE_DAYS: int = 7

    # CORS
    ALLOWED_ORIGINS: str = "http://localhost:5173,http://127.0.0.1:5173,http://localhost:3000"

    @property
    def cors_origins(self) -> List[str]:
        return [origin.strip() for origin in self.ALLOWED_ORIGINS.split(",") if origin.strip()]

    # Database Configuration
    POSTGRES_SERVER: str = "localhost"
    POSTGRES_PORT: int = 5432
    POSTGRES_USER: str = "smartcity_admin"
    POSTGRES_PASSWORD: str = "smartcity_secure_pass"
    POSTGRES_DB: str = "smartcity360_db"
    
    # Dynamic database URL: Defaults to local SQLite async if postgres is not configured
    DATABASE_URL: Optional[str] = None
    
    @property
    def effective_database_url(self) -> str:
        if self.DATABASE_URL and self.DATABASE_URL.strip():
            return self.DATABASE_URL
        # Fallback to local SQLite for frictionless local unit testing and quickstart
        return "sqlite+aiosqlite:///./data/smartcity360.db"

    # Redis Cache & Queue
    REDIS_URL: str = "redis://localhost:6379/0"

    # GIS Configuration (OpenStreetMap / Leaflet - Zero API Keys Required)
    MAP_DEFAULT_LATITUDE: float = 12.9716
    MAP_DEFAULT_LONGITUDE: float = 77.5946
    MAP_DEFAULT_ZOOM: int = 12
    TILE_SERVER_URL: str = "https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png"
    TILE_ATTRIBUTION: str = '&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors'

    # File Storage
    UPLOAD_DIR: str = "./data/uploads"
    MAX_UPLOAD_SIZE_MB: int = 25
    ALLOWED_EXTENSIONS: str = "jpg,jpeg,png,webp,pdf,doc,docx"

    # Mock Payments
    MOCK_PAYMENT_GATEWAY_ENABLED: bool = True
    MOCK_PAYMENT_SUCCESS_RATE: float = 0.98

    # Logging
    LOG_LEVEL: str = "INFO"
    ENABLE_AUDIT_LOGGING: bool = True

settings = Settings()
