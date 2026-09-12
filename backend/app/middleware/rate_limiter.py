"""
SmartCity360 - In-Memory Sliding-Window Rate Limiter
Prevents brute force attacks and denial-of-service on sensitive civic endpoints.
"""

import time
from collections import defaultdict
from typing import Dict, List
from fastapi import Request, status
from fastapi.responses import JSONResponse
from starlette.middleware.base import BaseHTTPMiddleware

class RateLimiterMiddleware(BaseHTTPMiddleware):
    def __init__(self, app, max_requests: int = 120, window_seconds: int = 60):
        super().__init__(app)
        self.max_requests = max_requests
        self.window_seconds = window_seconds
        self.clients: Dict[str, List[float]] = defaultdict(list)

    async def dispatch(self, request: Request, call_next):
        # Exempt health endpoints
        if request.url.path.startswith("/health"):
            return await call_next(request)

        client_ip = request.client.host if request.client else "unknown"
        now = time.time()
        
        # Clean older requests outside the window
        timestamps = [t for t in self.clients[client_ip] if now - t < self.window_seconds]
        
        if len(timestamps) >= self.max_requests:
            return JSONResponse(
                status_code=status.HTTP_429_TOO_MANY_REQUESTS,
                content={
                    "success": False,
                    "error": {
                        "code": "RATE_LIMIT_EXCEEDED",
                        "message": f"Rate limit of {self.max_requests} requests per {self.window_seconds}s exceeded. Please slow down.",
                        "details": {"retry_after_seconds": int(self.window_seconds - (now - timestamps[0]))},
                        "request_id": getattr(request.state, "request_id", "unknown")
                    }
                }
            )

        timestamps.append(now)
        self.clients[client_ip] = timestamps

        return await call_next(request)
