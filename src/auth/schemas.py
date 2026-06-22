# receive data from client and then validate it without sending it to the server
from pydantic import BaseModel, EmailStr, Field
from pydantic.v1 import EmailStr


class UserCreateModel(BaseModel):
    user_name : str = Field(min_length=6, max_length=10)
    email : EmailStr
    password : str = Field(min_length=8, max_length=8)


class UserUpdateModel(BaseModel):
    pass