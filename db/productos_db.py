from typing import Dict
from pydantic import BaseModel

class ProductInDB(BaseModel):
    codigo: str
    nombre: str
    precio: int
    cant_disponible: int

database_products = Dict[str, ProductInDB]
database_products = {
    "0001": ProductInDB(**{"codigo":"0001",
                            "nombre":"gaseosa personal 350 ml",
                            "precio":2000,
                            "cant_disponible":300}),
    "0002": ProductInDB(**{"codigo":"0002",
                            "nombre":"galletas festival",
                            "precio":1000,
                            "cant_disponible":3000}),
    "0003": ProductInDB(**{"codigo":"0003",
                            "nombre":"Arroz ROA 1Kg",
                            "precio":3400,
                            "cant_disponible":1000}),
}

def get_products(codigo: str):
    if codigo in database_products.keys():
        return database_products[codigo]
    else:
        return None

def update_product(product_in_db: ProductInDB):
    database_products[product_in_db.codigo] = product_in_db
    return product_in_db
