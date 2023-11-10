from sqlalchemy import select
from sqlalchemy.exc import ProgrammingError

from config import db


class BaseRepository():
    _db = db
    _session = db.Session(db.engine)
    _model: db.Model = None

    # Used only for spontaneous instantiation of a repository control scheme
    def __init__(self, model):
        self._model = model
    
    def get_session(self):
        return self._session    

    def add(self, entry):
        self._session.add(entry)
        self._session.commit()
        return entry

    def add_many(self, *entities):
        self._session.execute(insert(self._model), entities)
        return entities

    def get_all(self, order_filter=None):
        # self._session.refresh(self._model)
        result = self._model.query.all()
        # Equivalent with _session.scalars.execute(...).all() (i think at least)
        return result

    def get_where(self, column, value):
        result = select(self._model).where(column==value)
        return result

    def get_with_many(self, *params):
        result = select(self._model)
        for i in range(params.__len__()):
            result.where(params[i]==params[i+1])
            i+=1;

        return result

    def get_with_key(self, key):
        # self._session.refresh(self._model)
        result = self._session.get(self._model, key)
        return result

    def update(self, column, value, **kwargs):
        # self._session.refresh(self._model)
        self._session.execute(update(self._model.__tablename__).where(column=value).values(**kwargs)) 
        self._session.commit() 
        self._session.refresh(select(self._model).filter_by(column=value))
        return self.get_with_key(value)

    def remove(self, column, value):
        delete_target = self.get_with_key(key)
        self._session.execute(delete(self._model.__tablename__).where(column=value))
        self._session.commit()
        return delete_target

    def rollback(self):
        self._session.rollback()

    # Maybe make a foreach() function in the services folder
