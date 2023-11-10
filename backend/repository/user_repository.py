from repository.base_repository import BaseRepository
from models.user import User


class UserRepository(BaseRepository):
    def __init__(self):
        self._model = User  

    def get_by_username(self, username):
        return self.get_with_key(username)

