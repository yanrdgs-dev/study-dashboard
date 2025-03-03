from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_create_task():
    data = {
        "title": "Tarefa Teste",
        "description": "Descrição da tarefa teste",
        "done": False
    }
    
    response = client.post("/tasks/", json=data)
    
    assert response.status_code == 201
    
    assert response.json()["title"] == data["title"]
    
def test_get_single_task():
    data = {
        "title": "Tarefa Teste",
        "description": "Descrição da tarefa teste",
        "done": False
    }
    
    create_response = client.post("/tasks/", json=data)
    task_id = create_response.json()["id"]
    
    response = client.get(f"/tasks/{task_id}/")
    
    assert response.status_code == 200
    
    assert response.json()["id"] == task_id
    
def test_get_all_tasks():
    data = {
        "title": "Tarefa Teste",
        "description": "Descrição da tarefa teste",
        "done": False
    }
    
    client.post("/tasks/", json=data)
    
    response = client.get("/tasks/")
    
    assert response.status_code == 200
    
    assert len(response.json()) > 0
    
def test_update_task():
    data = {
        "title": "Tarefa Teste",
        "description": "Descrição da tarefa teste",
        "done": False
    }
    
    create_response = client.post("/tasks/", json=data)
    task_id = create_response.json()["id"]
    
    data["title"] = "Tarefa Teste Atualizada"
    
    response = client.put(f"/tasks/{task_id}/", json=data)
    
    assert response.status_code == 200
    
    assert response.json()["title"] == data["title"]
    
def test_delete_task():
    data = {
        "title": "Tarefa Teste",
        "description": "Descrição da tarefa teste",
        "done": False
    }
    
    create_response = client.post("/tasks/", json=data)
    task_id = create_response.json()["id"]
    
    response = client.delete(f"/tasks/{task_id}/")
    
    assert response.status_code == 204
    
    get_response = client.get(f"/tasks/{task_id}/")
    
    assert get_response.status_code == 404