from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.database import get_db
import app.models.user_model as user_model
import app.schemas.user_schemas as user_schemas
import app.crud.user_crud as user_crud

router = APIRouter()

"""Register a new user"""
@router.post("/register", response_model=user_schemas.UserOut, status_code=201)
def register_user(user: user_schemas.UserCreate, db: Session = Depends(get_db)):
    existing_user = user_crud.get_user_by_email(db, user.email)
    if existing_user:
        raise HTTPException(status_code=400, detail="Email already registered")
    
    new_user = user_crud.create_user(db=db, user=user)
    return new_user

