from backend.config import app
from models.init_db import init_db

#start application and generate database
app.app_context().push()
init_db()

#import routes that are exposed to frontend
import controller.router
import backend.controller.user_controller
import backend.controller.activity_controller

if __name__ == '__main__':
    app.run(debug=True , host='0.0.0.0', port=8081)