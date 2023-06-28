cart_shopping = {
    'products': []
}


def add_product(name, cost, revenues_percentage, tax_percentage):
    product = {
        'name': name,
        'cost': cost,
        'revenues_percentage': revenues_percentage,
        'tax_percentage': tax_percentage
    }
    cart_shopping['products'].append(product)
    return product


def calculate_price_unit(cost, revenues_percentage):
    price_unit = cost + (cost * revenues_percentage / 100)
    return round(price_unit, 2)


def calculate_price_final(price_unit, tax_percentage):
    price_final = price_unit + (price_unit * tax_percentage / 100)
    return round(price_final, 2)


def display_cart():
    print("| Product name | Price with VAT |")
    for product in cart_shopping['products']:
        price_unit = calculate_price_unit(product['cost'], product['revenues_percentage'])
        price_final = calculate_price_final(price_unit, product['tax_percentage'])
        print(f"| {product['name']} | {price_final} |")


add_product("Iceberg", 1.55, 15, 21)
add_product("Tomato", 0.52, 15, 21)
add_product("Chicken", 1.34, 12, 21)
add_product("Bread", 0.71, 12, 10)
add_product("Corn", 1.21, 12, 10)
display_cart()
