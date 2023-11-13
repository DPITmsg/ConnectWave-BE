from repository.base_repository import BaseRepository
from models.user_to_user import UserToUser
from models.user import User
from sqlalchemy import select, delete



class UserToUserRepository(BaseRepository):
    def __init__(self):
        self._model = UserToUser  
    
    def remove(self, username1, username2):
        result = self._session.query(UserToUser).all()
        filtered = UserToUser()
        for atu in result:
            if atu.username1 == username1 and atu.username2 == username2:
                filtered = atu
        if filtered is not None:
            self._session.query(UserToUser).filter(User.username == username1, User.username == username2)\
            .delete(synchronize_session='auto')
            self._session.commit()
        else: 
            result = self._session.query(UserToUser).all()
            filtered = UserToUser()
            for atu in result:
                if atu.username2 == username1 and atu.username1 == username2:
                    filtered = atu
            if filtered is not None:
                self._session.query(UserToUser).filter(User.username == username2, User.username == username1)\
                .delete(synchronize_session='auto')
                self._session.commit()
            else:
                return 404
        return 200
