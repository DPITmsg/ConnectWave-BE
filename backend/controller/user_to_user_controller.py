import json

from flask import  jsonify, request

from services.user_service import UserService
from config import app
from models.user_to_user import UserToUser
from services.user_to_user_service import UserToUserService
import logging

@app.route('/send_friend_request', methods=['POST'])
def add_friend():
    service = UserToUserService() 
    try:

        data = json.loads(request.data)
        username_user = data['username_user']
        username_friend = data['username_friend']
        service.add_friend(username_user, username_friend)
        return jsonify(200)
   
    except Exception as error:
        logging.error(error)
        service.rollback()
        return jsonify(error.__str__(), 400)

@app.route('/accept_friend_request', methods=['POST'])
def accept_friend_request():
    service = UserToUserService() 
    try:
        data = json.loads(request.data)
        username_user = data['username_user']
        username_friend = data['username_friend']
        service.accept_request(username_user, username_friend)
        return jsonify(200)
   
    except Exception as error:
        logging.error(error)
        service.rollback()
        return jsonify(error.__str__(), 400)

@app.route('/decline_friend_request', methods=['POST'])
def accept_friend_request():
    service = UserToUserService() 
    try:
        data = json.loads(request.data)
        username_user = data['username_user']
        username_friend = data['username_friend']
        service.decline_request(username_user, username_friend)
        return jsonify(200)
   
    except Exception as error:
        logging.error(error)
        service.rollback()
        return jsonify(error.__str__(), 400)

@app.route('/friend_relationships', methods=['GET'])
def friends():
    service = UserToUserService()
    try:
        result = service.get_all()
        return jsonify(result)
   
    except Exception as error:
        logging.error(error)
        service.rollback()
        return jsonify(error.__str__(), 400)

@app.rout('/friends_by_username', methods='GET')
def friends_by_username():
    service = UserToUserService()
    try:
        result = service.get_by_username()
        return jsonify(result)
   
    except Exception as error:
        logging.error(error)
        service.rollback()
        return jsonify(error.__str__(), 400)


