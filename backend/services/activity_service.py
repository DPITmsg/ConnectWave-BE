from models.activity import Activity
from repository.activity_repository import ActivityRepository
from services.base_service import BaseService


class ActivityService(BaseService):
    _repo = ActivityRepository()

    def parse_activity(self, name: str, category: str, description: str, location_id: str,
                       max_participants: int,
                       start_date: str, end_date: str, time: str, tags: str, address: str, author: str):
        return Activity(name=name, category=category, description=description,
                        location_id=location_id, max_participants=max_participants, start_date=start_date,
                        end_date=end_date, time=time, tags=tags, address=address, author=author)
    # Function exists in case we need to do something else when creating an activity

    def add_activity(self, name: str, category: str, description: str, location_id: int,
                     max_participants: int,
                     start_date: str, end_date: str, time: str, tags: str, address: str, author: str):
        activity = self.parse_activity(name, category, description, location_id, max_participants, start_date,
                                  end_date, time, tags, address, author)
        return self._repo.add(activity)

    def remove_activity(self, column, value):
        return self._repo.remove(column, value)
    def delete_activity(self, activity_id):
        return self._repo.remove_activity(activity_id)

    def update_activity(self, column, value, **kwargs):
        return self._repo.update(column, value, **kwargs)

    def get_activity(self, id):
        return self._repo.get_by_id(id)

    def get_all_activities(self):
        return self._repo.get_all()

    def rollback(self):
        self._repo.rollback()
