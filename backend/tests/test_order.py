from fastapi.testclient import TestClient

from app.main import app

client = TestClient(app)

def test_order_one_item():
    body = {
        "customer_name" : "John Doe",
        "product_ids" : [1]
    }
    response = client.post("/order", json=body)
    assert response.status_code == 200
    data = response.json()

    assert isinstance(data,dict)
    assert data["total_price"] == 12.4
    assert len(data["items"]) == 1

def test_order_many_items():
    body = {
        "customer_name" : "John Doe",
        "product_ids" : [1,3,2]
    }
    response = client.post("/order", json=body)
    assert response.status_code == 200
    data = response.json()

    assert isinstance(data,dict)
    assert data["total_price"] == 50.82
    assert len(data["items"]) == 3

def test_order_non_existing_item():
    body = {
        "customer_name" : "John Doe",
        "product_ids" : [0]
    }
    response = client.post("/order", json=body)
    assert response.status_code == 404

def test_order_non_existing_item_among_valid():
    body = {
        "customer_name" : "John Doe",
        "product_ids" : [1,0,2]
    }
    response = client.post("/order", json=body)
    assert response.status_code == 404

def test_order_bad_customer_name():
    body = {
        "customer_name" : "",
        "product_ids" : [1,2]
    }
    response = client.post("/order", json=body)
    assert response.status_code == 400

def test_order_bad_customer_name_whitespace():
    body = {
        "customer_name" : " ",
        "product_ids" : [1,2]
    }
    response = client.post("/order", json=body)
    assert response.status_code == 400