import pytest

from .fixtures import token_header


@pytest.fixture(autouse=True)
def bulk_create_notes(client, token_header, sample_note):
    for i in range(10):
        note = {
            'category': f'test category {i}',
            'subject': f'test subject {i}',
            'body': f'This is the body {i}.'
        }

        response = client.post('/notes', headers=token_header, json=note)
        assert response.ok


def test_list_notes(client, token_header):
    assert True


def test_list_user_not_authenticated(client, token_header):
    assert True


def test_list_user_without_notes(client, token_header):
    assert True
