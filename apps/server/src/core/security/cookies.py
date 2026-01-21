from fastapi import Response

from src.core.config import get_settings

settings = get_settings()


def set_auth_cookies(response: Response, access_token: str, refresh_token: str) -> None:
    """Set both auth cookies on the response."""
    response.set_cookie(
        key=settings.ACCESS_TOKEN_COOKIE_NAME,
        value=access_token,
        max_age=settings.ACCESS_TOKEN_EXPIRE * 60,
        httponly=True,
        samesite="lax",
        secure=False,
    )

    response.set_cookie(
        key=settings.REFRESH_TOKEN_COOKIE_NAME,
        value=refresh_token,
        max_age=settings.REFRESH_TOKEN_EXPIRE * 24 * 60 * 60,
        httponly=True,
        samesite="lax",
        secure=False,
    )


def clear_auth_cookies(response: Response) -> None:
    """Clear both auth cookies."""
    response.delete_cookie(key=settings.ACCESS_TOKEN_COOKIE_NAME)
    response.delete_cookie(key=settings.REFRESH_TOKEN_COOKIE_NAME)
