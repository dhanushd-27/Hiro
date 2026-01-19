from uuid import UUID
from fastapi import APIRouter, Depends, status
from starlette.status import HTTP_200_OK

from apps.server.src.db.session import get_db
from apps.server.src.schema.threads import ThreadCreate, ThreadRead, ThreadReadWithMessages
from apps.server.src.services.thread_service import ThreadService

router = APIRouter()

@router.post(
  "/threads", 
  response_model=ThreadRead, 
  status_code=status.HTTP_201_CREATED
)
async def create_thread(
  payload: ThreadCreate,
  session=Depends(get_db)
):
  service = ThreadService(session)
  return await service.create_thread(payload)

