import json

from flask import  jsonify, request

from services.user_service import *
from config import app
from models.user import User
import logging

@app.route('/users')
def get_users():
    try:
        users = service_get_all_users()
        user_data = [{'username': user.username, 'age': user.age, 'display_name': user.display_name,
                    'password': user.password} for user in users]
        return jsonify(user_data)
   
    except Exception as error:
        logging.error(error)
        # return jsonify(error), 400
        return jsonify(400)


@app.route('/user', methods=['POST'])
def create_user():
    print("Working")
    try:
        data = json.loads(request.data)
        created_user = service_add_user(username=data['username'], age=data['age'], display_name=data['name'], password="20john05")
        return created_user.username, 200

    except Exception as error:
        logging.error(error)
        service_rollback()
        return jsonify(error.__str__(), 400)

