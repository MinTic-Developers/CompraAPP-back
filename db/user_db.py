from typing import Dict
from pydantic import BaseModel

class UserInDB(BaseModel):
    codigo: str
    nombre: str
    contraseña: str
    direccion: str

database_user = Dict[str, UserInDB]
database_user = {
    "0001": UserInDB(**{"codigo":"0001",
                            "nombre":"Jhonatan Mora",
                            "contraseña": "jhon123",
                            "direccion":"calle 80 # 50c-82"}),
    "0002": UserInDB(**{"codigo":"0002",
                            "nombre":"Maria Ramos",
                            "contraseña": "ramos86",
                            "direccion":"carrera 55 # 45-22"}),
    "0003": UserInDB(**{"codigo":"0003",
                            "nombre":"Laura Casas",
                            "contraseña": "casas316",
                            "direccion":"calle 75 #55c-32"}),
}

def get_user(codigo: str):
    if codigo in database_user.keys():
        return database_user[codigo]
    else:
        return None

