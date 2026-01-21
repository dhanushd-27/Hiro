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
from src.core.security.google_oauth import oauth
from src.db.session import get_db
from src.schema.user_schema import (
    UserRegister,
    UserLogin,
    UserRead,
    AuthResponse,
    UserGoogleAuth,
)
from src.services.auth_service import AuthService

settings = get_settings()

router = APIRouter(prefix="/auth")


@router.post(
    "/register",
    response_model=AuthResponse,
    status_code=status.HTTP_201_CREATED,
)
async def register(
    response: Response,
    payload: UserRegister,
    session: AsyncSession = Depends(get_db),
):
    """Register a new user with email and password."""
    service = AuthService(session)
    user, access_token, refresh_token = await service.register_user(payload)
    
    # Set cookies
    set_auth_cookies(response, access_token, refresh_token)
    
    return {
        "user": user,
        "token": {
            "access_token": access_token,
            "token_type": "bearer"
        }
    }


@router.post(
    "/login",
    response_model=AuthResponse,
)
async def login(
    response: Response,
    payload: UserLogin,
    session: AsyncSession = Depends(get_db),
):
    """Login with email and password."""
    service = AuthService(session)
    result = await service.authenticate_user(payload)
    
    if not result:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid email or password"
        )
    
    user, access_token, refresh_token = result
    
    # Set cookies
    set_auth_cookies(response, access_token, refresh_token)
    
    return {
        "user": user,
        "token": {
            "access_token": access_token,
            "token_type": "bearer"
        }
    }


@router.get(
    "/google",
)
async def google_login(request: Request):
    """Redirect to Google OAuth login page."""
    service = AuthService()
    return await service.get_google_auth_redirect_url(request)


@router.get(
    "/google/callback",
    response_model=AuthResponse,
)
async def google_callback(
    request: Request,
    response: Response,
    session: AsyncSession = Depends(get_db),
):
    """Handle Google OAuth callback."""
    service = AuthService(session)
    user, access_token, refresh_token = await service.handle_google_callback(request)
    
    # Set cookies
    set_auth_cookies(response, access_token, refresh_token)
    
    return {
        "user": user,
        "token": {
            "access_token": access_token,
            "token_type": "bearer"
        }
    }


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
