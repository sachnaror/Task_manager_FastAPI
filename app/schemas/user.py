# app/schemas/user.py
from pydantic import BaseModel

class UserBase(BaseModel):
    email: str

class UserCreate(UserBase):
    password: str

class UserRead(UserBase):
    id: int
    class Config:
        from_attributes = True   # instead of orm_mode

class UserLogin(BaseModel):
    email: str
    password: str
