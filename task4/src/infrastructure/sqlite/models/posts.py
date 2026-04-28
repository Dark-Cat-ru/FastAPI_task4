from ..database import Base
from ..models.users import User
from ..models.locations import Location
from ..models.categories import Category

from datetime import datetime
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import ForeignKey

class Post(Base):
    __tablename__ = 'posts'

    title: Mapped[str] = mapped_column(
        nullable=False
    )
    text: Mapped[str] = mapped_column(
        nullable=False
    )
    id: Mapped[int] = mapped_column(
        unique=True,
        nullable=False,
        primary_key=True
    )
    pub_date: Mapped[datetime] = mapped_column(default=datetime.now())
    author_login: Mapped[str] = mapped_column(
        ForeignKey("users.login", ondelete="CASCADE", onupdate="CASCADE"),
        nullable=False
    )
    location_name: Mapped[str] = mapped_column(
        ForeignKey("locations.name", ondelete="CASCADE", onupdate="CASCADE")
    )
    category_title: Mapped[str] = mapped_column(
        ForeignKey("categories.title", ondelete="CASCADE", onupdate="CASCADE"),
        nullable=False
    )