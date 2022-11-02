from main import app
from flask import Blueprint, current_app
from utils.environment import get_environment
from flask_pymongo import PyMongo
from bson.objectid import ObjectId

serverConfig = get_environment("Server")
user_data = Blueprint("user_data", __name__)

mongo = PyMongo(app)
db = mongo.db.empleado

def get_usuario(correo):
    usuario = db.find_one({"usuario.correo" : correo})
    return usuario

def delete_usuario(id):
    usuario = db.find_one_and_update({"_id":ObjectId(id)},{"$pull":{"usuario": {"status":1}}})

    return usuario

def create_usuario(id_empleado, nombre_usuario, contraseña, correo):
    if get_usuario_por_nombre(nombre_usuario) != None:
        raise Exception("Ya existe un usuario con este nombre")
    if get_usuario(correo) != None:
        raise Exception("Ya existe un usuario con este correo")

    usuario = db.find_one_and_update({"_id":ObjectId(id_empleado)},{"$push":{"usuario":{"nombre_usuario":nombre_usuario, "correo":correo, "contraseña": contraseña, "status" : 1}}})

    return usuario

def update_usuario(contraseña, correo):
    usuario = db.find_one_and_update({"usuario.correo":correo}, {"$set":{"usuario.$.contraseña":contraseña}})

    return usuario

def get_usuario_por_nombre(nombre_usuario):
    return db.find_one({"usuario.nombre":nombre_usuario})