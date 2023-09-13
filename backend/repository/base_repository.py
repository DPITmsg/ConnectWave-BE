from sqlalchemy import select
from sqlalchemy.exc import ProgrammingError

from backend.config import db


class BaseRepository():
    _db = db
    _session = db.Session(db.engine)
    _model: db.Model = None

    # Used only for spontaneous instantiation of a repository control scheme
    def __init__(self, model):
        _model = model

    def add(self, entry):
        self.__sesession.add(entry)
        self._session.commit()
        return entry

    def insert(self, *entities):
        self._session.execute(insert(_model), entities)
        return entities

    def get_all(self, order_filter=None):
        self._session.refresh()
        result = self._session.scalars(select(_model).order_by(order_filter)).all()
         # Equivalent with _session.scalars.execute(...).all() (i think at least)
        return result

    def get_with_key(self, key):
        self._session.refresh()
        result = self._session.get(_model, key)
        return result

    def update(self, column, value, **kwargs):
        self._session.refresh()
        self._session.execute(update(_model.__tablename__).where(column==value).values(**kwargs)) 
        self._session.commit() 
        self._session.refresh()
        return self.get_with_key(value)

    def remove(self, column, value):
        delete_target = self.get_with_key(key)
        self._session.execute(delete(_model.__tablename__).where(column==value))
        self._session.commit()
        return delete_target

    # Maybe make a foreach() function in the services folder
