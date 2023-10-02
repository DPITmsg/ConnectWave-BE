from repository.base_repository import BaseRepository

class BaseService():
    _repo = BaseRepository()

    def __init__(self, repo):
        self._repo = repo
    
    def service_rollback(self):
        self._repo.rollback() 
