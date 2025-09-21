# app/db.py
from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.orm import sessionmaker
from app.config import settings

engine = create_async_engine(settings.DATABASE_URL, echo=True, future=True)

async_session = sessionmaker(
    bind=engine, class_=AsyncSession, expire_on_commit=False
)

# Dependency for FastAPI routes
async def get_db():
    async with async_session() as session:
        yield session
