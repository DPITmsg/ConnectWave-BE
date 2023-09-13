from sqlalchemy.orm import Mapped

from config import db


class Location(db.Model):
    __tablename__ = "location_table"

    id: Mapped[int] = db.mapped_column(primary_key=True, autoincrement=True)
    location_x: Mapped[int] = db.mapped_column()
    location_y: Mapped[int] = db.mapped_column()

    def __repr__(self):
        return f"({self.id}) {self.location_x}, {self.location_y}"


