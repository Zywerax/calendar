from sqlalchemy import Column, Integer, String, Boolean
from database import Base

"""database task model for SQLAlchemy ORM"""
class Task(Base):
    __tablename__ = "tasks"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True)
    done = Column(Boolean, default=False)
    deleted = Column(Boolean, default=False)
