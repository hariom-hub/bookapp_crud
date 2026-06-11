from sqlalchemy.ext.asyncio import AsyncSession
from src.db.schemas import BookModel, CreateBookModel, UpdateBookModel
from sqlalchemy import select
from src.model import Book


class BookService:

    async def get_all_books(self, book: BookModel, session: AsyncSession):
        pass

    async def get_book_byId(self, book_id: int, session: AsyncSession):
        pass

    async def create_book(self, add_book: CreateBookModel, session: AsyncSession):
        pass

    async def update_book(self, book_id: int, update_book: UpdateBookModel, session: AsyncSession):
        pass

    async def delete_book(self, book_id: int, session: AsyncSession):
        pass
