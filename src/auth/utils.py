# from passlib.context import CryptContext
from pwdlib import PasswordHash
from datetime import timedelta, timezone
import jwt



password_hash = PasswordHash.recommended()

# not using because passlib is being deprecated
# password_context = CryptContext(
#     schemes = ['bcrypt']
# )

def generate_password_hash(password:str)->str:
    hashed_password = password_hash.hash(password)
    return hashed_password

def verify_password_hash(password:str,hashed_password:str)->bool:
    return password_hash.verify(password,hashed_password)



