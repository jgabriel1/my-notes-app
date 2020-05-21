from fastapi import Depends, FastAPI

from .api import login, notes
from .deps import Database, get_db

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
app.include_router(login.router, prefix='/login')
