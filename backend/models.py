from backend import app, db
from sqlalchemy import MetaData
from sqlalchemy import Table, Column, Integer, String
from sqlalchemy import ForeignKey 
from typing import List
from typing import Optional
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from sqlalchemy.orm import relationship
from sqlalchemy.orm import DeclarativeBase

app.app_context().push()


class Location(db.Model):
    __tablename__ = "location_table"
    
    id: Mapped[int] = db.mapped_column(primary_key=True, autoincrement=True)
    location_x: Mapped[int] = db.mapped_column()
    location_y: Mapped[int] = db.mapped_column()

    def __repr__(self):
        return f"({self.id}) {self.location_x}, {self.location_y}"


class Activity(db.Model):
    __tablename__ = "activity_table"

    id:  Mapped[int]  = db.mapped_column(primary_key=True, autoincrement=True)
    name: Mapped[str] = db.mapped_column()
    description: Mapped[str] = db.mapped_column()
    location_id: Mapped[int] = db.mapped_column(db.ForeignKey(Location.id))
    number_of_participants: Mapped[int] = db.mapped_column(default=0)

    
    def __repr__(self):
        return f"({self.id}) {self.name}: {self.description} | {self.number_of_participants} participants"


class User(db.Model):
    __tablename__ = "user_table"

    username: Mapped[str] = db.mapped_column(primary_key=True)
    age: Mapped[int] = db.mapped_column()
    display_name: Mapped[str] = db.mapped_column()
    password: Mapped[str] = db.mapped_column()

    def __repr__(self):
        return f"({self.username}) {self.display_name}: {self.age}"



class ActivityToUser(db.Model):
    __tablename__ = "activity_to_user"

    activity_id: Mapped[int] = db.mapped_column(db.ForeignKey(Activity.id), primary_key=True)
    username: Mapped[str] = db.mapped_column(db.ForeignKey(User.username), primary_key=True)

    def __repr__(self):
        return f"{self.activity_id} - {self.username}"


session = db.Session(db.engine)

db.create_all()

