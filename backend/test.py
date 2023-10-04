from config import app, db
from models.init_db import init_db
from models.location import Location
from models.user import User
from sqlalchemy import select
# This is used to test the database

with app.app_context():
    db.session.add(Location(location_x=1, location_y=2))
    db.session.add(User(username="TRBF", age=3, display_name="TUDOR", password=1231241, profile_picture="pinterest.com", rating=4.5, completed_activity_count=2))
    db.session.commit()
    print(Location.query.all()) 

