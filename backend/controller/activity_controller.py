import json

from flask import jsonify, request, Response

from services.activity_service import *
from services.activity_service import ActivityService
from config import app
import logging


@app.route('/activities', methods=['GET'])
def get_activities():
    try:
        activity_service = ActivityService()
        location_service = LocationService()
        activities = activity_service.get_all_activities()
        activity_data = []
        for activity in activities:
            if (location_service.get_location(activity.location_id) is None):
                location = None
            else:
                location = {'latitude': location_service.get_location(activity.location_id).location_x,
                            'longitude': location_service.get_location(activity.location_id).location_y}
            activity_data.append({'id': activity.activity_id, 'date': activity.start_date, 'endDate': activity.end_date, 'time': activity.time,
                 'author': activity.author, 'title': activity.name, 'tags': activity.tags,
                 'category': activity.category, 'address': activity.address, 'description': activity.description,
                 'location': location, 'participants': activity.participants, 'maxParticipants': activity.max_participants})
        return jsonify(activity_data)

    except Exception as error:
        logging.error(error)
        service.rollback()
        return jsonify(error.__str__(), 400)

@app.route('/activity_by_id', methods=['GET'])
def get_activity_by_id():
    try:
        activity_service = ActivityService()
        location_service = LocationService()
        activity = activity_service.get_activity(request.args.get('id'))
        if (location_service.get_location(activity.location_id) is None):
            location = None
        else:
            location = {'latitude': location_service.get_location(activity.location_id).location_x,
                        'longitude': location_service.get_location(activity.location_id).location_y}
        activity_data = {'id': activity.id, 'date': activity.start_date, 'endDate': activity.end_date, 'time': activity.time,
                 'author': activity.author, 'title': activity.name, 'tags': activity.tags,
                 'category': activity.category, 'address': activity.address, 'description': activity.description,
                 'location': location, 'participants': activity.participants, 'maxParticipants': activity.max_participants}
        return jsonify(activity_data)

    except Exception as error:
        logging.error(error)
        # return jsonify(error), 400
        return "Not found", 404


@app.route('/activity', methods=['POST'])
def create_activity():
    activity_service = ActivityService()
    location_service = LocationService()
    try:
        data = json.loads(request.data)
        location = data['location']
        location_x = location.get('latitude')
        location_y = location.get('longitude')
        created_location = location_service.add_location(location_x, location_y)
        created_activity = activity_service.add_activity(activity_id=data['id'], name=data['title'], category=data['category'],
                                                         description=data['description'],
                                                         location_id=created_location.id,
                                                         max_participants=data['maxParticipants'],
                                                         start_date=data['date'], end_date=data['endDate'],
                                                         time=data['time'], tags=data['tags'], address=data['address'],
                                                         author=data['author'], participants=data['participants'])
        return str(created_activity.activity_id), 201

    except Exception as error:
        logging.error(error)
        activity_service.rollback()
        return jsonify(error.__str__(), 400)
