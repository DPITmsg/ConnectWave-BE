from config import app, db
from models.activity import Activity
from models.user import User
from models.location import Location



# importing models is required before initializing the database
from models.activity_to_user import ActivityToUser
from models.friend_list import FriendList


def init_db():
    with app.app_context():
        session = db.Session(db.engine)
        db.create_all()
        print('database created')


init_db()
