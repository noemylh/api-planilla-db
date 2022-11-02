from main import app
from flask import Blueprint,abort
from flask import current_app
from utils.config import http_error_dict
from utils.environment import get_environment
from flask_pymongo import PyMongo
from bson.objectid import ObjectId

serverConfig = get_environment("Server")
prueba_data = Blueprint("prueba_data", __name__)

# Rest API to validate a user
@prueba_data.route("/prueba", methods=["POST"])
def prueba():
    try:
        logger = current_app.logger
        logger.info("**prueba**")

        logger.info(get_hora_extra("6325182f8c373408643d2b32"))
        delete_hora_extra("6325182f8c373408643d2b32")
        logger.info(get_hora_extra("6325182f8c373408643d2b32"))
        #hora_extra_id,   cantidad,   fecha,   valor_calculo,   empleado_id

        hora_extra = create_hora_extra("2",None, "100", "78", )

        logger.info(hora_extra.inserted_id)
        update_hora_extra(hora_extra.inserted_id ,"2",None, "100","79" )
        
        return "", 200

    except Exception as e:
        logger.info(f"Response={e}")
        abort(http_error_dict[type(e).__name__])

mongo = PyMongo(app)
db = mongo.db.hora_extra

def get_hora_extra_all():
    resultado = db.find()
    
    return resultado

def get_hora_extra(id):
    hora_extra = db.find_one({"_id": ObjectId(id)})
    
    return hora_extra

def delete_hora_extra(id):
    hora_extra = db.find_one_and_delete({"_id":ObjectId(id)})
    
    return hora_extra

def create_hora_extra(cantidad,   fecha,   empleado_id):
    hora_extra = db.insert_one({ "cantidad": cantidad,   "fecha": fecha,   "empleado_id": empleado_id})

    return hora_extra

def update_hora_extra( hora_extra_id,   cantidad,   fecha,   empleado_id):
    hora_extra = db.update_one({"_id":ObjectId(hora_extra_id)}, {"$set": { "cantidad": cantidad,   "fecha": fecha,   "empleado_id": empleado_id}})
    
    return hora_extra