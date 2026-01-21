from fastapi import Request, HTTPException

from src.core.config import get_settings
from src.core.security import verify_token

settings = get_settings()


async def get_current_user(request: Request) -> dict:
    """
    Dependency to extract and verify the current user from access token cookie.
    
    This dependency only validates the access token. If the token is expired,
    the client should call POST /auth/refresh to get new tokens.
    
    Returns:
        dict: The token payload containing user info (sub, exp, type)
    
    Raises:
        HTTPException 401: If no token, token expired, or token invalid
    """
    access_token = request.cookies.get(settings.ACCESS_TOKEN_COOKIE_NAME)
    
    if not access_token:
        raise HTTPException(status_code=401, detail="Not authenticated")
    
    # verify_token raises HTTPException on expired/invalid token
    payload = verify_token(access_token, expected_type="access")
    return payload
