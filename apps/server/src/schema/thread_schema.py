from datetime import datetime
from uuid import UUID
from pydantic import BaseModel


class ThreadCreate(BaseModel):
    title: str | None = None
    pinned: bool | None = None


class ThreadUpdate(BaseModel):
    title: str | None = None
    pinned: bool | None = None


class ThreadRead(BaseModel):
    id: UUID
    title: str
    pinned: bool
    created_at: datetime
    updated_at: datetime

    class Config:
        from_attributes = True
