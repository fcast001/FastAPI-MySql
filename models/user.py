from sqlalchemy import Column, Table  # Tabla y que va a tener :columnas
from sqlalchemy.sql.sqltypes import Integer, String  # Importamos los tipos de datos
from config.db import meta, engine  # Importamos desde Configuracion BBDD

users = Table(
    "users",
    meta,
    Column("id", Integer, primary_key=True),
    Column(
        "name",
        String(255),
    ),
    Column("email", String(255)),
    Column("password", String(255)),
)

meta.create_all(engine)