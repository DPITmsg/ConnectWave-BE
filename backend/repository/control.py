from backend.config import app, db


class ControlScheme:
    def __init__(self, app, db):
        self.__app = app
        self.__db = db
        self.__session = db.Session(db.engine)

    def add(self, entry):
        try:
            self.__session.add(entry)
            self.__session.flush()
        except ProgrammingError:
            print("Programming error, table doesn't exist.")
        else:
            print("Value inserted successfully!")

    def get_all(self, model: db.Model, order_filter=None):
        try:
            result = self.__session.scalars(select(model).order_by(order_filter)).all()
            # Equivalent with self.__session.scalars.execute(...).all() (i think at least)
        except ProgrammingError:
            print("Programming error, table doesn't exist.")
            return None
        else:
            return result

    def get_with_key(self, model: db.Model, key):
        try:
            result = self.__session.get(model, key)
        except ProgrammingError:
            print("Programming error, table doesn't exist or maybe no row with the given key was found.")
            return None
        else:
            return result

    def update(self, model: db.Model, key, newmodel):
        pass

    def update_value(self, model: db.Model, key, column, new_value):
        pass

    def remove(self, model: db.Model, key):
        pass

    # Maybe make a foreach() function in the services folder
