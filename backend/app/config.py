import os

ROOT_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

PRODUCTS_FILE = os.path.join(ROOT_DIR, "model", "products.json")
ORDERS_FILE = os.path.join(ROOT_DIR, "model", "orders.json")