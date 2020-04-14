from tests import client


class TestEditNote:

    headers = {
        "Content-Type": "application/json",
        "Authorization": "1234"
    }

    edited_note = {
        "category": "New Category",
        "subject": "New Subject",
        "body": "New Body. This note has been edited."
    }

    def create_note_to_edit(self) -> int:
        created = client.post(
            url="/notes",
            headers=self.headers,
            json={
                "category": "Test Category",
                "subject": "Test Subject",
                "body": "Test Body. This is a sort of long text."
            }
        )

        return created.json()['id']

    def test_regular(self):
        """
        TODO: 
        Check if the note was really updated, since the response
        won't return anything.
        """
        id = self.create_note_to_edit()

        response = client.put(
            url=f"/notes/{id}",
            headers=self.headers,
            json=self.edited_note
        )

        assert response.status_code == 204
        assert not response.json()

    def test_no_header(self):
        id = self.create_note_to_edit()

        response = client.put(
            url=f"/notes/{id}",
            headers={"Content-Type": "application/json"},
            json=self.edited_note
        )

        assert 400 <= response.status_code < 500

    def test_different_id(self):
        """
        TODO:
        It shouldn't allow the user to edit a note they didn't create.
        It should also tell the user that he didn't create that note he's
        trying to edit through an error message.
        """
        id = self.create_note_to_edit()

        response = client.put(
            url=f"/notes/{id}",
            headers={
                "Content-Type": "application/json",
                "Authorization": "4321" # Wrong ID for authorization.
            },
            json=self.edited_note
        )

        assert 400 <= response.status_code < 500
