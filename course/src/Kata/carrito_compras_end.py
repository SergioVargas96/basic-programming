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

    def __str__(self):
        return f"{self.name} - price unit: {self.calculate_price_per_unit()} - Price: {self.calculate_price_with_tax()}"


class ShoppingCart:
    def __init__(self):
        self.products = []

    def add_product(self, product):
        self.products.append(product)

    def remove_product(self, product):
        self.products.remove(product)

    def sum_quantity(self):
        cantidad_total = 0
        for product in self.products:
            cantidad_total += 1
        return cantidad_total

    def sum_total_price(self):
        precio_total = 0
        for product in self.products:
            precio_total += product.calculate_price_with_tax()
        return round(precio_total, 2)

    def sum_total_produt_price_quantity(self):
        summation = {}
        for product in self.products:
            if product.name in summation:
                summation[product.name]["quantity"] += 1
                summation[product.name]["total_price"] += product.calculate_price_with_tax()
            else:
                summation[product.name] = {
                    "quantity": 1,
                    "total_price": product.calculate_price_with_tax()
                }
        return summation

    def get_total_price(self):
        total_price = sum(product['total_price'] * product['quantity'] for product in self.sum_total_produt_price_quantity().values())
        return round(total_price, 2)

    def display_cart(self):
        print("| Product name | Price with VAT | Quantity |")
        for product_name, product_price in cart.sum_total_produt_price_quantity().items():
            print(
                f"{product_name}: | {product_price['total_price']}, |{product_price['quantity']}")
        print(f"| total productos: {len(self.products):} | Total price {self.get_total_price()}|")




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
cart.display_cart()
cart.add_product(bread)
cart.add_product(corn)
cart.add_product(iceberg)
cantidad_total = cart.sum_quantity()
precio_total = cart.sum_total_price()
cart.display_cart()
print(f"Cantidad total de productos en el carrito: {cantidad_total}")
print(f"Precio total de productos en el carrito: {precio_total}")
