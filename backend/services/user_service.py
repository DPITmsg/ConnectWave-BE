from models.user import User
from repository.user_repository import UserRepository

# todo implement methods mentioned in router.py
class UserService(BaseRepository):
    _repo = UserRepository()

    def add_user(username: str, age: int, display_name: str, password: str, completed_activity_count: int = 0, profile_picture: str = '', rating: float = None):
        user = parse_user(username, age, display_name, password, completed_activity_count)
        return self._repo.add(user)
    
    def remove_user(column, value):
        return self._repo.remove(column, value)
    
    def update_user(column, value, **kwargs):
        return self._repo.update(column, value, **kwargs)
    
    def get_user(user_id):
        return self._repo.get_with_key(user_id)
    
    def get_all_users():
        return self._repo.get_all()
    
    def rollback():
        self._repo.rollback()
    
    
    def parse_user(username: str, age: int, display_name: str, password: str, completed_activity_count: float, profile_picture: str = '', rating: float = None):
        return User(username=username, age=age, display_name=display_name, password=password, completed_activity_count=completed_activity_count, profile_picture=profile_picture, rating=rating)
