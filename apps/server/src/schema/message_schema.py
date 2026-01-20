from datetime import datetime
from uuid import UUID
from pydantic import BaseModel
from src.helpers.enum import MessageRole

class MessageBase(BaseModel):
  role: MessageRole
  message: str

class MessageCreate(MessageBase):
  pass

class MessageRead(MessageBase):
  id: UUID
  thread_id: UUID
  created_at: datetime

  class Config:
    from_attributes = True
