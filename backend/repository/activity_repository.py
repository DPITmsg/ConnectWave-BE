from repository.base_repository import BaseRepository
from models.activity import Activity
from sqlalchemy import delete


class ActivityRepository(BaseRepository):
    def __init__(self):
        self._model = Activity

    def get_by_id(self, activity_id):
        return Activity.query.get(int(activity_id))
    def remove_activity(self, activity_id):
        target = self.get_by_id(activity_id)
        BaseRepository(Activity)._session.execute(delete(self._model).where(self._model.id == int(activity_id)))
        BaseRepository(Activity)._session.commit()
        return target
