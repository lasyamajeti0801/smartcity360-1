"""
SmartCity360 - Database Engine, Session Lifecycle, and Base Declarative Models
Uses SQLAlchemy 2.0 Async engine with connection pooling and session lifecycle management.
"""

from datetime import datetime, timezone
import uuid
from typing import AsyncGenerator
from sqlalchemy import Column, DateTime, Boolean, String
from sqlalchemy.ext.asyncio import AsyncSession, async_sessionmaker, create_async_engine
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from backend.app.core.config import settings

# Create Async SQLAlchemy 2.0 Engine
engine = create_async_engine(
    settings.effective_database_url,
    echo=settings.DEBUG and settings.ENVIRONMENT == "development",
    future=True,
    pool_pre_ping=True
)

# Async Session Factory
AsyncSessionLocal = async_sessionmaker(
    bind=engine,
    class_=AsyncSession,
    expire_on_commit=False,
    autocommit=False,
    autoflush=False
)

class Base(DeclarativeBase):
    """Base declarative class for all SmartCity360 relational models."""
    pass

class TimeStampedBase(Base):
    """
    Abstract base entity providing standard audit timestamps,
    UUID primary keys, and soft-delete capabilities across all municipal domains.
    """
    __abstract__ = True

    id: Mapped[str] = mapped_column(
        String(36),
        primary_key=True,
        default=lambda: str(uuid.uuid4()),
        index=True
    )
    created_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        default=lambda: datetime.now(timezone.utc),
        nullable=False,
        index=True
    )
    updated_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        default=lambda: datetime.now(timezone.utc),
        onupdate=lambda: datetime.now(timezone.utc),
        nullable=False
    )
    is_deleted: Mapped[bool] = mapped_column(
        Boolean,
        default=False,
        nullable=False,
        index=True
    )

async def get_db() -> AsyncGenerator[AsyncSession, None]:
    """
    FastAPI dependency yielding an isolated async database session per request.
    Automatically commits valid operations or rolls back on unhandled exceptions.
    """
    async with AsyncSessionLocal() as session:
        try:
            yield session
            await session.commit()
        except Exception:
            await session.rollback()
            raise
        finally:
            await session.close()

import os
from pathlib import Path

async def init_db() -> None:
    """Initializes all database tables defined in metadata."""
    data_dir = Path("data")
    data_dir.mkdir(parents=True, exist_ok=True)
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
