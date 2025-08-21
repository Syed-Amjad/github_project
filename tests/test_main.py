import pytest
from app.main import app

@pytest.fixture
def client():
    app.config["TESTING"] = True
    with app.test_client() as client:
        yield client

def test_health(client):
    response = client.get("/health")
    assert response.status_code == 200
    assert response.get_json() == {"status": "ok"}

def test_add(client):
    response = client.get("/add?a=5&b=3")
    assert response.status_code == 200
    assert response.get_json() == {"result": 8}

def test_add_invalid(client):
    response = client.get("/add?a=foo&b=bar")
    assert response.status_code == 400
    assert "error" in response.get_json()

