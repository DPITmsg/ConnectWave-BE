from config import app, db
from models.init_db import init_db

#start application and generate database
app.app_context().push()
init_db()

#import routes that are exposed to frontend
import controller.location_controller
import controller.user_controller
import controller.activity_controller
from services.location_service import *
from repository.location_repository import *
import sys

if __name__ == '__main__':
    print(sys.path)
    app.run(debug=True , host='0.0.0.0', port=8081)
