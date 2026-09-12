"""
SmartCity360 - Municipal Departments & Service Catalog Endpoints
"""

from typing import List
from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
from sqlalchemy.orm import selectinload
from backend.app.core.database import get_db
from backend.app.core.exceptions import EntityNotFoundException
from backend.app.models.department import Department, ServiceCategory, MunicipalService
from backend.app.schemas.department import (
    DepartmentResponse,
    MunicipalServiceResponse,
    ServiceCategoryResponse
)

router = APIRouter(tags=["Municipal Departments & Services"])

@router.get("/departments", response_model=List[DepartmentResponse], summary="List all active municipal departments")
async def list_departments(db: AsyncSession = Depends(get_db)):
    query = (
        select(Department)
        .where(Department.is_active == True, Department.is_deleted == False)
        .options(selectinload(Department.services))
        .order_by(Department.name.asc())
    )
    res = await db.execute(query)
    departments = res.scalars().all()
    return [DepartmentResponse.model_validate(d) for d in departments]

@router.get("/departments/{department_id}", response_model=DepartmentResponse, summary="Get department details")
async def get_department(department_id: str, db: AsyncSession = Depends(get_db)):
    query = (
        select(Department)
        .where(Department.id == department_id, Department.is_deleted == False)
        .options(selectinload(Department.services))
    )
    res = await db.execute(query)
    dept = res.scalars().first()
    if not dept:
        raise EntityNotFoundException("Department", department_id)
    return DepartmentResponse.model_validate(dept)

@router.get("/services/categories", response_model=List[ServiceCategoryResponse], summary="List service categories")
async def list_service_categories(db: AsyncSession = Depends(get_db)):
    query = (
        select(ServiceCategory)
        .where(ServiceCategory.is_deleted == False)
        .order_by(ServiceCategory.display_order.asc())
    )
    res = await db.execute(query)
    cats = res.scalars().all()
    return [ServiceCategoryResponse.model_validate(c) for c in cats]

@router.get("/services", response_model=List[MunicipalServiceResponse], summary="List public municipal services")
async def list_services(db: AsyncSession = Depends(get_db)):
    query = (
        select(MunicipalService)
        .where(MunicipalService.is_active == True, MunicipalService.is_deleted == False)
        .order_by(MunicipalService.title.asc())
    )
    res = await db.execute(query)
    services = res.scalars().all()
    return [MunicipalServiceResponse.model_validate(s) for s in services]
