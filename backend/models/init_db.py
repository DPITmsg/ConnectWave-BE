from main import app, db
from models.core_models import *
from models.feature_models import *

def init_db():
    with app.app_context():
       session = db.Session(db.engine)
       db.create_all()

init_db()

