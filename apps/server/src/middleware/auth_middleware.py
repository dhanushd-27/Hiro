from fastapi import Request, HTTPException
from starlette.middleware.base import BaseHTTPMiddleware
from starlette.responses import Response

from apps.server.src.core.config import get_settings
from apps.server.src.helpers.token import verify_token

settings = get_settings()


class AuthMiddleware(BaseHTTPMiddleware):
    """
    Middleware to verify access_token and refresh_token cookies on every request.
    Sets request.state.user if valid access_token is present.
    Raises HTTPException(401) if neither valid token is found.
    """

    async def dispatch(self, request: Request, call_next):
        access_token = request.cookies.get(settings.ACCESS_TOKEN_COOKIE_NAME)
        refresh_token = request.cookies.get(settings.REFRESH_TOKEN_COOKIE_NAME)
        user_data = None

        if access_token:
            try:
                payload = verify_token(access_token, expected_type="access")
                # You can set user info in request.state for route handlers
                request.state.user = payload
            except HTTPException as ae:
                # Access token is invalid or expired; try with refresh token
                access_token = None  # Make explicit
            except Exception:
                access_token = None

        if not access_token and refresh_token:
            try:
                refresh_payload = verify_token(refresh_token, expected_type="refresh")
                request.state.user = {"sub": refresh_payload.get("sub"), "token_type": "refresh"}
                # You can optionally force user to use refresh endpoint here
            except HTTPException:
                # Both tokens are invalid
                raise HTTPException(status_code=401, detail="Invalid authentication, please login again")
        elif not access_token and not refresh_token:
            raise HTTPException(status_code=401, detail="Authentication required")

        response = await call_next(request)
        return response