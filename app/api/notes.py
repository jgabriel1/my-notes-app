from fastapi import APIRouter, Request
from fastapi.responses import JSONResponse
from app.schemas import NoteSchema
from app.database import db
from app.database.models import notes_table

router = APIRouter()


@router.post('/notes', status_code=201)
async def create(note: NoteSchema, request: Request):

    # Turn this into a decorator that checks authorization header:
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
    query = notes_table.delete().where(
        (notes_table.c.id == note_id) &
        (notes_table.c.writer_id == request.headers['Authorization'])
    )

    return await db.execute(query)


@router.put('/notes/{note_id}', status_code=204)
async def edit(
    note_id: int,
    updated_note: NoteSchema,
    request: Request
):
    # Check security. As is, it can update writer_id:
    query = notes_table.update(
    ).values(
        **updated_note.dict()
    ).where(
        (notes_table.c.id == note_id) &
        (notes_table.c.writer_id == request.headers['Authorization'])
    )

    return await db.execute(query)
