from fastapi import APIRouter, status, Depends
from fastapi.responses import JSONResponse
from fastapi.exceptions import HTTPException
from typing import Optional, List
from sqlalchemy.ext.asyncio import AsyncSession
from src.services.book_service import BookService
from src.db.main import get_session
from src.db.schemas import BookModel, UpdateBookModel, CreateBookModel
from src.model import Book

router = APIRouter()
book_service = BookService()

'''all api endpoints'''


# get all books
@router.get("/", response_model=List[BookModel], status_code=status.HTTP_200_OK)
async def get_all_books(session: AsyncSession = Depends(get_session)):
    books = await book_service.get_all_books(session)
    if books is not None:
        return books
    else:
        return {"message": "Error occured"}


# get book by book id
@router.get("/{book_id}", response_model=BookModel, status_code=status.HTTP_200_OK)
async def get_book_byid(book_id: int, session: AsyncSession = Depends(get_session)):
    book = await  book_service.get_book_byId(book_id, session)
    if book:
        return book
    else:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Book with id {book_id} not found")


# add new book

@router.post("/addbook", response_model=BookModel, status_code=status.HTTP_201_CREATED)
async def add_book(book_data: CreateBookModel, session: AsyncSession = Depends(get_session)):
    return await book_service.add_book(book_data, session)


# update book

@router.patch("/update/{book_id}", response_model=UpdateBookModel, status_code=status.HTTP_200_OK)
async def update_book_byid(book_id: int, update_book_data: UpdateBookModel,
                           session: AsyncSession = Depends(get_session)):
    update_book = await book_service.update_book(book_id, update_book_data, session)
    if update_book:
        return update_book
    else:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Book with id {book_id} not found")


# delete book by id

@router.delete("/{book_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_book_byid(book_id: int, session: AsyncSession = Depends(get_session)):
    book_delete = await book_service.delete_book(book_id, session)

