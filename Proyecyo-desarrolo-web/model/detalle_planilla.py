from main import app
from flask import Blueprint
from utils.environment import get_environment
from flask_pymongo import PyMongo
from bson.objectid import ObjectId

serverConfig = get_environment("Server")
prueba_data = Blueprint("prueba_data", __name__)

mongo = PyMongo(app)
db = mongo.db.detalle_planilla

def get_detalle_planilla_all():
    resultado = db.find()
    
    return resultado

def get_detalle_planilla(id):
    detalle_planilla = db.find_one({"_id": ObjectId(id)})
    
    return detalle_planilla

def delete_detalle_planilla(id):
    detalle_planilla = db.find_one_and_delete({"_id":ObjectId(id)})
    
    return detalle_planilla

def create_detalle_planilla( sueldo_extraordinario,  bonificaciones, otros,  total_devengado,  total_de_descuento,  total_liquido,  igss,  isr,  judicial, anticipo, planilla_id ):
    
    if sueldo_extraordinario < 0:
        raise Exception(' debe ser numeros positivos.')
    
    if bonificaciones < 0:
        raise Exception('Precio debe ser positivo.')

    if igss < 0:
        raise Exception(' debe ser numeros positivos.')

    detalle_planilla = db.insert_one({ "anticipo": anticipo,   "bonificaciones": bonificaciones,   "igss": igss,   "isr": isr,   "judicial":judicial,   "otros":otros,  "planilla_id": ObjectId(planilla_id), "sueldo_extraordinario":sueldo_extraordinario, "total_de_descuento":total_de_descuento, "total_devengado":total_devengado, "total_liquido":total_liquido })

    return detalle_planilla

def update_detalle_planilla(detalle_planilla_id, sueldo_extraordinario,  bonificaciones, otros,  total_devengado,  total_de_descuento,  total_liquido,  igss,  isr,  judicial, anticipo, planilla_id  ):
    detalle_planilla = db.find_one({"_id":ObjectId(detalle_planilla_id)})

    if sueldo_extraordinario < 0:
        raise Exception(' debe ser numeros positivos.')
    
    if bonificaciones < 0:
        raise Exception('Precio debe ser positivo.')
        
    if igss < 0:
        raise Exception(' debe ser numeros positivos.')



    detalle_planilla = db.update_one({"_id":ObjectId(detalle_planilla_id)}, {"$set": {"anticipo": anticipo,   "bonificaciones": bonificaciones,   "igss": igss,   "isr": isr,   "judicial":judicial,   "otros":otros,  "planilla_id": ObjectId(planilla_id), "sueldo_extraordinario":sueldo_extraordinario, "total_de_descuento":total_de_descuento, "total_devengado":total_devengado, "total_liquido":total_liquido }})
    
    return detalle_planilla