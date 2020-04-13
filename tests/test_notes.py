from . import client
from pydantic import BaseModel


def test_create_note():
    test_note = {
        "category": "Test Category",
        "subject": "Test Subject",
        "body": "Test Body. This is a sort of long text."
    }

    class Response(BaseModel):
        id: int

    for key in test_note.keys():
        note = test_note.copy()
        note.pop(key)

        response = client.post(
            url="/notes",
            headers={
                "Content-Type": "application/json",
                "Authorization": "1234"
            },
            json=note
        )

        # If body is missing, it shouldn't accept it:
        if key == "body":
            assert response.status_code == 422

        else:
            assert response.status_code == 201
            assert Response(**response.json())


def test_delete_note():
    assert True


def test_edit_note():
    assert True
