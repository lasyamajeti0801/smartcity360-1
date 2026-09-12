"""
SmartCity360 - Structured Domain Exceptions & Error Envelopes
Ensures uniform REST error payloads without leaking raw tracebacks to clients.
"""

from typing import Any, Dict, Optional
from fastapi import Request, status
from fastapi.responses import JSONResponse
from fastapi.exceptions import RequestValidationError
from starlette.exceptions import HTTPException as StarletteHTTPException

class SmartCityException(Exception):
    """Base domain exception for SmartCity360 business rule violations."""
    def __init__(
        self,
        code: str,
        message: str,
        status_code: int = status.HTTP_400_BAD_REQUEST,
        details: Optional[Dict[str, Any]] = None
    ):
        self.code = code
        self.message = message
        self.status_code = status_code
        self.details = details or {}
        super().__init__(message)

class EntityNotFoundException(SmartCityException):
    def __init__(self, entity_name: str, identifier: Any):
        super().__init__(
            code=f"{entity_name.upper()}_NOT_FOUND",
            message=f"The requested {entity_name} with identifier '{identifier}' could not be found.",
            status_code=status.HTTP_404_NOT_FOUND,
            details={"entity": entity_name, "identifier": str(identifier)}
        )

class PermissionDeniedException(SmartCityException):
    def __init__(self, reason: str = "You do not have authorization to perform this civic action."):
        super().__init__(
            code="PERMISSION_DENIED",
            message=reason,
            status_code=status.HTTP_403_FORBIDDEN
        )

class InvalidStateTransitionException(SmartCityException):
    def __init__(self, entity: str, current_state: str, attempted_state: str):
        super().__init__(
            code="INVALID_STATE_TRANSITION",
            message=f"Cannot transition {entity} from '{current_state}' to '{attempted_state}'.",
            status_code=422,
            details={"current_state": current_state, "attempted_state": attempted_state}
        )

def format_error_response(
    code: str,
    message: str,
    status_code: int,
    request: Request,
    details: Optional[Dict[str, Any]] = None
) -> JSONResponse:
    """Builds standard uniform error payload."""
    request_id = getattr(request.state, "request_id", "unknown-request-id")
    return JSONResponse(
        status_code=status_code,
        content={
            "success": False,
            "error": {
                "code": code,
                "message": message,
                "details": details or {},
                "request_id": request_id
            }
        }
    )

async def smartcity_exception_handler(request: Request, exc: SmartCityException) -> JSONResponse:
    return format_error_response(
        code=exc.code,
        message=exc.message,
        status_code=exc.status_code,
        request=request,
        details=exc.details
    )

async def http_exception_handler(request: Request, exc: StarletteHTTPException) -> JSONResponse:
    code = "HTTP_ERROR"
    if exc.status_code == 401:
        code = "UNAUTHORIZED"
    elif exc.status_code == 403:
        code = "FORBIDDEN"
    elif exc.status_code == 404:
        code = "NOT_FOUND"
    elif exc.status_code == 429:
        code = "RATE_LIMIT_EXCEEDED"
        
    return format_error_response(
        code=code,
        message=str(exc.detail),
        status_code=exc.status_code,
        request=request
    )

async def validation_exception_handler(request: Request, exc: RequestValidationError) -> JSONResponse:
    errors = []
    for err in exc.errors():
        loc = " -> ".join([str(l) for l in err.get("loc", [])])
        errors.append({
            "field": loc,
            "message": err.get("msg"),
            "type": err.get("type")
        })
    return format_error_response(
        code="VALIDATION_ERROR",
        message="Request parameters failed validation constraints.",
        status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
        request=request,
        details={"validation_errors": errors}
    )
