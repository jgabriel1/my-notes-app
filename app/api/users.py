from fastapi import APIRouter, Body, HTTPException
from app.database import db
from app.database.models import users_table, notes_table
from app.schemas import UserSchema, NoteSchema, ReturnNote
from typing import List

router = APIRouter()


@router.get('/', response_model=List[ReturnNote])
async def login(user: UserSchema):
    """
    TODO:
    * Make a better query that uses the relationship;
    * Change errors to have custom error handling functions;
    """
    writer = await db.fetch_one(
        users_table.select().where(users_table.c.name == user.name)
    )

    if not writer:
        raise HTTPException(
            403, detail="You\'re not signed up! Create an account first."
        )

    elif user.pwd_hash != writer.pwd_hash:
        raise HTTPException(401, detail="Wrong Password!")

    notes = notes_table.select().where(notes_table.c.writer_id == writer.id)
    return await db.fetch_all(notes)


@router.post('/', status_code=201)
async def signup(user: UserSchema):
    query = users_table.insert().values(**user.dict())

    return {
        "id": await db.execute(query)
    }
