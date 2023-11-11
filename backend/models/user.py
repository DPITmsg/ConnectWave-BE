from typing import Optional, List

from config import db
from sqlalchemy.orm import Mapped


class User(db.Model):
    __tablename__ = "user_table"
    __table_args__ = {'extend_existing': True}
    
    # Functional Variables
    username: Mapped[str] = db.mapped_column(primary_key=True)
    age: Mapped[int] = db.mapped_column(default=0)
    display_name: Mapped[str] = db.mapped_column(default="")
    password: Mapped[str] = db.mapped_column()
    profile_picture: Mapped[Optional[str]] = db.mapped_column(default="")
    about: Mapped[str] = db.mapped_column(default="")
    interests: Mapped[str] = db.mapped_column(default="")
    tags: Mapped[str] = db.mapped_column(default="")
    activities_created: Mapped[str] = db.mapped_column(default="")
    activities_enrolled: Mapped[str] = db.mapped_column(default="")
    activities_completed: Mapped[str] = db.mapped_column(default="")
    friends: Mapped[str] = db.mapped_column(default="")



    # Other data
    rating: Mapped[Optional[float]] = db.mapped_column()
    # favorite_category: Mapped[]


    def __repr__(self):
        return f"({self.username}) {self.display_name}: {self.age}"

    
