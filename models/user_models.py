from pydantic import BaseModel

class UserctIn(BaseModel):
    codigo: str
    direccion: str

class ProductOut(BaseModel):
    nombre: str
    contraseña: str
    direccion: str