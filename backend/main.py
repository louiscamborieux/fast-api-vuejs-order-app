from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from config import PRODUCTS_FILE

import json
import uuid

app = FastAPI()

class Order(BaseModel):
     customer_name: str
     product_ids: list[int]

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
    
@app.post("/order")
async def productsOrder(order: Order):
    if (order.customer_name == None or order.customer_name.strip() == ""):
        raise HTTPException(400, "custommer name must not be empty")
    totalPrice = 0
    items = []
    try :
        with open(PRODUCTS_FILE) as products:
            prodData = json.load(products)
            for orderItemId in order.product_ids :
                #TODO optimize to reduce passes maybe with a dictionnary or an array
                productFound = next(filter(lambda product : product["id"] == orderItemId, prodData),None)
                if not productFound :
                    raise HTTPException(404, f"product {orderItemId} was not found")
                totalPrice += productFound["price"]
                items.append(productFound)
            return {
                "items" : items,
                "total price" : totalPrice,
                "order id" : uuid.uuid4()
            }
        
    except OSError as e :
            print ("error:", str(e))
            raise HTTPException(status_code=500, detail="error getting data: "+ str(e)) 
    
