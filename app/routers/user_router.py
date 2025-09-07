from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.database import get_db
import app.models.user_model as user_model
import app.schemas.user_schemas as user_schemas
import app.crud.user_crud as user_crud
from app.auth import security, jwt as jwt_utils

router = APIRouter()

"""Register a new user"""
@router.post("/register", response_model=user_schemas.UserOut, status_code=201)
def register_user(user: user_schemas.UserCreate, db: Session = Depends(get_db)):
    existing_user = user_crud.get_user_by_email(db, user.email)
    if existing_user:
        raise HTTPException(status_code=409, detail="Email already registered")
    
    existing_user = user_crud.get_user_by_username(db, user.username)
    if existing_user:
        raise HTTPException(status_code=409, detail="Username already registered")
    
    new_user = user_crud.create_user(db=db, user=user)
    return new_user

@router.post("/login")
def login_user(user_credentials: user_schemas.UserLogin, db: Session = Depends(get_db)):
    user = user_crud.get_user_by_email(db, user_credentials.email)
    if not user or not security.verify_password(user_credentials.password, user.hashed_password):
        raise HTTPException(status_code=401, detail="Invalid email or password")

    access_token = jwt_utils.create_access_token({"sub": str(user.id)})
    return {"access_token": access_token, "token_type": "bearer"}
