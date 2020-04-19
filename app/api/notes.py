from fastapi import APIRouter, Request, Header, HTTPException
from sqlalchemy.sql import select
from app.schemas import NoteSchema
from app.database import db
from app.database.models import notes_table

router = APIRouter()


@router.post('/notes', status_code=201)
async def create(note: NoteSchema, Authorization: str = Header(...)):
    query = notes_table.insert().values(
        **note.dict(),
        writer_id=Authorization
    )

    return {
        "id": await db.execute(query)
    }
# updated tests and authorization checks


@router.delete('/notes/{note_id}', status_code=204)
async def delete(note_id: int, Authorization: str = Header(...)):
    note = await db.fetch_one(
        select(
            [notes_table.c.id, notes_table.c.writer_id]
        ).where(
            notes_table.c.id == note_id
        )
    )

    if note.writer_id != int(Authorization):
        raise HTTPException(403, detail="Couldn't delete. Wrong Authorization")

    query = notes_table.delete().where(notes_table.c.id == note_id)

    await db.execute(query)


@router.put('/notes/{note_id}', status_code=204)
async def edit(
    note_id: int,
    updated_note: NoteSchema,
    Authorization: str = Header(...)
):
    """
    The authorization check may be inefficient since it's making 2 queries.
    It might be making the route significantly slower.
    """
    note = await db.fetch_one(
        select(
            [notes_table.c.id, notes_table.c.writer_id]
        ).where(
            notes_table.c.id == note_id
        )
    )

    if note.writer_id != int(Authorization):
        raise HTTPException(403, detail="Couldn't edit. Wrong Authorization.")

    query = notes_table.update(
    ).values(
        **updated_note.dict()
    ).where(
        notes_table.c.id == note_id
    )

    await db.execute(query)
