import pytest

from app.models import User


def test_health_check(client):
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json["status"] == "healthy"


def test_create_user(client):
    response = client.post("/users", json={"email": "test@example.com"})
    assert response.status_code == 201
    assert "id" in response.json
    assert response.json["email"] == "test@example.com"


def test_get_users(client):
    # Create a user first
    client.post("/users", json={"email": "test@example.com"})

    response = client.get("/users")
    assert response.status_code == 200
    assert len(response.json) == 1
    assert response.json[0]["email"] == "test@example.com"


def test_create_user_without_email(client):
    response = client.post("/users", json={})
    assert response.status_code == 400
    assert "error" in response.json
