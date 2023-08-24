from backend.config import db
from sqlalchemy.orm import Mapped
from backend.models.category import Category
from backend.models.user import User


class CategoryToUser(db.Model):
    __tablename__ = "category_to_user"

    category_id: Mapped[int] = db.mapped_column(db.ForeignKey(Category.id), primary_key=True)
    username: Mapped[str] = db.mapped_column(db.ForeignKey(User.username), primary_key=True)

    def __repr__(self):
        return f"{self.category_id - self.username}"
