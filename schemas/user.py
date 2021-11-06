from typing import Optional #Forma de traer los datos
from pydantic import BaseModel #añadir tipos de datos

class User(BaseModel):
    id:Optional[str]
    name:str
    email:str
    password:str