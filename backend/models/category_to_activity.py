from backend.config import db
from sqlalchemy.orm import Mapped
from backend.models.category import Category
from backend.models.activity import Activity


class CategoryToActivity(db.Model):
    __tablename__ = "category_to_activity"

    category_id: Mapped[int] = db.mapped_column(db.ForeignKey(Category.id), primary_key=True)
    activity_id: Mapped[int] = db.mapped_column(db.ForeignKey(Activity.id), primary_key=True)

    def __repr__(self):
        return f"{self.category_id - self.activity_id}"
