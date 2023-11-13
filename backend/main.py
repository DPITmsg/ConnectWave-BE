from config import app, db
from models.init_db import init_db
#start application and generate database
app.app_context().push()
init_db()


#import routes that are exposed to frontend
import controller.location_controller
import controller.user_controller
import controller.activity_controller
import controller.activity_to_user_controller
import controller.user_to_user_controller
# import controller.login
from services.location_service import *
from repository.location_repository import *
from the_adder_of_stuff import add_stuff
import sys

add_stuff()

if __name__ == '__main__':
    app.run(debug=True , host='localhost', port=8081)
