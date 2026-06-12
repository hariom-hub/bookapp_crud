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
        return book if book is not None else None

    async def add_book(self, add_book: CreateBookModel, session: AsyncSession):

        book_data_dict = add_book.model_dump()  # dictionary representation of the model + fields to include and exclude
        new_book = Book(
            **book_data_dict
        )
        session.add(new_book)
        await session.commit()
        return new_book

    async def update_book(self, book_id: int, update_book: UpdateBookModel, session: AsyncSession):

        book_update = self.get_book_byId(book_id, session)
        if book_update is not None:
            update_data_dict = update_book.model_dump()
            for key, value in update_data_dict.items():
                setattr(book_update, key, value)

            await session.commit()
            return book_update
        else:
            return None

    async def delete_book(self, book_id: int, session: AsyncSession):

        book_delete = self.get_book_byId(book_id, session)
        if book_delete is not None:
            await session.delete(book_delete)
            await session.commit()
        else:
            return None
