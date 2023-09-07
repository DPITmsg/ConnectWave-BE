from backend.models.user import User


def get_account_by_username_and_password(username, password):
    return User.query.filter_by(username=username, password=password).first()


def get_account_by_username(username):
    return User.query.filter_by(username=username).first()

