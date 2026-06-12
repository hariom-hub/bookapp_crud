from fastapi import APIRouter, status, Depends
from fastapi.responses import JSONResponse
from fastapi.exceptions import HTTPException
from typing import Optional, List
from sqlalchemy.ext.asyncio import AsyncSession

from services import book_service
from src.services.book_service import BookService
from src.db.main import get_session
from src.db.schemas import BookModel, UpdateBookModel
from src.model import Book


router = APIRouter()

#  all api endpoints

# get all books
@router.get("/", response_model = List[Book], status_code = status.HTTP_200_OK)
async def get_all_books(session : AsyncSession = Depends(get_session)):
    books = BookService.get_all_books(session)
    return books

# get book by book id
@router.get("/{book_id}", response_model=BookModel, status_code = status.HTTP_200_OK)
async def get_book_byid(book_id : int, session : AsyncSession = Depends(get_session)) -> dict:
    pass






