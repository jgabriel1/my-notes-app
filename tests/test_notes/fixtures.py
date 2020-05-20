import pytest


@pytest.fixture
def token_header(client, sample_user) -> dict:
    response = client.post(
        url='/login/register',
        headers={'Content-Type': 'application/json'},
        json=sample_user
    )
    assert response.ok

    token: str = response.json().get('access_token')
    token_header = {'Authorization': f'Bearer {token}'}

    return token_header


@pytest.fixture
def created_note_id(client, sample_note, token_header) -> int:
    """
    This fixture creates a note to be used for deletion or editing testing.
    It already returns the id of the created note to be used on tests.
    """
    creation_response = client.post(
        url='/notes', headers=token_header, json=sample_note
    )
    assert creation_response.ok

    note_id: int = creation_response.json().get('id')
    return note_id


@pytest.fixture
def bulk_create_notes():
    pass
