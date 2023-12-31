from uuid import UUID

from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column

from app.models.base_model import Base


# TODO: Column: Photo,
class Profile(Base):
    __abstract__ = True

    user_id: Mapped[UUID] = mapped_column(ForeignKey('user.id'))
