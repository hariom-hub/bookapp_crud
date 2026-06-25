from fastapi import APIRouter
from src.auth.schemas import UserCreateModel, UserModel
from src.db.main import get_session
from sqlalchemy.ext.asyncio import AsyncSession
from fastapi import Depends, HTTPException, status
from src.auth.service import UserService

user_service = UserService()

auth_router = APIRouter()

@auth_router.post("/signup", response_model = UserModel, status_code=status.HTTP_201_CREATED)
async def user_signup(user_data: UserCreateModel , session:AsyncSession = Depends(get_session)):
    email = user_data.email
    user_exists = user_service.user_exists(email,session)
    if await user_exists:
        raise HTTPException(status_code = status.HTTP_409_CONFLICT, detail="User with Email already exists")

    new_user = await user_service.create_user(user_data,session)
    return new_user


# task -> create all remaining endpoints