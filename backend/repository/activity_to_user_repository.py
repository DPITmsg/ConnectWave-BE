from repository.base_repository import BaseRepository
from models.activity_to_user import ActivityToUser
from models.user import User
from models.activity import Activity



class ActivityToUserRepository(BaseRepository):
    def __init__(self):
        self._model = ActivityToUser  
    
    def remove(self, username, id):
        result = select(self._model).filter_by(User.username == username, Activity.id == id)
        if result is not None:
            self._session.execute(delete(self._model.__tablename__).where(User.username == username, Activity.id == id))
            self._session.commit()
        else:
            return 404
        return 200
