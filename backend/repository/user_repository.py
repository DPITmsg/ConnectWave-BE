from repository.base_repository import BaseRepository
from models.user import User
from sqlalchemy import update


class UserRepository(BaseRepository):
    def __init__(self):
        self._model = User  

    def get_by_username(self, username):
        return self.get_with_key(username)

        self._model = User

    def get_user_by_username_and_password(self, username, password):
        return User.query.filter_by(username=username, password=password)

    def get_by_username2(self, username):
        return User.query.get(username)

    # def update_user(self, username, new_display_name, new_age, new_rating, new_about, new_interests, new_tags):
    #     return update(User).where(User.username == username).values(
    #         {"age": new_age})
