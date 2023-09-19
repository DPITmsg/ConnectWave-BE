from models.friend_list import FriendList
from models.user import User
from repository.friend_list_repository import FriendListRepository


def service_add_friend(user: User, friend: User):
    repo = FriendListRepository()
    user_friend_list: Friendlist = repo.get_with_key(user.username)
    friend_friend_list: Friendlist = repo.get_with_key(friend.username)

    if (user_friend_list.friend_list.find(friend.username) == -1):
        repo.update(username, friend.username, friend_friend_list = friend_friend_list + user.username)
        return repo.update(username, user.username, user_friend_list = user_friend_list + friend.username), 
        
def service_remove_friend(user: User, friend: User):
    repo = FriendListRepository()
    user_friend_list: Friendlist = repo.get_with_key(user.username)
    friend_friend_list: Friendlist = repo.get_with_key(friend.username)

    if (user_friend_list.friend_list.find(friend.username) != -1):
        repo.update(username, friend.username, friend_friend_list = friend_friend_list.replace(user.username, ''))
        return repo.update(username, user.username, user_friend_list = user_friend_list.replace(friend.username, '')),

def service_get_friends(user: User, friend: User):
    repo = FriendListRepository()
    user_friend_list:FriendList = repo.get_with_key(user.username)
    return user_friend_list.friend_list



