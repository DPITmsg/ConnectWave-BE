from models.location import Location
from repository.location_repository import LocationRepository
from services.base_service import BaseService

class LocationService(BaseService):
    _repo = LocationRepository()

    def add_location(self, location_x: int, location_y: int):
        location = self.parse_location(location_x, location_y)
        return self._repo.add(location)

    def remove_location(self, column, value):
        return self._repo.remove(column, value)

    def update_location(self, column, value, **kwargs):
        return self._repo.update(column, value, **kwargs)

    def get_location(self, location_id):
        return self._repo.get_by_id(location_id)

    def get_all_locations(self):
        return self._repo.get_all()

    def parse_location(self, location_x: int, location_y: int):
        return Location(location_x = location_x, location_y = location_y)
