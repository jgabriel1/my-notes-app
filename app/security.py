from typing import Union
from fastapi import Depends, HTTPException
from fastapi.security import OAuth2PasswordBearer
from databases import Database
from passlib.context import CryptContext
from app.database import db
from app.database.models import users_table, User
from app.token import decode_token

# All functions here grab user information from db while authenticating
# their credentials and raising errors if they occur. All of this will
# be abstracted by the last function which should just return the User
# object that can be used in the routes.

pwd_context = CryptContext(schemes=['bcrypt'], deprecated='auto')

oauth2_scheme = OAuth2PasswordBearer(tokenUrl='/token')


def verify_password(password: str, hashed_password: str) -> bool:
    return pwd_context.verify(password, hashed_password)


def hash_password(password: str) -> str:
    return pwd_context.hash(password)


async def get_user_db(db: Database, username: str) -> User:
    user = await db.fetch_one(
        users_table.select().where(
            users_table.c.username == username
        )
    )
    return user


async def authenticate_user(
        db: Database, username: str, password: str) -> Union[bool, User]:
    user = await get_user_db(db, username)
    if not user:
        return False
    if not verify_password(password, user.password):
        return False
    return user


async def get_current_user(token: str = Depends(oauth2_scheme)) -> User:
    credentials_exception = HTTPException(
        status_code=401,
        detail='Invalid authentication credentials.',
        headers={'WWW-Authenticate': 'Bearer'}
    )

    payload = decode_token(token)
    username: str = payload.get('sub')
    if username is None:
        raise credentials_exception

    user = await get_user_db(db, username=username)
    if user is None:
        raise credentials_exception

    return user


# https://fastapi.tiangolo.com/tutorial/security/simple-oauth2/
