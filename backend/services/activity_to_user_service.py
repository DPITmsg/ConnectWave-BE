from models.activity_to_user import ActivityToUser
from models.user import User
from models.activity import Activity
from repository.activity_to_user_repository import ActivityToUserRepository
from repository.activity_repository import ActivityRepository

class ActivityToUserService(BaseService):
    _repo = ActivityToUserRepository()
    _activity_repo = ActivityRepository()

    def get_activity_to_user(self, username, id):
        result = self._repo.get_with_many(User.username == username, Activity.id == id)
        return result

    def join_activity(self, username, id):
        if(get_activity_to_user(username, id) is None):
            activityToUser = ActivityToUser(id = id, username = username) 
            self._repo.add(activityToUser)
            return activityToUser
        activityToUser = get_activity_to_user(username, id)
        return activityToUser

    def remove_user_from_activity(self, username, id):
        return self._repo.remove(username, id)

