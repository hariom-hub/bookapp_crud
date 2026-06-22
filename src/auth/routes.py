from fastapi import APIRouter
from src.auth.schemas import UserCreateModel
auth_router = APIRouter()

@auth_router.post("/signup")
async def user_signup(user : UserCreateModel):
    pass
