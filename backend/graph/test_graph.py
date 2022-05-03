# Copyright 2022 the author Rodney Sostras. All rights reserved.

from cgitb import text
from appconfig.core import application
from appconfig.database_test import dependency_overrides
from fastapi.testclient import TestClient

app = dependency_overrides(application)

client_testing = TestClient(app)

def test_create_user():
    response = client_testing.post(
        "/graph",
        json={"data": [
            {"source": "A", "target": "B", "distance": 5},
            {"source": "B", "target": "C", "distance": 4}
        ]}
    )
    
    assert response.status_code == 201, response.text
