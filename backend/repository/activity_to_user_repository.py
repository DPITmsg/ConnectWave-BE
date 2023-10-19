from repository.base_repository import BaseRepository
from models.activity_to_user import ActivityToUser
from models.user import User
from models.activity import Activity



class ActivityToUserRepository(BaseRepository):
    def __init__(self):
        self._model = ActivityToUser  
    
    def remove(self, username, activity_id):
        result = select(self._model).filter_by(User.username == username, Activity.activity_id == activity_id)
        self._session.execute(delete(self._model.__tablename__).where(User.username == username, Activity.activity_id == activity_id))
        self._session.commit()
        return result 
