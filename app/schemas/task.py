
from pydantic import BaseModel

class TaskBase(BaseModel):
    title: str
    description: str | None = None

class TaskCreate(TaskBase):
    pass

class TaskUpdate(TaskBase):
    completed: bool

class TaskRead(TaskBase):
    id: int
    completed: bool
    class Config:
        orm_mode = True
