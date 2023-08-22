from config import app, db
from models.init_db import init_db
from models.location import Location
from controller.router import *

init_db()


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
