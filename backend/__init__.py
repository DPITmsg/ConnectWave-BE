from flask import Flask

from backend.init_db import init_db
from backend.model.core_models import db
from backend.repository.UserRepository import UserRepository


def create_app():
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite+pysqlite:///connectwave.db'
    db.init_app(app)

    return app
