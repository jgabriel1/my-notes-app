import pytest

from .fixtures import created_note_id, token_header


@pytest.fixture
def edited_note():
    return {
        'category': 'test edited category',
        'subject': 'test edited subject',
        'body': 'This body has been edited for test purposes.'
    }


def test_edit_note(client, token_header, created_note_id, edited_note):
    response = client.put(
        f'/notes/{created_note_id}', headers=token_header, json=edited_note
    )

    assert (response.status_code == 204)  # No content
    assert not response.json()


def test_edit_inexistent_note(client, token_header, edited_note):
    arbitrary_note_id: int = 42

    response = client.put(
        f'/notes/{arbitrary_note_id}', headers=token_header, json=edited_note
    )
    error_message: str = response.json().get('detail')

    assert (response.status_code == 404)
    assert (error_message == 'Not Found')


def test_edit_with_wrong_authorization(client, created_note_id, edited_note):
    # Create new user:
    new_user_creation = client.post(url='/login/register', headers={
        'Content-Type': 'application/json'
    }, json={
        'username': 'different_username', 'password': 'newpass123'
    })
    assert new_user_creation.ok

    new_user_token: str = new_user_creation.json().get('access_token')
    new_user_header = {'Authorization': f'Bearer {new_user_token}'}

    # Attempt to edit note:
    response = client.put(
        f'/notes/{created_note_id}', json=edited_note, headers=new_user_header
    )
    error_message: str = response.json().get('detail')

    assert (response.status_code == 403)  # Unauthorized
    assert (error_message == 'Couldn\'t edit. Wrong Authorization.')
