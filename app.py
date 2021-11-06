from fastapi import FastAPI
from router.user import user #Desde router llamamos sus funciones de user (Modulo)

app = FastAPI() #Esta es mi aplicación

app.include_router(user) #Incluimos las rutas que vienen desde user