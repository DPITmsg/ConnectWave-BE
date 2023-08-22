from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite+pysqlite:///connectwave.db'
# app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite+pysqlite:///:memory:' # USE THIS FOR TESTING PURPOSES ONLY

db = SQLAlchemy(app)

with app.app_context():
    db.engine.echo = True # FOR TESTING PURPOSES

