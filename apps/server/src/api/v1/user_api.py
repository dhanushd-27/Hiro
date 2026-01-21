from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession

from src.db.session import get_db
from src.schema.user_schema import UserUpdate, UserRead
from src.services.user_service import UserService
from src.dependencies.auth import get_current_user

router = APIRouter(prefix="/user")


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
    user_id = current_user["sub"]
    service = UserService(session)
    raise HTTPException(status_code=501, detail="Not implemented")


@router.delete(
    "",
    status_code=status.HTTP_204_NO_CONTENT,
)
async def delete_user(
    current_user: dict = Depends(get_current_user),
    session: AsyncSession = Depends(get_db),
):
    """Delete current user account."""
    user_id = current_user["sub"]
    service = UserService(session)
    raise HTTPException(status_code=501, detail="Not implemented")
