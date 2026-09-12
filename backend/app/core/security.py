"""
SmartCity360 - Cryptographic Security & RBAC Guard
Handles password hashing, JWT encoding/decoding, and fine-grained authorization.
"""

from datetime import datetime, timedelta, timezone
from typing import Any, Dict, List, Optional, Union
from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from jose import JWTError, jwt
import bcrypt
from backend.app.core.config import settings

oauth2_scheme = OAuth2PasswordBearer(
    tokenUrl=f"{settings.API_V1_STR}/auth/login"
)

# Standard Platform Roles
ROLE_CITIZEN = "Citizen"
ROLE_DEPT_STAFF = "Department Staff"
ROLE_FIELD_STAFF = "Field Staff"
ROLE_SUPERVISOR = "Supervisor"
ROLE_EMERGENCY_OPERATOR = "Emergency Operator"
ROLE_MUNICIPAL_OFFICER = "Municipal Officer"
ROLE_CITY_ADMIN = "City Administrator"
ROLE_SYSTEM_ADMIN = "System Administrator"

ALL_ROLES = [
    ROLE_CITIZEN,
    ROLE_DEPT_STAFF,
    ROLE_FIELD_STAFF,
    ROLE_SUPERVISOR,
    ROLE_EMERGENCY_OPERATOR,
    ROLE_MUNICIPAL_OFFICER,
    ROLE_CITY_ADMIN,
    ROLE_SYSTEM_ADMIN
]

def verify_password(plain_password: str, hashed_password: str) -> bool:
    """Verifies a plaintext password against a stored cryptographic hash."""
    try:
        return bcrypt.checkpw(plain_password.encode("utf-8"), hashed_password.encode("utf-8"))
    except Exception:
        return False

def get_password_hash(password: str) -> str:
    """Generates a secure cryptographic hash of a plaintext password."""
    # Bcrypt maximum length is 72 bytes
    pwd_bytes = password.encode("utf-8")[:72]
    salt = bcrypt.gensalt(rounds=12)
    return bcrypt.hashpw(pwd_bytes, salt).decode("utf-8")

def create_access_token(
    subject: Union[str, Any],
    roles: List[str],
    permissions: Optional[List[str]] = None,
    expires_delta: Optional[timedelta] = None
) -> str:
    """Creates a signed HMAC-SHA256 JWT access token."""
    if expires_delta:
        expire = datetime.now(timezone.utc) + expires_delta
    else:
        expire = datetime.now(timezone.utc) + timedelta(minutes=settings.ACCESS_TOKEN_EXPIRE_MINUTES)
    
    to_encode: Dict[str, Any] = {
        "sub": str(subject),
        "roles": roles,
        "permissions": permissions or [],
        "exp": expire,
        "iat": datetime.now(timezone.utc)
    }
    return jwt.encode(to_encode, settings.SECRET_KEY, algorithm=settings.ALGORITHM)

def decode_token(token: str) -> Dict[str, Any]:
    """Decodes and validates JWT token integrity and expiration."""
    try:
        payload = jwt.decode(token, settings.SECRET_KEY, algorithms=[settings.ALGORITHM])
        return payload
    except JWTError as e:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid, expired, or tampered authentication token.",
            headers={"WWW-Authenticate": "Bearer"}
        ) from e

class RoleChecker:
    """Dependency that verifies that the active authenticated user possesses at least one authorized role."""
    def __init__(self, allowed_roles: List[str]):
        self.allowed_roles = set(allowed_roles)

    def __call__(self, token: str = Depends(oauth2_scheme)) -> Dict[str, Any]:
        payload = decode_token(token)
        user_roles = set(payload.get("roles", []))
        
        # System Administrator has broad operational access
        if ROLE_SYSTEM_ADMIN in user_roles:
            return payload

        if not self.allowed_roles.intersection(user_roles):
            raise HTTPException(
                status_code=status.HTTP_403_FORBIDDEN,
                detail=f"Access denied. Requires one of roles: {list(self.allowed_roles)}"
            )
        return payload

def require_roles(*roles: str) -> RoleChecker:
    """Helper returning a RoleChecker dependency for route guards."""
    return RoleChecker(list(roles))
