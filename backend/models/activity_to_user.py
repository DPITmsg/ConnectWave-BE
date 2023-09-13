from config import db
from models.activity import Activity
from models.user import User
from sqlalchemy.orm import Mapped


class ActivityToUser(db.Model):
    __tablename__ = "activity_to_user"

    activity_id: Mapped[int] = db.mapped_column(db.ForeignKey(Activity.id), primary_key=True)
    username: Mapped[str] = db.mapped_column(db.ForeignKey(User.username), primary_key=True)
    administrator: Mapped[bool] = db.mapped_column()
    
    def __repr__(self):
        return f"{self.activity_id} - {self.username}"
