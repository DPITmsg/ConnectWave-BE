from models.user_to_user import UserToUser
from models.user import User
from repository.user_to_user_repository import UserToUserRepository
from services.base_service import BaseService



class UserToUserService(BaseService):
    _repo = UserToUserRepository()
    _session = UserToUserRepository().get_session()

    def get_user_to_user(self, username1, username2):
        result = self._session.query(UserToUser).all()
        for utu in result:
            if utu.username1 == username1 and utu.username2 == username2:
                return result
        return None

    def send_request(self, username_user, username_friend):
        if self.get_user_to_user(username_user, username_friend) is None:
            userToUser = UserToUser(username_user, username_friend)
            self._repo.add(userToUser)
            return userToUser
        userToUser = self.get_user_to_user(username_user, username_friend)
        return userToUser

    def add_friend(self, username_user, username_friend):
        request: UserToUser = self.get_user_to_user(username_user, username_friend)
        if result is not None:
            request.accepted = True
            return 200
        return 404
        
    def decline_request(self, username_user, username_friend):
        request: UserToUser = self.get_user_to_user(username_user, username2_friend)
        if request is not None:
            self._repo.remove(username_user, username_friend)
            return 200
        return 404

    def accept_request(self, username_user, username_friend):
        request: UserToUser = self.get_user_to_user(username_user, username_friend)
        if request is not None:
            self._repo.add_friend(username_user, username_friend)
            return 200
        return 404


       
