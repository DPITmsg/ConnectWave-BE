from backend.config import app, db
from sqlalchemy import Table, Column, Integer, String
from sqlalchemy import ForeignKey
from typing import List
from typing import Optional
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from backend.models.user import User


class FriendList(db.Model):
    __tablename__ = "user_to_friends_list"

    username: Mapped[str] = db.mapped_column(db.ForeignKey(User.username), primary_key=True)
    friends_list: Mapped[Optional[
        str]] = db.mapped_column()  # We store the list as a string of usernames that will be joined by the \0 character
