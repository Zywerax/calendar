from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from database import get_db
import models.task as task_model
import schemas.task as task_schemas
import crud.task as task_crud

router = APIRouter()

"""Add task with title and status"""
@router.post("/task", response_model=task_schemas.Task)
def create_task(task: task_schemas.TaskCreate, db: Session = Depends(get_db)):
    return task_crud.create_task(task=task, db=db)

"""Read whole tasks from db"""
@router.get("/task", response_model=list[task_schemas.Task])
def read_tasks(db: Session = Depends(get_db)):
    return task_crud.read_tasks(db=db)

"""Delete task by marking it as deleted"""
@router.delete("/task/{task_id}", response_model=task_schemas.Task)
def delete_task(task_id: int, db: Session = Depends(get_db)):
    return task_crud.delete_task(task_id=task_id, db=db)

"""Modify whole task by id"""
@router.put("/task/{task_id}", response_model=task_schemas.Task)
def update_task(task_id: int, updated_task: task_schemas.TaskCreate, db: Session = Depends(get_db)):
    return task_crud.update_task(task_id=task_id, updated_task=updated_task, db=db)

"""Modify part of task by id"""
@router.patch("/task/{task_id}", response_model=task_schemas.Task)
def patch_task(task_id: int, updated_task: task_schemas.TaskUpdate, db: Session = Depends(get_db)):
    return task_crud.patch_task(task_id=task_id, updated_task=updated_task, db=db)