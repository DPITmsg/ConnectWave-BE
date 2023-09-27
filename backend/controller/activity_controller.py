import json

from flask import jsonify, request

from services.activity_service import *
from config import app
from models.activity import Activity
import logging


@app.route('/activities')
def get_activities():
    try:
        activities = service_get_all_activities()
        activity_data = [{'id': activity.id, 'name': activity.name, 'category': activity.category,
                          'description': activity.description, 'location_id': activity.location_id,
                          'number_of_participants': activity.number_of_participants} for activity in activities]
        return jsonify(activity_data)

    except Exception as error:
        logging.error(error)
        # return jsonify(error), 400
        return jsonify(400)


@app.route('/activity', methods=['POST'])
def create_activity():
    print("Working")
    try:
        data = json.loads(request.data)
        created_activity = service_add_activity(id=data['id'], name=data['name'], category=data['category'],
                                        description=data['description'])
        return created_user.username, 200

    except Exception as error:
        logging.error(error)
        service_rollback()
        return jsonify(error.__str__(), 400)
