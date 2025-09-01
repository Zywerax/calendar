from sqlalchemy import Column, Integer, String, Boolean, ForeignKey, NVARCHAR
from sqlalchemy.orm import relationship
from app.database import Base

"""database task model for SQLAlchemy ORM"""
class Task(Base):
    __tablename__ = "tasks"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(NVARCHAR(150), index=True)
    done = Column(Boolean, default=False)
    deleted = Column(Boolean, default=False)
    
    # Relationship to User
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    
    user = relationship("User", back_populates="tasks")
