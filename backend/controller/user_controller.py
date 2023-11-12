import json

from flask import jsonify, request
from services.activity_to_user_service import ActivityToUserService

from services.user_service import UserService
from config import app
from models.user import User
import logging


@app.route('/users', methods=['GET'])
def get_users():
    service = UserService()
    atu = ActivityToUserService()
    
    try:
        users = service.get_all_users()
        user_data = []

        for user in users:
            created_activities = atu.get_activities_created(user.username)
            enrolled_activities = atu.get_enrolled_activities(user.username)

            user_data.append({
                'username': user.username,
                'age': user.age,
                'display_name': user.display_name,
                'password': user.password,
                'about': user.about,
                'tags': user.tags,
                'interests': user.interests,
                'activities_created': created_activities,
                'activities_enrolled': enrolled_activities,
                'pfp': user.profile_picture
            })

        return jsonify(user_data)

    except Exception as error:
        logging.error(error)
        service.rollback()
        return jsonify(error.__str__(), 400)

@app.route('/user', methods=['POST'])
def create_user():
    service = UserService()
    try:
        data = json.loads(request.data)

        tags = data['tags']
        string_of_tags = ""
        for tag in tags:
            string_of_tags += tag
            string_of_tags += ","
        string_of_tags = string_of_tags[:len(string_of_tags) - 1]

        interests = data['interests']
        string_of_interests = ""
        for interest in interests:
            string_of_interests += interest
            string_of_interests += ","
        string_of_interests = string_of_interests[:len(string_of_interests) - 1]
        string_of_interests = string_of_interests[1:]

        created_user = service.add_user(username=data['username'], age=data['age'], display_name=data['name'],
                                        password=data['password'], tags=string_of_tags, interests=string_of_interests,
                                        about=data['about'], rating=data['rating'], profile_picture=data['pfp'])
        return created_user.username, 200

    except Exception as error:
        logging.error(error)
        service.rollback()
        return jsonify(error.__str__(), 400)
    
@app.route('/login', methods=['POST', 'GET'])
def login_user():
    service = UserService()
    atu = ActivityToUserService()

    try:
        data = json.loads(request.data)

        username = data['username']
        password = data['password']

        if not password or not username:
            return jsonify({'message': 'json content missing'}), 400

        user = service.get_user(username)
        if not user:
            return jsonify({'message': 'User not found'}), 404
        
        
        if password == user.password:
            created_activities = atu.get_activities_created(username)
            enrolled_activities = atu.get_enrolled_activities(username)

            response_data = {
                'username': user.username,
                'name': user.display_name,
                'age': user.age,
                'tags': user.tags,
                'interests': user.interests,
                'about': user.about,
                'activities_created': created_activities,
                'activities_enrolled': enrolled_activities,
                'pfp': user.profile_picture
            }
            return jsonify({'user': response_data}), 200
        
        print('invalid password')
        return jsonify({'message': 'invalid password'})
        
    except Exception as error:
        logging.error(error)
        service.rollback()
        return jsonify(error.__str__(), 400)
    

@app.route('/get_user_by_username', methods=['POST'])
def get_user_by_username():
    service = UserService()
    atu = ActivityToUserService()

    try:
        data = json.loads(request.data)

        username = data['username']

        user = service.get_user(username)

        if not user:
            return jsonify({'message': 'user not found'})
        
        created_activities = atu.get_activities_created(username)
        enrolled_activities = atu.get_enrolled_activities(username)
        
        response_data = {
                'username': user.username,
                'name': user.display_name,
                'age': user.age,
                'tags': user.tags,
                'interests': user.interests,
                'about': user.about,
                'activities_created': created_activities,
                'activities_enrolled': enrolled_activities,
                'pfp': user.profile_picture
        }
        return jsonify(response_data), 200
        

    except Exception as error:
        logging.error(error)
        service.rollback()
        return jsonify(error.__str__(), 400)

        
@app.route('/edit_user', methods=['POST'])
def edit_user():
    user_service = UserService()
    try:
        data = json.loads(request.data)

        tags = data['tags']
        string_of_tags = ""
        for tag in tags:
            string_of_tags += tag
            string_of_tags += ","
        string_of_tags = string_of_tags[:len(string_of_tags) - 2]

        interests = data['interests']
        string_of_interests = ""
        for interest in interests:
            string_of_interests += interest
            string_of_interests += ","
        string_of_interests = string_of_interests[:len(string_of_interests) - 2]

        updated_user = user_service.update_user_by_username(username=data['username'], new_display_name=data['name'],
                                                        new_age=data['age'], new_rating=data['rating'],
                                                        new_about=data['about'], new_tags=string_of_tags,
                                                        new_interests=string_of_interests)
        return jsonify(str(updated_user.username), 200)

    except Exception as error:
        logging.error(error)
        user_service.rollback()
        return jsonify(error.__str__(), 400)
