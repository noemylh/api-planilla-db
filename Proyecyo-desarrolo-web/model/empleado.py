from main import app
from flask import Blueprint
from utils.environment import get_environment
from flask_pymongo import PyMongo
from bson.objectid import ObjectId

serverConfig = get_environment("Server")
prueba_data = Blueprint("prueba_data", __name__)

mongo = PyMongo(app)
db = mongo.db.empleado

def get_empleado_all():
   resultado = db.find()
   
   return resultado

def get_empleado(id):
   empleado = db.find_one({"_id": ObjectId(id)})
   
   return empleado

def delete_empleado(id):
   puesto = db.find_one_and_delete({"_id":ObjectId(id)})
   
   return puesto

def create_empleado(telefono2, telefono1, puesto_id, nombre_segundo, nombre_primero,nit,jornada,fecha_nacimiento,estado,dpi,carnet_igss,apellido_segundo,apellido_primero):
    
   if len(nombre_primero) > 100:
      raise Exception('Nombre excede los 100 caracteres permitidos.')
    
   if len(nombre_segundo)  > 100:
      raise Exception('Nombre excede los 100 caracteres permitidos.')

   if len(apellido_primero) > 100:
      raise Exception('Nombre excede los 100 caracteres permitidos.')

   if len (apellido_segundo) > 100:
      raise Exception('Nombre excede los 100 caracteres permitidos.')

   if len(dpi) >13:
      raise Exception(' excedio numeros de digitos permitidos.')
   
   if len(telefono1) > 15:
      raise Exception('El numero excedio de digitos.')

   if len(telefono2) > 15:
      raise Exception('El numero excedio de digitos.')

   empleado = db.insert_one({"telefono2":telefono2,"telefono1":telefono1,"puesto_id":puesto_id,"nombre_segundo": nombre_segundo,"nombre_primero":nombre_primero,"nit":nit,"jornada":jornada,"fecha_nacimiento":fecha_nacimiento,"estado":estado,"dpi":dpi,"carnet_igss":carnet_igss,"apellido_segundo":apellido_segundo,"apellido_primero":apellido_primero})

   return empleado

def update_empleado(id, telefono2, telefono1, puesto_id, nombre_segundo, nombre_primero,nit,jornada,fecha_nacimiento,estado,dpi,carnet_igss,apellido_segundo,apellido_primero):
    
   if len(nombre_primero) > 100:
      raise Exception('Nombre excede los 100 caracteres permitidos.')
   
   if len(nombre_segundo)  > 100:
      raise Exception('Nombre excede los 100 caracteres permitidos.')

   if len(apellido_primero) > 100:
      raise Exception('Nombre excede los 100 caracteres permitidos.')

   if len (apellido_segundo) > 100:
      raise Exception('Nombre excede los 100 caracteres permitidos.')

   if len(dpi) >13:
      raise Exception(' eccedio numeros de digitos permitidos.')
   
   if len(telefono1) > 15:
      raise Exception('El numero excedio de digitos.')

   if len(telefono2) > 15:
      raise Exception('El numero excedio de digitos.')

   empleado = db.update_one({"_id":ObjectId(id)}, {"$set": {"telefono2":telefono2,"telefono1":telefono1,"puesto_id":puesto_id,"nombre_segundo": nombre_segundo,"nombre_primero":nombre_primero,"nit":nit,"jornada":jornada,"fecha_nacimiento":fecha_nacimiento,"estado":estado,"dpi":dpi,"carnet_igss":carnet_igss,"apellido_segundo":apellido_segundo,"apellido_primero":apellido_primero}})

   return empleado