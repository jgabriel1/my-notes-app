from fastapi import APIRouter
from app.schemas import NoteSchema
from app.database import db
from app.database.models import Note

router = APIRouter()


@router.post('/notes', status_code=204)
async def create(note: NoteSchema):
    query = """
        INSERT INTO notes (
            category,
            subject,
            body,
            writer_id
        ) VALUES (
            :category,
            :subject,
            :body,
            :writer_id
        )
    """
    await db.execute(
        query=query,
        values=note.dict()
    )
    return
