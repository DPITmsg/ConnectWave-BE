from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from authlib.integrations.flask_client import OAuth

app = Flask(__name__)
# app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite+pysqlite:///connectwave.db'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite+pysqlite:///test_db.db'  # USE THIS FOR TESTING PURPOSES ONLY

db = SQLAlchemy(app)
oauth = OAuth(app)

with app.app_context():
    db.engine.echo = True  # FOR TESTING PURPOSES
