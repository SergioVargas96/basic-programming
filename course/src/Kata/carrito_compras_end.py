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
        self.products = []

    def add_product(self, product):
        self.products.append(product)

    def remove_product(self, product):
        self.products.remove(product)
        print("Product elimination ")

    def sum_price_quantity(self):
        info_products = {}
        for product in self.products:
            if product.name in info_products:
                info_products[product.name]["quantity"] += 1
                info_products[product.name]["total_price"] += product.calculate_price_with_tax()
            else:
                info_products[product.name] = {
                    "quantity": 1,
                    "total_price": product.calculate_price_with_tax()
                }
        return info_products

    def get_total_price(self):
        total_price = sum(product['total_price'] * product['quantity']
                          for product in self.sum_price_quantity().values())
        return round(total_price, 2)

    def display_cart(self):
        result = [
            ("Product name", "Price with VAT", "Quantity")
        ]
        for product_name, product_info in self.sum_price_quantity().items():
            result.append(
                (product_name, product_info['total_price'], product_info['quantity']))
        total = [("total productos:", len(self.products), "Total price:", self.get_total_price())]
        return result + total

