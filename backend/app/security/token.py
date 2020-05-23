from datetime import datetime, timedelta

import jwt
from fastapi import HTTPException
from pydantic import BaseModel

SECRET_KEY = 'supersecret'
ALGORITHM = "HS256"


class Token(BaseModel):
    access_token: str
    token_type: str


def create_access_token(
        data: dict, expires_delta: timedelta = timedelta(days=7)) -> str:
    expire: datetime = datetime.utcnow() + expires_delta

    to_encode = data.copy()
    to_encode.update({'exp': expire})

    return jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)


def decode_token(token: str) -> dict:
    try:
        return jwt.decode(token, SECRET_KEY, algotrithms=[ALGORITHM])
    except jwt.PyJWTError:
        raise HTTPException(
            status_code=401,
            detail='Invalid authentication credentials.',
            headers={'WWW-Authenticate': 'Bearer'}
        )
