from Infrastructure.DB.Base import Base
from sqlalchemy.orm import mapped_column, Mapped

class Hello(Base):

    __tablename__ = "messages"
    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    message: Mapped[str]