from models.activity_to_user import ActivityToUser
from models.user import User
from models.activity import Activity
from repository.activity_to_user_repository import ActivityToUserRepository

class ActivityToUserService(BaseService):
    _repo = ActivityToUserRepository()

    def join_activity(self, username, activity_id):
        aTusr = ActivityToUser(activity_id = activity_id, username = username)
        self._repo.add(aTusr)
        return aTusr

    def get_activities_with_username(self, username):
        entries = self._repo.get_where(username)
        return entries




