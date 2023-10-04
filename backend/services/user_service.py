from models.user import User
from repository.user_repository import UserRepository
from backend.services.base_service import BaseService

# from backend.models.user import User
# from backend.repository.user_repository import UserRepository


# todo implement methods mentioned in router.py
class UserService(BaseService):
    _repo = UserRepository()

    def add_user(self, username: str, age: int, display_name: str, password: str, completed_activity_count: int = 0, profile_picture: str = '', rating: float = None):
        user = parse_user(username, age, display_name, password, completed_activity_count)
        return self._repo.add(user)
    
    def remove_user(self, column, value):
        return self._repo.remove(column, value)
    
    def update_user(self, column, value, **kwargs):
        return self._repo.update(column, value, **kwargs)
    
    def get_user(self, user_id):
        return self._repo.get_with_key(user_id)
    
    def get_all_users(self, ):
        return self._repo.get_all()
    
    def rollback(self, ):
        self._repo.rollback()
    
    
    def parse_user(username: str, age: int, display_name: str, password: str, completed_activity_count: float, profile_picture: str = '', rating: float = None):
        return User(username=username, age=age, display_name=display_name, password=password, completed_activity_count=completed_activity_count, profile_picture=profile_picture, rating=rating)