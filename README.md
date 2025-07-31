# Fullstack Order application project

This project is a simple project that use Python FastAPI framework as
backend and VueJs as frontend

The VueJs application display items provided by a REST API delivered by the backend
using axios

## Features
1. Get item list and display names, prices and categories. The items can be filtered by category using a query parameter in the API (/products?category=...)
2. Place order by selecting items with a given custommer name, the backend computes a total price then return it to the frontend, which displays it
3. Order history, list every order made, in the current version orders are stored in memory and are cleared every time the backend reboot

# Architecture 

## /backend

/app/ the logic and algortihm used in the application
    /main.py contains every endpoint implementations
    /config.py contains variable that help main load JSON files used to store products data

/model/ Where the data is stored
      /products.json contains all product's data (name, price, category, id)

/tests/ Unit tests for the backend
/tests/test_product.py tests for /product GET endpoint
/tests/test_order.py tests for /order POST endpoint

# How to start the application

## 1. Install Dependencies

1. [Python](https://www.python.org/downloads/)
2. [Python3-pip](https://pip.pypa.io/en/stable/installation/)
2. [FastAPI](https://fastapi.tiangolo.com/tutorial/#run-the-code)
3. [nodeJS (min 22.12.0)](https://nodejs.org/en/download)

## 2. Install modules
In /frontend root do:
```npm install ```

In /backend root do:
``` 
pip install "fastapi[standard]"
pip install pytest
```

## 3. Start the application

1. Start backend : in /backend do
```
fastapi dev app/main.py
```
Now the backend will start listening on port 8000
2. Start front-end : in /frontend do
```
npm run dev
```

And now you may access the application by connecting to localhost:5173
A swagger UI is also available at localhost:8000/docs