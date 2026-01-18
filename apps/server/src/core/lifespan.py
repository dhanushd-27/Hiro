from contextlib import asynccontextmanager

from fastapi import FastAPI

from src.core.db import init_db, close_db


@asynccontextmanager
async def lifespan(app: FastAPI):
    """
    FastAPI lifespan context manager for startup and shutdown events.
    
    - Startup: Initialize database engine and connection pool
    - Shutdown: Dispose engine and cleanup connections
    """
    # Startup
    await init_db()
    print("Database connection pool initialized")
    
    yield
    
    # Shutdown
    await close_db()
    print("Database connection pool closed")
