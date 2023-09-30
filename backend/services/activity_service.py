from models.activity import Activity
from repository.activity_repository import ActivityRepository


def service_add_activity(activity_id: int, name: str, category: str, description: str, location_id: str):
    activity = parse_activity(activity_id, name, category, description, location_id)
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


def parse_activity(activity_id: int, name: str, category: str, description: str, location_id: str):
    return Activity(id=activity_id, name=name, category=category, description=description,
                    location_id=location_id)  # Function exists in case we need to do something else when creating an activity
