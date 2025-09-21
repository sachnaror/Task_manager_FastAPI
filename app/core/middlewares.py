from starlette.middleware.base import BaseHTTPMiddleware
from fastapi import Request
import time
import json


class LoggingMiddleware(BaseHTTPMiddleware):
    async def dispatch(self, request: Request, call_next):
        start = time.time()
        response = await call_next(request)
        duration = time.time() - start

        # --- Option 1: Simple text log ---
        print(f"{request.method} {request.url.path} -> {response.status_code} in {duration:.2f}s")

        # --- Option 2: JSON log (for structured logging) ---
        log_data = {
            "method": request.method,
            "path": request.url.path,
            "status": response.status_code,
            "duration": round(duration, 3)
        }
        print(json.dumps(log_data))

        return response
