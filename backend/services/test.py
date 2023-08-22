from backend.repository.control import ControlScheme
from models import app, db
from models.location import Location


controller = ControlScheme(app=app, db=db)
controller.add(Location(location_x=2, location_y=3))

# This is for testing purposes, as the name "test.py" suggests
