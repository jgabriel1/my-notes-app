from fastapi import Depends, HTTPException, security
from .database import Database, SQLALCHEMY_DATABASE_URL
from .security.token import decode_token
from .schemas import UserSchema
from .crud import crud_users

oauth2_scheme = security.OAuth2PasswordBearer(tokenUrl='/token')


async def get_db() -> Database:
    database = Database(url=SQLALCHEMY_DATABASE_URL)
    return database


async def get_current_user(
    token: str = Depends(oauth2_scheme),
    database: Database = Depends(get_db)
) -> UserSchema:
    """
    To put this into crud_users as well or not?
    Only concern is the http exception. No other crud operations have exceptions.
    """
    credentials_exception = HTTPException(
        status_code=401,
        detail='Invalid authentication credentials.',
        headers={'WWW-Authenticate': 'Bearer'}
    )

    payload = decode_token(token)
    username: str = payload.get('sub')
    if username is None:
        raise credentials_exception

    user = await crud_users.get_info(database, username=username)
    if user is None:
        raise credentials_exception

    return user
