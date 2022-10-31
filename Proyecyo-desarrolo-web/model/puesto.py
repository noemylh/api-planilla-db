from main import app
from bson import json_util
from flask import Blueprint, session, abort, request, jsonify
from flask import current_app
from utils.config import http_error_dict
from validator import validate
from utils.environment import get_environment
from flask_pymongo import PyMongo
from bson.objectid import ObjectId

serverConfig = get_environment("Server")
prueba_data = Blueprint("prueba_data", __name__)

mongo = PyMongo(app)
db = mongo.db.puesto

@prueba_data.route("/prueba", methods=["POST"])
def prueba():
    try:
        logger = current_app.logger
        logger.info("**prueba**")

        resultado = create_puesto(10, 10, "gerente 3", 1, 1, 2)
        update_puesto(resultado.inserted_id, 20, 100, "gerente 3", 1, 1, 2)
        
        return "", 200

    except Exception as e:
        logger.info(f"Response={e}")
        abort(http_error_dict[type(e).__name__])

def get_puesto_all():
    resultado = db.find()
    
    return resultado

def get_puesto(id):
    puesto = db.find_one({"_id": ObjectId(id)})
    
    return puesto

def get_puesto_por_nombre(nombre):
    return db.find_one({"nombre": nombre})

def get_puesto_por_nombre_y_id_distinto(nombre, id):
    return db.find_one({"nombre": nombre, "_id": { "$ne": ObjectId(id) } })

def delete_puesto(id):
    puesto = db.find_one_and_delete({"_id":ObjectId(id)})
    
    return puesto

def create_puesto(sueldo, precio, nombre, horas, factor_hora_extra, bonos):
    # VALIDACIONES

    if sueldo < 0:
        raise Exception('Sueldo debe ser positivo.')
    
    if precio < 0:
        raise Exception('Precio debe ser positivo.')

    if len(nombre) >= 100:
        raise Exception('Nombre excede los 100 caracteres permitidos.')

    if horas < 0:
        raise Exception('Horas debe ser positivo.')

    if factor_hora_extra < 0:
        raise Exception('Factor hora extra debe ser positivo.')

    if bonos < 0:
        raise Exception('El numero de bonos debe ser positivo.')

    # existe puesto con el mismo nombre
    if get_puesto_por_nombre(nombre) != None:
        raise Exception('Ya existe un puesto con el mismo nombre.')

    # INSERTAR

    puesto = db.insert_one({"sueldo": sueldo, "precio": precio, "nombre": nombre, "horas": horas, "factor_hora_extra": factor_hora_extra, "bonos": bonos})
    
    return puesto

def update_puesto(id, sueldo, precio, nombre, horas, factor_hora_extra, bonos):

    # VALIDACIONES

    if sueldo < 0:
        raise Exception('Sueldo debe ser positivo.')
    
    if precio < 0:
        raise Exception('Precio debe ser positivo.')

    if len(nombre) >= 100:
        raise Exception('Nombre excede los 100 caracteres permitidos.')

    if horas < 0:
        raise Exception('Horas debe ser positivo.')

    if factor_hora_extra < 0:
        raise Exception('Factor hora extra debe ser positivo.')

    if bonos < 0:
        raise Exception('El numero de bonos debe ser positivo.')

    # existe puesto con el mismo nombre y distinto ID
    if get_puesto_por_nombre_y_id_distinto(nombre, id) != None:
        raise Exception('Ya existe un puesto con el mismo nombre.')

    # INSERTAR

    puesto = db.find_one({"_id":ObjectId(id)})

    puesto = db.update_one({"_id":ObjectId(id)}, {"$set": {"sueldo": sueldo, "precio": precio, "nombre": nombre, "horas": horas, "factor_hora_extra": factor_hora_extra, "bonos": bonos}})
    
    return puesto