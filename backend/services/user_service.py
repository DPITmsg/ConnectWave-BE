from models.user import User
from repository.user_repository import UserRepository
from services.base_service import BaseService


class UserService(BaseService):
    _repo = UserRepository()

    def add_user(self, username: str, age: int, display_name: str, password: str, profile_picture: str, about: str,
                 interests: str = '', tags: str = '', activities_created: str = '', activities_enrolled: str = '',
                 activities_completed: str = '', friends: str = '', rating: float = 0.0):
        # Ensure that the rating is a float


        user = self.parse_user(username, age, display_name, password, profile_picture, about, interests, tags,
                               activities_created, activities_enrolled, activities_completed, friends, rating=0.0)
        return self._repo.add(user)

    def remove_user(self, column, value):
        return self._repo.remove(column, value)

    def update_user(self, column, value, **kwargs):
        return self._repo.update(column, value, **kwargs)

    def get_user(self, username):
        return self._repo.get_by_username(username)

    def get_all_users(self):
        return self._repo.get_all()

    # def update_user_by_username(self, username, new_display_name, new_age, new_rating, new_about, new_interests,
    #                             new_tags):
    #     return self._repo.update_user(username, new_display_name, new_age, new_rating, new_about, new_interests,
    #                                   new_tags)
    def update_user_by_username(self, username, new_display_name, new_age, new_rating, new_about, new_interests,
                                new_tags):
        return self._repo.update_user(username, new_display_name, new_age, new_rating, new_about, new_interests,
                                      new_tags)

    def login(self, username, password):
        return self._repo.get_user_by_username_and_password(username, password)

    def regiser(self, username):
        return self._repo.get_user_by_username(username)

    def rollback(self):
        self._repo.rollback()

    def parse_user(self, username, age, display_name, password, profile_picture, about, interests, tags, activities_created: str = "",
                   activities_enrolled: str = "", activities_completed: str = "", friends: str = "",
                   rating: float = 0.0,):
        return User(username=username, age=age, display_name=display_name, password=password,
                    about=about, interests=interests, tags=tags,
                    activities_created=activities_created, activities_enrolled=activities_enrolled,
                    activities_completed=activities_completed, friends=friends, rating=rating, profile_picture=profile_picture)
