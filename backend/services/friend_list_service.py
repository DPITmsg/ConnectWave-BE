from models.friend_list import FriendList
from models.user import User
from repository.friend_list_repository import FriendListRepository

class FriendListService(BaseService):
    _repo = FriendListRepository()
    
    def add_friend(self, username, friendname):
        user_friend_list: Friendlist = self._repo.get_with_key(username)
        friend_friend_list: Friendlist = self._repo.get_with_key(friendname)

        if (user_friend_list.friend_list.find(friendname) == -1):
            self._repo.update(username, friendname, friend_friend_list = friend_friend_list + username)
            return self._repo.update(friendname, username, user_friend_list = user_friend_list + friendname), 
        
    def remove_friend(self, username, friendname):
        user_friend_list: Friendlist = self._repo.get_with_key(username)
        friend_friend_list: Friendlist = self._repo.get_with_key(friendname)

        if (user_friend_list.friend_list.find(friendname) != -1):
            self._repo.update(friendname, username, friend_friend_list = friend_friend_list.replace(username, ''))
            return self._repo.update(username, friendname, user_friend_list = user_friend_list.replace(friendname, '')),

    def get_friends(self, username):
        user_friend_list:FriendList = self._repo.get_with_key(username)
        return user_friend_list.friend_list



