from flask import Blueprint, abort, request
from utils.config import http_error_dict
from utils.environment import get_environment
from bson import json_util
import json

from model.planilla import get_planilla_all, get_planilla, delete_planilla, create_planilla, update_planilla

serverConfig = get_environment("Server")
api_planilla = Blueprint("api_planilla", __name__)

@api_planilla.route("/planilla/actualizar/<string:id>", methods=["PUT"])
def update_api_planilla(id):
    try:
        planilla = request.get_json()

        dia_pago = int(planilla["dia_pago"])
        empleado_id = planilla["empleado_id"]
        monto_ordinario = float(planilla["monto_ordinario"])
        numero_de_documento_de_pago = int(planilla["numero_de_documento_de_pago"])
        numero_de_pago = int(planilla["numero_de_pago"])
        numero_de_planilla = int(planilla["numero_de_planilla"])

        mongo_data = update_db_planilla(id, dia_pago, empleado_id, monto_ordinario, numero_de_documento_de_pago, numero_de_pago, numero_de_planilla)
            
        return mongo_data, 200

    except Exception as e:
        abort(http_error_dict[type(e).__name__])


@api_planilla.route("/planilla/crear/", methods=["POST"])
def create_api_planilla():
    try:
        planilla = request.get_json()

        dia_pago = planilla["dia_pago"]
        empleado_id = planilla["empleado_id"]
        monto_ordinario = planilla["monto_ordinario"]
        numero_de_documento_de_pago = planilla["numero_de_documento_de_pago"]
        numero_de_pago = planilla["numero_de_pago"]
        numero_de_planilla = planilla["numero_de_planilla"]

        mongo_data = create_db_planilla(dia_pago, empleado_id, monto_ordinario, numero_de_documento_de_pago, numero_de_pago, numero_de_planilla)
            
        return mongo_data, 200

    except Exception as e:
        abort(http_error_dict[type(e).__name__])


@api_planilla.route("/planilla/eliminar/<string:id>", methods=["DELETE"])
def delete_api_planilla_by_id(id):
    try:
        if id:
            mongo_data = delete_db_planilla(id)
            
            return mongo_data, 200
        else:
            abort(400)

    except Exception as e:
        abort(http_error_dict[type(e).__name__])

@api_planilla.route("/planilla/ver/<string:id>", methods=["GET"])
def get_planilla_by_id(id):
    try:
        if id:
            mongo_data = get_db_planilla(id)
            
            return mongo_data, 200
        else:
            abort(400)

    except Exception as e:
        abort(http_error_dict[type(e).__name__])

@api_planilla.route("/planilla/ver/", methods=["GET"])
def get_api_planilla_all():
    try:
        if id:
            mongo_data = get_db_planilla_all()
            
            return mongo_data, 200
        else:
            abort(400)

    except Exception as e:
        abort(http_error_dict[type(e).__name__])

def get_db_planilla(id):
    data = None
    mensaje = ""
    status = "Success"
    response = {}
    try:
        resultado = get_planilla(id)

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

def get_db_planilla_all():
    data = None
    mensaje = ""
    status = "Success"
    response = {}
    try:
        lista = []
        for planilla in get_planilla_all():
            lista.append(planilla)

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

def delete_db_planilla(id):
    data = None
    mensaje = ""
    status = "Success"
    response = {}
    try:
        resultado = delete_planilla(id)

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

def create_db_planilla(dia_pago, empleado_id, monto_ordinario, numero_de_documento_de_pago, numero_de_pago, numero_de_planilla):
    data = None
    mensaje = ""
    status = "Success"
    response = {}
    try:
        resultado = create_planilla(numero_de_pago,   numero_de_planilla,   numero_de_documento_de_pago, monto_ordinario,   dia_pago , empleado_id )

        if resultado:
            data =  json.loads(json.dumps(get_planilla(resultado.inserted_id), default=json_util.default))
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


def update_db_planilla(id, dia_pago, empleado_id, monto_ordinario, numero_de_documento_de_pago, numero_de_pago, numero_de_planilla):
    data = None
    mensaje = ""
    status = "Success"
    response = {}
    try:
        resultado = update_planilla(id, numero_de_pago,   numero_de_planilla,   numero_de_documento_de_pago, monto_ordinario,   dia_pago , empleado_id )

        if resultado:
            data =  json.loads(json.dumps(get_planilla(id), default=json_util.default))
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