from backend.models.user import User
from backend.repository.control import ControlScheme


def service_add_user(user):
    return ControlScheme.add(user)


def service_get_users():
    return ControlScheme.get_all(User)


def service_get_user_by_id(user_id):
    friendlist = ControlScheme.get_with_key(User, user_id)

