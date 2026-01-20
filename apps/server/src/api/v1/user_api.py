from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession

from src.db.session import get_db
from src.schema.user_schema import UserUpdate, UserRead
from src.services.user_service import UserService

router = APIRouter(prefix="/user")


@router.put(
    "",
    response_model=UserRead,
)
async def update_user(
    payload: UserUpdate,
    # TODO: Add auth dependency to get current user from token
    session: AsyncSession = Depends(get_db),
):
    """Update current user profile."""
    # TODO: Implement
    # - Extract user ID from auth token
    # - Call user service to update
    # - Return updated user
    service = UserService(session)
    raise HTTPException(status_code=501, detail="Not implemented")


@router.delete(
    "",
    status_code=status.HTTP_204_NO_CONTENT,
)
async def delete_user(
    # TODO: Add auth dependency to get current user from token
    session: AsyncSession = Depends(get_db),
):
    """Delete current user account."""
    # TODO: Implement
    # - Extract user ID from auth token
    # - Call user service to delete
    # - Return success
    service = UserService(session)
    raise HTTPException(status_code=501, detail="Not implemented")
