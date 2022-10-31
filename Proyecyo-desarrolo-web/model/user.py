from main import app
from bson import json_util
from flask import Blueprint, session, abort, request, jsonify
from flask import current_app
from utils.config import http_error_dict
from validator import validate
from utils.environment import get_environment
from flask_pymongo import PyMongo

mongo = PyMongo(app)
db = mongo.db.user

serverConfig = get_environment("Server")
user_data = Blueprint("user_data", __name__)

# Rest API to validate a user
@user_data.route("/login", methods=["POST"])
def get_user_by_password():
    try:
        logger = current_app.logger
        logger.info("url=/api/login")

        user = request.form['user']
        password = request.form['password']

        logger.info(user)
        logger.info(password)
        
        user_data = get_user_data(user)
        # json_user_data = jsonify(user_data)

        if user_data['password'] == password:
            return "", 200
        else:
            abort(400)
    except Exception as e:
        logger.info(f"Response={e}")
        abort(http_error_dict[type(e).__name__])

def get_user_data(username):
    user = db.find()
    
    a_user = user[0]
    return a_user