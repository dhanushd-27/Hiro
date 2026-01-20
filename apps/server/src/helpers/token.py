from datetime import datetime, timedelta, timezone
from fastapi import HTTPException, Response
import jwt

from apps.server.src.core.config import get_settings

settings = get_settings()

def create_access_token(data: dict) -> str:
  """Create a short-lived access token with user data."""
  to_encode = data.copy()
  expire = datetime.now(timezone.now()) + timedelta(minutes=settings.ACCESS_TOKEN_EXPIRE)
  to_encode.update({"exp": expire, "type": "access"})
  return jwt.encode(to_encode, settings.SECRET_KEY, algorithm=settings.ALGORITHM)

def create_refresh_token(user_id: str) -> str:
  """Create a long-lived refresh token with minimal data."""
  expire = datetime.now(timezone.utc) + timedelta(days=settings.REFRESH_TOKEN_EXPIRE)
  to_encode={"sub": user_id, "exp": expire, "type": "refresh"}
  return jwt.encode(to_encode, settings.SECRET_KEY, algorithm=settings.ALGORITHM)

def verify_token(token: str, expected_type: str) -> dict:
  """Verify and decode a JWT token."""
  try:
    payload = jwt.decode(
      token, settings.SECRET_KEY, algorithms=[settings.ALGORITHM]
    )
    if payload.get("type") != expected_type:
      raise HTTPException(status_code=401, detail="Invalid token type")
    return payload
  except jwt.ExpiredSignatureError:
    raise HTTPException(status_code=401, detail="Token has expired")
  except jwt.jwt.InvalidTokenError:
    raise HTTPException(status_code=401, detail="Invalid token")

def set_auth_cookies(response: Response, access_token: str, refresh_token: str):
  # Setting up access token
  """Set both auth cookies as a response"""
  response.set_cookie(
    key=settings.ACCESS_TOKEN_COOKIE_NAME,
    value=access_token,
    max_age=settings.ACCESS_TOKEN_EXPIRE * 60,
    httponly=True,
    samesite="lax",
    secure=False
  )

  # Setting up refresh token
  response.set_cookie(
    key=settings.REFRESH_TOKEN_COOKIE_NAME,
    value=refresh_token,
    max_age=settings.ACCESS_TOKEN_EXPIRE * 24 * 60 * 60,
    httponly=True,
    samesite="lax",
    secure=False
  )

def clear_auth_cookie(response: Response):
  """Clear both auth cookies."""
  response.delete_cookie(key=settings.ACCESS_TOKEN_COOKIE_NAME)
  response.delete_cookie(key=settings.REFRESH_TOKEN_COOKIE_NAME)
