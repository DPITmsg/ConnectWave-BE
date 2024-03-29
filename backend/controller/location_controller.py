from flask import jsonify, request, json

from config import app
from services.location_service import LocationService 
from services.user_service import *
import logging

# todo rename router.py to location_controller.py
@app.route('/')
def hello_world():
    return "Hello Warudo!"


# todo move model object mapping to data to the service.
@app.route('/locations', methods=['GET'])
def get_locations():
    service = LocationService()
    try:
        locations = service.get_all_locations()
        location_data = [{'id': location.id, 'longitude': location.location_y, 'latitude': location.location_x}
        for location in locations]
        return jsonify(location_data), 400
    
    except Exception as error:
        logging.error(error)
        service.rollback()
        return jsonify(error.__str__(), 400)

# take data from the body of the request and create a new Location object
# todo move model object creation to service. 'Model' objects should be used only in
#  repositories and services, and 'data' only in services and controllers
@app.route('/location', methods=['POST'])
def create_location():
    service = LocationService()
    data = json.loads(request.data)
    try:
        created_location = service.add_location(Location(location_x=data['latitude'], location_y=['longitude']))
        return jsonify(created_location), 200

    except Exception as error:
        logging.error(error)
        service.rollback()
        return jsonify(error.__str__(), 400)



