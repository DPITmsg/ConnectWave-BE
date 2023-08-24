from backend.config import app, db


def init_db():
    with app.app_context():
        session = db.Session(db.engine)
        db.create_all()


init_db()
