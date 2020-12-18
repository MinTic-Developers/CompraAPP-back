from db.productos_db import ProductInDB, update_product, get_product, database_products
from models.productos_models import ProductIn, ProductOut

from fastapi import FastAPI
from fastapi import HTTPException
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

origins = [
    "https://compraapp-front.herokuapp.com/",
]

app.add_middleware(
    CORSMiddleware, allow_origins=origins,
    allow_credentials=True, allow_methods=["*"], allow_headers=["*"],
)

@app.get("/") #GET / HTTP/1.1 (LADO DEL)
async def root():
    return {"message": "Hello: ComprAPP"}

@app.get("/products") #GET / HTTP/1.1 (LADO DEL)
async def productos():
    return {"Productos": database_products}

@app.get("/products/{codigo}") #GET / HTTP/1.1 (LADO DEL)
async def get_user_br_codigo(codigo: str):
    if codigo in database_products:
        return {"Productos": database_products[codigo]}
    else:
        raise HTTPException(status_code=404, detail="El producto no se encuentra registrado!")

@app.post("/products/")
async def create_product(producto: ProductInDB):
    database_products[producto.codigo]=producto
    return producto

@app.delete("/products/")
async def delete_producto(producto: ProductInDB):
    del database_products[producto.codigo]
    return producto

@app.put("/products/")
async def update_producto(producto: ProductInDB):
    database_products[producto.codigo]=producto
    return producto
