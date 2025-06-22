from fastapi import FastAPI
from app.routers import task as task_routes
from app.init_db import init_db

app = FastAPI()

init_db() 

app.include_router(task_routes.router)


