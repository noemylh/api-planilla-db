from flask import Blueprint, abort, request
from utils.config import http_error_dict
from utils.environment import get_environment
from bson import json_util
import json

from model.usuario import get_usuario, delete_usuario, create_usuario, update_usuario

serverConfig = get_environment("Server")
api_usuario = Blueprint("api_usuario", __name__)

@api_usuario.route("/usuario/actualizar/<string:id>", methods=["PUT"])
def update_api_usuario(id):
    try:
        usuario = request.get_json()

        nombre_usuario = usuario["nombre_usuario"]
        contraseña = usuario["contraseña"]
        correo = usuario["correo"]

        mongo_data = update_db_usuario(id, nombre_usuario, contraseña, correo)

        return mongo_data, 200

    except Exception as e:
        abort(http_error_dict[type(e).__name__])

@api_usuario.route("/usuario/crear", methods=["POST"])
def create_api_usuario():
    try:
        usuario = request.get_json()

        id_empleado = usuario["id_empleado"]
        nombre_usuario = usuario["nombre_usuario"]
        contraseña = usuario["contraseña"]
        correo = usuario["correo"]

        mongo_data = create_db_usuario(id_empleado, nombre_usuario, contraseña, correo)

        return mongo_data, 200
    except Exception as e:
        abort(http_error_dict[type(e).__name__])

@api_usuario.route("/usuario/ver/<string:correo>", methods=["GET"])
def get_usuario_by_correo(correo):
    try:
        if correo:
            mongo_data = get_db_usuario(correo)

            return mongo_data, 200
        else:
            abort(400)
    except Exception as e:
        abort(http_error_dict[type.__name__])

@api_usuario.route("/usuario/eliminar/<string:id>", methods=["DELETE"])
def delete_api_usuario_by_id(id):
    try:
        if id:
            mongo_data = delete_db_usuario(id)

            return mongo_data, 200
        else:
            abort(400)

    except Exception as e:
        abort(http_error_dict[type(e).__name__])

def get_db_usuario(id):
    data = None
    mensaje = ""
    status = "Success"
    response = {}
    try:
        resultado = get_usuario(id)
        if resultado:
            data = json.loads(json.dumps(resultado, default=json_util.default))
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

def delete_db_usuario(id):
    data = None
    mensaje = ""
    status = "Success"
    response = {}
    try:
        resultado = delete_usuario(id)

        if resultado:
            data = json.loads(json.dumps(resultado, default=json_util.default))
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

def create_db_usuario(id_empleado, nombre_usuario, contraseña, correo):
    data = None
    mensaje = ""
    status = "Success"
    response = {}
    try:
        resultado = create_usuario(id_empleado, nombre_usuario, contraseña, correo)

        if resultado:
            data = json.load(json.dumps(get_usuario(resultado.inserted_id), default=json_util.default))
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

def update_db_usuario(id_empleado, nombre_usuario, contraseña, correo):
    data = None
    mensaje = ""
    status = "Success"
    response = {}
    try:
        resultado = update_usuario(id_empleado, nombre_usuario, contraseña, correo)

        if resultado:
            data = json.loads(json.dumps(get_usuario(id_empleado), default=json_util.default))
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