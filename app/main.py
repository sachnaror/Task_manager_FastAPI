from fastapi import FastAPI, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from app.db import get_db
from app.routers import tasks_router, users_router, auth_router, websocket_router

app = FastAPI(title="Task Manager API")


@app.get("/")
async def root():
    return {"message": "Task Manager API is running 🚀"}


# Routers
app.include_router(tasks_router)
app.include_router(users_router)
app.include_router(auth_router)
app.include_router(websocket_router)
