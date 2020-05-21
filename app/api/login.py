from fastapi import APIRouter, Depends, HTTPException, security

from ..crud import crud_users
from ..deps import Database, get_db
from ..schemas import UserSchema
from ..security.token import Token, create_access_token

router = APIRouter()


@router.post('/register', status_code=201, response_model=Token)
async def register(user: UserSchema, database: Database = Depends(get_db)):
    await crud_users.register_new(database, user)
    access_token = create_access_token(data={'sub': user.username})
    return {'access_token': access_token, 'token_type': 'bearer'}


@router.post('/token', response_model=Token)
async def get_access_token(
    form: security.OAuth2PasswordRequestForm = Depends(),
    database: Database = Depends(get_db)
):
    user = await crud_users.authenticate(database, form.username, form.password)
    if not user:
        raise HTTPException(
            status_code=401,
            detail='Incorrect username or password',
            headers={'WWW-Authenticate': 'Bearer'}
        )
    access_token = create_access_token(data={'sub': user.username})
    return {'access_token': access_token, 'token_type': 'bearer'}
