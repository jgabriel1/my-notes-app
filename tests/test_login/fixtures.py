from typing import Callable

import pytest
from pydantic import create_model


@pytest.fixture
def validate_token_response() -> Callable:
    model = create_model('TokenModel', field_definitions={
        'access_token': (str, ...),
        'token_type': (str, ...)
    })
    return model.validate
