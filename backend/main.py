from fastapi import FastAPI, HTTPException
from config import PRODUCTS_FILE

import json

app = FastAPI()

@app.get("/hello")
async def root():
    return  {"message": "Hello World"}

@app.get("/products")
async def productsGet(category : str = None):
    try :
        with open(PRODUCTS_FILE) as products:
            prodData = json.load(products)
            return list(filter(lambda product : 
                            (category == None or product["category"] == category)
                            ,prodData
                            )
                        )
            # return json.load(products)
    except Exception as e :
            print ("error:", str(e))
            raise HTTPException(status_code=500, detail="error getting data: "+ str(e)) 
    
