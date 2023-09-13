from models.activity import Activity
from repository.activity_repository import ActivityRepository


def service_add_activity(activity: Activity):
    repo = ActivityRepository()
    return repo.add(activity)

def service_remove_activity(activity: Activity):
    repo = ActivityRepository()
    return repo.remove(column, value)

def service_update_activity(activity: Activity, **kwargs):
    repo = ActivityRepository()
    return repo.update(column, value, **kwargs)

def service_get_activity(activity_id):
    repo = ActivityRepository()
    return repo.get_with_key(activity_id)

def service_get_all_activities(activity_id):
    repo = ActivityRepository()
    return repo.get_all()
