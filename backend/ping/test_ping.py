# Copyright 2022 the author Rodney Sostras. All rights reserved.

from appconfig.core import application
from fastapi.testclient import TestClient

client_testing = TestClient(application)

def test_router_ping():
    response = client_testing.get('/ping')
    assert response.status_code == 200
    assert response.json() == {"message": "pong!!!"}

