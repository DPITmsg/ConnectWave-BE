from flask import jsonify, request

from config import app, db
from models.location import Location

@app.route('/')
def get_locations():
    return "Hello Warudo!"
