from repository.base_repository import BaseRepository
from models.friend_list import FriendList


class FriendListRepository(BaseRepository):
    def __init__(self):
        self._model = FriendList 
