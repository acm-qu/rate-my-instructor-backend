from db.session import engine, Base
from db import models
from fastapi import FastAPI

def init_db():
    Base.metadata.create_all(bind=engine)

if __name__ == "__main__":
    init_db()
    print("Tables created")

app = FastAPI()

@app.get("/")
async def root():
  return {
    "message": "Hello World"
  }