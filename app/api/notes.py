from fastapi import APIRouter, Header, HTTPException, Depends
from sqlalchemy.sql import select
from typing import List
from app.schemas import NoteSchema, ReturnNote, UserSchema
from app.database import db
from app.database.models import notes_table
from app.security import get_current_user

router = APIRouter()


@router.get('/notes', response_model=List[ReturnNote])
async def list_all(user: UserSchema = Depends(get_current_user)):
    query = notes_table.select().where(
        notes_table.c.writer_id == user.id
    )
    return await db.fetch_all(query)


@router.post('/notes', status_code=201)
async def create(note: NoteSchema, user: UserSchema = Depends(get_current_user)):
    query = notes_table.insert().values(
        **note.dict(),
        writer_id=user.id
    )
    return {
        "id": await db.execute(query)
    }


@router.delete('/notes/{note_id}', status_code=204)
async def delete(note_id: int, user: UserSchema = Depends(get_current_user)):
    note = await db.fetch_one(
        select(
            [notes_table.c.id, notes_table.c.writer_id]
        ).where(
            notes_table.c.id == note_id
        )
    )

    if note.writer_id != user.id:
        raise HTTPException(
            403, detail="Couldn't delete. Wrong Authorization.")

    query = notes_table.delete().where(notes_table.c.id == note_id)

    await db.execute(query)


@router.put('/notes/{note_id}', status_code=204)
async def edit(
    note_id: int,
    updated_note: NoteSchema,
    user: UserSchema = Depends(get_current_user)
):
    note = await db.fetch_one(
        select(
            [notes_table.c.id, notes_table.c.writer_id]
        ).where(
            notes_table.c.id == note_id
        )
    )

    if note.writer_id != user.id:
        raise HTTPException(403, detail="Couldn't edit. Wrong Authorization.")

    query = notes_table.update(
    ).values(
        **updated_note.dict()
    ).where(
        notes_table.c.id == note_id
    )

    await db.execute(query)
