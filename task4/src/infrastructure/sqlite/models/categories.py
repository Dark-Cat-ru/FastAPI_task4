from ..database import Base

from sqlalchemy.orm import Mapped, mapped_column

class Category(Base):
    __tablename__ = "categories"

    title: Mapped[str] = mapped_column(
        primary_key=True,
        nullable=False,
        unique=True,
    )
    description: Mapped[str] = mapped_column(
        nullable=False
    )
    slug: Mapped[int] = mapped_column(
        nullable=False,
        unique=True
    )