from models import app, db
from models.core_models import *
from models.feature_models import *

@app.cli.command("init_db")
def init_db():
    session = db.Session(db.engine)
    db.create_all()

