import bcrypt
from flask import Blueprint, abort, request
from utils.config import http_error_dict
from utils.environment import get_environment
from bson import json_util
import json

from model.empleado import get_empleado_all, get_empleado, delete_empleado, create_empleado, update_empleado, add_bono, remove_bono, add_descuento, remove_descuento

serverConfig = get_environment("Server")
api_empleado = Blueprint("api_empleado", __name__)

@api_empleado.route("/empleado/actualizar/<string:id>", methods=["PUT"])
def update_api_empleado(id):
    try:
        empleado = request.get_json()

        apellido_primero = empleado["apellido_primero"]
        apellido_segundo = empleado["apellido_segundo"]
        carnet_igss = empleado["carnet_igss"]
        dpi = empleado["dpi"]
        estado = empleado["estado"]
        fecha_nacimiento = empleado["fecha_nacimiento"]
        jornada = empleado["jornada"]
        nit = empleado["nit"]
        nombre_primero = empleado["nombre_primero"]
        nombre_segundo = empleado["nombre_segundo"]
        puesto_id = empleado["puesto_id"]
        telefono1 = empleado["telefono1"]
        telefono2 = empleado["telefono2"]

        mongo_data = update_db_empleado(id, apellido_primero, apellido_segundo, carnet_igss, dpi, estado, fecha_nacimiento, jornada, nit, nombre_primero, nombre_segundo, puesto_id, telefono1, telefono2)
            
        return mongo_data, 200

    except Exception as e:
        abort(http_error_dict[type(e).__name__])


@api_empleado.route("/empleado/crear/", methods=["POST"])
def create_api_empleado():
    try:
        empleado = request.get_json()

        apellido_primero = empleado["apellido_primero"]
        apellido_segundo = empleado["apellido_segundo"]
        carnet_igss = empleado["carnet_igss"]
        dpi = empleado["dpi"]
        estado = empleado["estado"]
        fecha_nacimiento = empleado["fecha_nacimiento"]
        jornada = empleado["jornada"]
        nit = empleado["nit"]
        nombre_primero = empleado["nombre_primero"]
        nombre_segundo = empleado["nombre_segundo"]
        puesto_id = empleado["puesto_id"]
        telefono1 = empleado["telefono1"]
        telefono2 = empleado["telefono2"]

        mongo_data = create_db_empleado(apellido_primero, apellido_segundo, carnet_igss, dpi, estado, fecha_nacimiento, jornada, nit, nombre_primero, nombre_segundo, puesto_id, telefono1, telefono2)
            
        return mongo_data, 200

    except Exception as e:
        abort(http_error_dict[type(e).__name__])


@api_empleado.route("/empleado/eliminar/<string:id>", methods=["DELETE"])
def delete_api_empleado_by_id(id):
    try:
        if id:
            mongo_data = delete_db_empleado(id)
            
            return mongo_data, 200
        else:
            abort(400)

    except Exception as e:
        abort(http_error_dict[type(e).__name__])

@api_empleado.route("/empleado/ver/<string:id>", methods=["GET"])
def get_empleado_by_id(id):
    try:
        if id:
            mongo_data = get_db_empleado(id)
            
            return mongo_data, 200
        else:
            abort(400)

    except Exception as e:
        abort(http_error_dict[type(e).__name__])

@api_empleado.route("/empleado/ver/", methods=["GET"])
def get_api_empleado_all():
    try:
        if id:
            mongo_data = get_db_empleado_all()
            
            return mongo_data, 200
        else:
            abort(400)

    except Exception as e:
        abort(http_error_dict[type(e).__name__])

@api_empleado.route("/empleado/agregar_bono/", methods=["POST"])
def post_api_empleado_add_bonus():
    try:
        bono = request.get_json()
        bono_id = bono["bono_id"]
        empleado_id = bono["empleado_id"]
        mongo_data = get_db_empleado_add_bonus(bono_id, empleado_id)

        return mongo_data, 200
    except Exception as e:
        abort(http_error_dict[type(e).__name__])

@api_empleado.route("/empleado/quitar_bono/", methods=["POST"])
def post_api_empleado_remove_bonus():
    try:
        bono = request.get_json()
        bono_id = bono["bono_id"]
        empleado_id = bono["empleado_id"]
        mongo_data = get_db_empleado_remove_bonus(bono_id, empleado_id)

        return mongo_data, 200
    except Exception as e:
        abort(http_error_dict[type(e).__name__])

@api_empleado.route("/empleado/agregar_descuento/", methods=["POST"])
def post_api_empleado_add_discount():
    try:
        descuento = request.get_json()
        descuento_id = descuento["descuento_id"]
        empleado_id = descuento["empleado_id"]
        mongo_data = get_db_empleado_add_discount(descuento_id)

        return mongo_data, 200
    except Exception as e:
        abort(http_error_dict[type(e).__name__])

@api_empleado.route("/empleado/quitar_descuento/", methods=["POST"])
def post_api_empleado_remove_discount():
    try:
        descuento = request.get_json()
        descuento_id = descuento["descuento_id"]
        empleado_id = descuento["empleado_id"]
        mongo_data = get_db_empleado_remove_discount(descuento_id)

        return mongo_data, 200
    except Exception as e:
        abort(http_error_dict[type(e).__name__])

def get_db_empleado(id):
    data = None
    mensaje = ""
    status = "Success"
    response = {}
    try:
        resultado = get_empleado(id)

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

def get_db_empleado_all():
    data = None
    mensaje = ""
    status = "Success"
    response = {}
    try:
        lista = []
        for empleado in get_empleado_all():
            lista.append(empleado)

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

def delete_db_empleado(id):
    data = None
    mensaje = ""
    status = "Success"
    response = {}
    try:
        resultado = delete_empleado(id)

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

def create_db_empleado(apellido_primero, apellido_segundo, carnet_igss, dpi, estado, fecha_nacimiento, jornada, nit, nombre_primero, nombre_segundo, puesto_id, telefono1, telefono2):
    data = None
    mensaje = ""
    status = "Success"
    response = {}
    try:
        resultado = create_empleado(telefono2, telefono1, puesto_id, nombre_segundo, nombre_primero,nit,jornada,fecha_nacimiento,estado,dpi,carnet_igss,apellido_segundo,apellido_primero)

        if resultado:
            data =  json.loads(json.dumps(get_empleado(resultado.inserted_id), default=json_util.default))
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


def update_db_empleado(id, apellido_primero, apellido_segundo, carnet_igss, dpi, estado, fecha_nacimiento, jornada, nit, nombre_primero, nombre_segundo, puesto_id, telefono1, telefono2):
    data = None
    mensaje = ""
    status = "Success"
    response = {}
    try:
        resultado = update_empleado(id, telefono2, telefono1, puesto_id, nombre_segundo, nombre_primero,nit,jornada,fecha_nacimiento,estado,dpi,carnet_igss,apellido_segundo,apellido_primero)

        if resultado:
            data =  json.loads(json.dumps(get_empleado(id), default=json_util.default))
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

def get_db_empleado_add_bonus(bono_id, empleado_id):
    data = None
    mensaje = ""
    status = "Success"
    response = {}
    try:
        resultado = add_bono(bono_id, empleado_id)

        if resultado:
            data = json.loads(json.dumps(get_empleado(empleado_id), default=json_util.default))
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

def get_db_empleado_remove_bonus(bono_id, empleado_id):
    data = None
    mensaje = ""
    status = "Success"
    response = {}
    try:
        resultado = remove_bono(bono_id, empleado_id)

        if resultado:
            data = json.loads(json.dumps(get_empleado(empleado_id), default=json_util.default))
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

def get_db_empleado_add_discount(descuento_id, empleado_id):
    data = None
    mensaje = ""
    status = "Success"
    response = {}
    try:
        resultado = add_descuento(descuento_id, empleado_id)

        if resultado:
            data = json.loads(json.dumps(get_empleado(empleado_id), default=json_util.default))
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

def get_db_empleado_remove_discount(descuento_id, empleado_id):
    data = None
    mensaje = ""
    status = "Success"
    response = {}
    try:
        resultado = remove_bono(descuento_id, empleado_id)

        if resultado:
            data = json.loads(json.dumps(get_empleado(empleado_id), default=json_util.default))
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