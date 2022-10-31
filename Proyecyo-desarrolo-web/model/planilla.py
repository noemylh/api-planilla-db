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
db = mongo.db.planilla

def get_planilla_all():
    resultado = db.find()
    
    return resultado

def get_planilla(id):
    planilla = db.find_one({"_id": ObjectId(id)})
    
    return planilla

def delete_planilla(id):
    planilla = db.find_one_and_delete({"_id":ObjectId(id)})
    
    return planilla

def create_planilla(numero_de_pago,   numero_de_planilla,   numero_de_documento_de_pago, monto_ordinario,   dia_pago , empleado_id ):
    
    if numero_de_pago < 0:
        raise Exception(' debe ser numeros positivos.')
    
    if numero_de_planilla < 0:
        raise Exception('Precio debe ser positivo.')

    if numero_de_documento_de_pago >= 100:
        raise Exception('debe de ser numeros positivos')
        
    if numero_de_pago < 0:
        raise Exception(' debe ser numeros positivos.')
    
    planilla = db.insert_one({"numero_de_pago": numero_de_pago,   "numero_de_planilla": numero_de_planilla,   "numero_de_documento_de_pago": numero_de_documento_de_pago,   "monto_ordinario":monto_ordinario,   "dia_pago":dia_pago,  "empleado_id": ObjectId(empleado_id)})

    return planilla

def update_planilla(planilla_id ,numero_de_pago,   numero_de_planilla,   numero_de_documento_de_pago, monto_ordinario,   dia_pago , empleado_id  ):
    planilla = db.find_one({"_id":ObjectId(planilla_id)})

    if numero_de_pago < 0:
        raise Exception(' debe ser numeros positivos.')
    
    if numero_de_planilla < 0:
        raise Exception('Precio debe ser positivo.')

    if numero_de_documento_de_pago >= 100:
        raise Exception('debe de ser numeros positivos')
    
    if numero_de_pago < 0:
        raise Exception(' debe ser numeros positivos.')
    
    planilla = db.update_one({"_id":ObjectId(planilla_id)}, {"$set": {"numero_de_pago": numero_de_pago,   "numero_de_planilla": numero_de_planilla,   "numero_de_documento_de_pago": numero_de_documento_de_pago,   "monto_ordinario":monto_ordinario,   "dia_pago":dia_pago,  "empleado_id": ObjectId(empleado_id) }})
    
    return planilla