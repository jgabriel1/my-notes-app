from fastapi import APIRouter
from app.database import db
from app.database.models import users_table

router = APIRouter()


@router.post('/', status_code=201)
async def signup():
    return {'message': 'user created!'}


@router.post('/', status_code=201)
async def login():
    return {'message': 'user created!'}
