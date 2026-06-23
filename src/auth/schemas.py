# receive data from client and then validate it without sending it to the server
from datetime import date, datetime

from pydantic import BaseModel, EmailStr, Field
from pydantic.v1 import EmailStr
from language_type.languages import Language


class UserCreateModel(BaseModel):
    user_name : str = Field(min_length=6, max_length=10)
    email : EmailStr
    password : str = Field(min_length=8, max_length=8)


class UserUpdateModel(BaseModel):
    pass


class UserModel(BaseModel):
    user_id: int
    username: str
    age: int
    email: EmailStr
    first_name:str
    last_name: str
    created_at: datetime
    is_verified: bool
    updated_at: datetime
    password_hash: str
    language: Language