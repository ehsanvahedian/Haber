from .Base import Base
from sqlalchemy.orm import mapped_column, Mapped
from datetime import datetime

class document_ORM(Base):
    __tablename__ = "document"

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    name: Mapped[str]
    topic: Mapped[str]
    content: Mapped[str]
    created_at: Mapped[datetime]
    updated_at: Mapped[datetime]