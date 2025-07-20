from fastapi.testclient import TestClient
from app.main import app
from faker import Faker

fake = Faker()

client = TestClient(app)

def generate_fake_user():
    return {
        "username": fake.user_name(),
        "password": fake.password(),
        "email": fake.unique.email()
    }

def test_register_user():
    """Register a new user and verify the response"""
    
    payload = generate_fake_user()

    response = client.post("/register", json=payload)
    assert response.status_code == 201
    data = response.json()
    assert data["email"] == payload["email"]
    assert data["username"] == payload["username"]
    assert "password" not in data

def test_login_user():
    """Login with the registered user and verify the response"""
    payload = {
        "email": "test1333user@example.com",
        "password": "testpass1"
    }

    response = client.post("/login", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "access_token" in data
    assert data["token_type"] == "bearer"