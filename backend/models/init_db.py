from config import app, db
from models.activity import Activity
from models.activity_to_user import ActivityToUser
from models.friend_list import FriendList
from models.location import Location
from models.user import User

def init_db():
    with app.app_context():
       session = db.Session(db.engine)
       db.create_all()

init_db()

