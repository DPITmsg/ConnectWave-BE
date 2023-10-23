import json

from flask import jsonify, request, Response

from services.activity_service import *
from backend.services.activity_service import ActivityService
from config import app
import logging


@app.route('/activities', methods=['GET'])
def get_activities():
    try:
        service = ActivityService()
        activities = service.get_all_activities()
        activity_data = [
            {'id': activity.id, 'date': activity.start_date, 'endDate': activity.end_date, 'time': activity.time,
             'author': activity.author, 'title': activity.name, 'tags': activity.tags,
             'category': activity.category, 'address': activity.address, 'description': activity.description,
             'location_id': activity.location_id, 'participants': activity.participants,
             'maxParticipants': activity.max_participants} for activity in activities]
        return jsonify(activity_data)

    except Exception as error:
        logging.error(error)
        # return jsonify(error), 400
        return jsonify(400)


@app.route('/activity_by_id', methods=['GET'])
def get_activity_by_id():
    try:
        service = ActivityService()
        activity = service.get_activity(request.args.get('id'))
        activity_data = [
            {'id': activity.id, 'start_date': activity.start_date, 'end_date': activity.end_date, 'time': activity.time,
             'author': activity.author, 'title': activity.name, 'tags': activity.tags,
             'category': activity.category, 'address': activity.address, 'description': activity.description,
             'location_id': activity.location_id, 'participants': activity.participants,
             'maxParticipants': activity.max_participants}]
        return jsonify(activity_data)

    except Exception as error:
        logging.error(error)
        # return jsonify(error), 400
        return "Not found", 404


@app.route('/activity', methods=['POST'])
def create_activity():
    print("Working")
    service = ActivityService()
    try:
        data = json.loads(request.data)
        created_activity = service.add_activity(id=data['id'], name=data['title'], category=data['category'],
                                                description=data['description'], location_id=data['location'],
                                                max_participants=data['maxParticipants'],
                                                start_date=data['date'], end_date=data['endDate'],
                                                time=data['time'], tags=data['tags'], address=data['address'],
                                                author=data['author'], participants=data['participants'])
        return str(created_activity.id), 201

    except Exception as error:
        logging.error(error)
        service.rollback()
        return jsonify(error.__str__(), 400)
