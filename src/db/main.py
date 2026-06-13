# from sqlalchemy import text
from sqlalchemy.ext.asyncio import create_async_engine
from src.config import Config
from src.db.base import Base
from src.model import Book
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import sessionmaker

async_engine = create_async_engine(
    Config.MYSQL_DB_URL,
    echo=True
)

AsynSessionLocal = sessionmaker(
    bind=async_engine,
    class_=AsyncSession,
    expire_on_commit=False
)


# db connection
async def init_db():
    async with async_engine.begin() as conn:
        # print(Base.metadata.tables.keys())
        await conn.run_sync(Base.metadata.create_all)


# returning the session that will be used across all the routes


async def get_session():
    async with AsynSessionLocal() as session:
        yield session
