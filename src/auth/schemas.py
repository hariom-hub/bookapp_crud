# receive data from client and then validate it without sending it to the server
from datetime import date, datetime
from email import message

from pydantic import BaseModel, Field
from pydantic import EmailStr
from src.auth.language_type.languages import Language


class UserCreateModel(BaseModel):
    username : str = Field(min_length=6, max_length=15)
    age : int
    email : EmailStr
    first_name : str = Field(min_length=1, max_length=10)
    last_name : str = Field(min_length=1, max_length=10)
    language : Language
    password_hash : str = Field(min_length=8, max_length=8)


class UserUpdateModel(BaseModel):
    username: str
    age: int
    email: EmailStr
    first_name: str
    last_name: str
    created_at: datetime
    language: Language


class UserModel(BaseModel):
    user_id: int
    username: str
    age: int
    email: EmailStr
    first_name:str
    last_name: str
    created_at: datetime
    is_verified: bool = Field(default=False)
    updated_at: datetime
    password_hash: str = Field(exclude=True)
    language: Language