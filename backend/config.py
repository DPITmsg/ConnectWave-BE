from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
# app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite+pysqlite:///connectwave.db'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite+pysqlite:///test_db.db'  # USE THIS FOR TESTING PURPOSES ONLY

app.secret_key = 'your secret key'

db = SQLAlchemy(app)

with app.app_context():
    db.engine.echo = True  # FOR TESTING PURPOSES
