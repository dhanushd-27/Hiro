from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from src.core.config import get_settings
from src.api.v1.health import router as health_router
from src.api.v1.messages import router as messages_router
from src.api.v1.threads import router as threads_router
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
app.include_router(threads_router, tags=["threads"])
app.include_router(messages_router, tags=["messages"])