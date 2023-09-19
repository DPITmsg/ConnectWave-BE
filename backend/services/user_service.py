from models.user import User
from repository.user_repository import UserRepository


user_repo = UserRepository()


# todo implement methods mentioned in router.py
def service_add_user(username: str, age: int, display_name: str, password: str, completed_activity_count: float, profile_picture: str = '', rating: float = None):
    user = parse_user(username, age, display_name, password, completed_activity_count)
    return repo.add(user)

def service_remove_user(column, value):
    return repo.remove(column, value)

def service_update_user(column, value, **kwargs):
    return repo.update(column, value, **kwargs)

def service_get_user(user_id):
    return repo.get_with_key(user_id)

def service_get_all_users():
    return repo.get_all()

def parse_user(username: str, age: int, display_name: str, password: str, completed_activity_count: float, profile_picture: str = '', rating: float = None):
    return User(username=username, age=age, display_name=display_name, password=password, completed_activity_count=completed_activity_count, profile_picture=profile_picture, rating=rating)
