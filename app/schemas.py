from pydantic import BaseModel


class NoteSchema(BaseModel):
    category: str = 'Other'
    subject: str = 'No Subject'
    body: str


class ReturnNote(NoteSchema):
    id: int = None


class UserSchema(BaseModel):
    username: str
    password: str


class UserRegister(BaseModel):
    username: str
    password: str
