from datetime import datetime
from uuid import UUID
from pydantic import BaseModel
from typing import List, Optional

from src.schema.messages import MessageRead

class ThreadBase(BaseModel):
  title: str
  pinned: bool = False

class ThreadCreate(ThreadBase):
  title: Optional[str] = None
  pinned: Optional[str] = None

class ThreadRead(BaseModel):
  id: UUID
  title: str
  pinned: bool
  created_at: datetime
  updated_at: datetime

  class Config:
    from_attributes = True

class ThreadReadWithMessages(ThreadRead):
  messages: List[MessageRead]