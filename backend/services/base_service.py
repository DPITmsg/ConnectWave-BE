from repository.base_repository import BaseRepository
from backend.models.activity import Activity

class BaseService():
    _repo = BaseRepository(Activity)
    def service_rollback(self):
        self._repo.rollback() 
