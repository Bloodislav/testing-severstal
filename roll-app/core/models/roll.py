from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import Date, text
from datetime import date

from .base import Base
from .mixins.int_id_pk import IntIdPkMixin

class Roll(IntIdPkMixin, Base):
  length: Mapped[int] = mapped_column(nullable=False)
  weight: Mapped[int] = mapped_column(nullable=False)
  data_deleted: Mapped[date] = mapped_column(Date, nullable=True)
  data_added: Mapped[date] = mapped_column(
      Date, 
      nullable=False,
      server_default=text("TIMEZONE('utc', now())")
  )