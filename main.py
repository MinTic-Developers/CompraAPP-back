from db.productos_db import ProductInDB, update_product, get_products
from models.productos_models import ProductIn, ProductOut

from fastapi import FastAPI
from fastapi import HTTPException
app = FastAPI()

@app.get("/") #GET / HTTP/1.1 (LADO DEL)
async def root():
    return {"message": "Hello: ComprAPP"}