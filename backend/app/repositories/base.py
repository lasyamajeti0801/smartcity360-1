"""
SmartCity360 - Base Generic Repository Pattern
Provides asynchronous CRUD, pagination, filtering, and soft-delete handling.
"""

from typing import Any, Dict, Generic, List, Optional, Type, TypeVar
from sqlalchemy import select, update, func
from sqlalchemy.ext.asyncio import AsyncSession
from backend.app.core.database import TimeStampedBase

ModelType = TypeVar("ModelType", bound=TimeStampedBase)

class BaseRepository(Generic[ModelType]):
    def __init__(self, model: Type[ModelType], session: AsyncSession):
        self.model = model
        self.session = session

    async def get_by_id(self, entity_id: str) -> Optional[ModelType]:
        query = select(self.model).where(
            self.model.id == entity_id,
            self.model.is_deleted == False
        )
        result = await self.session.execute(query)
        return result.scalars().first()

    async def list_all(
        self,
        skip: int = 0,
        limit: int = 50,
        order_by: Any = None
    ) -> List[ModelType]:
        query = select(self.model).where(self.model.is_deleted == False)
        if order_by is not None:
            query = query.order_by(order_by)
        else:
            query = query.order_by(self.model.created_at.desc())
        query = query.offset(skip).limit(limit)
        result = await self.session.execute(query)
        return list(result.scalars().all())

    async def count(self) -> int:
        query = select(func.count()).select_from(self.model).where(self.model.is_deleted == False)
        result = await self.session.execute(query)
        return result.scalar() or 0

    async def create(self, entity: ModelType) -> ModelType:
        self.session.add(entity)
        await self.session.flush()
        await self.session.refresh(entity)
        return entity

    async def soft_delete(self, entity_id: str) -> bool:
        stmt = (
            update(self.model)
            .where(self.model.id == entity_id)
            .values(is_deleted=True)
        )
        result = await self.session.execute(stmt)
        return result.rowcount > 0
