from typing import TYPE_CHECKING
import uuid
from datetime import datetime, timezone

from sqlalchemy import Text, DateTime, ForeignKey, Enum, Index
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import Mapped, mapped_column, relationship

from src.db.base import Base
from src.helpers.enum import MessageRole

if TYPE_CHECKING:
    from src.db.models.threads import Thread


class Message(Base):
    __tablename__ = "messages"

    id: Mapped[uuid.UUID] = mapped_column(
        UUID(as_uuid=True),
        primary_key=True,
        default=uuid.uuid4,
    )

    thread_id: Mapped[uuid.UUID] = mapped_column(
        UUID(as_uuid=True),
        ForeignKey("threads.id", ondelete="CASCADE"),
        nullable=False,
        index=True,
    )

    role: Mapped[MessageRole] = mapped_column(
        Enum(MessageRole, name="message_role_enum"),
        nullable=False,
    )

    message: Mapped[str] = mapped_column(
        Text,
        nullable=False,
    )

    created_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        default=lambda: datetime.now(timezone.utc),
        nullable=False,
    )

    updated_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        default=lambda: datetime.now(timezone.utc),
        onupdate=lambda: datetime.now(timezone.utc),
        nullable=False,
    )

    thread: Mapped["Thread"] = relationship(
        back_populates="messages",
    )

    __table_args__ = (
        Index("ix_messages_thread_created", "thread_id", "created_at"),
    )