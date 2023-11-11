from repository.base_repository import BaseRepository
from models.user_to_user import UserToUser
from models.user import User



class UserToUserRepository(BaseRepository):
    def __init__(self):
        self._model = UserToUser  
    
    def remove(self, username1, username2):
        result = select(self._model).filter_by(User.username == username1, User.username == username2)
        if result is not None:
            self._session.execute(delete(self._model.__tablename__).where(User.username == username1, User.username == username2))
            self._session.commit()
        else: 
            result = select(self._model).filter_by(User.username == username2, User.username == username1)
            if result is not None:
                self._session.execute(delete(self._model.__tablename__).where(User.username == username1, User.username == username2))
                self._session.commit()
            else:
                return 404
        return 200
