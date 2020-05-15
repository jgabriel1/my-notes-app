import jwt
from fastapi import HTTPException
from pydantic import BaseModel
from datetime import datetime, timedelta

SECRET_KEY = 'supersecret'


class Token(BaseModel):
    access_token: str
    token_type: str


def create_access_token(
        data: dict, expires_delta: timedelta = timedelta(days=7)) -> str:
    expire: datetime = datetime.utcnow() + expires_delta

    to_encode = data.copy()
    to_encode.update({'exp': expire})

    return jwt.encode(to_encode, SECRET_KEY)


def decode_token(token: str) -> dict:
    try:
        return jwt.decode(token, SECRET_KEY)
    except jwt.PyJWTError:
        raise HTTPException(
            status_code=401,
            detail='Invalid authentication credentials.',
            headers={'WWW-Authenticate': 'Bearer'}
        )
