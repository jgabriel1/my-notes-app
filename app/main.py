from fastapi import FastAPI
from app.database import db
from app.api import notes, users

app = FastAPI()


@app.on_event('startup')
async def startup():
    await db.connect()


@app.on_event('shutdown')
async def shutdown():
    await db.disconnect()


app.include_router(notes.router)
app.include_router(users.router)
