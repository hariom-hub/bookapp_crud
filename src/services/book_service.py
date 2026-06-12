from sqlalchemy.ext.asyncio import AsyncSession
from src.db.schemas import BookModel, CreateBookModel, UpdateBookModel
from sqlalchemy import select, desc
from src.model import Book
from fastapi.exceptions import HTTPException


class BookService:

    async def get_all_books(self, book: BookModel, session: AsyncSession):
        statement = select(Book).order_by(desc(Book.created_at))
        result = await session.execute(statement)
        return result.all()

    async def get_book_byId(self, book_id: int, session: AsyncSession):
        statement = select(Book).where(Book.id == book_id)
        result = await  session.execute(statement)
        book = result.first()
        return book

    async def create_book(self, add_book: CreateBookModel, session: AsyncSession):
        pass

    async def update_book(self, book_id: int, update_book: UpdateBookModel, session: AsyncSession):
        pass

    async def delete_book(self, book_id: int, session: AsyncSession):
        pass
