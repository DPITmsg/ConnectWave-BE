from repository.base_repository import BaseRepository
from models.location import Location


class LocationRepository(BaseRepository):
    def __init__(self):
        self._model = Location  
