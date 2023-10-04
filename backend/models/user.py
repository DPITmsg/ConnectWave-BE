from typing import Optional, List

from config import db
from sqlalchemy.orm import Mapped


class User(db.Model):
    __tablename__ = "user_table"
    
    # Functional Variables
    username: Mapped[str] = db.mapped_column(primary_key=True)
    age: Mapped[int] = db.mapped_column()
    display_name: Mapped[str] = db.mapped_column()
    password: Mapped[str] = db.mapped_column()
    profile_picture: Mapped[Optional[str]] = db.mapped_column
    about: Mapped[str] = db.mapped_column()
    interests: Mapped[str] = db.mapped_column
    tags: Mapped[str] = db.mapped_column
    activities_created: Mapped[str] = db.mapped_column(default=0)
    activities_enrolled: Mapped[str] = db.mapped_column(default=0)
    friends: Mapped[str] = db.mapped_column(default=[])



    # Other data
    rating: Mapped[Optional[float]] = db.mapped_column()
    completed_activity_count: Mapped[int] = db.mapped_column(default=0)
    # favorite_category: Mapped[]


    def __repr__(self):
        return f"({self.username}) {self.display_name}: {self.age}"


