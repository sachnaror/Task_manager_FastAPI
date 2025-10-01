from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.core.middlewares import LoggingMiddleware
from app.routers import tasks_router, users_router, auth_router, websocket_router
from sqlalchemy.ext.asyncio import AsyncSession
from app.db import engine

app = FastAPI(title="Task Manager API", version="1.0")

# --- Custom Logging Middleware ---
app.add_middleware(LoggingMiddleware)

# --- CORS Middleware ---
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],   # 👈 allow all (for dev). Replace with ["http://localhost:3000"] for React, etc.
    allow_credentials=True,
    allow_methods=["*"],   # allow all HTTP methods
    allow_headers=["*"],   # allow all headers
)

@app.get("/")
async def root():
    return {"message": "Task Manager API is running 🚀"}

# Routers
app.include_router(tasks_router)
app.include_router(users_router)
app.include_router(auth_router)
app.include_router(websocket_router)






@app.on_event("startup")
async def startup_event():
    try:
        async with engine.begin() as conn:
            await conn.run_sync(lambda conn: print("✅ Connected to Postgres:", conn.engine.url))
    except Exception as e:
        print("❌ Failed to connect to Postgres:", e)
