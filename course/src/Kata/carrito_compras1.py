product = {
    'name': None,
    'cost': None,
    'revenues_percentage': None,
    'tax_percentage':None
}

cart_shoping = {
    'product': []
}
def add_product(name, cost, revenues_percentage, tax_percentage):
    product = {
        'name': name,
        'cost': cost,
        'revenues_percentage': revenues_percentage,
        'tax_percentage': tax_percentage
    }
    cart_shoping['product'].append(product)
    return product

def calculate_price_unit(name, cost, revenues_percentage, tax_percentage):
    price_unit = cost + (cost * revenues_percentage / 100)
    return round(price_unit, 2)

def calculate_price_final(name, cost, revenues_percentage, tax_percentage):
    price_unit = calculate_price_unit(name, cost, revenues_percentage, tax_percentage)
    price_final = price_unit + (price_unit * tax_percentage / 100)
    return round(price_final, 2)

def display_cart():
    for product in cart_shoping['product']:
        price_unit = calculate_price_unit(product['name'], product['cost'],product['revenues_percentage'], product['tax_percentage'])
        price_final = calculate_price_final(product['name'], product['cost'],product['revenues_percentage'], product['tax_percentage'])
        print(f"| {product['name']} | {price_final} |")

add_product("Iceberg", 1.55, 15, 21)
add_product("Tomato", 0.52, 15, 21)
add_product("Chicken", 1.34, 12, 21)
add_product("Bread", 0.71, 12, 10)
add_product("Corn", 1.21, 12, 10)
display_cart()


