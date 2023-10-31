from models.activity import Activity
from repository.activity_repository import ActivityRepository
from services.base_service import BaseService

class ActivityService(BaseService):
    _repo = ActivityRepository()
    def add_activity(self, name: str, category: str, description: str, location_id: str, number_of_participants: int):
        activity = self.parse_activity(name=name, category=category, description=description, 
        location_id=location_id, number_of_participants=number_of_participants)
        return self._repo.add(activity)

    def remove_activity(self, column, value):
        return self._repo.remove(column, value)

    def update_activity(self, column, value, **kwargs):
        return self._repo.update(column, value, **kwargs)

    def get_activity(self, activity_id):
        return self._repo.get_with_key(activity_id)

    def get_all_activities(self):
            return self._repo.get_all()

    def parse_activity(self, name: str, category: str, description: str, location_id: str, number_of_participants: int):
        return Activity(name=name, category=category, description=description, 
        location_id=location_id, number_of_participants=number_of_participants) # Function exists in case we need to do something else when creating an activity 
