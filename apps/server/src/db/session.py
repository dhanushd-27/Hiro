from typing import AsyncGenerator

from sqlalchemy.ext.asyncio import (
    AsyncSession,
    AsyncEngine,
    create_async_engine,
    async_sessionmaker,
)

from src.core.config import get_settings

DB_URL = get_settings().database_urL

# Global engine and session factory - initialized in lifespan
engine: AsyncEngine | None = None
async_session_factory: async_sessionmaker[AsyncSession] | None = None


async def init_db() -> None:
    """Initialize the database engine and session factory."""
    global engine, async_session_factory
    
    engine = create_async_engine(
        url=DB_URL,
        echo=True,
        pool_pre_ping=True,  # Verify connections before using
        pool_size=5,         # Connection pool size
        max_overflow=10,     # Max overflow connections
    )
    
    async_session_factory = async_sessionmaker(
        bind=engine,
        class_=AsyncSession,
        expire_on_commit=False,
        autocommit=False,
        autoflush=False,
    )


async def close_db() -> None:
    """Dispose the database engine and cleanup connections."""
    global engine, async_session_factory
    
    if engine is not None:
        await engine.dispose()
        engine = None
        async_session_factory = None


async def get_db() -> AsyncGenerator[AsyncSession, None]:
    """
    FastAPI dependency that provides a database session.
    
    Usage:
        @app.get("/items")
        async def get_items(db: AsyncSession = Depends(get_db)):
            result = await db.execute(select(Item))
            return result.scalars().all()
    """
    if async_session_factory is None:
        raise RuntimeError("Database not initialized. Call init_db() first.")
    
    async with async_session_factory() as session:
        try:
            yield session
            await session.commit()
        except Exception:
            await session.rollback()
            raise
