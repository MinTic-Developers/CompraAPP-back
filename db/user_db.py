from typing import Dict
from pydantic import BaseModel

class UserInDB(BaseModel):
    codigo: str
    nombre: str
    contrasena: str
    direccion: str

database_user = Dict[str, UserInDB]
database_user = {
    "0001": UserInDB(**{"codigo":"0001",
                            "nombre":"Jhonatan Mora",
                            "contrasena": "jhon123",
                            "direccion":"calle 80 # 50c-82"}),
    "0002": UserInDB(**{"codigo":"0002",
                            "nombre":"Maria Ramos",
                            "contrasena": "ramos86",
                            "direccion":"carrera 55 # 45-22"}),
    "0003": UserInDB(**{"codigo":"0003",
                            "nombre":"Laura Casas",
                            "contrasena": "casas316",
                            "direccion":"calle 75 #55c-32"}),
}

def get_user(codigo: str):
    if codigo in database_user.keys():
        return database_user[codigo]
    else:
        return None

def update_user(user_in_db: UserInDB):
    database_user[user_in_db.codigo] =  user_in_db
    return user_in_db

