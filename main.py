from fastapi import FastAPI
from contextlib import asynccontextmanager
from src.db.main import init_db

@asynccontextmanager
async def life_span(app:FastAPI):
    print(f"server is starting...")
    await init_db()
    yield
    print(f"server has been stopped")

version = "v1"
app = FastAPI(
    title="fastapi db_webapp",
    description= "simple crud app",
    version=version,
    lifespan=life_span
)

@app.get("/")
async def home():
    return "hello world"