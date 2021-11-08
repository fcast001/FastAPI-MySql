from fastapi import FastAPI
from router.user import user #Desde router llamamos sus funciones de user (Modulo)

#Esta es mi aplicación
app = FastAPI(
        title="Mi primera API desde fastapi",
        description="Es mi primer desarrollo de FastAPI",
        version="0.0.0.1",
        openapi_tags=[{
            "name" : "Users",
            "description":"Metodos de Eliminacion de Usuarios"
        }]
) 

app.include_router(user) #Incluimos las rutas que vienen desde user