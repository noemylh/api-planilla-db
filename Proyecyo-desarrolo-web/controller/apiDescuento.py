import bcrypt
from flask import Blueprint, abort, request
from utils.config import http_error_dict
from utils.environment import get_environment
from bson import json_util
import json

from model.descuento import get_descuento_all, get_descuento, delete_descuento, create_descuento, update_descuento

serverConfig = get_environment("Server")
api_descuento = Blueprint("api_descuento", __name__)

@api_descuento.route("/descuento/actualizar/<string:id>", methods=["PUT"])
def update_api_descuento(id):
    try:
        descuento = request.get_json()

        cantidad = int(descuento["cantidad"])
        nombre = descuento["nombre"]
        empleado_id = descuento["empleado_id"]
        fecha_aplicacion = descuento["fecha_aplicacion"]
        porcentaje = int(descuento["porcentaje"])

        mongo_data = update_db_descuento(id, nombre, cantidad, empleado_id, fecha_aplicacion, porcentaje)
            
        return mongo_data, 200

    except Exception as e:
        abort(http_error_dict[type(e).__name__])


@api_descuento.route("/descuento/crear/", methods=["POST"])
def create_api_descuento():
    try:
        descuento = request.get_json()

        nombre = descuento["nombre"]
        cantidad = int(descuento["cantidad"])
        empleado_id = descuento["empleado_id"]
        fecha_aplicacion = descuento["fecha_aplicacion"]
        porcentaje = int(descuento["porcentaje"])

        mongo_data = create_db_descuento(nombre, cantidad, empleado_id, fecha_aplicacion, porcentaje)
            
        return mongo_data, 200

    except Exception as e:
        abort(http_error_dict[type(e).__name__])


@api_descuento.route("/descuento/eliminar/<string:id>", methods=["DELETE"])
def delete_api_descuento_by_id(id):
    try:
        if id:
            mongo_data = delete_db_descuento(id)
            
            return mongo_data, 200
        else:
            abort(400)

    except Exception as e:
        abort(http_error_dict[type(e).__name__])

@api_descuento.route("/descuento/ver/<string:id>", methods=["GET"])
def get_descuento_by_id(id):
    try:
        if id:
            mongo_data = get_db_descuento(id)
            
            return mongo_data, 200
        else:
            abort(400)

    except Exception as e:
        abort(http_error_dict[type(e).__name__])

@api_descuento.route("/descuento/ver/", methods=["GET"])
def get_api_descuento_all():
    try:
        if id:
            mongo_data = get_db_descuento_all()
            
            return mongo_data, 200
        else:
            abort(400)

    except Exception as e:
        abort(http_error_dict[type(e).__name__])

def get_db_descuento(id):
    data = None
    mensaje = ""
    status = "Success"
    response = {}
    try:
        resultado = get_descuento(id)

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

def get_db_descuento_all():
    data = None
    mensaje = ""
    status = "Success"
    response = {}
    try:
        lista = []
        for descuento in get_descuento_all():
            lista.append(descuento)

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

def delete_db_descuento(id):
    data = None
    mensaje = ""
    status = "Success"
    response = {}
    try:
        resultado = delete_descuento(id)

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

def create_db_descuento(nombre, cantidad, empleado_id, fecha_aplicacion, porcentaje):
    data = None
    mensaje = ""
    status = "Success"
    response = {}
    try:
        resultado = create_descuento(nombre, cantidad, empleado_id, fecha_aplicacion, porcentaje)

        if resultado:
            data =  json.loads(json.dumps(get_descuento(resultado.inserted_id), default=json_util.default))
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


def update_db_descuento(id, nombre, cantidad, empleado_id, fecha_aplicacion, porcentaje):
    data = None
    mensaje = ""
    status = "Success"
    response = {}
    try:
        resultado = update_descuento(id, nombre, cantidad, empleado_id, fecha_aplicacion, porcentaje)

        if resultado:
            data =  json.loads(json.dumps(get_descuento(id), default=json_util.default))
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