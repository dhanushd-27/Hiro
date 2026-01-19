from uuid import UUID
from fastapi import Depends, APIRouter, status

from apps.server.src.db.session import get_db
from apps.server.src.schema.messages import MessageCreate, MessageRead
from apps.server.src.services.message_service import MessageService

router = APIRouter()

@router.post(
  "/threads/{thread_id}/messages",
  response_model=MessageCreate,
  status_code=status.HTTP_201_CREATED
)
async def add_message(
  thread_id: UUID,
  payload: MessageCreate,
  session=Depends(get_db)
):
  service = MessageService(session)
  return await service.create_message(thread_id, payload)

@router.get(
  "/threads/{thread_id}/messages",
  response_model=list[MessageRead],
  status_code=status.HTTP_200_OK
)
async def list_messages(
  thread_id: UUID,
  session=Depends(get_db),
):
  service = MessageService(session)
  return await service.list_messages(thread_id)