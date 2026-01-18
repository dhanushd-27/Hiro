# Import all models here for Alembic to detect them
from src.schema.base import Base
from src.schema.threads import Thread
from src.schema.messages import Message

__all__ = ["Base", "Thread", "Message"]
