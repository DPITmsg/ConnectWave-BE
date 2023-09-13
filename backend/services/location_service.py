from models.location import Location
from repository.location_repository import LocationRepository

# todo implement methods mentioned in router.py
def service_add_location(location: Location):
    return LocationRepository().add(location)

def service_remove_location(column, value):
    return LocationRepository().remove(column, value)

def service_update_location(column, value, **kwargs):
    return LocationRepository().update(column, value, **kwargs)

def service_get_location(location_id):
    return LocationRepository().get_with_key(location_id)

def service_get_all_locations():
    return LocationRepository().get_all()

