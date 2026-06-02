from api.middleware.rate_limiter import RateLimiterMiddleware
from fastapi import FastAPI

app = FastAPI()

app.add_middleware(RateLimiterMiddleware)

@app.get("/")
async def root():
    return {"message": "Hello World"}
