from main import app, db
from sqlalchemy import Table, Column, Integer, String
from sqlalchemy import ForeignKey 
from typing import List
from typing import Optional
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column


class User(db.Model):
    __tablename__ = "user_table"
    
    # Functional Variables
    username: Mapped[str] = db.mapped_column(primary_key=True)
    age: Mapped[int] = db.mapped_column()
    display_name: Mapped[str] = db.mapped_column()
    password: Mapped[str] = db.mapped_column()
    
    # Other data
    rating: Mapped[Optional[float]] = db.mapped_column()
    completed_activity_count: Mapped[float] = db.mapped_column(default=0)
    # favorite_category: Mapped[]


    def __repr__(self):
        return f"({self.username}) {self.display_name}: {self.age}"


