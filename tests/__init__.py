from app import app
from fastapi.testclient import TestClient
from pydantic import BaseModel

client = TestClient(app)


def test_create_note():

    test_notes = {
        "no_category": {
            "subject": "Test Subject",
            "body": "Test Body. This is a sort of long text."
        },
        "no_subject": {
            "category": "Test Category",
            "body": "Test Body. This is a sort of long text."
        },
        "no_body": {
            "category": "Test Category",
            "subject": "Test Subject",
        }
    }

    class Response(BaseModel):
        id: int

    for situation in test_notes.keys():
        response = client.post(
            url="/notes",
            headers={
                "Content-Type": "application/json",
                "Authorization": "1234"
            },
            json=test_notes[situation]
        )

        if situation != "no_body":
            assert response.status_code == 201
            assert Response(**response.json())
        else:
            assert response.status_code == 422
