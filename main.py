from fastapi import FastAPI
from pydantic import BaseModel
from typing import List
from datetime import datetime, date

app = FastAPI()

# Model danych (opisuje jak wygląda zadanie)
class Task(BaseModel):
    id: int
    title: str
    date: date
    done: bool = False

# "Baza danych" w pamięci – lista zadań
tasks: List[Task] = []

# GET: pobierz wszystkie zadania
@app.get("/tasks")
def get_tasks():
    return tasks

# POST: dodaj nowe zadanie
@app.post("/tasks")
def create_task(task: Task):
    tasks.append(task)
    return {"message": "Zadanie dodane", "task": task}

# PUT: edytuj zadanie
@app.put("/tasks/{task_id}")
def update_task(task_id: int, updated_task: Task):
    for i, task in enumerate(tasks):
        if task.id == task_id:
            tasks[i] = updated_task
            return {"message": "Zaktualizowano", "task": updated_task}
    return {"error": "Nie znaleziono zadania"}

# DELETE: usuń zadanie
@app.delete("/tasks/{task_id}")
def delete_task(task_id: int):
    global tasks
    tasks = [task for task in tasks if task.id != task_id]
    return {"message": f"Zadanie {task_id} usunięte"}
