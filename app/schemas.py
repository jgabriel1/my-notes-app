from pydantic import BaseModel


class NoteSchema(BaseModel):
    category: str = 'Other'
    subject: str = 'No Subject'
    body: str


class UserSchema(BaseModel):
    name: str
    pwd_hash: str
