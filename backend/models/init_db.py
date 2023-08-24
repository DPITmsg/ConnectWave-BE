from backend.config import app, db
from backend.models.activity import Activity
from backend.models.user import User
from backend.models.location import Location




def init_db():
    with app.app_context():
        session = db.Session(db.engine)
        db.create_all()


init_db()
