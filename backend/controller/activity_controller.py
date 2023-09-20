import json

from flask import jsonify, request

from backend.services.activity_service import *
from backend.config import app


@app.route('/activities')
def get_activities():
    activities = servicer_get_activities()
    activity_data = [{'id': activity.id, 'name': activity.name, 'description': activity.description,
                      'number_of_participants': activity.number_of_participants} for activity in activities]
    return jsonify(activity_data)


@app.route('/activity', methods=['GET'])
def create_activity():
    data = json.loads(request.data)
    service_add_activity(Activity(id=data['id'], name=data['name'], description=data['description'],
                                  number_of_participants=data['number_of_participants']))

    return jsonify()