from fastapi import APIRouter, Body
from app.database import db
from app.database.models import users_table, notes_table
from app.schemas import UserSchema, NoteSchema
from typing import List

router = APIRouter()

# Figure out a way to grab notes using relationship table:
@router.get('/', response_model=List[NoteSchema])
async def login(user_id: int = Body(..., embed=True)):
    query = notes_table.select().where(notes_table.c.writer_id == user_id)

    return await db.fetch_all(query)


@router.post('/', status_code=201)
async def signup(user: UserSchema):
    query = users_table.insert().values(**user.dict())

    return {
        "id": await db.execute(query)
    }

# @router.get('/')  # , response_model=List[NoteSchema])
# async def login(user: UserSchema):
#     # query = users_table.select(['notes']).where(
#     #     users_table.c.name == user.name)
#     query = """
#     SELECT category, subject, body FROM notes
#     JOIN users WHERE name = :name
#     """

#     return await db.fetch_all(query, values={
#         "name": user.name
#     })
