from uuid import UUID

from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from src.db.models.threads import Thread
from src.schema.threads import ThreadCreate, ThreadUpdate


class ThreadService:
    def __init__(self, session: AsyncSession):
        self.session = session

    async def create_thread(self, data: ThreadCreate) -> Thread:
        thread = Thread(
            title=data.title or "New Chat",
            pinned=data.pinned or False,
        )
        self.session.add(thread)
        await self.session.flush()
        return thread

    async def list_threads(self) -> list[Thread]:
        stmt = select(Thread).order_by(Thread.pinned.desc(), Thread.updated_at.desc())
        result = await self.session.execute(stmt)
        return list(result.scalars().all())

    async def get_thread(self, thread_id: UUID) -> Thread | None:
        stmt = select(Thread).where(Thread.id == thread_id)
        result = await self.session.execute(stmt)
        return result.scalar_one_or_none()

    async def update_thread(self, thread_id: UUID, data: ThreadUpdate) -> Thread | None:
        thread = await self.get_thread(thread_id)
        if not thread:
            return None

        update_data = data.model_dump(exclude_unset=True)
        for field, value in update_data.items():
            setattr(thread, field, value)

        await self.session.flush()
        return thread

    async def delete_thread(self, thread_id: UUID) -> bool:
        thread = await self.get_thread(thread_id)
        if not thread:
            return False
        await self.session.delete(thread)
        await self.session.flush()
        return True