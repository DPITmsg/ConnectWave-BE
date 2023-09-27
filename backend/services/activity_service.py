from models.activity import Activity
from repository.activity_repository import ActivityRepository


def service_add_activity(name: str, category: str, description: str, location_id: str, number_of_participants: int):
    activity = parse_activity(name, category, description, location_id, number_of_participants)
    repo = ActivityRepository()
    return repo.add(activity)

def service_remove_activity(column, value):
    repo = ActivityRepository()
    return repo.remove(column, value)

def service_update_activity(column, value, **kwargs):
    repo = ActivityRepository()
    return repo.update(column, value, **kwargs)

def service_get_activity(activity_id):
    repo = ActivityRepository()
    return repo.get_with_key(activity_id)

def service_get_all_activities():
    repo = ActivityRepository()
    return repo.get_all()

def service_rollback():
    repo = ActivityRepository()
    repo.rollback()

def parse_activity(name: str, category: str, description: str, location_id: str, number_of_participants: int):
    return Activity(name=name, category=category, description=description, location_id=location_id, number_of_participants=number_of_participants) # Function exists in case we need to do something else when creating an activity 
