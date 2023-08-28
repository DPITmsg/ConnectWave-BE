from typing import Optional

from backend.config import db
from backend.models.user import User
from sqlalchemy.orm import Mapped


class FriendList(db.Model):
    __tablename__ = "user_to_friends_list"

    username: Mapped[str] = db.mapped_column(db.ForeignKey(User.username), primary_key=True)
    friends_list: Mapped[Optional[str]] = db.mapped_column() # We store the list as a string of usernames that will be joined by the \0 character 
