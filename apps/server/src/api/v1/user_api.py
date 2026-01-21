from uuid import UUID

from fastapi import APIRouter, Depends, HTTPException, Response, status
from sqlalchemy.ext.asyncio import AsyncSession

from src.db.session import get_db
from src.schema.user_schema import UserUpdate, UserRead
from src.services.user_service import UserService
from src.dependencies.auth import get_current_user

router = APIRouter(prefix="/user")


@router.get(
    "/me",
    response_model=UserRead,
)
async def get_me(
    current_user: dict = Depends(get_current_user),
    session: AsyncSession = Depends(get_db),
):
    """Get current authenticated user profile."""
    user_id = UUID(current_user["sub"])
    service = UserService(session)
    user = await service.get_user_by_id(user_id)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return user


@router.put(
    "",
    response_model=UserRead,
)
async def update_user(
    payload: UserUpdate,
    current_user: dict = Depends(get_current_user),
    session: AsyncSession = Depends(get_db),
):
    """Update current user profile."""
    user_id = UUID(current_user["sub"])
    service = UserService(session)
    user = await service.update_user(user_id, payload)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return user


@router.delete(
    "",
    status_code=status.HTTP_204_NO_CONTENT,
)
async def delete_user(
    response: Response,
    current_user: dict = Depends(get_current_user),
    session: AsyncSession = Depends(get_db),
):
    """Delete current user account."""
    user_id = UUID(current_user["sub"])
    service = UserService(session)
    success = await service.delete_user(user_id)
    if not success:
        raise HTTPException(status_code=404, detail="User not found")
    
    # Ideally clear cookies here too
    from src.core.security.cookies import clear_auth_cookies
    clear_auth_cookies(response)
    
    return Response(status_code=status.HTTP_204_NO_CONTENT)
