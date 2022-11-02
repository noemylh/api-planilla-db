import bcrypt
from flask import Blueprint, abort, request
from utils.config import http_error_dict
from utils.environment import get_environment
from bson import json_util
import json

from model.detalle_planilla import get_detalle_planilla_all, get_detalle_planilla, delete_detalle_planilla, create_detalle_planilla, update_detalle_planilla

serverConfig = get_environment("Server")
api_detalle_planilla = Blueprint("api_detalle_planilla", __name__)

@api_detalle_planilla.route("/detalle_planilla/actualizar/<string:id>", methods=["PUT"])
def update_api_detalle_planilla(id):
    try:
        detalle_planilla = request.get_json()

        anticipo = float(detalle_planilla["anticipo"])
        bonificaciones = float(detalle_planilla["bonificaciones"])
        igss = float(detalle_planilla["igss"])
        isr = float(detalle_planilla["isr"])
        judicial = detalle_planilla["judicial"]
        otros = detalle_planilla["otros"]
        planilla_id = detalle_planilla["planilla_id"]
        sueldo_extraordinario = float(detalle_planilla["sueldo_extraordinario"])
        total_de_descuento = float(detalle_planilla["total_de_descuento"])
        total_devengado = float(detalle_planilla["total_devengado"])
        total_liquido = float(detalle_planilla["total_liquido"])

        mongo_data = update_db_detalle_planilla(id, anticipo, bonificaciones, igss, isr, judicial, otros, planilla_id, sueldo_extraordinario, total_de_descuento,total_devengado, total_liquido)
        
        return mongo_data, 200

    except Exception as e:
        abort(http_error_dict[type(e).__name__])


@api_detalle_planilla.route("/detalle_planilla/crear/", methods=["POST"])
def create_api_detalle_planilla():
    try:
        detalle_planilla = request.get_json()

        anticipo = float(detalle_planilla["anticipo"])
        bonificaciones = float(detalle_planilla["bonificaciones"])
        igss = float(detalle_planilla["igss"])
        isr = float(detalle_planilla["isr"])
        judicial = detalle_planilla["judicial"]
        otros = detalle_planilla["otros"]
        planilla_id = detalle_planilla["planilla_id"]
        sueldo_extraordinario = float(detalle_planilla["sueldo_extraordinario"])
        total_de_descuento = float(detalle_planilla["total_de_descuento"])
        total_devengado = float(detalle_planilla["total_devengado"])
        total_liquido = float(detalle_planilla["total_liquido"])

        mongo_data = create_db_detalle_planilla(anticipo, bonificaciones, igss, isr, judicial, otros, planilla_id, sueldo_extraordinario, total_de_descuento,total_devengado, total_liquido)
            
        return mongo_data, 200

    except Exception as e:
        abort(http_error_dict[type(e).__name__])


@api_detalle_planilla.route("/detalle_planilla/eliminar/<string:id>", methods=["DELETE"])
def delete_api_detalle_planilla_by_id(id):
    try:
        if id:
            mongo_data = delete_db_detalle_planilla(id)
            
            return mongo_data, 200
        else:
            abort(400)

    except Exception as e:
        abort(http_error_dict[type(e).__name__])

@api_detalle_planilla.route("/detalle_planilla/ver/<string:id>", methods=["GET"])
def get_detalle_planilla_by_id(id):
    try:
        if id:
            mongo_data = get_db_detalle_planilla(id)
            
            return mongo_data, 200
        else:
            abort(400)

    except Exception as e:
        abort(http_error_dict[type(e).__name__])

@api_detalle_planilla.route("/detalle_planilla/ver/", methods=["GET"])
def get_api_detalle_planilla_all():
    try:
        if id:
            mongo_data = get_db_detalle_planilla_all()
            
            return mongo_data, 200
        else:
            abort(400)

    except Exception as e:
        abort(http_error_dict[type(e).__name__])

def get_db_detalle_planilla(id):
    data = None
    mensaje = ""
    status = "Success"
    response = {}
    try:
        resultado = get_detalle_planilla(id)

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

def get_db_detalle_planilla_all():
    data = None
    mensaje = ""
    status = "Success"
    response = {}
    try:
        lista = []
        for detalle_planilla in get_detalle_planilla_all():
            lista.append(detalle_planilla)

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

def delete_db_detalle_planilla(id):
    data = None
    mensaje = ""
    status = "Success"
    response = {}
    try:
        resultado = delete_detalle_planilla(id)

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

def create_db_detalle_planilla(anticipo, bonificaciones, igss, isr, judicial, otros, planilla_id, sueldo_extraordinario, total_de_descuento,total_devengado, total_liquido):
    data = None
    mensaje = ""
    status = "Success"
    response = {}
    try:
        resultado = create_detalle_planilla(sueldo_extraordinario,  bonificaciones, otros,  total_devengado,  total_de_descuento,  total_liquido,  igss,  isr,  judicial, anticipo, planilla_id )

        if resultado:
            data =  json.loads(json.dumps(get_detalle_planilla(resultado.inserted_id), default=json_util.default))
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


def update_db_detalle_planilla(id, anticipo, bonificaciones, igss, isr, judicial, otros, planilla_id, sueldo_extraordinario, total_de_descuento,total_devengado, total_liquido):
    data = None
    mensaje = ""
    status = "Success"
    response = {}
    try:
        resultado = update_detalle_planilla(id, sueldo_extraordinario,  bonificaciones, otros,  total_devengado,  total_de_descuento,  total_liquido,  igss,  isr,  judicial, anticipo, planilla_id )

        if resultado:
            data =  json.loads(json.dumps(get_detalle_planilla(id), default=json_util.default))
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