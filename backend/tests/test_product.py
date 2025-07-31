from fastapi.testclient import TestClient

from app.main import app

client = TestClient(app)

def test_product_get_unfiltered():
    response = client.get("/products")
    assert response.status_code == 200
    data = response.json()

    assert isinstance(data,list)
    assert len(data) == 20

def test_product_get_filtered():
    response = client.get("/products?category=electronics")
    assert response.status_code == 200
    data = response.json()

    assert isinstance(data,list)
    assert len(data) == 8

def test_product_get_filtered_notfound():
    response = client.get("/products?category=elec")
    assert response.status_code == 200
    data = response.json()

    assert isinstance(data,list)
    assert len(data) == 0

def test_product_get_filtered_caseSensitive():
    response = client.get("/products?category=Electronics")
    assert response.status_code == 200
    data = response.json()

    assert isinstance(data,list)
    assert len(data) == 0