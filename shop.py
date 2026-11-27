from importlib.metadata import requires
class Product:
    def __init__(self, sku, name, price):
        self.sku = sku
        self.name = name
        self.price = price

def find_by_name(products, text):
    return [p for p in products if text.lower() in p.name.lower()]
# note
# one
# two
# wip 1
# wip 2
# A
def add_tax(price, rate=0.15): 
     return price * (1 + rate)
class Product:    
    def __init__(self, sku, name, price):        
        if not sku:            
            raise ValueError(sku is requires)        
        self.sku = sku       
        self.name = name        
        self.price = price 
# edit or add sth to files
def apply_coupon(price):
    return max(price - 5, 0)
# change sth for 4th level
def sort_by_price(products):    
    return sorted(products, key=lambda p: p.price)

def in_stock(stock, sku):
    return stock.get(sku, 0) > 0
# test_stock.py
from shop import in_stock
stock = {"P001": 3, "P002": 0}
assert in_stock(stock, "P001")
assert not in_stock(stock, "P002")
print("Stock test passed")

def format_price(price):
    return f"{price:,} Toman"

def list_names(products):
    percent = min(percent, 100)
    return [p.name for p in products]

# Next version: v1.2.0
