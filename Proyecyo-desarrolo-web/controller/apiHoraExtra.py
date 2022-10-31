import bcrypt
from flask import Blueprint, session, abort, request, jsonify
from flask import current_app
from utils.config import http_error_dict
from validator import validate
from utils.environment import get_environment
from bson import json_util
import json

from model.hora_extra import get_hora_extra_all, get_hora_extra, delete_hora_extra, create_hora_extra, update_hora_extra

serverConfig = get_environment("Server")
api_hora_extra = Blueprint("api_hora_extra", __name__)

@api_hora_extra.route("/hora_extra/actualizar/<string:id>", methods=["PUT"])
def update_api_hora_extra(id):
    try:
        hora_extra = request.get_json()

        cantidad = hora_extra["cantidad"]
        fecha = hora_extra["fecha"]
        planilla_id = hora_extra["planilla_id"]
        valor_calculo = hora_extra["valor_calculo"]
        empleado_id = hora_extra["empleado_id"]

        mongo_data = update_db_hora_extra(id, cantidad, fecha,   valor_calculo,   empleado_id,   planilla_id)
            
        return mongo_data, 200

    except Exception as e:
        abort(http_error_dict[type(e).__name__])


@api_hora_extra.route("/hora_extra/crear/", methods=["POST"])
def create_api_hora_extra():
    try:
        hora_extra = request.get_json()

        cantidad = hora_extra["cantidad"]
        fecha = hora_extra["fecha"]
        planilla_id = hora_extra["planilla_id"]
        valor_calculo = hora_extra["valor_calculo"]
        empleado_id = hora_extra["empleado_id"]

        mongo_data = create_db_hora_extra(cantidad, fecha,   valor_calculo,   empleado_id,   planilla_id)
            
        return mongo_data, 200

    except Exception as e:
        abort(http_error_dict[type(e).__name__])


@api_hora_extra.route("/hora_extra/eliminar/<string:id>", methods=["DELETE"])
def delete_api_hora_extra_by_id(id):
    try:
        if id:
            mongo_data = delete_db_hora_extra(id)
            
            return mongo_data, 200
        else:
            abort(400)

    except Exception as e:
        abort(http_error_dict[type(e).__name__])

@api_hora_extra.route("/hora_extra/ver/<string:id>", methods=["GET"])
def get_hora_extra_by_id(id):
    try:
        if id:
            mongo_data = get_db_hora_extra(id)
            
            return mongo_data, 200
        else:
            abort(400)

    except Exception as e:
        abort(http_error_dict[type(e).__name__])

@api_hora_extra.route("/hora_extra/ver/", methods=["GET"])
def get_api_hora_extra_all():
    try:
        if id:
            mongo_data = get_db_hora_extra_all()
            
            return mongo_data, 200
        else:
            abort(400)

    except Exception as e:
        abort(http_error_dict[type(e).__name__])

def get_db_hora_extra(id):
    data = None
    mensaje = ""
    status = "Success"
    response = {}
    try:
        resultado = get_hora_extra(id)

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

def get_db_hora_extra_all():
    data = None
    mensaje = ""
    status = "Success"
    response = {}
    try:
        lista = []
        for hora_extra in get_hora_extra_all():
            lista.append(hora_extra)

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

def delete_db_hora_extra(id):
    data = None
    mensaje = ""
    status = "Success"
    response = {}
    try:
        resultado = delete_hora_extra(id)

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

def create_db_hora_extra(cantidad, fecha,   valor_calculo,   empleado_id,   planilla_id):
    data = None
    mensaje = ""
    status = "Success"
    response = {}
    try:
        resultado = create_hora_extra(cantidad, fecha,   valor_calculo,   empleado_id,   planilla_id)

        if resultado:
            data =  json.loads(json.dumps(get_hora_extra(resultado.inserted_id), default=json_util.default))
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


def update_db_hora_extra(id, cantidad, fecha,   valor_calculo,   empleado_id,   planilla_id):
    data = None
    mensaje = ""
    status = "Success"
    response = {}
    try:
        resultado = update_hora_extra(id, cantidad, fecha,   valor_calculo,   empleado_id,   planilla_id)

        if resultado:
            data =  json.loads(json.dumps(get_hora_extra(id), default=json_util.default))
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