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
def add_tax(price, rate=0.2):
    return price * (1 + rate)
def add_tax(price, rate=0.2):
    return price * (1 + rate)
def add_taxii(price, rate=0.2):
    return price * (1 + rate)
class Product:    def __init__(self, sku, name, price):        if not sku:            raise ValueError(sku is required)        self.sku = sku        self.name = name        self.price = price 
