from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.auth.deps import get_current_user
from app.database import get_db
import app.models.task as task_model
from app.models.user_model import User
import app.schemas.task as task_schemas
import app.crud.task as task_crud

router = APIRouter()

"""Add task with title and status"""
@router.post("/tasks", response_model=task_schemas.Task)
def create_task(task: task_schemas.TaskCreate, 
                db: Session = Depends(get_db), 
                current_user: User = Depends(get_current_user)):
    return task_crud.create_task(task=task, db=db, current_user=current_user)

"""Read whole tasks from db"""
@router.get("/tasks", response_model=list[task_schemas.Task])
def read_tasks(db: Session = Depends(get_db)):
    return task_crud.read_tasks(db=db)

"""Read task by if not returns 404"""
@router.get("/tasks/{task_id}", response_model=task_schemas.Task)
def read_task_by_id(task_id: int, db: Session = Depends(get_db)):
    task = task_crud.read_task_by_id(task_id=task_id, db=db)
    if not task:
        raise HTTPException(status_code=404, detail="Task not found")
    return task

"""Delete task by marking it as deleted"""
@router.delete("/tasks/{task_id}", response_model=task_schemas.Task)
def delete_task(task_id: int, db: Session = Depends(get_db)):
    return task_crud.delete_task(task_id=task_id, db=db)

"""Modify whole task by id"""
@router.put("/tasks/{task_id}", response_model=task_schemas.Task)
def update_task(task_id: int, updated_task: task_schemas.TaskCreate, db: Session = Depends(get_db)):
    return task_crud.update_task(task_id=task_id, updated_task=updated_task, db=db)

"""Modify part of task by id"""
@router.patch("/tasks/{task_id}", response_model=task_schemas.Task)
def patch_task(task_id: int, updated_task: task_schemas.TaskUpdate, db: Session = Depends(get_db)):
    return task_crud.patch_task(task_id=task_id, updated_task=updated_task, db=db)