from models.location import Location
from repository.location_repository import LocationRepository

# todo implement methods mentioned in router.py
def service_add_location(location_x: int, location_y: int):
    location = parse_location(location_x, location_y)
    repo = LocationRepository()
    return repo.add(location)

def service_remove_location(column, value):
    repo = LocationRepository()
    return repo.remove(column, value)

def service_update_location(column, value, **kwargs):
    repo = LocationRepository()
    return repo.update(column, value, **kwargs)

def service_get_location(location_id):
    repo = LocationRepository()
    return repo.get_with_key(location_id)

def service_get_all_locations():
    repo = LocationRepository()
    print(repo._model)
    return repo.get_all()

def parse_location(location_x: int, location_y: int):
    return Location(location_x = location_x, location_y = location_y)
