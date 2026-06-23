from sqlalchemy import select
from pydantic.v1 import EmailStr
from src.auth.schemas import UserCreateModel, UserModel
from src.auth.model import User
from sqlalchemy.ext.asyncio import AsyncSession
from src.auth.utils import generate_password_hash, verify_password_hash


class UserService:

    async def get_user_by_id(self, user_id: int, session: AsyncSession):

        statement = select(User).where(User.user_id == user_id)
        user = await session.execute(statement)
        await session.commit()
        return user.scalar_one_or_none()

    async def get_user_by_email(self, email: EmailStr, session: AsyncSession):
        statement = select(User).where(User.email == email)
        result = await session.execute(statement)
        user = result.scalar_one_or_none()
        return user if user is not None else None

    # add update service

    async def user_exists(self, email: EmailStr, session: AsyncSession) -> bool:
        user = await self.get_user_by_email(email, session)
        return True if user is not None else False

    async def create_user(self, user_data: UserCreateModel, session: AsyncSession):
        user_data_dict = user_data.model_dump()
        new_user = User(
            **user_data_dict
        )
        new_user.password_hash = generate_password_hash(user_data_dict['password'])
        session.add(new_user)
        await session.commit()
        return new_user
