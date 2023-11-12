from repository.base_repository import BaseRepository
from models.user import User
from sqlalchemy import update, select


class UserRepository(BaseRepository):
    def __init__(self):
        self._model = User

    def get_user_by_username_and_password(self, username, password):
        return User.query.filter_by(username=username, password=password)

    def get_by_username(self, username):
        return User.query.get(username)

    def update_user(self, username, new_display_name, new_age, new_rating, new_about, new_interests, new_tags):
        BaseRepository(User)._session.execute(update(self._model).where(self._model.username == username).values(
            {'display_name': new_display_name, 'age': new_age, 'rating': new_rating, 'about': new_about,
             'interests': new_interests, 'tags': new_tags}))
        BaseRepository(User)._session.commit()
        return User.query.get(username)
