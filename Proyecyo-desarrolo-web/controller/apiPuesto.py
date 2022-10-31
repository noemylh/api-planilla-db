import bcrypt
from flask import Blueprint, session, abort, request, jsonify
from flask import current_app
from utils.config import http_error_dict
from validator import validate
from utils.environment import get_environment
from bson import json_util
import json

from model.puesto import get_puesto_all, get_puesto, delete_puesto, create_puesto, update_puesto

serverConfig = get_environment("Server")
api_puesto = Blueprint("api_puesto", __name__)

@api_puesto.route("/puesto/actualizar/<string:id>", methods=["PUT"])
def update_api_puesto(id):
    try:
        puesto = request.get_json()

        bonos = puesto["bonos"]
        factor_hora_extra = puesto["factor_hora_extra"]
        horas = puesto["horas"]
        nombre = puesto["nombre"]
        precio = puesto["precio"]
        sueldo = puesto["sueldo"]

        mongo_data = update_db_puesto(id, bonos, factor_hora_extra,   horas,   nombre,   precio,  sueldo)
            
        return mongo_data, 200

    except Exception as e:
        abort(http_error_dict[type(e).__name__])


@api_puesto.route("/puesto/crear/", methods=["POST"])
def create_api_puesto():
    try:
        puesto = request.get_json()

        bonos = puesto["bonos"]
        factor_hora_extra = puesto["factor_hora_extra"]
        horas = puesto["horas"]
        nombre = puesto["nombre"]
        precio = puesto["precio"]
        sueldo = puesto["sueldo"]

        mongo_data = create_db_puesto(bonos, factor_hora_extra,   horas,   nombre,   precio,  sueldo)
            
        return mongo_data, 200

    except Exception as e:
        abort(http_error_dict[type(e).__name__])


@api_puesto.route("/puesto/eliminar/<string:id>", methods=["DELETE"])
def delete_api_puesto_by_id(id):
    try:
        if id:
            mongo_data = delete_db_puesto(id)
            
            return mongo_data, 200
        else:
            abort(400)

    except Exception as e:
        abort(http_error_dict[type(e).__name__])

@api_puesto.route("/puesto/ver/<string:id>", methods=["GET"])
def get_puesto_by_id(id):
    try:
        if id:
            mongo_data = get_db_puesto(id)
            
            return mongo_data, 200
        else:
            abort(400)

    except Exception as e:
        abort(http_error_dict[type(e).__name__])

@api_puesto.route("/puesto/ver/", methods=["GET"])
def get_api_puesto_all():
    try:
        if id:
            mongo_data = get_db_puesto_all()
            
            return mongo_data, 200
        else:
            abort(400)

    except Exception as e:
        abort(http_error_dict[type(e).__name__])

def get_db_puesto(id):
    data = None
    mensaje = ""
    status = "Success"
    response = {}
    try:
        resultado = get_puesto(id)

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

def get_db_puesto_all():
    data = None
    mensaje = ""
    status = "Success"
    response = {}
    try:
        lista = []
        for puesto in get_puesto_all():
            lista.append(puesto)

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

def delete_db_puesto(id):
    data = None
    mensaje = ""
    status = "Success"
    response = {}
    try:
        resultado = delete_puesto(id)

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

def create_db_puesto(bonos, factor_hora_extra,   horas,   nombre,   precio,  sueldo):
    data = None
    mensaje = ""
    status = "Success"
    response = {}
    try:
        resultado = create_puesto(sueldo, precio, nombre, horas, factor_hora_extra,  bonos)

        if resultado:
            data =  json.loads(json.dumps(get_puesto(resultado.inserted_id), default=json_util.default))
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


def update_db_puesto(id, bonos, factor_hora_extra,   horas,   nombre,   precio,  sueldo):
    data = None
    mensaje = ""
    status = "Success"
    response = {}
    try:
        resultado = update_puesto(id, sueldo, precio, nombre, horas, factor_hora_extra,  bonos)

        if resultado:
            data =  json.loads(json.dumps(get_puesto(id), default=json_util.default))
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