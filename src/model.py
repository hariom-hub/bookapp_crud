from datetime import date, datetime, UTC

from sqlalchemy.orm import Mapped, mapped_column
from src.db.base import Base
from sqlalchemy import String


class Book(Base):
    __tablename__ = "books"
    id: Mapped[int] = mapped_column(
        autoincrement=True,
        primary_key=True
    )
    title: Mapped[str] = mapped_column(String(500))
    author: Mapped[str] = mapped_column(String(500))
    publisher: Mapped[str] = mapped_column(String(500))
    published_date: Mapped[date]
    page_count: Mapped[int]
    language: Mapped[str] = mapped_column(String(500))
    created_at: Mapped[datetime] = mapped_column(
        default=lambda: datetime.now(UTC)
    )
    updated_at: Mapped[datetime] = mapped_column(
        default=lambda: datetime.now(UTC),
        onupdate=lambda: datetime.now(UTC)
    )


    class Users(Base):
        __tablename__ = "Users"
        user_id : Mapped[int] = mapped_column(
            primary_key=True,
            autoincrement=True
        )
        name : Mapped[str] = mapped_column(String(500))
        age : Mapped[int]
        city : Mapped[str] = mapped_column(String(255))
    

def __repr__(self):
    return f"<Book {self.title}>"
