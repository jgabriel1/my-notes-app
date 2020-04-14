from tests import client
from pydantic import BaseModel


class TestCreateNote:

    class Response(BaseModel):
        id: int

    test_note = {
        "category": "Test Category",
        "subject": "Test Subject",
        "body": "Test Body. This is a sort of long text."
    }

    def response(self, without: str):
        note = self.test_note.copy()
        note.pop(without)

        return client.post(
            url="/notes",
            headers={
                "Content-Type": "application/json",
                "Authorization": "1234"
            },
            json=note
        )

    def test_no_category(self):
        response = self.response(without="category")

        assert response.status_code == 201
        assert self.Response(**response.json())

    def test_no_subject(self):
        response = self.response(without="subject")

        assert response.status_code == 201
        assert self.Response(**response.json())

    def test_no_body(self):
        response = self.response(without="body")

        assert 400 <= response.status_code < 500

    def test_no_authorization(self):
        response = client.post(url="/notes", json=self.test_note)

        assert 400 <= response.status_code < 500
