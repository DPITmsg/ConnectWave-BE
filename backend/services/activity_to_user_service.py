from models.activity_to_user import ActivityToUser
from models.user import User
from models.activity import Activity
from repository.activity_to_user_repository import ActivityToUserRepository
from repository.activity_repository import ActivityRepository
from repository.user_repository import UserRepository
from services.base_service import BaseService
from sqlalchemy import select

class ActivityToUserService(BaseService):
    _repo = ActivityToUserRepository()
    _activity_repo = ActivityRepository()
    _session = ActivityToUserRepository().get_session()

    def get_activity_to_user(self, username, id):
        result = self._session.query(ActivityToUser).all()
        for atu in result:
            if atu.username == username and atu.id == id:
                return result
        return None

    def join_activity(self, username, id):
        if(self.get_activity_to_user(username, id) is None):
            activityToUser = ActivityToUser(id = id, username = username) 
            self._repo.add(activityToUser)
            return activityToUser
        activityToUser = self.get_activity_to_user(username, id)
        return activityToUser

    def remove_user_from_activity(self, username, id):
        return self._repo.remove(username, id)

    def get_all_activity_to_users(self):
        return self._repo.get_all()
