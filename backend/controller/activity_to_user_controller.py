import json

from flask import jsonify, request

from services.activity_service import *
from services.activity_to_user_service import ActivityToUserService
from config import app
import logging


@app.route('/join', methods=['POST'])
def get_activities():
    try:
        service = ActivityToUserService()
        data = json.loads(request.data)
        created_join = service.join_activity(username=data['username'], id=data['id'])
        return jsonify(created_join)

    except Exception as error:
        logging.error(error)
        service.rollback()
        return jsonify(error.__str__(), 400)


@app.route('/quit', methods=['POST'])
def create_activity():
    service = ActivityToUserService()
    try:
        data = json.loads(request.data)
        code = service.remove_user_from_activity(username=data['username'], id=data['id'])
        return jsonify(code)

    except Exception as error:
        logging.error(error)
        service.rollback()
        return jsonify(error.__str__(), 400)
