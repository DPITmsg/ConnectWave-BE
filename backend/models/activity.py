from typing import List

from config import db
from models.location import Location
from sqlalchemy.orm import Mapped
from models.user import User


class Activity(db.Model):
    __tablename__ = "activity_table"
    __table_args__ = {'extend_existing': True}

    id: Mapped[int] = db.mapped_column(primary_key=True, autoincrement=True)

    name: Mapped[str] = db.mapped_column()
    start_date: Mapped[str] = db.mapped_column()
    end_date: Mapped[str] = db.mapped_column()
    time: Mapped[str] = db.mapped_column()
    author: Mapped[str] = db.mapped_column(db.ForeignKey(User.username))

    tags: Mapped[str] = db.mapped_column()
    category: Mapped[str] = db.mapped_column()
    description: Mapped[str] = db.mapped_column()
    address: Mapped[str] = db.mapped_column()
    location_id: Mapped[int] = db.mapped_column(db.ForeignKey(Location.id))

    participants: Mapped[str] = db.mapped_column()
    max_participants: Mapped[int] = db.mapped_column()

    def __repr__(self):
        return f"({self.id}) {self.name}: {self.description} | {self.number_of_participants} participants"
