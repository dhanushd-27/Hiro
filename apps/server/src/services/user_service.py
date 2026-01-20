from uuid import UUID

from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from src.db.models.user_model import User
from src.schema.user_schema import (
    UserRegister,
    UserLogin,
    UserUpdate,
    UserGoogleAuth,
)


class UserService:
    def __init__(self, session: AsyncSession):
        self.session = session

    async def get_user_by_id(self, user_id: UUID) -> User | None:
        """Get user by ID."""
        # TODO: Implement
        pass

    async def get_user_by_email(self, email: str) -> User | None:
        """Get user by email."""
        # TODO: Implement
        pass

    async def get_user_by_google_id(self, google_id: str) -> User | None:
        """Get user by Google ID."""
        # TODO: Implement
        pass

    async def register_user(self, data: UserRegister) -> User:
        """Register a new user with email and password."""
        # TODO: Implement
        # - Check if email already exists
        # - Hash password
        # - Create user
        pass

    async def authenticate_user(self, data: UserLogin) -> User | None:
        """Authenticate user with email and password."""
        # TODO: Implement
        # - Get user by email
        # - Verify password hash
        # - Return user or None
        pass

    async def authenticate_or_create_google_user(self, data: UserGoogleAuth) -> User:
        """Authenticate existing Google user or create new one."""
        # TODO: Implement
        # - Check if user exists by google_id
        # - If not, create new user
        # - Return user
        pass

    async def update_user(self, user_id: UUID, data: UserUpdate) -> User | None:
        """Update user profile."""
        # TODO: Implement
        # - Get user by ID
        # - Update fields
        # - Return updated user
        pass

    async def delete_user(self, user_id: UUID) -> bool:
        """Delete user account."""
        # TODO: Implement
        # - Get user by ID
        # - Delete user
        # - Return success status
        pass
