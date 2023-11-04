from repository.base_repository import BaseRepository
from models.user import User


class UserRepository(BaseRepository):
    def __init__(self):
        self._model = User

    def get_user_by_username_and_password(self, username, password):
        return User.query.filter_by(username=username, password=password)


    def get_by_username(self, username):
        return User.query.get(username)