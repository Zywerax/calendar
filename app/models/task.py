from sqlalchemy import Column, Integer, String, Boolean, ForeignKey, NVARCHAR
from sqlalchemy.orm import relationship, Mapped, mapped_column
from app.database import Base

"""database task model for SQLAlchemy ORM"""
class Task(Base):
    __tablename__ = "tasks"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True)
    title: Mapped[str] = mapped_column(NVARCHAR(150), index=True)
    done: Mapped[bool] = mapped_column(Boolean, default=False)
    deleted: Mapped[bool] = mapped_column(Boolean, default=False)

    # Relationship to User
    user_id: Mapped[int] = mapped_column(Integer, ForeignKey("users.id"), nullable=False)

    user = relationship("User", back_populates="tasks")
