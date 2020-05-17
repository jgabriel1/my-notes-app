from fastapi import FastAPI, Depends
from .database import get_db, Database
from .api import notes, login

app = FastAPI()


@app.on_event('startup')
async def startup():
    database: Database = await get_db()
    await database.connect()


@app.on_event('shutdown')
async def shutdown():
    database: Database = await get_db()
    await database.disconnect()


app.include_router(notes.router)
app.include_router(login.router)
