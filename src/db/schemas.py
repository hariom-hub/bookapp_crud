from pydantic import BaseModel
from datetime import date, datetime


class BookModel(BaseModel):
    id: int
    title: str
    author: str
    publisher: str
    published_date: date
    page_count: int
    language: str
    created_at: datetime
    updated_at: datetime


class CreateBookModel(BaseModel):
    title: str
    author: str
    publisher: str
    published_date: date
    page_count: int
    language: str
    created_at: datetime
    updated_at: datetime


class UpdateBookModel(BaseModel):
    title: str | None = None
    author: str | None = None
    publisher: str | None = None
    published_date: date | None = None
    page_count: int | None = None
    language: str | None = None
    created_at: datetime
    updated_at: datetime


