from tests import client
from app.schemas import ReturnNote
from typing import List


class TestUserLogin:

    user = {"name": "TestUser", "pwd_hash": "0f0f0f0f0f"}

    @staticmethod
    def create_notes_for_user(id: int, bulk: int = 1):
        for i in range(bulk):
            headers = {"Authorization": str(id)}
            note = {"body": f"Test Note {i}"}
            client.post("/notes", headers=headers, json=note)

    def create_user_id(self) -> int:
        response = client.post("/", json=self.user)

        return response.json().get('id')

    def test_expected(self):
        id = self.create_user_id()
        self.create_notes_for_user(id, 10)

        response = client.get("/", json=self.user)
        notes_list = response.json()

        assert response.status_code == 200
        assert isinstance(notes_list, list)
        assert ReturnNote(**notes_list[0])

        assert len(notes_list) == 10
        assert notes_list[-1]["body"] == "Test Note 9"

    def test_wrong_password(self):
        self.create_user_id()
        wrong_pwd = {"name": "TestUser", "pwd_hash": "0f0f0fff"}

        response = client.get("/", json=wrong_pwd)

        assert response.status_code == 401
        assert response.json() == {"Error": "Wrong Password!"}

    def test_not_signedup(self):
        not_signed_user = {"name": "Timmy", "pwd_hash": "1234"}

        response = client.get("/", json=not_signed_user)

        assert response.status_code == 403
        assert response.json() == {
            "Error": "You're not signed up! Create an account first."
        }
