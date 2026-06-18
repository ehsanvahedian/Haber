from sqlalchemy.orm import mapped_column, Mapped
from datetime import datetime
from .Base import Base

class task_ORM(Base):
    __tablename__ = "tasks"


    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    task_txt: Mapped[str]
    description: Mapped[str]
    created_at: Mapped[datetime]
    due_time: Mapped[datetime]
    completed: Mapped[bool]
    priority: Mapped[int]
