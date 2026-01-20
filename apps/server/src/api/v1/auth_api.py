from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.responses import RedirectResponse
from sqlalchemy.ext.asyncio import AsyncSession

from src.db.session import get_db
from src.schema.user_schema import (
    UserRegister,
    UserLogin,
    UserRead,
    AuthResponse,
)
from src.services.user_service import UserService

router = APIRouter(prefix="/user/auth")


@router.get(
    "/me",
    response_model=UserRead,
)
async def get_current_user(
    # TODO: Add auth dependency to get current user from token
    session: AsyncSession = Depends(get_db),
):
    """Get current authenticated user."""
    # TODO: Implement
    # - Extract user from auth token
    # - Return user data
    raise HTTPException(status_code=501, detail="Not implemented")


@router.post(
    "/register",
    response_model=AuthResponse,
    status_code=status.HTTP_201_CREATED,
)
async def register(
    payload: UserRegister,
    session: AsyncSession = Depends(get_db),
):
    """Register a new user with email and password."""
    # TODO: Implement
    # - Call user service to register
    # - Generate JWT token
    # - Return user and token
    service = UserService(session)
    raise HTTPException(status_code=501, detail="Not implemented")


@router.post(
    "/login",
    response_model=AuthResponse,
)
async def login(
    payload: UserLogin,
    session: AsyncSession = Depends(get_db),
):
    """Login with email and password."""
    # TODO: Implement
    # - Call user service to authenticate
    # - Generate JWT token
    # - Return user and token
    service = UserService(session)
    raise HTTPException(status_code=501, detail="Not implemented")


@router.get(
    "/google",
)
async def google_login():
    """Initiate Google OAuth login flow."""
    # TODO: Implement
    # - Generate OAuth state
    # - Build Google OAuth URL
    # - Redirect to Google
    raise HTTPException(status_code=501, detail="Not implemented")


@router.get(
    "/google/callback",
)
async def google_callback(
    code: str | None = None,
    error: str | None = None,
    session: AsyncSession = Depends(get_db),
):
    """Handle Google OAuth callback."""
    # TODO: Implement
    # - Validate OAuth response
    # - Exchange code for tokens
    # - Get user info from Google
    # - Create or authenticate user
    # - Generate JWT token
    # - Redirect to frontend with token
    if error:
        raise HTTPException(status_code=400, detail=f"Google OAuth error: {error}")
    
    service = UserService(session)
    raise HTTPException(status_code=501, detail="Not implemented")
