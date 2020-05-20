from .fixtures import token_header, created_note_id


def test_delete_note(client, token_header, created_note_id):
    deletion_response = client.delete(
        url=f'/notes/{created_note_id}', headers=token_header
    )

    assert (deletion_response.status_code == 204)  # No content.
    assert not deletion_response.json()


def test_delete_already_deleted_note(client, token_header, created_note_id):
    # Delete the note:
    first_deletion_attempt = client.delete(
        url=f'/notes/{created_note_id}', headers=token_header
    )
    assert first_deletion_attempt.ok

    # Attempt to delete it again:
    second_deletion_attempt = client.delete(
        url=f'/notes/{created_note_id}', headers=token_header
    )
    error_message: str = second_deletion_attempt.json().get('detail')

    assert (second_deletion_attempt.status_code == 404)  # Couldn't find note
    assert (error_message == 'Not Found')


def test_delete_never_created_note(client, token_header):
    arbitrary_note_id: int = 42

    deletion_attempt = client.delete(
        url=f'/note/{arbitrary_note_id}', headers=token_header
    )
    error_message: str = deletion_attempt.json().get('detail')

    assert (deletion_attempt.status_code == 404)  # Couldn't find note
    assert (error_message == 'Not Found')


def test_delete_with_wrong_authorization(client, token_header, created_note_id):
    # Attempt to delete note with wrong credentials:
    deletion_attempt = client.delete(
        url=f'/notes/{created_note_id}', headers={'Authorization': 'Bearer 12345'}
    )
    error_message: str = deletion_attempt.json().get('detail')

    assert (deletion_attempt.status_code == 401)  # Unauthorized
    assert (error_message == 'Invalid authentication credentials.')
