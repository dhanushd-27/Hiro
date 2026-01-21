from fastapi import APIRouter, Depends, HTTPException, Request, Response, status
from fastapi.responses import RedirectResponse
from sqlalchemy.ext.asyncio import AsyncSession

from src.core.config import get_settings
from src.core.security import (
    verify_token,
    create_access_token,
    create_refresh_token,
    set_auth_cookies,
    clear_auth_cookies,
)
from src.db.session import get_db
from src.schema.user_schema import (
    UserRegister,
    UserLogin,
    UserRead,
    AuthResponse,
)
from src.services.user_service import UserService

settings = get_settings()

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


@router.post("/refresh")
async def refresh_tokens(request: Request, response: Response):
    """
    Use refresh token to get new access + refresh tokens.
    
    Implements token rotation: the old refresh token is replaced with a new one
    each time this endpoint is called. This limits the damage window if a refresh
    token is compromised.
    
    The client should call this endpoint when they receive a 401 with
    "Token has expired" detail from a protected endpoint.
    """
    refresh_token = request.cookies.get(settings.REFRESH_TOKEN_COOKIE_NAME)
    
    if not refresh_token:
        clear_auth_cookies(response)
        raise HTTPException(status_code=401, detail="No refresh token")
    
    try:
        payload = verify_token(refresh_token, expected_type="refresh")
    except HTTPException:
        # Invalid or expired refresh token - clear cookies and require re-login
        clear_auth_cookies(response)
        raise HTTPException(status_code=401, detail="Invalid refresh token, please login again")
    
    user_id = payload.get("sub")
    
    # Issue new tokens (rotation - both access and refresh are new)
    new_access_token = create_access_token(data={"sub": user_id})
    new_refresh_token = create_refresh_token(user_id=user_id)
    set_auth_cookies(response, new_access_token, new_refresh_token)
    
    return {"message": "Tokens refreshed successfully"}


@router.post("/logout")
async def logout(response: Response):
    """
    Clear authentication cookies to log the user out.
    
    This endpoint clears both the access token and refresh token cookies.
    """
    clear_auth_cookies(response)
    return {"message": "Logged out successfully"}
