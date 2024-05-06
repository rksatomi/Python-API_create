from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_collum
from uuid import uuid4
from sqlalchemy.orm import UUID
from sqlalchemy.dialects.postgreasql import UUID as PG_UUID


class BaseModel(DeclarativeBase):
    id: Mapped[UUID] = mapped_collum(PG_UUID(as_uuid=True), default=uuid4, nullable=False)