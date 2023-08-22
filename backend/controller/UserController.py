from flask import jsonify, request

from backend.main import app
from backend.repository.UserRepository import UserRepository


@app.route('/', methods=['GET'])
def get_users():
    users = UserRepository.get_all()
    users_data = [{'id': user.id, 'username': user.username} for user in users]
    return "hello worl"

@app.route('/users', methods=['GET'])
def get_users():
    users = UserRepository.get_all()
    users_data = [{'id': user.id, 'username': user.username} for user in users]
    return jsonify(users_data)


@app.route('/user', methods=['POST'])
def create_user():
    data = request.get_json()
    if 'username' not in data:
        return jsonify({'error': 'Username is required'}), 400

    new_user = UserRepository.create(data['username'])
    return jsonify({'message': 'User created successfully', 'user_id': new_user.id}), 201
