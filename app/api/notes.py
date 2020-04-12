from typing import List
from fastapi import APIRouter, Request, Body
from fastapi.responses import JSONResponse
from app.schemas import NoteSchema
from app.database import db
from app.database.models import notes_table

router = APIRouter()


@router.get('/notes', response_model=List[NoteSchema])
async def view(user_id: int = Body(..., embed=True)):
    query = notes_table.select().where(notes_table.c.writer_id == user_id)

    return await db.fetch_all(query)


@router.post('/notes', status_code=201)
async def create(note: NoteSchema, request: Request):
    try:
        writer_id = request.headers['Authorization']
    except KeyError:
        return JSONResponse({
            "Error": "Missing Writer ID on headers."
        }, status_code=403)

    query = notes_table.insert().values(
        **note.dict(),
        writer_id=writer_id
    )

    return {
        "id": await db.execute(query)
    }


@router.delete('/notes/{note_id}', status_code=204)
async def delete(note_id: int, request: Request):
    # Problem: this deletes even if the id doesn't match
    query = notes_table.delete().where(
        notes_table.c.id == note_id and
        notes_table.c.writer_id == request.headers['Authorization']
    )

    return await db.execute(query)
