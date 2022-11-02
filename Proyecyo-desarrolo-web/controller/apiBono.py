import bcrypt
from flask import Blueprint, abort, request
from flask import current_app
from utils.config import http_error_dict
from utils.environment import get_environment
from bson import json_util
import json

from model.bono import get_bono, get_bono_all, delete_bono, create_bono, update_bono

serverConfig = get_environment("Server")
api_bono = Blueprint("api_bono", __name__)

@api_bono.route("/bono/actualizar/<string:id>", methods=["PUT"])
def update_api_bono(id):
    try:
        bono = request.get_json()

        nombre = bono["nombre"]
        cantidad =  int(bono["cantidad"]) if bono["cantidad"].isdigit() else bono["cantidad"]
        porcentaje = int(bono["porcentaje"]) if bono["porcentaje"].isdigit() else bono["porcentaje"]
        fecha_aplicacion = bono["fecha_aplicacion"]

        mongo_data = update_db_bono(id, nombre, cantidad, porcentaje, fecha_aplicacion)

        return mongo_data, 200

    except Exception as e:
        abort(http_error_dict[type(e).__name__])


@api_bono.route("/bono/crear/", methods=["POST"])
def create_api_bono():
    try:
        bono = request.get_json()

        nombre = bono["nombre"]
        cantidad = int(bono["cantidad"]) if bono["cantidad"].isdigit() else bono["cantidad"]
        porcentaje = int(bono["porcentaje"]) if bono["porcentaje"].isdigit() else bono["porcentaje"]
        fecha_aplicacion = bono["fecha_aplicacion"]

        mongo_data = create_db_bono(nombre, cantidad, porcentaje, fecha_aplicacion)
            
        return mongo_data, 200

    except Exception as e:
        abort(http_error_dict[type(e).__name__])


@api_bono.route("/bono/eliminar/<string:id>", methods=["DELETE"])
def delete_api_bono_by_id(id):
    try:
        if id:
            mongo_data = delete_db_bono(id)
            
            return mongo_data, 200
        else:
            abort(400)

    except Exception as e:
        abort(http_error_dict[type(e).__name__])

@api_bono.route("/bono/ver/<string:id>", methods=["GET"])
def get_bono_by_id(id):
    try:
        if id:
            mongo_data = get_db_bono(id)
            
            return mongo_data, 200
        else:
            abort(400)

    except Exception as e:
        abort(http_error_dict[type(e).__name__])

@api_bono.route("/bono/ver/", methods=["GET"])
def get_api_bono_all():
    logger = current_app.logger
    try:
        if id:
            mongo_data = get_db_bono_all()
            
            return mongo_data, 200
        else:
            abort(400)

    except Exception as e:
        abort(http_error_dict[type(e).__name__])

def get_db_bono(id):
    data = None
    mensaje = ""
    status = "Success"
    response = {}
    try:
        resultado = get_bono(id)

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

def get_db_bono_all():
    data = None
    mensaje = ""
    status = "Success"
    response = {}
    try:
        lista = []
        for bono in get_bono_all():
            lista.append(bono)

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

def delete_db_bono(id):
    data = None
    mensaje = ""
    status = "Success"
    response = {}
    try:
        resultado = delete_bono(id)

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

def create_db_bono(nombre, cantidad, porcentaje, fecha_aplicacion):
    data = None
    mensaje = ""
    status = "Success"
    response = {}
    try:
        resultado = create_bono(nombre, cantidad, porcentaje, fecha_aplicacion)

        if resultado:
            data =  json.loads(json.dumps(get_bono(resultado.inserted_id), default=json_util.default))
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


def update_db_bono(id, nombre, cantidad, porcentaje, fecha_aplicacion):
    data = None
    mensaje = ""
    status = "Success"
    response = {}
    try:
        resultado = update_bono(id, nombre, cantidad, porcentaje, fecha_aplicacion)

        if resultado:
            data =  json.loads(json.dumps(get_bono(id), default=json_util.default))
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