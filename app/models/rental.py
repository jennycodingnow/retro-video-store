from sqlalchemy.orm import Mapped, mapped_column
from ..db import db

class Rental(db.Model):
    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)