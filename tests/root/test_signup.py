from tests import client
from pydantic import BaseModel
from requests.models import Response
from app.database import Session
from app.database.models import users_table


class TestCreateUser:

    class ResponseSchema(BaseModel):
        id: int

    def create_user(self) -> Response:
        user = {
            "name": "TestUser",
            "pwd_hash": "0f0f0f0f0f"
        }

        return client.post(url="/", json=user)

    def test_user_signup(self):
        response = self.create_user()

        assert response.status_code == 201
        assert self.ResponseSchema(**response.json())

    def test_if_creates(self):
        response = self.create_user()
        id = response.json()['id']

        db = Session()
        query = users_table.select().where(users_table.c.id == id)
        created_user = db.execute(query).fetchone()

        assert created_user
        assert created_user.name == "TestUser"
        assert created_user.pwd_hash == "0f0f0f0f0f"
