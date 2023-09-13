from models.user import User
from repository.user_repository import UserRepository

# todo implement methods mentioned in router.py
def service_add_user(location: User):
    repo = UserRepository()
    return repo.add(user)

def service_remove_user(column, value):
    repo = UserRepository()
    return repo.remove(column, value)

def service_update_user(column, value, **kwargs):
    repo = UserRepository()
    return repo.update(column, value, **kwargs)

def service_get_user(user_id):
    repo = UserRepository()
    return repo.get_with_key(user_id)

def service_get_all_users():
    repo = UserRepository()
    return repo.get_all()

