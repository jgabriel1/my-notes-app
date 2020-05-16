from fastapi import Depends, HTTPException, security
from app.database import db
from app.security.token import decode_token
from app.schemas import UserSchema
from app.crud import crud_users

oauth2_scheme = security.OAuth2PasswordBearer(tokenUrl='/token')


async def get_current_user(token: str = Depends(oauth2_scheme)) -> UserSchema:
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

    user = await crud_users.get_info(db, username=username)
    if user is None:
        raise credentials_exception

    return user
