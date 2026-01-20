from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from apps.server.src.middleware import auth_middleware
from src.core.config import get_settings
from src.api.v1.health_api import router as health_router
from src.api.v1.message_api import router as messages_router
from src.api.v1.thread_api import router as threads_router
from src.api.v1.auth_api import router as auth_router
from src.api.v1.user_api import router as user_router
from src.core.lifespan import lifespan

app = FastAPI(lifespan=lifespan)

settings = get_settings()

app.add_middleware(
  CORSMiddleware,
  allow_origins=[settings.APP_CLIENT_API],
  allow_credentials=True,
  allow_methods=["*"],
  allow_headers=["*"]
)

app.include_router(health_router)
app.include_router(threads_router, auth_middleware, tags=["threads"])
app.include_router(messages_router, tags=["messages"])
app.include_router(auth_router, tags=["auth"])
app.include_router(user_router, tags=["user"])