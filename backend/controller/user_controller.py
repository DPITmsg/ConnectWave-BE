import json

from flask import  jsonify, request

from services.user_service import UserService
from config import app
from models.user import User
import logging

@app.route('/users')
def get_users():
    service = UserService() 
    try:
        users = service.get_all_users()
        user_data = [
            {'username': user.username, 
             'age': user.age, 
             'display_name': user.display_name,
             'password': user.password,
             'about': user.about,
             } 
             for user in users]
            
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

        interests = ',\0'.join(data['interests'])  
        tags = ',\0'.join(data['tags'])

        print(interests)
        print(tags)

        created_user = service.add_user(
            username=data['username'], 
            age=data['age'], 
            display_name=data['name'], 
            password=data['password'],
            about=data['about'],
            interests=interests,
            tags=tags,

            profile_picture='',
            activities_created='',
            activities_enrolled='',
            activities_completed='',
            friends='',
            rating=0.0,
            )
        return created_user.username, 200

    except Exception as error:
        logging.error(error)
        service.rollback()
        return jsonify(error.__str__(), 400)
    
@app.route('/login', methods=['POST', 'GET'])
def login_user():
    service = UserService()

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
            response_data = {
                'username': user.username,
                'name': user.display_name,
                'age': user.age,
            }
            return jsonify({'user': response_data}), 200
        
        print('invalid password')
        return jsonify({'message': 'invalid password'})
        
    except Exception as error:
        logging.error(error)
        service.rollback()
        return jsonify(error.__str__(), 400)

        
