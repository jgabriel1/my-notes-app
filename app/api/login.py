from fastapi import APIRouter, Depends, HTTPException
from fastapi.security import OAuth2PasswordRequestForm
from app.database import db
from app.schemas import UserSchema
from app.crud import crud_users
from app.security.token import Token, create_access_token

router = APIRouter()


@router.post('/register', status_code=201, response_model=Token)
async def register(user: UserSchema):
    crud_users.register_new(db, user)
    access_token = create_access_token(data={'sub': user.username})
    return {'access_token': access_token, 'token_type': 'bearer'}


@router.post('/token', response_model=Token)
async def get_access_token(form: OAuth2PasswordRequestForm = Depends()):
    user = await crud_users.authenticate(db, form.username, form.password)
    if not user:
        raise HTTPException(
            status_code=401,
            detail='Incorrect username or password',
            headers={'WWW-Authenticate': 'Bearer'}
        )
    access_token = create_access_token(data={'sub': user.username})
    return {'access_token': access_token, 'token_type': 'bearer'}
