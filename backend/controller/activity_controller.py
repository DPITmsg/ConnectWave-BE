import json

from flask import jsonify, request, Response

from services.activity_service import *
from backend.services.activity_service import ActivityService
from backend.services.location_service import LocationService
from backend.services.user_service import UserService
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
            activity_data.append({'id': activity.id, 'date': activity.start_date, 'endDate': activity.end_date, 'time': activity.time,
                 'author': activity.author, 'title': activity.name, 'tags': activity.tags,
                 'category': activity.category, 'address': activity.address, 'description': activity.description,
                 'location': location, 'participants': activity.participants, 'maxParticipants': activity.max_participants})
        return jsonify(activity_data)

    except Exception as error:
        logging.error(error)
        # return jsonify(error), 400
        return jsonify(400)


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
    # TODO: fix tags and participants params (make them a list)
    print("Working")
    activity_service = ActivityService()
    location_service = LocationService()
    user_service = UserService()
    try:
        data = json.loads(request.data)

        location = data['location']
        location_x = location.get('latitude')
        location_y = location.get('longitude')
        created_location = location_service.add_location(location_x, location_y)

        tags = data['tags']
        string_of_tags = ""
        for tag in tags:
            string_of_tags += tag
            string_of_tags += ", "
        string_of_tags = string_of_tags[:len(string_of_tags) - 2]

        participants = data['participants']
        string_of_participants = ""
        for participant in participants:
            user = user_service.get_user(participant)
            if user is not None:
                string_of_participants += user.display_name
                string_of_participants += ", "
        string_of_participants = string_of_participants[:len(string_of_participants) - 2]

        created_activity = activity_service.add_activity(id=data['id'], name=data['title'], category=data['category'],
                                                         description=data['description'],
                                                         location_id=created_location.id,
                                                         max_participants=data['maxParticipants'],
                                                         start_date=data['date'], end_date=data['endDate'],
                                                         time=data['time'], tags=string_of_tags, address=data['address'],
                                                         author=data['author'], participants=string_of_participants)
        return str(created_activity.id), 201

    except Exception as error:
        logging.error(error)
        activity_service.rollback()
        return jsonify(error.__str__(), 400)
