from models.activity import Activity
from repository.activity_repository import ActivityRepository


def service_add_activity(activity: Activity):
    ActivityRepository().add(activity)

def service_remove_activity(activity: Activity):
    ActivityRepository().remove(column, value)

def service_update_activity(activity: Activity, **kwargs):
    ActivityRepository().update(column, value, **kwargs)

def service_get_activity(activity_id):
    ActivityRepository().get_with_key(activity_id)

def service_get_all_activities(activity_id):
    ActivityRepository().get_all()
