from datetime import datetime

from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column


class Base(DeclarativeBase):
    pass


class UserModelSQL(Base):
    __tablename__ = "users"

    id: Mapped[str] = mapped_column(primary_key=True, nullable=False)
    username: Mapped[str] = mapped_column(nullable=False)
    email: Mapped[str] = mapped_column(unique=True, nullable=False)
    pwd: Mapped[str] = mapped_column(nullable=False)
    createdAt: Mapped[datetime] = mapped_column(nullable=False)
    editedAt: Mapped[datetime] = mapped_column(nullable=False)
