from uuid import UUID

from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from src.db.models.message_model import Message
from src.db.models.thread_model import Thread
from src.schema.message_schema import MessageCreate


class MessageService:
    def __init__(self, session: AsyncSession):
        self.session = session

    async def create_message(self, thread_id: UUID, data: MessageCreate) -> Message | None:
        # Verify thread exists
        thread_check = await self.session.execute(
            select(Thread.id).where(Thread.id == thread_id)
        )
        if not thread_check.scalar_one_or_none():
            return None

        message = Message(
            thread_id=thread_id,
            role=data.role,
            message=data.message,
        )
        self.session.add(message)
        await self.session.flush()
        return message

    async def list_messages(self, thread_id: UUID) -> list[Message] | None:
        # Verify thread exists
        thread_check = await self.session.execute(
            select(Thread.id).where(Thread.id == thread_id)
        )
        if not thread_check.scalar_one_or_none():
            return None

        stmt = (
            select(Message)
            .where(Message.thread_id == thread_id)
            .order_by(Message.created_at.asc())
        )
        result = await self.session.execute(stmt)
        return list(result.scalars().all())