import bcrypt
from flask import Blueprint, session, abort, request, jsonify
from flask import current_app
from utils.config import http_error_dict
from validator import validate
from utils.environment import get_environment
from bson import json_util
import json

from model.familiar import get_familiar_all, get_familiar, delete_familiar, create_familiar, update_familiar

serverConfig = get_environment("Server")
api_familiar = Blueprint("api_familiar", __name__)

@api_familiar.route("/familiar/actualizar/<string:id>", methods=["PUT"])
def update_api_familiar(id):
    try:
        familiar = request.get_json()

        apellido_primero = familiar["apellido_primero"]
        apellido_segundo = familiar["apellido_segundo"]
        nombre_primero = familiar["nombre_primero"]
        nombre_segundo = familiar["nombre_segundo"]
        parentesco = familiar["parentesco"]
        telefono1 = familiar["telefono1"]
        telefono2 = familiar["telefono2"]
        empleado_id = familiar["empleado_id"]

        mongo_data = update_db_familiar(id, nombre_primero,nombre_segundo,   apellido_primero,   apellido_segundo,   telefono1,   telefono2,   parentesco,   empleado_id)
            
        return mongo_data, 200

    except Exception as e:
        abort(http_error_dict[type(e).__name__])


@api_familiar.route("/familiar/crear/", methods=["POST"])
def create_api_familiar():
    try:
        familiar = request.get_json()

        apellido_primero = familiar["apellido_primero"]
        apellido_segundo = familiar["apellido_segundo"]
        nombre_primero = familiar["nombre_primero"]
        nombre_segundo = familiar["nombre_segundo"]
        parentesco = familiar["parentesco"]
        telefono1 = familiar["telefono1"]
        telefono2 = familiar["telefono2"]
        empleado_id = familiar["empleado_id"]

        mongo_data = create_db_familiar(nombre_primero,nombre_segundo,   apellido_primero,   apellido_segundo,   telefono1,   telefono2,   parentesco,   empleado_id)
            
        return mongo_data, 200

    except Exception as e:
        abort(http_error_dict[type(e).__name__])


@api_familiar.route("/familiar/eliminar/<string:id>", methods=["DELETE"])
def delete_api_familiar_by_id(id):
    try:
        if id:
            mongo_data = delete_db_familiar(id)
            
            return mongo_data, 200
        else:
            abort(400)

    except Exception as e:
        abort(http_error_dict[type(e).__name__])

@api_familiar.route("/familiar/ver/<string:id>", methods=["GET"])
def get_familiar_by_id(id):
    try:
        if id:
            mongo_data = get_db_familiar(id)
            
            return mongo_data, 200
        else:
            abort(400)

    except Exception as e:
        abort(http_error_dict[type(e).__name__])

@api_familiar.route("/familiar/ver/", methods=["GET"])
def get_api_familiar_all():
    try:
        if id:
            mongo_data = get_db_familiar_all()
            
            return mongo_data, 200
        else:
            abort(400)

    except Exception as e:
        abort(http_error_dict[type(e).__name__])

def get_db_familiar(id):
    data = None
    mensaje = ""
    status = "Success"
    response = {}
    try:
        resultado = get_familiar(id)

        if resultado:
            data =  json.loads(json.dumps(resultado, default=json_util.default))
        else:
            data = None
        
        status = "Success"
    except Exception as e:
        status = "Error"
        mensaje = str(e)

    response["data"] = data
    response["status"] = status
    response["mensaje"] = mensaje
    
    return response

def get_db_familiar_all():
    data = None
    mensaje = ""
    status = "Success"
    response = {}
    try:
        lista = []
        for familiar in get_familiar_all():
            lista.append(familiar)

        if lista:
            data =  json.loads(json.dumps(lista, default=json_util.default))
        else:
            data = None
        
        status = "Success"
    except Exception as e:
        status = "Error"
        mensaje = str(e)

    response["data"] = data
    response["status"] = status
    response["mensaje"] = mensaje
    
    return response

def delete_db_familiar(id):
    data = None
    mensaje = ""
    status = "Success"
    response = {}
    try:
        resultado = delete_familiar(id)

        if resultado:
            data =  json.loads(json.dumps(resultado, default=json_util.default))
        else:
            data = None
        
        status = "Success"
    except Exception as e:
        status = "Error"
        mensaje = str(e)

    response["data"] = data
    response["status"] = status
    response["mensaje"] = mensaje
    
    return response

def create_db_familiar(apellido_primero, apellido_segundo, nombre_primero, nombre_segundo, parentesco, telefono1, telefono2, empleado_id):
    data = None
    mensaje = ""
    status = "Success"
    response = {}
    try:
        resultado = create_familiar(nombre_primero,nombre_segundo,   apellido_primero,   apellido_segundo,   telefono1,   telefono2,   parentesco,   empleado_id)

        if resultado:
            data =  json.loads(json.dumps(get_familiar(resultado.inserted_id), default=json_util.default))
        else:
            data = None
        
        status = "Success"
    except Exception as e:
        status = "Error"
        mensaje = str(e)

    response["data"] = data
    response["status"] = status
    response["mensaje"] = mensaje
    
    return response


def update_db_familiar(id, apellido_primero, apellido_segundo, nombre_primero, nombre_segundo, parentesco, telefono1, telefono2, empleado_id):
    data = None
    mensaje = ""
    status = "Success"
    response = {}
    try:
        resultado = update_familiar(id, nombre_primero,nombre_segundo,   apellido_primero,   apellido_segundo,   telefono1,   telefono2,   parentesco,   empleado_id)

        if resultado:
            data =  json.loads(json.dumps(get_familiar(id), default=json_util.default))
        else:
            data = None
        
        status = "Success"
    except Exception as e:
        status = "Error"
        mensaje = str(e)

    response["data"] = data
    response["status"] = status
    response["mensaje"] = mensaje
    
    return response