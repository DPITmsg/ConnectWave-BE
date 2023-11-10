import json

from flask import jsonify, request

from backend.services.user_service import UserService
from config import app
from backend.models.user import User
import logging


@app.route('/users', methods=['GET'])
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
             'tags': user.tags,
             'interests': user.interests
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

        created_user = service.add_user(username=data['username'], age=data['age'], display_name=data['name'],
                                        password="20john05", tags=string_of_tags, interests=string_of_interests,
                                        about=data['about'])
        return created_user.username, 200

    except Exception as error:
        logging.error(error)
        service.rollback()
        return jsonify(error.__str__(), 400)

# TODO: finsih this endpoint
# @app.route('/edit_user', methods=['POST'])
# def edit_user():
#     user_service = UserService()
#     try:
#         data = json.loads(request.data)
#
#         tags = data['tags']
#         string_of_tags = ""
#         for tag in tags:
#             string_of_tags += tag
#             string_of_tags += ", "
#         string_of_tags = string_of_tags[:len(string_of_tags) - 2]
#
#         interests = data['interests']
#         string_of_interests = ""
#         for interest in interests:
#             string_of_interests += interest
#             string_of_interests += ", "
#         string_of_interests = string_of_interests[:len(string_of_interests) - 2]
#
#         user_service.update_user_by_username(username=data['username'], new_display_name=data['name'],
#                                                         new_age=data['age'], new_rating=data['rating'],
#                                                         new_about=data['about'], new_tags=string_of_tags,
#                                                         new_interests=string_of_interests)
#         return str(200)
#
#     except Exception as error:
#         logging.error(error)
#         user_service.rollback()
#         return jsonify(error.__str__(), 400)
