from typing import List

import pytest
from pydantic import create_model

from .fixtures import token_header


@pytest.fixture
def bulk_create_notes(client, token_header, sample_note):
    for i in range(10):
        note = {
            'category': f'test category {i}',
            'subject': f'test subject {i}',
            'body': f'This is the body {i}.'
        }

        response = client.post('/notes', headers=token_header, json=note)
        assert response.ok


@pytest.fixture
def notes_list_model():
    model = create_model('', notes=(List[dict], ...))
    return model


def test_list_notes(client, token_header, bulk_create_notes, notes_list_model):
    response = client.get('/notes', headers=token_header)

    assert (response.status_code == 200)

    assert notes_list_model.validate(response.json())
    notes_list = notes_list_model(**response.json()).notes

    assert (len(notes_list) == 10)


def test_list_user_not_authenticated(client, token_header):
    response = client.get('/notes', headers={
        'Authorization': 'Bearer 12345asdf'
    })

    error_message: str = response.json().get('detail')

    assert (response.status_code == 401)
    assert (error_message == 'Invalid authentication credentials.')


def test_list_user_without_notes(client, token_header, notes_list_model):
    response = client.get('/notes', headers=token_header)

    assert (response.status_code == 200)

    assert notes_list_model.validate(response.json())
    notes_list = notes_list_model(**response.json()).notes

    assert (len(notes_list) == 0)
