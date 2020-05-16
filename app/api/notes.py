from fastapi import APIRouter, HTTPException, Depends
from typing import List
from app.crud import crud_notes
from app.schemas import NoteSchema, ReturnNote, UserSchema
from app.database import db
from app.security import get_current_user

router = APIRouter()


@router.get('/notes', response_model=List[ReturnNote])
async def list_all(user: UserSchema = Depends(get_current_user)):
    notes_list = await crud_notes.read_all(db, user.id)
    return notes_list


@router.post('/notes', status_code=201)
async def create(note: NoteSchema, user: UserSchema = Depends(get_current_user)):
    note_id = await crud_notes.create(db, note, user.id)
    return {'id': note_id}


@router.delete('/notes/{note_id}', status_code=204)
async def delete(note_id: int, user: UserSchema = Depends(get_current_user)):
    try:
        writer_id = await crud_notes.get_writer_id(db, note_id)
    except AttributeError:
        raise HTTPException(
            404, detail='Note doesn\'t exist or has already been deleted')

    if writer_id != user.id:
        raise HTTPException(
            403, detail="Couldn't delete. Wrong Authorization.")

    await crud_notes.delete(db, note_id)


@router.put('/notes/{note_id}', status_code=204)
async def edit(
    note_id: int,
    updated_note: NoteSchema,
    user: UserSchema = Depends(get_current_user)
):
    try:
        writer_id = await crud_notes.get_writer_id(db, note_id)
    except AttributeError:
        raise HTTPException(
            404, detail='Note doesn\'t exist or has already been deleted')

    if writer_id != user.id:
        raise HTTPException(403, detail='Couldn\'t edit. Wrong Authorization.')

    await crud_notes.update(db, note_id, updated_note)
