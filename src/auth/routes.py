from fastapi import APIRouter
from src.auth.schemas import UserCreateModel, UserModel, UserUpdateModel
from src.db.main import get_session
from sqlalchemy.ext.asyncio import AsyncSession
from fastapi import Depends, HTTPException, status
from src.auth.service import UserService
from typing import List

user_service = UserService()

auth_router = APIRouter()


@auth_router.get("/user/{user_id}", response_model=UserModel, status_code=status.HTTP_200_OK)
async def get_user(user_id: int, session: AsyncSession = Depends(get_session)):
    user = await user_service.get_user_by_id(user_id, session)
    if user:
        return user
    else:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"User with id {user_id} not found")


# return all users
@auth_router.get("/users", response_model=List[UserModel], status_code=status.HTTP_200_OK)
async def get_users(session: AsyncSession = Depends(get_session)):
    users = await user_service.get_all_users(session)
    if users:
        return users
    else:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Users not found")


@auth_router.post("/signup", response_model=UserModel, status_code=status.HTTP_201_CREATED)
async def user_signup(user_data: UserCreateModel, session: AsyncSession = Depends(get_session)):
    email = user_data.email
    user_exists = user_service.user_exists(email, session)
    if await user_exists:
        raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail="User with Email already exists")

    new_user = await user_service.create_user(user_data, session)
    return new_user


@auth_router.patch("/update/{user_id}", response_model=UserModel, status_code=status.HTTP_200_OK)
async def update_user(user_id: int, user_data: UserUpdateModel, session: AsyncSession = Depends(get_session)):
    update_user = await user_service.update_user(user_id, user_data, session)
    if update_user:
        return update_user
    else:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"User with id {user_id} not found",
        )
