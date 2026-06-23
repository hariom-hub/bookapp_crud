
from sqlalchemy.orm import Mapped, mapped_column
from datetime import date, datetime, UTC
from sqlalchemy import String, Boolean
from sqlalchemy import Enum as SQL_ENUM
from src.db.base import Base
from src.auth.language_type.languages import Language

class User(Base):
    __tablename__ = 'User'
    user_id: Mapped[int] = mapped_column(
        primary_key=True,
        autoincrement=True,
        unique=True,
    )
    username: Mapped[str] = mapped_column(String(30))
    age: Mapped[int]
    email: Mapped[str] = mapped_column(String(20))
    first_name: Mapped[str] = mapped_column(String(30))
    last_name: Mapped[str] = mapped_column(String(20))
    created_at: Mapped[datetime] = mapped_column(
        default=lambda: datetime.now(UTC),
    )
    is_verified : Mapped[bool] = mapped_column(
        Boolean,
        default=False
    )
    updated_at: Mapped[datetime] = mapped_column(
        default=lambda: datetime.now(UTC),
        onupdate=lambda: datetime.now(UTC)
    )
    password_hash : Mapped[str] = mapped_column(
        String(255),
        nullable=False
    )
    language: Mapped[Language] = mapped_column(
        SQL_ENUM(Language)
    )
    def __repr__(self):
        return f"<User.{self.username}"


