from .fixtures import sample_note, token_header


def test_create(client, sample_note, token_header):
    response = client.post('/notes', headers=token_header, json=sample_note)

    assert (response.status_code == 201)  # Created
    assert ('id' in response.json().keys())  # response carries id
    assert isinstance(response.json().get('id'), int)  # id is an integer


def test_create_no_note_category(client, sample_note, token_header):
    note = sample_note.copy()
    note.pop('category')

    response = client.post('/notes', headers=token_header, json=note)

    assert (response.status_code == 201)  # should still create
    assert ('id' in response.json().keys())
    assert isinstance(response.json().get('id'), int)


def test_create_no_note_subject(client, sample_note, token_header):
    note = sample_note.copy()
    note.pop('subject')

    response = client.post('/notes', headers=token_header, json=note)

    assert (response.status_code == 201)  # should still create
    assert ('id' in response.json().keys())
    assert isinstance(response.json().get('id'), int)


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
