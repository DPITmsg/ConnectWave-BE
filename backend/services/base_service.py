from repository.base_repository import BaseRepository
from models.activity import Activity

class BaseService():
    _repo = BaseRepository(Activity)
    def rollback(self):
        self._repo.rollback() 
