import json

from flask import jsonify, request

from backend.services.activity_service import *
from backend.config import app


@app.route('/activities', methods=['GET'])
def get_all_activities():
    activities = service_get_activities()
    activity_data = [{'id': activity.id, 'name': activity.name, 'description': activity.description,
                      'location_id': activity.location_id, 'number_of_participants': activity.number_of_participants}
                     for activity in activities]
    return jsonify(activity_data)


@app.route('/p_activities', methods=['GET'])
def get_paginated_activities():
    activities = service_get_paginated_activities(1)
    activity_data = [{'id': activity.id, 'name': activity.name, 'description': activity.description,
                      'location_id': activity.location_id, 'number_of_participants': activity.number_of_participants}
                     for activity in activities]
    return jsonify(activity_data)


@app.route('/activity', methods=['POST'])
def create_activity():
    data = json.loads(request.data)
    service_add_activity(
        Activity(id=data['id'], name=data['name'], description=data['description'], location_id=data['location_id'],
                 number_of_participants=data['number_of_participants']))

    return jsonify()
