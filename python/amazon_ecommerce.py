# ecommerce.py 

def add_product(name, price):
    print(f'Adding new products with Name: {name} and price: {price}')

def delete_product(product_id):
    print(f'Deleting products with product {product_id}')

def update_inventory(product_id, quantity):
    print(f"Updating inventory for product ID: {product_id} to {quantity} units")

def check_inventory(product_id):
    print(f"Checking inventory for product ID: {product_id}")

def create_order(customer_id, products):
    print(f"Creating order for customer ID: {customer_id} with products: {products}")

def cancel_order(order_id):
    print(f"Cancelling order with ID: {order_id}")

def process_payment(order_id, amount):
    print(f"Processing payment for order ID: {order_id} amount ${amount}")

def refund_payment(order_id, amount):
    print(f"Refunding payment for order ID: {order_id} amount ${amount}")

