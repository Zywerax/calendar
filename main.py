from fastapi import FastAPI
from routes import task as task_routes
from init_db import init_db

app = FastAPI()

init_db() 

app.include_router(task_routes.router)


