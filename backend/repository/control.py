from sqlalchemy import select
from sqlalchemy.exc import ProgrammingError

from backend.config import db


class ControlScheme:
    __db = db
    __session = db.Session(db.engine)
        
    @classmethod
    def add(cls, entry):
        try:
            cls.__session.add(entry)
            cls.__session.flush()
            cls.__session.commit()
        except ProgrammingError:
            print("Programming error, table doesn't exist.")
        else:
            print("Value inserted successfully!")

    @classmethod
    def get_all(cls, model: db.Model, order_filter=None):
        try:
            result = cls.__session.scalars(select(model).order_by(order_filter)).all()
            # Equivalent with __session.scalars.execute(...).all() (i think at least)
        except ProgrammingError:
            print("Programming error, table doesn't exist.")
            return None
        else:
            return result

    @classmethod
    def get_with_key(cls, model: db.Model, key):
        try:
            result = cls.__session.get(model, key)
        except ProgrammingError:
            print("Programming error, table doesn't exist or maybe no row with the given key was found.")
            return None
        else:
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
