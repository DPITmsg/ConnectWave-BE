from backend.config import app, db
from backend.models.activity import Activity
from backend.models.user import User
from backend.models.location import Location



# importing models is required before initializing the database
from backend.models.activity import Activity
from backend.models.activity_to_user import ActivityToUser
from backend.models.friend_list import FriendList
from backend.models.location import Location
from backend.models.user import User


def init_db():
    with app.app_context():
        session = db.Session(db.engine)
        db.create_all()
        print('database created')


init_db()
