from main import app
from flask_pymongo import PyMongo
from bson.objectid import ObjectId


mongo = PyMongo(app)
db = mongo.db.descuento

def get_descuento_all():
    resultado = db.find()
    
    return resultado

def get_descuento(id):
    descuento = db.find_one({"_id": ObjectId(id)})
    
    return descuento

def delete_descuento(id):
    descuento = db.find_one_and_delete({"_id":ObjectId(id)})
    
    return descuento

def create_descuento( nombre, cantidad, fecha_aplicacion, porcentaje ):


    if len(nombre) >= 100:
        raise Exception('Nombre excede los 100 caracteres permitidos.')

    if porcentaje < 0:
        raise Exception('el numero debe de ser positivo')


    if cantidad < 0:
        raise Exception('El numero debe ser positivo.')

    descuento = db.insert_one({ "nombre":nombre,   "porcentaje":porcentaje,   "fecha_aplicacion":fecha_aplicacion,   "cantidad": cantidad })
    return descuento

    

def update_descuento(id, nombre, cantidad, fecha_aplicacion, porcentaje):
    
    if len(nombre) >= 100:
        raise Exception('Nombre excede los 100 caracteres permitidos.')


    if porcentaje < 0:
        raise Exception('el numero debe de ser positivo')


    if cantidad < 0:
        raise Exception('El numero debe ser positivo.')


    descuento = db.update_one({"_id":ObjectId(id)}, {"$set": {    "nombre":nombre,   "porcentaje":porcentaje, "fecha_aplicacion":fecha_aplicacion, "cantidad": cantidad } })
    
    return descuento