from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
from fastapi import Request
from authlib.integrations.starlette_client import OAuth

from src.db.models.user_model import User
from src.schema.user_schema import (
    UserRegister,
    UserLogin,
    UserGoogleAuth,
)
from src.core.security.google_oauth import oauth
from src.core.security.passwords import hash_password, verify_password
from src.core.security.tokens import create_access_token, create_refresh_token
from src.services.user_service import UserService

class AuthService:
    def __init__(self, session: AsyncSession | None = None):
        self.session = session
        self.user_service = UserService(session) if session else None

    async def register_user(self, data: UserRegister) -> tuple[User, str, str]:
        """Register a new user and generate tokens."""
        if not self.session:
            raise RuntimeError("Database session required for registration")
        
        # Check if email already exists
        existing_user = await self.user_service.get_user_by_email(data.email)
        if existing_user:
            from fastapi import HTTPException, status
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="Email already registered"
            )
        
        # Create user
        user = User(
            email=data.email,
            name=data.name,
            password_hash=hash_password(data.password)
        )
        self.session.add(user)
        await self.session.commit()
        await self.session.refresh(user)
        
        # Generate tokens
        access_token = create_access_token(data={"sub": str(user.id)})
        refresh_token = create_refresh_token(user_id=str(user.id))
        
        return user, access_token, refresh_token

    async def authenticate_user(self, data: UserLogin) -> tuple[User, str, str] | None:
        """Authenticate user and generate tokens."""
        if not self.session:
            raise RuntimeError("Database session required for authentication")

        user = await self.user_service.get_user_by_email(data.email)
        if not user or not user.password_hash:
            return None
            
        if not verify_password(data.password, user.password_hash):
            return None
            
        # Generate tokens
        access_token = create_access_token(data={"sub": str(user.id)})
        refresh_token = create_refresh_token(user_id=str(user.id))
        
        return user, access_token, refresh_token

    async def get_google_auth_redirect_url(self, request: Request):
        """Get the Google OAuth redirect URL."""
        redirect_uri = request.url_for("google_callback")  # Matches route name in auth_api.py
        return await oauth.google.authorize_redirect(request, redirect_uri)

    async def handle_google_callback(self, request: Request) -> tuple[User, str, str]:
        """Handle Google OAuth callback, exchange tokens, and find/create user."""
        from fastapi import HTTPException, status
        try:
            token = await oauth.google.authorize_access_token(request)
        except Exception as e:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail=f"Could not authenticate with Google: {str(e)}"
            )

        user_info = token.get("userinfo")
        if not user_info:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Failed to retrieve user information from Google"
            )

        google_data = UserGoogleAuth(
            google_id=user_info["sub"],
            email=user_info.get("email"),
            name=user_info.get("name"),
            avatar_url=user_info.get("picture"),
        )
        
        user = await self.google(google_data)
        
        # Generate tokens
        access_token = create_access_token(data={"sub": str(user.id)})
        refresh_token = create_refresh_token(user_id=str(user.id))
        
        return user, access_token, refresh_token

    async def google(self, data: UserGoogleAuth) -> User:
        """Authenticate existing Google user or create new one."""
        if not self.session:
            raise RuntimeError("Database session required for Google auth")
            
        # 1. Try to find user by google_id
        stmt = select(User).where(User.google_id == data.google_id)
        result = await self.session.execute(stmt)
        user = result.scalar_one_or_none()

        if not user and data.email:
            # 2. Try to find user by email (account might exist from email/pass registration)
            stmt = select(User).where(User.email == data.email)
            result = await self.session.execute(stmt)
            user = result.scalar_one_or_none()
            
            if user:
                # Link Google ID to existing account
                user.google_id = data.google_id

        if not user:
            # 3. Create new user
            user = User(
                email=data.email,
                google_id=data.google_id,
                name=data.name or (data.email.split("@")[0] if data.email else "User"),
                avatar_url=data.avatar_url,
            )
            self.session.add(user)
        else:
            # 4. Update info if changed
            if data.name:
                user.name = data.name
            if data.avatar_url:
                user.avatar_url = data.avatar_url

        await self.session.commit()
        await self.session.refresh(user)
        return user