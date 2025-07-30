from fastapi import FastAPI, HTTPException
from config import PRODUCTS_FILE

import json

app = FastAPI()

@app.get("/hello")
async def root():
    return  {"message": "Hello World"}

@app.get("/products")
async def productsGet():
    try :
        with open(PRODUCTS_FILE) as products:
            prodData = json.load(products)
            return json.load(products)
    except :
            raise HTTPException(status_code=500, detail="error getting data") 
    return [
            {"id" : 0, 
             "name" : "productName",
             "category" : "test"}
        ]
    