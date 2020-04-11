from pydantic import BaseModel


class NoteSchema(BaseModel):
    category: str = 'Other'
    subject: str = 'No Subject'
    body: str


class UserSchema(BaseModel):
    id: int
