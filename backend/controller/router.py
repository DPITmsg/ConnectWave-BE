from flask import jsonify

from backend.config import app
from backend.services.location_service import *


@app.route('/')
def hello_world():
    return "Hello Warudo!"


@app.route('/locations')
def get_locations():
    locations = service_get_locations()
    location_data = [{'id': location.id, 'longitude': location.location_y, 'latitude': location.location_x}
                     for location in locations]
    return jsonify(location_data)


@app.route('/location')
def create_location():
    service_add_location(Location(location_x=1, location_y=2))

    return jsonify()
