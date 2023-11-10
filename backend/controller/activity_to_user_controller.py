import json

from flask import jsonify, request

from services.activity_service import *
from services.activity_to_user_service import ActivityToUserService
from config import app
import logging


@app.route('/join', methods=['POST'])
def join():
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
def quit():
    service = ActivityToUserService()
    try:
        data = json.loads(request.data)
        code = service.remove_user_from_activity(username=data['username'], id=data['id'])
        return jsonify(code)

    except Exception as error:
        logging.error(error)
        service.rollback()
        return jsonify(error.__str__(), 400)


@app.route('/atus', methods=['GET'])
def get_activity_to_users():
    try:
        atu_service = ActivityToUserService()
        atu_data = [] 
        for atu in atu_service.get_all_activity_to_users():
            atu_data.append({'id': atu.id, 'username': atu.username})

        return jsonify(atu_data)

    except Exception as error:
        logging.error(error)
        # return jsonify(error), 400
        return jsonify(400)


