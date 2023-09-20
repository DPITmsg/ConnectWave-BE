from backend.models.activity import Activity
from backend.repository.control import ControlScheme

def service_add_activity(activity):
    return ControlScheme.add(activity)


def servicer_get_activities():
    return ControlScheme.get_all(Activity)