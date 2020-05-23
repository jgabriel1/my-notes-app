import time

from .fixtures import validate_token_response


def test_get_new_token(client, sample_user, validate_token_response):
    # Register user:
    register_response = client.post(
        url='/login/register',
        headers={'Content-Type': 'application/json'},
        json=sample_user
    )

    # Wait some time to request a new token, since the encoding is based
    # on current datetime:
    time.sleep(1)

    # Request a new token with form data:
    token_response = client.post(url='/login/token', data=sample_user)

    token_type_is_bearer: bool = token_response.json().get('token_type') == 'bearer'

    assert token_response.status_code == 200
    assert validate_token_response(token_response.json())
    assert token_type_is_bearer

    first_token = register_response.json().get('access_token')
    second_token = token_response.json().get('access_token')

    assert first_token != second_token


def test_send_json_data_to_token(client, sample_user):
    response = client.post(url='/login/token', json=sample_user)

    assert response.status_code == 422  # Unprocessable Entity


def test_request_token_with_wrong_password(client, sample_user):
    # Register user:
    client.post(
        url='/login/register',
        headers={'Content-Type': 'application/json'},
        json=sample_user
    )

    # Change password:
    wrong_password = sample_user.copy()
    wrong_password.update({'password': 'mywrongpassword'})

    # Request a new token for different password:
    token_response = client.post(url='/login/token', data=wrong_password)

    assert token_response.status_code == 401  # Unauthorized


def test_request_token_for_unregistered_user(client, sample_user):
    # Register user:
    client.post(
        url='/login/register',
        headers={'Content-Type': 'application/json'},
        json=sample_user
    )

    # Request a new token for different user:
    token_response = client.post(url='/login/token', data={
        'username': 'different_than_test_username',
        'password': 'different_than_test_password'
    })

    assert token_response.status_code == 401
