from fastapi import APIRouter, Depends, HTTPException
from fastapi.security import OAuth2PasswordRequestForm
from app.token import Token, create_access_token
from app.security import authenticate_user, get_current_user, hash_password
from app.database import db, users_table
from app.schemas import UserSchema

router = APIRouter()


@router.post('/register', status_code=201, response_model=Token)
async def register(user: UserSchema):
    query = users_table.insert().values(
        username=user.username,
        password=hash_password(user.password)
    )
    await db.execute(query)
    access_token = create_access_token(data={'sub': user.username})
    return {'access_token': access_token, 'token_type': 'bearer'}


@router.post('/token', response_model=Token)
async def get_access_token(form: OAuth2PasswordRequestForm = Depends()):
    user = await authenticate_user(db, form.username, form.password)
    if not user:
        raise HTTPException(
            status_code=401,
            detail='Incorrect username or password',
            headers={'WWW-Authenticate': 'Bearer'}
        )
    access_token = create_access_token(data={'sub': user.username})
    return {'access_token': access_token, 'token_type': 'bearer'}
