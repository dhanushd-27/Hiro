"""
Security primitives (JWT tokens, password hashing, OAuth helpers).

This package intentionally provides a small "public surface" via re-exports
so callers can keep using `from src.core.security import ...`.
"""

from .cookies import clear_auth_cookies, set_auth_cookies
from .passwords import hash_password, verify_password
from .tokens import create_access_token, create_refresh_token, verify_token

__all__ = [
    "create_access_token",
    "create_refresh_token",
    "verify_token",
    "set_auth_cookies",
    "clear_auth_cookies",
    "hash_password",
    "verify_password",
]
