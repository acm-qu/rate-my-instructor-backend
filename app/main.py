from fastapi import FastAPI
from api.middleware.rate_limiter import RateLimiterMiddleware

app = FastAPI()

app.add_middleware(RateLimiterMiddleware)

@app.get("/")
async def root():
    return {"message": "Hello World"}
