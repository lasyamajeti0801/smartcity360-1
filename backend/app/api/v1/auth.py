"""
SmartCity360 - Authentication & User Endpoints
"""

from fastapi import APIRouter, Depends, status
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
from sqlalchemy.orm import selectinload
from backend.app.core.database import get_db
from backend.app.core.security import decode_token, oauth2_scheme
from backend.app.models.user import User, Role
from backend.app.schemas.user import (
    CitizenRegisterRequest,
    LoginRequest,
    TokenResponse,
    UserResponse
)
from backend.app.services.auth_service import AuthService
from backend.app.core.exceptions import EntityNotFoundException

router = APIRouter(prefix="/auth", tags=["Authentication & Identity"])

@router.post(
    "/register",
    response_model=UserResponse,
    status_code=status.HTTP_201_CREATED,
    summary="Register a new citizen account"
)
async def register_citizen(
    req: CitizenRegisterRequest,
    db: AsyncSession = Depends(get_db)
):
    service = AuthService(db)
    user = await service.register_citizen(req)
    # Reload with relationships
    query = (
        select(User)
        .where(User.id == user.id)
        .options(
            selectinload(User.roles).selectinload(Role.permissions),
            selectinload(User.citizen_profile)
        )
    )
    res = await db.execute(query)
    full_user = res.scalars().first()
    return UserResponse.model_validate(full_user)

@router.post(
    "/login",
    response_model=TokenResponse,
    summary="Authenticate and receive JWT bearer access token"
)
async def login(
    req: LoginRequest,
    db: AsyncSession = Depends(get_db)
):
    service = AuthService(db)
    return await service.authenticate_user(req)

@router.get(
    "/me",
    response_model=UserResponse,
    summary="Retrieve profile of the currently authenticated user"
)
async def get_current_user_profile(
    token: str = Depends(oauth2_scheme),
    db: AsyncSession = Depends(get_db)
):
    payload = decode_token(token)
    user_id = payload.get("sub")
    query = (
        select(User)
        .where(User.id == user_id, User.is_deleted == False)
        .options(
            selectinload(User.roles).selectinload(Role.permissions),
            selectinload(User.citizen_profile),
            selectinload(User.staff_profile)
        )
    )
    res = await db.execute(query)
    user = res.scalars().first()
    if not user:
        raise EntityNotFoundException("User", user_id)
    return UserResponse.model_validate(user)
