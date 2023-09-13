import json

from flask import jsonify, request

from backend.services.user_service import *
from backend.config import app


@app.route('/users')
def get_users():
    users = service_get_all_users()
    user_data = [{'username': user.username, 'age': user.age, 'display_name': user.display_name,
                  'password': user.password} for user in users]
    return jsonify(user_data)


@app.route('/user', methods=['POST'])
def create_user():
    data = json.loads(request.data)
    service_add_user(User(username=data['username'], age=data['age'], display_name=data['name'], password="20john05"))

    return jsonify()
