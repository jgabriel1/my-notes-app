from fastapi import Depends, FastAPI
from fastapi.middleware.cors import CORSMiddleware

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


app.add_middleware(
    CORSMiddleware,
    allow_origins=['http://localhost:3000'],
    allow_credentials=True,
    allow_methods=['*'],
    allow_headers=['*'],
)

app.include_router(notes.router)
app.include_router(login.router, prefix='/login')
