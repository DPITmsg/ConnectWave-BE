from models.friend_list import FriendList
from models.user import User
from repository.friend_list_repository import FriendListRepository

class FriendListService(BaseService):
    _repo = FriendListRepository()

    def add_friend(user: User, friend: User):
        user_friend_list: Friendlist = self._repo.get_with_key(user.username)
        friend_friend_list: Friendlist = self._repo.get_with_key(friend.username)

        if (user_friend_list.friend_list.find(friend.username) == -1):
            self._repo.update(username, friend.username, friend_friend_list = friend_friend_list + user.username)
            return self._repo.update(username, user.username, user_friend_list = user_friend_list + friend.username), 
        
    def remove_friend(user: User, friend: User):
        user_friend_list: Friendlist = self._repo.get_with_key(user.username)
        friend_friend_list: Friendlist = self._repo.get_with_key(friend.username)

        if (user_friend_list.friend_list.find(friend.username) != -1):
            self._repo.update(username, friend.username, friend_friend_list = friend_friend_list.replace(user.username, ''))
            return self._repo.update(username, user.username, user_friend_list = user_friend_list.replace(friend.username, '')),

    def get_friends(user: User, friend: User):
        user_friend_list:FriendList = self._repo.get_with_key(user.username)
        return user_friend_list.friend_list



