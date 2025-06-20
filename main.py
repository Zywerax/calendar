from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
import models, schemas
from database import engine, SessionLocal

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

# Dependency – tworzenie sesji DB
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

"Add task with title and status"
@app.post("/tasks", response_model=schemas.Task)
def create_task(task: schemas.TaskCreate, db: Session = Depends(get_db)):
    db_task = models.Task(title=task.title, done=task.done)
    db.add(db_task)
    db.commit()
    db.refresh(db_task)
    return db_task

"Read whole tasks from db"
@app.get("/tasks", response_model=list[schemas.Task])
def read_tasks(db: Session = Depends(get_db)):
    return db.query(models.Task)\
            .filter(models.Task.deleted == False)\
            .all()


"Modify task whole task"
@app.put("/tasks/{task_id}", response_model=schemas.Task)
def update_task(task_id: int, updated_task: schemas.TaskCreate, db: Session = Depends(get_db)):
    db_task = db.query(models.Task).filter(models.Task.id == task_id).first()
    if db_task is None: 
        raise HTTPException(status_code=404, detail="Task not found")
    
    db_task.title = updated_task.title
    db_task.done = updated_task.done

    db.commit()
    db.refresh(db_task)
    return db_task

"Delete task by marking it as deleted"
@app.delete("/tasks/{task_id}", response_model=schemas.Task)
def delete_task(task_id: int, db: Session = Depends(get_db)):
    db_task = db.query(models.Task).filter(models.Task.id == task_id).first()
    if db_task is None:
        raise HTTPException(status_code=404, detail="Task not found")

    db_task.deleted = True  # Mark as deleted instead of removing from DB
    db.commit()
    db.refresh(db_task)
    return db_task

"patch status of task or fragment of task"
@app.patch("/tasks/{task_id}", response_model=schemas.Task)
def patch_task(task_id: int, updated_task: schemas.TaskUpdate, db: Session = Depends(get_db)):
    db_task = db.query(models.Task).filter(models.Task.id == task_id).first()
    if db_task is None:
        raise HTTPException(status_code=404, detail="Task not found")

    if updated_task.title is not None:
        db_task.title = updated_task.title
    if updated_task.done is not None:
        db_task.done = updated_task.done

    db.commit()
    db.refresh(db_task)
    return db_task