from config import app, db
from models.init_db import init_db
from models.location import Location

init_db()

# This is used to test the database

with app.app_context():
    db.session.add(Location(location_x=1, location_y=2))
    db.session.commit()
