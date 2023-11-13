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
        service.send_request(username_user, username_friend)
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
def decline_friend_request():
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
        utu_data = []
        for utu in result:
            utu_data.append({'username1': utu.username1, 'username2': utu.username2})
        return jsonify(utu_data)
   
    except Exception as error:
        logging.error(error)
        service.rollback()
        return jsonify(error.__str__(), 400)

@app.route('/friends_by_username', methods=['POST', 'GET'])
def friends_by_username():
    service = UserToUserService()
    try:
        data = json.loads(request.data)
        result = service.get_by_username(data['username'])
        utu_data = []
        for utu in result:
            utu_data.append({'username1': utu.username1, 'username2': utu.username2})
        return jsonify(utu_data)  

    except Exception as error:
        logging.error(error)
        service.rollback()
        return jsonify(error.__str__(), 400)


