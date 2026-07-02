

from fastapi import HTTPException, status
from sqlalchemy import select
from pydantic.v1 import EmailStr

from src.auth.schemas import UserCreateModel, UserModel, UserUpdateModel
from src.auth.model import User
from sqlalchemy.ext.asyncio import AsyncSession
from src.auth.utils import generate_password_hash, verify_password_hash


class UserService:

    async def get_user_by_id(self, user_id: int, session: AsyncSession):
        statement = select(User).where(User.user_id == user_id)
        result = await session.execute(statement)
        user = result.scalar_one_or_none()
        return user if user is not None else None

    async def get_user_by_email(self, email: EmailStr, session: AsyncSession):
        statement = select(User).where(User.email == email)
        result = await session.execute(statement)
        user = result.scalar_one_or_none()
        return user if user is not None else None

    async def get_all_users(self,session:AsyncSession):
        statement = select(User).order_by(User.created_at)
        users = await session.execute(statement)
        return users.scalars()

    async def user_exists(self, email: EmailStr, session: AsyncSession) -> bool:
        user = await self.get_user_by_email(email, session)
        return True if user is not None else False

    async def create_user(self, user_data: UserCreateModel, session: AsyncSession):
        user_data_dict = user_data.model_dump()
        new_user = User(
            **user_data_dict
        )
        new_user.password_hash = generate_password_hash(user_data_dict['password_hash'])
        session.add(new_user)
        await session.commit()
        return new_user

    async def update_user(self, user_id: int, user_update: UserUpdateModel, session: AsyncSession):

        user = await self.get_user_by_id(user_id, session)
        if user is not None:
            user_update_dict = user_update.model_dump()
            for key, value in user_update_dict.items():
                setattr(user, key, value)
            await session.commit()
            return user
        else:
            return None

    async def delete_user(self, user_id: int, session: AsyncSession):
        user_delete = await self.get_user_by_id(user_id, session)
        if user_delete is None:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="User not found"
            )

        await session.delete(user_delete)
        await session.commit()
