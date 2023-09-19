from repository.base_repository import BaseRepository
from models.activity import Activity


class ActivityRepository(BaseRepository):
    def __init__(self):
        self._model = Activity  
