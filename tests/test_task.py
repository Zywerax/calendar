from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_get_tasks():
    """Fetch all tasks and verify the response"""

    response = client.get("/tasks")
    assert response.status_code == 200
    assert isinstance(response.json(), list)

def test_create_task():
    """Create a new task and verify its creation"""

    payload = {"title": "New Task", "done": False}
    response = client.post("/tasks", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert data["title"] == payload["title"]
    assert data["done"] == payload["done"]
    assert "id" in data

def test_update_task_put():
    """Create a task and then update it using PUT method"""

    payload = {"title": "Task to update", "done": False}
    response = client.post("/tasks/", json=payload)
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
    
    payload = {"title": "Task to patch", "done": False}
    response = client.post("/tasks/", json=payload)
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
    payload = {"title": "Task to delete", "done": False}
    response = client.post("/tasks/", json=payload)
    assert response.status_code == 200
    task_id = response.json()["id"]

    response = client.delete(f"/tasks/{task_id}")
    assert response.status_code == 204  # No content expected on successful deletion

    response = client.get(f"/tasks/{task_id}")
    assert response.status_code == 404 # Task should not be found after deletion