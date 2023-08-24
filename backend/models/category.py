from backend.config import db
from sqlalchemy.orm import Mapped


class Category(db.Model):
    __tablename__ = "category_table"

    id: Mapped[int] = db.mapped_column(primary_key=True, autoincrement=True)
    name: Mapped[str] = db.mapped_column()

    def __repr__(self):
        return f"({self.id}) {self.name}"
