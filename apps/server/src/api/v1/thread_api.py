from uuid import UUID

from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession

from src.db.session import get_db
from src.schema.thread_schema import ThreadCreate, ThreadRead, ThreadUpdate
from src.services.thread_service import ThreadService

router = APIRouter()


@router.post(
    "/threads",
    response_model=ThreadRead,
    status_code=status.HTTP_201_CREATED,
)
async def create_thread(
    payload: ThreadCreate,
    session: AsyncSession = Depends(get_db),
):
    service = ThreadService(session)
    return await service.create_thread(payload)


@router.get(
    "/threads",
    response_model=list[ThreadRead],
)
async def list_threads(
    session: AsyncSession = Depends(get_db),
):
    service = ThreadService(session)
    return await service.list_threads()


@router.get(
    "/threads/{thread_id}",
    response_model=ThreadRead,
)
async def get_thread(
    thread_id: UUID,
    session: AsyncSession = Depends(get_db),
):
    service = ThreadService(session)
    thread = await service.get_thread(thread_id)
    if not thread:
        raise HTTPException(status_code=404, detail="Thread not found")
    return thread


@router.patch(
    "/threads/{thread_id}",
    response_model=ThreadRead,
)
async def update_thread(
    thread_id: UUID,
    payload: ThreadUpdate,
    session: AsyncSession = Depends(get_db),
):
    service = ThreadService(session)
    thread = await service.update_thread(thread_id, payload)
    if not thread:
        raise HTTPException(status_code=404, detail="Thread not found")
    return thread


@router.delete(
    "/threads/{thread_id}",
    status_code=status.HTTP_204_NO_CONTENT,
)
async def delete_thread(
    thread_id: UUID,
    session: AsyncSession = Depends(get_db),
):
    service = ThreadService(session)
    deleted = await service.delete_thread(thread_id)
    if not deleted:
        raise HTTPException(status_code=404, detail="Thread not found")
    return None
