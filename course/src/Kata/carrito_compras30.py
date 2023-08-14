class Product:
    def __init__(self, name, cost, profit_percentage, tax_percentage):
        self.name = name
        self.cost = cost
        self.profit_percentage = profit_percentage
        self.tax_percentage = tax_percentage

    def calculate_price_per_unit(self):
        price_per_unit = self.cost + (self.cost * self.profit_percentage / 100)
        return round(price_per_unit, 2)

    def calculate_price_with_tax(self):
        price_per_unit = self.calculate_price_per_unit()
        price_with_tax = price_per_unit + (price_per_unit * self.tax_percentage / 100)
        return round(price_with_tax, 2)


class ShoppingCart:
    def __init__(self):
        self.products = {}

    def add_product(self, product):
        if product.name in self.products:
            self.products[product.name]['quantity'] += 1
        else:
            self.products[product.name] = {'price_with_tax': product.calculate_price_with_tax(), 'quantity': 1}

    def get_total_price(self):
        total_price = sum(product['price_with_tax'] * product['quantity'] for product in self.products.values())
        return round(total_price, 2)

    def display_cart(self):
        print("| Product name | Price with VAT | Quantity |")
        for product_name, product_info in self.products.items():
            print(f"| {product_name:} | {product_info['price_with_tax']:} | {product_info['quantity']:} |")
        print(f"| Total productos: {len(self.products):} | Total price: {self.get_total_price():} |")



iceberg = Product("Iceberg", 1.55, 15, 21)
tomato = Product("Tomatoe", 0.52, 15, 21)
chicken = Product("Chicken", 1.34, 12, 21)
bread = Product("Bread", 0.71, 12, 10)
corn = Product("Corn", 1.21, 12, 10)

cart = ShoppingCart()
cart.display_cart()
cart.add_product(iceberg)
cart.add_product(tomato)
cart.add_product(chicken)
cart.add_product(bread)
cart.add_product(corn)
cart.display_cart()
cart.add_product(iceberg)
cart.add_product(iceberg)
cart.add_product(iceberg)
cart.add_product(tomato)
cart.add_product(chicken)
cart.add_product(bread)
cart.add_product(bread)
cart.add_product(corn)
cart.display_cart()
