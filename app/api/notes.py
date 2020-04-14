from fastapi import APIRouter, Request, Header
from fastapi.responses import JSONResponse
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


@router.delete('/notes/{note_id}', status_code=204)
async def delete(note_id: int, Authorization: str = Header(...)):
    query = notes_table.delete().where(
        (notes_table.c.id == note_id) &
        (notes_table.c.writer_id == Authorization)
    )

    await db.execute(query)


@router.put('/notes/{note_id}', status_code=204)
async def edit(
    note_id: int,
    updated_note: NoteSchema,
    Authorization: str = Header(...)
):
    # Check how to update only values that were sent;
    # Check security! As is, it can update writer_id:
    query = notes_table.update(
    ).values(
        **updated_note.dict()
    ).where(
        (notes_table.c.id == note_id) &
        (notes_table.c.writer_id == Authorization)
    )

    await db.execute(query)
