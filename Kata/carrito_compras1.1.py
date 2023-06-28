class product_store:

    def __init__(self, name, cost, revenues_percentage, tax_percentage):
        self.name = name
        self.cost = cost
        self.revenues_percentage = revenues_percentage
        self.tax_percentage = tax_percentage

    def calculate_price_unit(self):
        price_unit = self.cost + (self.cost * self.revenues_percentage / 100)
        return round(price_unit, 2)

    def calculate_price_final(self):
        price_unit = self.calculate_price_unit()
        price_final = price_unit + (price_unit * self.tax_percentage / 100)
        return round(price_final, 2)


class cart_shopping:
    def __init__(self):
        self.products = {}

    def add_product(self, product):
        self.products[product.name] = {'price_with_tax':product.calculate_price_final(), 'quantity': 1}

    def get_total_price(self):
        total_price = sum(product['price_with_tax'] * product['quantity'] for product in self.products.values())
        return round(total_price, 2)

    def display_cart(self):
        print("| Product name | Price with VAT | Quantity |")
        for product_name, product_info in self.products.items():
            print(f"| {product_name:} | {product_info['price_with_tax']:} | {product_info['quantity']:} |")
        print("| Promotion:|")
        print(f"| Total productos: {len(self.products):} | Total price: {self.get_total_price():} |")



iceberg = product_store("Iceberg ", 1.55, 15, 21)
tomato = product_store("Tomatoe ", 0.52, 15, 21)
chicken = product_store("Chicken ", 1.34, 12, 21)
bread = product_store("Bread ", 0.71, 12, 10)
corn = product_store("Corn ", 1.21, 12, 10)
cart = cart_shopping()
cart.add_product(iceberg)
cart.add_product(tomato)
cart.add_product(chicken)
cart.add_product(bread)
cart.add_product(corn)
cart.display_cart()