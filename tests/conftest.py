import pytest
from databases import Database
from fastapi.testclient import TestClient
from sqlalchemy import create_engine

from app import app
from app.deps import get_db
from app.database import Base

TEST_DATABASE_URL = 'sqlite:///./tests/test_db.sqlite3'


async def get_test_db():
    database = Database(url=TEST_DATABASE_URL)
    return database


@pytest.fixture(scope='session', autouse=True)
def override_db():
    app.dependency_overrides[get_db] = get_test_db


@pytest.fixture(scope='function', autouse=True)
def reset_db():
    test_engine = create_engine(
        TEST_DATABASE_URL,
        connect_args={'check_same_thread': False}
    )

    Base.metadata.drop_all(test_engine)
    Base.metadata.create_all(test_engine)


@pytest.fixture(scope='session')
def client() -> TestClient:
    return TestClient(app)


@pytest.fixture
def sample_user() -> dict:
    return {
        'username': 'test_username',
        'password': 'mypassword123'
    }


@pytest.fixture
def sample_note() -> dict:
    return {
        'category': 'test category',
        'subject': 'test subject',
        'body': 'This is the body.'
    }
