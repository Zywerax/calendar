from pydantic import BaseModel
from typing import Optional

""" Base model for task schemas """
class TaskBase(BaseModel):
    title: str
    done: bool = False

"""clases used to create task"""
class TaskCreate(TaskBase):
    pass

"""clases used to create task"""
class Task(TaskBase):
    id: int

    model_config = {
        "from_attributes": True,  # odpowiada orm_mode = True
    }

"""clases used to update task"""
class TaskUpdate(BaseModel):
    title: Optional[str] = None # Optional allows the field to be omitted
    done: Optional[bool] = None # Optional allows the field to be omitted

    model_config = {
        "from_attributes": True,  # odpowiada orm_mode = True
    }

Task.model_rebuild()