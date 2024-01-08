from config import db
from models.user import User
from sqlalchemy.orm import Mapped


class UserToUser(db.Model):
    __tablename__ = "user_to_user"

    username1: Mapped[int] = db.mapped_column(db.ForeignKey(User.username), primary_key=True)
    username2: Mapped[int] = db.mapped_column(db.ForeignKey(User.username), primary_key=True)
    accepted: Mapped[bool] = db.mapped_column(default=False)
    
    def __repr__(self):
        return f"{self.username1} - {self.username2}"
