from repository.base_repository import BaseRepository
from models.location import Location


class LocationRepository(BaseRepository):
    def __init__(self):
        self._model = Location

    def get_by_id(self, location_id):
        return Location.query.get(int(location_id))
