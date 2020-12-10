from pydantic import BaseModel

class ProductIn(BaseModel):
    codigo: str
    cant_disponible: int

class ProductOut(BaseModel):
    codigo: str
    nombre: str
    precio: int
    cant_disponible: int