from sqlalchemy.orm import Session
from fastapi import Depends, HTTPException
from database import get_db
import models.task as task_model
import schemas.task as task_schemas


"Add task with title and status"
def create_task(task: task_schemas.TaskCreate, db: Session = Depends(get_db)):
    db_task = task_model.Task(title=task.title, done=task.done)
    db.add(db_task)
    db.commit()
    db.refresh(db_task)
    return db_task

"""Read whole tasks from db"""
def read_tasks(db: Session = Depends(get_db)):
    return db.query(task_model.Task)\
            .filter(task_model.Task.deleted == False)\
            .all()

"""Modify whole task by id"""
def update_task(task_id: int, updated_task: task_schemas.TaskCreate, db: Session = Depends(get_db)):
    db_task = db.query(task_model.Task).filter(task_model.Task.id == task_id).first()
    if db_task is None: 
        raise HTTPException(status_code=404, detail="Task not found")
    
    db_task.title = updated_task.title
    db_task.done = updated_task.done

    db.commit()
    db.refresh(db_task)
    return db_task

"""Delete task by marking it as deleted"""
def delete_task(task_id: int, db: Session = Depends(get_db)):
    db_task = db.query(task_model.Task).filter(task_model.Task.id == task_id).first()
    if db_task is None:
        raise HTTPException(status_code=404, detail="Task not found")

    db_task.deleted = True  # Mark as deleted instead of removing from DB
    db.commit()
    db.refresh(db_task)
    return db_task

"""Modify part of task by id"""
def patch_task(task_id: int, updated_task: task_schemas.TaskUpdate, db: Session = Depends(get_db)):
    db_task = db.query(task_model.Task).filter(task_model.Task.id == task_id).first()
    if db_task is None:
        raise HTTPException(status_code=404, detail="Task not found")

    if updated_task.title is not None:
        db_task.title = updated_task.title
    if updated_task.done is not None:
        db_task.done = updated_task.done

    db.commit()
    db.refresh(db_task)
    return db_task
