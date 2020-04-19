from tests import client
from app.database import Session
from app.database.models import notes_table


class TestDeleteNote:

    headers = {
        "Content-Type": "application/json",
        "Authorization": "1234"
    }

    def create_note_to_delete(self) -> int:
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

    def test_expected(self):
        id = self.create_note_to_delete()

        response = client.delete(url=f"/notes/{id}", headers=self.headers)

        assert response.status_code == 204
        assert not response.json()

    def test_if_deletes(self):
        id = self.create_note_to_delete() 

        response = client.delete(url=f"/notes/{id}", headers=self.headers)

        db = Session()
        query = notes_table.select().where(notes_table.c.id == id)
        still_exists = db.execute(query).fetchone()

        assert response.status_code == 204
        assert not still_exists

    def test_no_authorization(self):
        id = self.create_note_to_delete()

        response = client.delete(
            url=f"/notes/{id}",
            headers={"Content-Type": "application/json"}
        )

        assert 400 <= response.status_code < 500

    def test_wrong_id(self):
        """
        It shouldn't allow the user to delete a note they didn't create.
        It should also tell the user that he didn't create that note he's
        trying to delete through an error message.
        """
        id = self.create_note_to_delete()

        response = client.delete(
            url=f"/notes/{id}",
            headers={
                "Content-Type": "application/json",
                "Authorization": "4321"
            }
        )

        assert 400 <= response.status_code < 500
