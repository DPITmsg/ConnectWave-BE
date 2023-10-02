from models.location import Location
from self._repository.location_repository import LocationRepository
from services.base_service import BaseService

class LocationService(BaseRepository):
    _repo = ActivityRepository()

    def add_location(location_x: int, location_y: int):
        location = parse_location(location_x, location_y)
        return self._repo.add(location)

    def remove_location(column, value):
        return self._repo.remove(column, value)

    def update_location(column, value, **kwargs):
        return self._repo.update(column, value, **kwargs)

    def get_location(location_id):
        return self._repo.get_with_key(location_id)

    def get_all_locations():
        print(repo._model)
        return self._repo.get_all()

    def parse_location(location_x: int, location_y: int):
        return Location(location_x = location_x, location_y = location_y)
