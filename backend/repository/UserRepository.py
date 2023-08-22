
from backend.model.core_models import User, db


class UserRepository:
    @staticmethod
    def create(username):
        new_user = User(username=username)
        db.session.add(new_user)
        db.session.commit()
        return new_user

    @staticmethod
    def get_by_id(user_id):
        return User.query.get(user_id)

    @staticmethod
    def get_by_username(username):
        return User.query.filter_by(username=username).first()

    @staticmethod
    def get_all():
        return User.query.all()

    @staticmethod
    def update(user, new_username):
        user.username = new_username
        db.session.commit()
        return user

    @staticmethod
    def delete(user):
        db.session.delete(user)
        db.session.commit()
