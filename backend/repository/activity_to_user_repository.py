from repository.base_repository import BaseRepository
from models.activity_to_user import ActivityToUser
from models.user import User
from models.activity import Activity
from sqlalchemy import select, delete



class ActivityToUserRepository(BaseRepository):
    def __init__(self):
        self._model = ActivityToUser  
    
    def remove(self, username, id):
        result = self._session.query(self._model).filter_by(username=username, id=id).first()

        if result:
            self._session.delete(result)
            self._session.commit()
            return 200
        else:
            return 404 
