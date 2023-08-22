from main import app, db
from sqlalchemy import Table, Column, Integer, String
from sqlalchemy import ForeignKey 
from typing import List
from typing import Optional
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column

class Activity(db.Model):
    __tablename__ = "activity_table"

    id:  Mapped[int]  = db.mapped_column(primary_key=True, autoincrement=True)
    name: Mapped[str] = db.mapped_column()
    description: Mapped[str] = db.mapped_column()
    location_id: Mapped[int] = db.mapped_column(db.ForeignKey(Location.id))
    number_of_participants: Mapped[int] = db.mapped_column(default=0)

    
    def __repr__(self):
        return f"({self.id}) {self.name}: {self.description} | {self.number_of_participants} participants"


