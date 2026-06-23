from copy import deepcopy

import pytest
from fastapi.testclient import TestClient

from src import app


@pytest.fixture(scope="function")
def client():
    """Provide a fresh TestClient and restore app state after each test."""
    original_activities = deepcopy(app.activities)
    test_client = TestClient(app.app)
    yield test_client
    app.activities = deepcopy(original_activities)
