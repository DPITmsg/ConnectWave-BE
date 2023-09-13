from config import db
from models.location import Location
from sqlalchemy.orm import Mapped


class Activity(db.Model):
    __tablename__ = "activity_table"

    id:  Mapped[int]  = db.mapped_column(primary_key=True, autoincrement=True)
    name: Mapped[str] = db.mapped_column()
    description: Mapped[str] = db.mapped_column()
    location_id: Mapped[int] = db.mapped_column(db.ForeignKey(Location.id))
    number_of_participants: Mapped[int] = db.mapped_column(default=0)

    
    def __repr__(self):
        return f"({self.id}) {self.name}: {self.description} | {self.number_of_participants} participants"

