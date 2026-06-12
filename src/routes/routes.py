from fastapi import APIRouter, status, Depends
from fastapi.responses import JSONResponse
from fastapi.exceptions import HTTPException
from typing import Optional, List
from sqlalchemy.ext.asyncio import AsyncSession
from src.services.book_service import BookService
from src.db.main import get_session
from src.db.schemas import BookModel, UpdateBookModel
from src.model import Book

router = APIRouter()
book_service = BookService()

'''all api endpoints'''


# get all books
@router.get("/", response_model=List[Book], status_code=status.HTTP_200_OK)
async def get_all_books(session: AsyncSession = Depends(get_session)):
    books = await book_service.get_all_books(session)
    try:
        return books
    except Exception as e:
        raise e


# get book by book id
@router.get("/{book_id}", response_model=BookModel, status_code=status.HTTP_200_OK)
async def get_book_byid(book_id: int, session: AsyncSession = Depends(get_session)):
    book = await  book_service.get_book_byId(book_id, session)
    if book:
        return book
    else:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Book with id {book_id} not found")


# add new book

@router.post("/", response_model=BookModel, status_code=status.HTTP_201_CREATED)
async def add_book(book_data: BookModel, session: AsyncSession = Depends(get_session)):
    new_book = book_data.model_dump()
    for book in book_data:
        if book['id'] == book_data.id:
            raise HTTPException(status_code=status.HTTP_409_CONFLICT,
                                detail=f"Book with id {book_data.id} already exists")

    new_book = await book_service.add_book(new_book, session)
    return new_book


# update book

@router.patch("/{book_id}", response_model=UpdateBookModel, status_code=status.HTTP_200_OK)
async def update_book_byid(book_id: int, update_book_data: UpdateBookModel,
                           session: AsyncSession = Depends(get_session)):
    update_book = await book_service.update_book(book_id, update_book_data, session)
    if update_book:
        return update_book
    else:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Book with id {book_id} not found")


# delete book by id

@router.delete("/{book_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_book_byid(book_id: int, session: AsyncSession):
    book_delete = await book_service.delete_book(book_id, session)
    if book_delete:
        return None
    else:
        return JSONResponse(status_code=status.HTTP_204_NO_CONTENT, content=f"Book with id {book_id} deleted successfully.")
