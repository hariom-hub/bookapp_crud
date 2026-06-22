from sqlalchemy import select
from pydantic.v1 import EmailStr
from schemas import UserCreateModel
from src.auth.model import User
from sqlalchemy.ext.asyncio import AsyncSession
from utils import generate_passwd_hash, verify_passwd_hash


class UserService:
    async def get_user_by_email(self, email : EmailStr, session : AsyncSession):
        statement = select(User).where(User.email == email)
        result = await session.execute(statement)
        user = result.scalar_one_or_none()
        return user if user is not None else None

    async def user_exists(self,email:EmailStr, session:AsyncSession)->bool:
        user = await self.get_user_by_email(email,session)
        return True if user is not None else False


    async def create_user(self, user_data : UserCreateModel, session : AsyncSession):

        user_data_dict = user_data.model_dump() # dict representation of the model
        new_user = User(
            **user_data_dict
        )
        await session.add(new_user)
        await session.commit()
        await session.refresh(new_user)
        return new_user



