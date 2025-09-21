from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
from app.db import get_db
from app.models.task import Task
from app.schemas.task import TaskCreate, TaskRead, TaskUpdate

router = APIRouter(prefix="/tasks", tags=["Tasks"])

@router.get("/", response_model=list[TaskRead])
async def list_tasks(db: AsyncSession = Depends(get_db)):
    result = await db.execute(select(Task))
    return result.scalars().all()

@router.post("/", response_model=TaskRead)
async def create_task(task: TaskCreate, db: AsyncSession = Depends(get_db)):
    db_task = Task(**task.dict())
    db.add(db_task)
    await db.commit()
    await db.refresh(db_task)
    return db_task

@router.put("/{task_id}", response_model=TaskRead)
async def update_task(task_id: int, task: TaskUpdate, db: AsyncSession = Depends(get_db)):
    result = await db.execute(select(Task).where(Task.id == task_id))
    db_task = result.scalar_one_or_none()
    if not db_task:
        raise HTTPException(status_code=404, detail="Task not found")
    for key, value in task.dict().items():
        setattr(db_task, key, value)
    await db.commit()
    await db.refresh(db_task)
    return db_task

@router.delete("/{task_id}")
async def delete_task(task_id: int, db: AsyncSession = Depends(get_db)):
    result = await db.execute(select(Task).where(Task.id == task_id))
    db_task = result.scalar_one_or_none()
    if not db_task:
        raise HTTPException(status_code=404, detail="Task not found")
    await db.delete(db_task)
    await db.commit()
    return {"message": "Task deleted"}
