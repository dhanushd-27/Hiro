from uuid import UUID

from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from src.db.models.user_model import User
from src.schema.user_schema import (
    UserRegister,
    UserUpdate,
)


class UserService:
    def __init__(self, session: AsyncSession):
        self.session = session

    async def get_user_by_id(self, user_id: UUID) -> User | None:
        """Get user by ID."""
        stmt = select(User).where(User.id == user_id)
        result = await self.session.execute(stmt)
        return result.scalar_one_or_none()

    async def get_user_by_email(self, email: str) -> User | None:
        """Get user by email."""
        stmt = select(User).where(User.email == email)
        result = await self.session.execute(stmt)
        return result.scalar_one_or_none()

    async def get_user_by_google_id(self, google_id: str) -> User | None:
        """Get user by Google ID."""
        stmt = select(User).where(User.google_id == google_id)
        result = await self.session.execute(stmt)
        return result.scalar_one_or_none()

    async def create_user(self, data: UserRegister) -> User:
        """Create a new user. (Moved from register_user logic)"""
        # Note: Password hashing should happen in AuthService before calling this
        # or we can pass hashed password here. For now, let's assume it's pre-hashed
        # or we handle it in AuthService.
        user = User(
            email=data.email,
            name=data.name,
            password_hash=None, # To be set by caller if needed
        )
        self.session.add(user)
        # We don't commit here, let the service or API decide when to commit
        return user


    async def update_user(self, user_id: UUID, data: UserUpdate) -> User | None:
        """Update user profile."""
        user = await self.get_user_by_id(user_id)
        if not user:
            return None
            
        if data.name is not None:
            user.name = data.name
        if data.avatar_url is not None:
            user.avatar_url = data.avatar_url
            
        await self.session.commit()
        await self.session.refresh(user)
        return user

    async def delete_user(self, user_id: UUID) -> bool:
        """Delete user account."""
        user = await self.get_user_by_id(user_id)
        if not user:
            return False
            
        await self.session.delete(user)
        await self.session.commit()
        return True

