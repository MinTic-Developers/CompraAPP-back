from pydantic import BaseModel

class UserIn(BaseModel):
    codigo: str
    nombre: str
    contraseña: str
    direccion: str

class UserOut(BaseModel):
    codigo: str
    nombre: str
    direccion: str