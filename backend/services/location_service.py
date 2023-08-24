from backend.models.location import Location
from backend.repository.control import ControlScheme


def service_add_location(location):
    return ControlScheme.add(location)


def service_get_locations():
    return ControlScheme.get_all(Location)
