from typing import List
from fastapi import APIRouter, Response, status  # Definir Sub Rutas
from config.db import conn  # Importar la bbdd conexion
from models.user import users  # Importar el esquema, es la tabla
from schemas.user import User  # Importamos el esquema de usuarios
from cryptography.fernet import Fernet  # Para encriptar password
# Para responder el estado de la peticion
from starlette.status import HTTP_204_NO_CONTENT


key = Fernet.generate_key()  # Iniciamos Fernet
f = Fernet(key)  # Creamos la funcion
user = APIRouter()  # Ejecutamos el API

# Decorador

# Rutas tipicas de un CRUD


# Para generar conexion a la BBDD es necesario configurar en archivo config.py
# response_model=list[User] = Que es lo que necesita 
# tags=["Users"] Agrupamos los metodos
@user.get("/users",response_model=list[User],tags=["Users"])
def get_users():
    return conn.execute(users.select()).fetchall()


@user.post("/users",response_model=User,tags=["Users"])
def create_user(user: User):
    # Creamos el diccionario
    new_user = {"name": user.name, "email": user.email}
    new_user["password"] = f.encrypt(
        user.password.encode("utf-8"))  # Encriptamos la password
    result = conn.execute(users.insert().values(
        new_user))  # Ejecutamos el inser
    # Imprimimos el resultado para el cliente
    return conn.execute(users.select().where(users.c.id == result.lastrowid)).first()


# Seleccionamos registro con parametro ingresado por el user
@user.get("/users/{id}",response_model=list[User],tags=["Users"])
def get_users(id: str):
    # Imprimimos el resultado para el cliente
    return conn.execute(users.select().where(users.c.id == id)).first()


@user.delete("/delete/{id}", status_code=HTTP_204_NO_CONTENT,tags=["Users"])  # Eliminamos el registro ingresado
def delete_users(id: str):
    # Imprimimos el resultado para el cliente
    conn.execute(users.delete().where(users.c.id == id))
    return Response(status_code=HTTP_204_NO_CONTENT)


@user.put("/update/{id}",response_model=User,tags=["Users"])  # Eliminamos el registro ingresado
def update_users(id: str, user: User):
    conn.execute(users.update().values(name=user.name, email=user.email, password=f.encrypt(
        user.password.encode("utf-8"))).where(users.c.id == id))  # Imprimimos el resultado para el cliente
    return Response(status_code=HTTP_204_NO_CONTENT)
