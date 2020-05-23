from typing import List, Optional

from databases import Database
from sqlalchemy.sql import select

from ..database import Note, notes_table
from ..schemas import NoteSchema, ReturnNote


async def create(database: Database, note: NoteSchema, user_id: int) -> int:
    query = notes_table.insert().values(
        **note.dict(),
        writer_id=user_id
    )
    note_id: int = await database.execute(query)
    return note_id


async def read_all(database: Database, user_id: int) -> List[ReturnNote]:
    query = notes_table.select().where(
        notes_table.c.writer_id == user_id
    )
    notes_list: List[Note] = await database.fetch_all(query)
    return [ReturnNote(**note) for note in notes_list]


async def update(
        database: Database, note_id: int, updated_note: NoteSchema) -> None:
    query = notes_table.update().values(
        **updated_note.dict()
    ).where(
        notes_table.c.id == note_id
    )
    await database.execute(query)


async def delete(database: Database, note_id: int) -> None:
    query = notes_table.delete().where(notes_table.c.id == note_id)
    await database.execute(query)


async def get_writer_id(database: Database, note_id: int) -> Optional[int]:
    query = select([
        notes_table.c.writer_id
    ]).where(
        notes_table.c.id == note_id
    )
    note = await database.fetch_one(query)

    if note is not None:
        return note.writer_id
