import uuid
from sqlalchemy import Column, String, DateTime, func, UniqueConstraint
from sqlalchemy.dialects.postgresql import UUID

from clan_api.db.base import Base

class Clan(Base):
    __tablename__ = "clans"
    __table_args__ = (
        UniqueConstraint("name", name="uq_clans_name"),
    )

    id = Column(
        UUID(as_uuid=True),
        primary_key=True,
        default=uuid.uuid4,
    )

    name = Column(String, nullable=False)
    region = Column(String, nullable=False)

    created_at = Column(
        DateTime(timezone=True),
        server_default=func.now(),
        nullable=False,
    )
