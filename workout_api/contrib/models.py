from sqlalchemy import UUID
from sqlalchemy.orm import DeclarativeBase, Mapped
from sqlalchemy.orm import mapped_column

from uuid import uuid4
from sqlalchemy.dialects.postgresql import UUID as PG_UUID


class BaseModel(DeclarativeBase):
    id: Mapped[UUID] = mapped_column(PG_UUID(as_uuid=True), default=uuid4, nullable=False)