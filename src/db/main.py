# from sqlalchemy import text
from sqlalchemy.ext.asyncio import create_async_engine
from src.config import Config
from src.db.base import Base
from src.model import Book

engine = create_async_engine(
    Config.MYSQL_DB_URL,
    echo=True
)


async def init_db():
    async with engine.begin() as conn:
        # print(Base.metadata.tables.keys())
        await conn.run_sync(Base.metadata.create_all)
