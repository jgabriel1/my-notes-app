from typing import Callable

import pytest
from pydantic import BaseModel


@pytest.fixture
def validate_token_response() -> Callable:

    class ResponseModel(BaseModel):
        access_token: str
        token_type: str

    return ResponseModel.validate
