from passlib.context import CryptContext
from passlib.handlers import bcrypt

password_context = CryptContext(
    schemes = [bcrypt]
)

def generate_password_hash(password:str)->str:
    hashed_password = password_context.hash(password)
    return hashed_password

def verify_password_hash(password:str,hashed_password:str)->bool:
    return password_context.verify(password,hashed_password)