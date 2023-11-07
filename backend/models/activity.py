from typing import Optional, List

from config import db
from models.location import Location
from sqlalchemy.orm import Mapped
from backend.models.user import User


class Activity(db.Model):
    __tablename__ = "activity_table"
    __table_args__ = {'extend_existing': True}

    id: Mapped[int] = db.mapped_column(primary_key=True, autoincrement=True)

    name: Mapped[str] = db.mapped_column()
    start_date: Mapped[Optional[str]] = db.mapped_column()
    end_date: Mapped[Optional[str]] = db.mapped_column()
    time: Mapped[Optional[str]] = db.mapped_column()
    author: Mapped[Optional[str]] = db.mapped_column()

    tags: Mapped[Optional[str]] = db.mapped_column()
    category: Mapped[Optional[str]] = db.mapped_column()
    description: Mapped[Optional[str]] = db.mapped_column()
    address: Mapped[Optional[str]] = db.mapped_column(default="")
    location_id: Mapped[Optional[int]] = db.mapped_column(db.ForeignKey(Location.id))

    number_of_participants: Mapped[Optional[int]] = db.mapped_column(default=0)
    max_participants: Mapped[Optional[int]] = db.mapped_column(default=0)

    def __repr__(self):
        return f"({self.id}) {self.name}: {self.description} | {self.number_of_participants} participants"
