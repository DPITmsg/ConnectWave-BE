import json

from flask import jsonify, request

from services.activity_service import *
from services.activity_service import ActivityService
from config import app
import logging


@app.route('/activities')
def get_activities():
    try:
        service = ActivityService()
        activities = service.get_all_activities()
        activity_data = [{'id': activity.activity_id, 'date': activity.start_date, 'endDate': activity.end_date, 'time': activity.time, 'author': activity.author,  'title': activity.name, 'tags': activity.tags,
                          'category': activity.category, 'address': activity.address, 'description': activity.description, 'location_id': activity.location_id, 'participants': activity.number_of_participants, 'maxParticipants': activity.max_participants} for activity in activities]
        return jsonify(activity_data)

    except Exception as error:
        logging.error(error)
        service.rollback()
        return jsonify(error.__str__(), 400)

@app.route('/activity', methods=['POST'])
def create_activity():
    service = ActivityService()
    try:
        data = json.loads(request.data)
        created_activity = service.add_activity(activity_id=data['id'], name=data['name'], category=data['category'],
                                        description=data['description'])
        return created_user.username, 200

    except Exception as error:
        logging.error(error)
        service.rollback()
        return jsonify(error.__str__(), 400)
