import os

import redis
from dotenv import load_dotenv
from fastapi import Request
from fastapi.responses import JSONResponse
from starlette.middleware.base import BaseHTTPMiddleware

load_dotenv()

REDIS_URL = os.getenv("REDIS_URL")
MAX_REQUESTS = 10
WINDOW_SECONDS = 120

redis_client = redis.asyncio.from_url(REDIS_URL, decode_responses=True)


class RateLimiterMiddleware(BaseHTTPMiddleware):
    async def dispatch(self, request: Request, call_next):
        ip = request.client.host
        key = f"rate:{ip}"

        count = await redis_client.incr(key)

        if count == 1:
            await redis_client.expire(key, WINDOW_SECONDS)

        if count > MAX_REQUESTS:
            ttl = await redis_client.ttl(key)
            return JSONResponse(
                status_code=429,
                headers={"Retry-After": str(ttl)},
                content={"detail": "Too many requests. Try again later."},
            )

        response = await call_next(request)
        response.headers["X-RateLimit-Limit"] = str(MAX_REQUESTS)
        response.headers["X-RateLimit-Remaining"] = str(max(0, MAX_REQUESTS - count))
        return response
