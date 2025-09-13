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

global_payload = generate_fake_user()

def test_get_tasks():
    """Fetch all tasks and verify the response"""

    response = client.get("/tasks")
    assert response.status_code == 200
    assert isinstance(response.json(), list)

def test_create_task():
    """Create a new task and verify its creation"""


    register_payload = {
        "username": global_payload.get("username"),
        "password": global_payload.get("password"),
        "email": global_payload.get("email")
    }
    response = client.post("/register", json=register_payload)
    assert response.status_code == 201
    login_payload = {
        "email": global_payload.get("email"),
        "password": global_payload.get("password")
    }

    response = client.post("/login", json=login_payload)
    print("Login response:", response.json())
    assert response.status_code == 200
    access_token = response.json().get("access_token")
    assert access_token is not None, "No access token in response"
    payload = {"title": "New Task", "done": False}
    response = client.post("/tasks", json=payload, params={"token": access_token})
    print(response.json())
    assert response.status_code == 200
    data = response.json()
    assert data["title"] == payload["title"]
    assert data["done"] == payload["done"]
    assert "id" in data

def test_update_task_put():
    """Create a task and then update it using PUT method"""

    login_payload = {
        "email": global_payload.get("email"),
        "password": global_payload.get("password")
    }
    response = client.post("/login", json=login_payload)
    assert response.status_code == 200
    access_token = response.json().get("access_token")

    payload = {"title": "Task to delete", "done": False}
    response = client.post("/tasks/", json=payload, params={"token": access_token})
    assert response.status_code == 200
    task_id = response.json()["id"]

    updated_payload = {"title": "Updated task", "done": True}
    response = client.put(f"/tasks/{task_id}", json=updated_payload)
    assert response.status_code == 200
    data = response.json()

    assert data["title"] == updated_payload["title"]
    assert data["done"] is True

def test_update_task_patch():
    """Create a task and then partially update it using PATCH method"""
    login_payload = {
        "email": global_payload.get("email"),
        "password": global_payload.get("password")
    }
    response = client.post("/login", json=login_payload)
    assert response.status_code == 200
    access_token = response.json().get("access_token")

    payload = {"title": "Task to delete", "done": False}
    response = client.post("/tasks/", json=payload, params={"token": access_token})
    assert response.status_code == 200
    task_id = response.json()["id"]

    patch_payload = {"done": True}
    response = client.patch(f"/tasks/{task_id}", json=patch_payload)
    assert response.status_code == 200
    data = response.json()

    assert data["done"] is True
    assert data["title"] == payload["title"]

def test_delete_task():
    """Create a task and then delete it, verifying it no longer exists"""
    login_payload = {
        "email": global_payload.get("email"),
        "password": global_payload.get("password")
    }
    response = client.post("/login", json=login_payload)
    assert response.status_code == 200
    access_token = response.json().get("access_token")
    
    payload = {"title": "Task to delete", "done": False}
    response = client.post("/tasks/", json=payload, params={"token": access_token})
    print(response.json())
    assert response.status_code == 200
    task_id = response.json()["id"]

    response = client.delete(f"/tasks/{task_id}")
    assert response.status_code == 204  # No content expected on successful deletion

    response = client.get(f"/tasks/{task_id}")
    assert response.status_code == 404 # Task should not be found after deletion