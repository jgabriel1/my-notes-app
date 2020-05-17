from app import app
from app.deps import get_db
from fastapi.testclient import TestClient
from databases import Database


async def get_test_db():
    database = Database(
        url='sqlite:///./tests/test_db.sqlite3',
        force_rollback=True
    )
    return database

app.dependency_overrides[get_db] = get_test_db

client = TestClient(app)
