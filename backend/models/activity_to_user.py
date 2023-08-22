from config import app, db 
from sqlalchemy import Table, Column, Integer, String
from sqlalchemy import ForeignKey 
from typing import List
from typing import Optional
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from models.activity import Activity
from models.user import User

class ActivityToUser(db.Model):
    __tablename__ = "activity_to_user"

    activity_id: Mapped[int] = db.mapped_column(db.ForeignKey(Activity.id), primary_key=True)
    username: Mapped[str] = db.mapped_column(db.ForeignKey(User.username), primary_key=True)
    administrator: Mapped[bool] = db.mapped_column()
    
    def __repr__(self):
        return f"{self.activity_id} - {self.username}"
