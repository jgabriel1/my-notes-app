from .fixtures import validate_token_response


def test_register_user(client, sample_user, validate_token_response):
    response = client.post(
        url='/login/register',
        headers={'Content-Type': 'application/json'},
        json=sample_user
    )
    json_response = response.json()

    assert response.status_code == 201
    assert validate_token_response(json_response)
    assert json_response.get('token_type') == 'bearer'


def test_username_already_taken(client, sample_user):
    first_registry = client.post(
        url='/login/register',
        headers={'Content-Type': 'application/json'},
        json=sample_user
    )

    assert first_registry.status_code == 201

    taken_username = sample_user.get('username')

    second_registry = client.post(
        url='/login/register',
        headers={'Content-Type': 'application/json'},
        json={
            'username': taken_username,
            'password': 'different_password123'
        }
    )

    # Response code should still be OK, since the request was successfully
    # processed. However, the response message should behave as if an error
    # had occurred, showing the username was already taken.

    assert second_registry.status_code == 200
    assert second_registry.json() == {
        'detail': f'The username {taken_username} is already taken.'
    }
