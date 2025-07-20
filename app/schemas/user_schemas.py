from pydantic import BaseModel, EmailStr

class UserBase(BaseModel):
    email: EmailStr

class UserCreate(UserBase):
    password: str
    email: EmailStr
    username: str

class UserRead(UserBase):
    id: int
    username: str
    email: EmailStr
    is_active: bool
    is_superuser: bool

class UserOut(BaseModel):
    id: int
    username: str
    email: EmailStr

class UserLogin(BaseModel):
    email: str
    password: str

    model_config = {
        "from_attributes": True,  # odpowiada orm_mode = True
    }

