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
def sample_note() -> dict:
    return {
        'category': 'test category',
        'subject': 'test subject',
        'body': 'This is the body.'
    }
