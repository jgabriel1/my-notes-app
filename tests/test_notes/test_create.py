from typing import Callable

import pytest
from pydantic import create_model

from .fixtures import token_header


@pytest.fixture
def validate_response() -> Callable:
    model = create_model('ResponseModel', id=(int, ...))
    return model.validate


def test_create(client, sample_note, token_header, validate_response):
    response = client.post('/notes', headers=token_header, json=sample_note)

    assert (response.status_code == 201)  # Created
    assert validate_response(response.json())


def test_create_no_note_category(client, sample_note, token_header, validate_response):
    note = sample_note.copy()
    note.pop('category')

    response = client.post('/notes', headers=token_header, json=note)

    assert (response.status_code == 201)  # should still create
    assert validate_response(response.json())


def test_create_no_note_subject(client, sample_note, token_header, validate_response):
    note = sample_note.copy()
    note.pop('subject')

    response = client.post('/notes', headers=token_header, json=note)

    assert (response.status_code == 201)  # should still create
    assert validate_response(response.json())


def test_create_no_note_body(client, sample_note, token_header):
    note = sample_note.copy()
    note.pop('body')

    response = client.post('/notes', headers=token_header, json=note)

    # Should require the note body:
    assert (response.status_code == 422)  # Unprocessable Entity


def test_create_for_unauthenticated_user(client, sample_note, token_header):
    response = client.post('/notes', json=sample_note, headers={
        'Authorization': 'Bearer 12345'
    })

    error_message: str = 'Invalid authentication credentials.'

    assert (response.status_code == 401)  # Unauthorized
    assert (response.json().get('detail') == error_message)
