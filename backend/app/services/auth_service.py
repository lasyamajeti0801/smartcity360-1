"""
SmartCity360 - Authentication & User Registration Business Service
"""

from datetime import datetime, timezone
from typing import Optional
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import selectinload
from backend.app.core.security import get_password_hash, verify_password, create_access_token, ROLE_CITIZEN
from backend.app.core.exceptions import SmartCityException, EntityNotFoundException
from backend.app.models.user import User, Role, CitizenProfile
from backend.app.schemas.user import CitizenRegisterRequest, LoginRequest, TokenResponse, UserResponse

class AuthService:
    def __init__(self, session: AsyncSession):
        self.session = session

    async def register_citizen(self, req: CitizenRegisterRequest) -> User:
        # Check duplicate email
        query = select(User).where(User.email == req.email.lower())
        res = await self.session.execute(query)
        if res.scalars().first():
            raise SmartCityException(
                code="EMAIL_ALREADY_REGISTERED",
                message=f"An account with email '{req.email}' is already registered.",
                status_code=409
            )

        # Retrieve or create Citizen role
        role_query = select(Role).where(Role.name == ROLE_CITIZEN)
        role_res = await self.session.execute(role_query)
        citizen_role = role_res.scalars().first()
        if not citizen_role:
            citizen_role = Role(
                name=ROLE_CITIZEN,
                description="Registered urban resident eligible for public civic services."
            )
            self.session.add(citizen_role)
            await self.session.flush()

        # Create user
        user = User(
            email=req.email.lower(),
            hashed_password=get_password_hash(req.password),
            full_name=req.full_name,
            phone_number=req.phone_number,
            is_active=True,
            is_verified=True,
            roles=[citizen_role]
        )
        self.session.add(user)
        await self.session.flush()

        # Create citizen profile
        profile = CitizenProfile(
            user_id=user.id,
            address_line=req.address_line,
            ward_number=req.ward_number,
            preferred_language=req.preferred_language
        )
        self.session.add(profile)
        await self.session.flush()
        await self.session.refresh(user)
        return user

    async def authenticate_user(self, req: LoginRequest) -> TokenResponse:
        query = (
            select(User)
            .where(User.email == req.email.lower(), User.is_deleted == False)
            .options(
                selectinload(User.roles).selectinload(Role.permissions),
                selectinload(User.citizen_profile),
                selectinload(User.staff_profile)
            )
        )
        res = await self.session.execute(query)
        user = res.scalars().first()

        if not user or not verify_password(req.password, user.hashed_password):
            raise SmartCityException(
                code="INVALID_CREDENTIALS",
                message="Invalid email or password combination.",
                status_code=401
            )

        if not user.is_active:
            raise SmartCityException(
                code="ACCOUNT_DEACTIVATED",
                message="Your municipal account has been temporarily deactivated.",
                status_code=403
            )

        user.last_login_at = datetime.now(timezone.utc)
        role_names = [r.name for r in user.roles]
        
        token = create_access_token(
            subject=user.id,
            roles=role_names
        )

        return TokenResponse(
            access_token=token,
            token_type="bearer",
            expires_in_seconds=86400,
            user=UserResponse.model_validate(user)
        )
