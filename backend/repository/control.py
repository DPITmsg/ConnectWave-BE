from sqlalchemy import select
from sqlalchemy.exc import ProgrammingError

from backend.config import db


class ControlScheme:
    __db = db
    __session = db.Session(db.engine)
        
    @classmethod
    def add(cls, entry):
        cls.__sesession.add(entry)
        cls.__session.flush()
        return entry

    @classmethod
    def get_all(cls, model: db.Model, order_filter=None):
        result = cls.__session.scalars(select(model).order_by(order_filter)).all()
         # Equivalent with __session.scalars.execute(...).all() (i think at least)
        return result

    @classmethod
    def get_with_key(cls, model: db.Model, key):
        result = cls.__session.get(model, key)
        return result

    @classmethod
    def update(cls, model: db.Model, key, newmodel):
        pass

    @classmethod
    def update_value(cls, model: db.Model, key, column, new_value):
        pass

    @classmethod
    def remove(cls, model: db.Model, key):
        pass

    # Maybe make a foreach() function in the services folder
