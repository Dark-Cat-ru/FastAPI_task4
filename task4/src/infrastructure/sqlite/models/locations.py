from ..database import Base
from sqlalchemy.orm import Mapped, mapped_column

class Location(Base):
    __tablename__ = 'locations'

    name: Mapped[str] = mapped_column(
        nullable=False,
        primary_key=True
    )