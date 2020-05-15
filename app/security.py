from fastapi import Depends, HTTPException
from fastapi.security import OAuth2PasswordBearer
from app.database import db
from app.database.models import users_table, User

# All functions here grab user information from db while authenticating
# their credentials and raising errors if they occur. All of this will
# be abstracted by the last function which should just return the User
# object that can be used in the routes.

oauth2_schema = OAuth2PasswordBearer(tokenUrl='/token')


async def get_user_db(db, username: str):
    user = await db.fetch_one(
        users_table.select(
        ).where(
            users_table.c.name == username
        )
    )
    return user


async def decode_token(token: str) -> User:
    """
    This function should decode the token and
    return the user from database.
    """
    user = await get_user_db(db, token)
    return user


async def get_current_user(token: str = Depends(oauth2_schema)):
    user = decode_token(token)
    if not user:
        raise HTTPException(
            status_code=401,
            detail="Invalid authentication credentials.",
            headers={'WWW-Authenticate': 'Bearer'}
        )
    return user

# https://fastapi.tiangolo.com/tutorial/security/simple-oauth2/
