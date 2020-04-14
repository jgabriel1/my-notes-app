from tests import client


class TestDeleteNote:

    @staticmethod
    def create_note_to_delete() -> int:
        created = client.post(
            url="/notes",
            headers={
                "Content-Type": "application/json",
                "Authorization": "1234"
            },
            json={
                "category": "Test Category",
                "subject": "Test Subject",
                "body": "Test Body. This is a sort of long text."
            }
        )

        return created.json()['id']

    def test_regular(self):
        id = self.create_note_to_delete()

        response = client.delete(
            url=f"/notes/{id}",
            headers={
                "Content-Type": "application/json",
                "Authorization": "1234"
            }
        )

        assert response.status_code == 204
        assert not response.json()

    def test_no_authorization(self):
        id = self.create_note_to_delete()

        response = client.delete(
            url=f"/notes/{id}",
            headers={"Content-Type": "application/json"}
        )
        
        assert 400 <= response.status_code < 500

    def test_different_id(self):
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
