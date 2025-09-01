from sqlalchemy import Column, Integer, String, Boolean, NVARCHAR
from sqlalchemy.orm import relationship
from app.database import Base

'''database task model for SQLAlchemy ORM'''
class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    username = Column(NVARCHAR(30), unique=True, index=True)
    email = Column(NVARCHAR(100), unique=True, index=True)
    hashed_password = Column(String)
    is_active = Column(Boolean, default=True)
    is_superuser = Column(Boolean, default=False)
    
    # relationship to Task
    tasks = relationship("Task", back_populates="user")