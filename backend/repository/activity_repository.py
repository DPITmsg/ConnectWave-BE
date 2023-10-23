from repository.base_repository import BaseRepository
from models.activity import Activity


class ActivityRepository(BaseRepository):
    def __init__(self):
        self._model = Activity

    def get_by_id(self, activity_id):
        return Activity.query.get(int(activity_id))
