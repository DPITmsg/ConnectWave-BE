from models.user import User
from repository.user_repository import UserRepository

# todo implement methods mentioned in router.py
def service_add_user(location: User):
    return UserRepository.add(user)

def service_remove_user(column, value):
    return UserRepository.remove(column, value)

def service_update_user(column, value, **kwargs):
    return UserRepository.update(column, value, **kwargs)

def service_get_user(user_id):
    return UserRepository.get_with_key(user_id)

def service_get_all_users():
    return UserRepository.get_all()

