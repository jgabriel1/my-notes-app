from typing import List
from pydantic import BaseModel


class NoteSchema(BaseModel):
    category: str = 'Other'
    subject: str = 'No Subject'
    body: str


class ReturnNote(NoteSchema):
    id: int = None


class NotesListSchema(BaseModel):
    notes: List[ReturnNote]


class UserSchema(BaseModel):
    id: int = None
    username: str
    password: str
