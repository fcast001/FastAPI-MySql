from fastapi import APIRouter #Definir Sub Rutas
from config.db import conn # Importar la bbdd conexion
from models.user import users #Importar el esquema, es la tabla
from schemas.user import User #Importamos el esquema de usuarios
from cryptography.fernet import Fernet #Para encriptar password

key = Fernet.generate_key() #Iniciamos Fernet
f = Fernet(key) #Creamos la funcion
user = APIRouter() #Ejecutamos el API

#Decorador

##Rutas tipicas de un CRUD
@user.get("/users") #Para generar conexion a la BBDD es necesario configurar en archivo config.py
def get_users():
    return conn.execute(users.select()).fetchall()

@user.post("/users")
def create_user(user: User):
    new_user = {"name": user.name, "email": user.email}#Creamos el diccionario
    new_user["password"] = f.encrypt(user.password.encode("utf-8"))#Encriptamos la password
    result = conn.execute(users.insert().values(new_user))#Ejecutamos el inser
    return conn.execute(users.select().where(users.c.id == result.lastrowid)).first()#Imprimimos el resultado para el cliente
    

@user.get("/users/{id}") #Seleccionamos registro con parametro ingresado por el user
def get_users(id:str):
    return conn.execute(users.select().where(users.c.id == id)).first()#Imprimimos el resultado para el cliente
