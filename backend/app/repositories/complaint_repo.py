"""
SmartCity360 - Complaint Repository Implementation
"""

from typing import List, Optional
from datetime import datetime, timezone
from sqlalchemy import select, func, and_
from sqlalchemy.orm import selectinload
from backend.app.models.complaint import Complaint, ComplaintCategory, ComplaintStatusHistory
from backend.app.repositories.base import BaseRepository

class ComplaintRepository(BaseRepository[Complaint]):
    def __init__(self, session):
        super().__init__(Complaint, session)

    async def get_by_ticket_number(self, ticket_number: str) -> Optional[Complaint]:
        query = (
            select(Complaint)
            .where(Complaint.ticket_number == ticket_number, Complaint.is_deleted == False)
            .options(
                selectinload(Complaint.comments),
                selectinload(Complaint.status_history),
                selectinload(Complaint.category),
                selectinload(Complaint.department)
            )
        )
        res = await self.session.execute(query)
        return res.scalars().first()

    async def list_with_filters(
        self,
        department_id: Optional[str] = None,
        citizen_id: Optional[str] = None,
        status: Optional[str] = None,
        priority: Optional[str] = None,
        ward_number: Optional[int] = None,
        is_escalated: Optional[bool] = None,
        skip: int = 0,
        limit: int = 50
    ) -> List[Complaint]:
        conditions = [Complaint.is_deleted == False]
        if department_id:
            conditions.append(Complaint.department_id == department_id)
        if citizen_id:
            conditions.append(Complaint.citizen_id == citizen_id)
        if status:
            conditions.append(Complaint.status == status)
        if priority:
            conditions.append(Complaint.priority == priority)
        if ward_number is not None:
            conditions.append(Complaint.ward_number == ward_number)
        if is_escalated is not None:
            conditions.append(Complaint.is_escalated == is_escalated)

        query = (
            select(Complaint)
            .where(and_(*conditions))
            .options(
                selectinload(Complaint.category),
                selectinload(Complaint.department)
            )
            .order_by(Complaint.created_at.desc())
            .offset(skip)
            .limit(limit)
        )
        res = await self.session.execute(query)
        return list(res.scalars().all())

    async def count_by_status(self, department_id: Optional[str] = None):
        conditions = [Complaint.is_deleted == False]
        if department_id:
            conditions.append(Complaint.department_id == department_id)
        
        query = (
            select(Complaint.status, func.count(Complaint.id))
            .where(and_(*conditions))
            .group_by(Complaint.status)
        )
        res = await self.session.execute(query)
        return dict(res.all())
