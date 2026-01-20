from datetime import datetime
from uuid import UUID
from pydantic import BaseModel, EmailStr


class UserRegister(BaseModel):
    email: EmailStr
    password: str
    name: str

class UserLogin(BaseModel):
    email: EmailStr
    password: str

class UserGoogleAuth(BaseModel):
    google_id: str
    email: EmailStr | None = None
    name: str | None = None
    avatar_url: str | None = None

class UserRead(BaseModel):
    id: UUID
    email: EmailStr | None = None
    google_id: str | None = None
    name: str
    avatar_url: str | None = None
    created_at: datetime
    updated_at: datetime

    class Config:
        from_attributes = True
