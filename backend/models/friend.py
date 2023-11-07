from typing import Optional

from config import db
from models.user import User
from sqlalchemy.orm import Mapped


class Friend(db.Model):
    __tablename__ = "friend_table"

    username: Mapped[str] = db.mapped_column(db.ForeignKey(User.username))
    profile_picture: Mapped[Optional[str]] = db.mapped_column()
