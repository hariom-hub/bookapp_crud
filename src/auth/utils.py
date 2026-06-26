# from passlib.context import CryptContext  # not using passlib bcoz it's outdated


from pwdlib import PasswordHash
from datetime import timedelta, timezone, date, datetime
import jwt
import logging

from src.config import Config

password_hash = PasswordHash.recommended()


# not using because passlib is being deprecated
# password_context = CryptContext(
#     schemes = ['bcrypt']
# )

def generate_password_hash(password: str) -> str:
    hashed_password = password_hash.hash(password)
    return hashed_password


def verify_password_hash(password: str, hashed_password: str) -> bool:
    return password_hash.verify(password, hashed_password)


def create_access_token(user_data: dict, expiry: timedelta = None):
    payload = {}

    payload['user'] = user_data
    payload['exp'] = datetime.now() + expiry
    token = jwt.encode(
        payload=payload,
        key=Config.JWT_SECRET,
        algorithm=Config.JWT_ALGORITHM
    )

    return token


def decode_token(token: str) -> dict:
    try:
        token_dict = jwt.decode(
            token=token,
            key=Config.JWT_SECRET,
            algorithms=[Config.JWT_ALGORITHM]
        )
        return token_dict
    except jwt.PyJWTError as e:
        logging.exception(e)
