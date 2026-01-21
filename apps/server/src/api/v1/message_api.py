from uuid import UUID

from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession

from src.db.session import get_db
from src.schema.message_schema import MessageCreate, MessageRead
from src.services.message_service import MessageService
from src.dependencies.auth import get_current_user

router = APIRouter()


@router.post(
    "/threads/{thread_id}/messages",
    response_model=MessageRead,
    status_code=status.HTTP_201_CREATED,
)
async def create_message(
    thread_id: UUID,
    payload: MessageCreate,
    current_user: dict = Depends(get_current_user),
    session: AsyncSession = Depends(get_db),
):
    service = MessageService(session)
    message = await service.create_message(thread_id, payload)
    if not message:
        raise HTTPException(status_code=404, detail="Thread not found")
    return message


@router.get(
    "/threads/{thread_id}/messages",
    response_model=list[MessageRead],
)
async def list_messages(
    thread_id: UUID,
    current_user: dict = Depends(get_current_user),
    session: AsyncSession = Depends(get_db),
):
    service = MessageService(session)
    messages = await service.list_messages(thread_id)
    if messages is None:
        raise HTTPException(status_code=404, detail="Thread not found")
    return messages
