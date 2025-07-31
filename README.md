# Fullstack Order application project

This project is a simple project that use Python FastAPI framework as
backend and VueJs as frontend

The VueJs application uses axios to display items provided by a REST API delivered by the backend

## Features
1. Get item list and display names, prices and categories. The items can be filtered by category using a query parameter in the API (/products?category=...)
2. Place order by selecting items with a given custommer name, the backend computes a total price then return it to the frontend, which displays it
3. Order history, list every order made, orders are stored in backend/store/orders.json, this file may be create if it does not already exist.

# Architecture 

## backend

/app/ the logic and algortihm used in the application

/app/main.py contains every endpoint implementations

/app/config.py contains variable that help main load JSON files used to store products data

/model/ Where the data is stored

/model/products.json contains all product's data (name, price, category, id)

/tests/ Unit tests for the backend

/tests/test_product.py tests for /product GET endpoint

/tests/test_order.py tests for /order POST endpoint

## frontend
This frontend is derived from standard [VueJS template](https://vuejs.org/guide/quick-start)

/public every static images and icons

/src main directory containing the application

/src/components VueJS components and icons displayed to the user

/src/components/NavBar.vue navigation bar used to navigate between sections

/src/components/OrderItem.vue Order recap

/src/components/OrdersPage.vue List every order fetched from the API

/src/components/ProductItem.vue Product card with its informations displayed

/src/components/ProductList.vue List of ProductItem as well as a selected item list

/src/components/ProductPage.vue Handle display for products list and placing an order

/src/components/icons/*.vue Default used in the applications

/router/index.js route logic binding URL to Vue components

/services Handle logic behind fetching data from the API 

/services/orderService.js handle axios call to order related endpoints (/order and /orders)

/services/orderService.js handle axios call to product related endpoints (/products)

/App.vue application entrypoint, load router selected view as well as navigation bar

/main.js mount Vue app and router and launch the application.

index.html first loaded file, import application entrypoint

package.json list project dependencies, those are installed using npm install

package-lock.json list exact dependencies tree to ensure reproductivity

vite.config.js Configuration file, contains proxy settings to connect to the API 

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