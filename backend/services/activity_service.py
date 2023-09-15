from backend.models.activity import Activity
from backend.repository.control import ControlScheme


def service_add_activity(activity):
    return ControlScheme.add(activity)


def service_get_activities():
    return ControlScheme.get_all(Activity)


def service_get_paginated_activities(number):
    return ControlScheme.get_limited(Activity, number)
