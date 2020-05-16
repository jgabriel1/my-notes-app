from fastapi import Depends
from databases import Database
from sqlalchemy.sql import select
from typing import List
from app.database import notes_table, Note
from app.schemas import ReturnNote, NoteSchema


async def create(database: Database, note: NoteSchema, user_id: int) -> int:
    query = notes_table.insert().values(
        **note.dict(),
        writer_id=user_id
    )
    note_id: int = await database.execute(query)
    return note_id


async def read_all(database: Database, user_id: int) -> List[Note]:
    query = notes_table.select().where(
        notes_table.c.writer_id == user_id
    )
    notes_list: List[Note] = await database.fetch_all(query)
    return notes_list


async def update(
        database: Database, note_id: int, updated_note: ReturnNote) -> None:
    query = notes_table.update(
    ).values(
        **updated_note.dict()
    ).where(
        notes_table.c.id == note_id
    )
    return await database.execute(query)


async def delete(database: Database, note_id: int) -> None:
    query = notes_table.delete().where(notes_table.c.id == note_id)
    return await database.execute(query)


async def get_writer_id(database: Database, note_id: int) -> int:
    query = select([
        notes_table.c.writer_id
    ]).where(
        notes_table.c.id == note_id
    )
    note = await database.fetch_one(query)
    return note.writer_id
