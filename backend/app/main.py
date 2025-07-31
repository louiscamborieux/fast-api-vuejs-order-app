from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from .config import PRODUCTS_FILE, ORDERS_FILE

import json
import uuid

app = FastAPI()

#global orders variable, load orders file or make it empty is the file is non-existent / corrupted
orders = []
try:
    with open(ORDERS_FILE) as orders_file:
                orders = json.load(orders_file)
except (OSError, json.JSONDecodeError):
    orders = []

class Order(BaseModel):
     customer_name: str
     product_ids: list[int]

#Hello world enpoint for testing
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
    except Exception as e :
            print ("error:", str(e))
            raise HTTPException(status_code=500, detail="error getting data: "+ str(e)) 
    
@app.post("/order")
async def productsOrder(order: Order):
    if (order.customer_name == None or order.customer_name.strip() == ""):
        raise HTTPException(400, "custommer name must not be empty")
    global orders
    totalPrice = 0
    items = []
    try :
        with open(PRODUCTS_FILE) as products:
            prodData = json.load(products)
            for orderItemId in order.product_ids :
                #TODO optimize to reduce passes for bigger maybe with a dictionnary or an array
                productFound = next(filter(lambda product : product["id"] == orderItemId, prodData),None)
                if not productFound :
                    raise HTTPException(404, f"product {orderItemId} was not found")
                totalPrice += productFound["price"]
                items.append(productFound)
            order =  {
                "items" : items,
                "total_price" : totalPrice,
                "order_id" : str(uuid.uuid4())
            }
            orders.append(order)
            with open(ORDERS_FILE, "w") as orders_file:
                 json.dump(orders,orders_file, indent=4)
            return order
        
    except OSError as e :
            print ("error:", str(e))
            raise HTTPException(status_code=500, detail="error getting data: "+ str(e)) 
    
@app.get("/orders")
async def getAllOrders():
    return orders