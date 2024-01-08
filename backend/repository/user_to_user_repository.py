from repository.base_repository import BaseRepository
from models.user_to_user import UserToUser
from models.user import User
from sqlalchemy import and_, or_, select, delete



class UserToUserRepository(BaseRepository):
    def __init__(self):
        self._model = UserToUser  
    
    def remove(self, username1, username2):
        # Use filter condition to find the record to delete
        filter_condition = or_(
            and_(UserToUser.username1 == username1, UserToUser.username2 == username2),
            and_(UserToUser.username1 == username2, UserToUser.username2 == username1)
        )

        # Query and delete
        record = self._session.query(UserToUser).filter(filter_condition).first()
        if record:
            self._session.delete(record)
            self._session.commit()
            return 200
        else:
            return 404
