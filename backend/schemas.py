# backend/schemas.py
from pydantic import BaseModel



class UserBase(BaseModel):
    email: str
    name: str
    

class UserCreate(UserBase):
    password: str

class UserOut(UserBase):
    id: int

    class Config:
        from_attributes = True

class LoginRequest(BaseModel):
    username: str  # This will be the email
    password: str
