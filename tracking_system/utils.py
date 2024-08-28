import json
import os

# File path to store the orders
ORDERS_FILE = 'data.json'

def read_orders():
    if not os.path.exists(ORDERS_FILE):
        return []
    f = open(ORDERS_FILE)
    data = json.load(f)
    f.close()
    return data

def add_order(order):
    orders = read_orders()
    orders.append(order)

    with open(ORDERS_FILE, 'w') as file:
        json.dump(orders, file, indent=4)