from course.src.Kata.carrito_compras30 import Product, ShoppingCart
from pytest import mark

params = (
    ("Iceberg", 1.55, 15, 21, 1.78, 2.15),
    ("Tomato", 0.52, 15, 21, 0.6, 0.73),
    ("Chicken", 1.34, 12, 21, 1.5, 1.81),
    ("Bread", 0.71, 12, 10, 0.8, 0.88),
    ("Corn", 1.21, 12, 10, 1.36, 1.5)
)


@mark.parametrize('name, cost, profit_percentage, tax_percentage, price_per_unit, expected_price_with_tax', params)
def test_calculate_price(name, cost, profit_percentage, tax_percentage, price_per_unit, expected_price_with_tax):
    product = Product(name, cost, profit_percentage, tax_percentage)
    assert product.calculate_price_per_unit() == price_per_unit
    assert product.calculate_price_with_tax() == expected_price_with_tax


params = (
    ("Iceberg", 1.55, 15, 21),
    ("Tomato", 0.52, 15, 21),
    ("Chicken", 1.34, 12, 21),
)


@mark.parametrize('name, cost, profit_percentage, tax_percentage')
def test_add_product(name, cost, profit_percentage, tax_percentage):
    cart = ShoppingCart()
    product = Product(name, cost, profit_percentage, tax_percentage)
    cart.add_product(product)
    assert name in cart.products
    assert cart.products[name]['quantity'] == 1
    assert cart.products[name]['price_with_tax'] == product.calculate_price_with_tax()
