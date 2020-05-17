from fastapi import APIRouter, HTTPException, Depends
from ..crud import crud_notes
from ..schemas import NoteSchema, UserSchema, NotesListSchema
from ..database import get_db, Database
from ..security import get_current_user

router = APIRouter()


@router.get('/notes', response_model=NotesListSchema)
async def list_all(
    user: UserSchema = Depends(get_current_user),
    database: Database = Depends(get_db)
):
    notes_list = await crud_notes.read_all(database, user.id)
    return {'notes': notes_list}


@router.post('/notes', status_code=201)
async def create(
    note: NoteSchema,
    user: UserSchema = Depends(get_current_user),
    database: Database = Depends(get_db)
):
    note_id = await crud_notes.create(database, note, user.id)
    return {'id': note_id}


@router.delete('/notes/{note_id}', status_code=204)
async def delete(
    note_id: int,
    user: UserSchema = Depends(get_current_user),
    database: Database = Depends(get_db)
):
    writer_id = await crud_notes.get_writer_id(database, note_id)

    if not writer_id:
        raise HTTPException(
            404, detail='Note doesn\'t exist or has already been deleted.')

    if writer_id != user.id:
        raise HTTPException(
            403, detail='Couldn\'t delete. Wrong Authorization.')

    await crud_notes.delete(database, note_id)


@router.put('/notes/{note_id}', status_code=204)
async def edit(
    note_id: int,
    updated_note: NoteSchema,
    user: UserSchema = Depends(get_current_user),
    database: Database = Depends(get_db)
):
    writer_id = await crud_notes.get_writer_id(database, note_id)

    if not writer_id:
        raise HTTPException(
            404, detail='Note doesn\'t exist or has already been deleted.')

    if writer_id != user.id:
        raise HTTPException(403, detail='Couldn\'t edit. Wrong Authorization.')

    await crud_notes.update(database, note_id, updated_note)
