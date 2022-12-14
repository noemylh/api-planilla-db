from main import app
from flask_pymongo import PyMongo
from bson.objectid import ObjectId

mongo = PyMongo(app)
db = mongo.db.bono

def get_bono_all():
    resultado = db.find()
    
    return resultado

def get_bono(id):
    bono = db.find_one({"_id": ObjectId(id)})
    
    return bono

def delete_bono(id):
    bono = db.find_one_and_delete({"_id":ObjectId(id)})
    
    return bono

def create_bono( nombre,   cantidad,   porcentaje,   fecha_aplicacion ):

    if len(nombre) >100:
        raise Exception('Nombre excede los 100 caracteres permitidos.')
    if cantidad != "null":
        if cantidad < 0:
            raise Exception('Precio debe ser positivo.')

    if len(nombre) >= 100:
        raise Exception('Nombre excede los 100 caracteres permitidos.')
    if porcentaje != "null":
        if porcentaje < 0 :
            raise Exception('debe ser positivo.')

    bono = db.insert_one({ "_id":ObjectId(),"nombre":nombre,   "cantidad":cantidad,   "porcentaje":porcentaje,   "fecha_aplicacion":fecha_aplicacion })
    return bono

def update_bono(id, nombre,   cantidad,   porcentaje,   fecha_aplicacion):

    if len(nombre) >100:
        raise Exception('Nombre excede los 100 caracteres permitidos.')
    if cantidad != "null":
        if cantidad < 0:
            raise Exception('Precio debe ser positivo.')

    if len(nombre) >= 100:
        raise Exception('Nombre excede los 100 caracteres permitidos.')
    if porcentaje != "null":
        if porcentaje < 0 :
            raise Exception('debe ser positivo.')

    bono = db.update_one({"_id":ObjectId(id)}, {"$set": { "nombre":nombre,   "cantidad":cantidad,   "porcentaje":porcentaje,   "fecha_aplicacion":fecha_aplicacion  } })
    
    return bono