from course.src.Kata.carrito_compras_end import Product, ShoppingCart
from pytest import mark, fixture


params = (
    ("Iceberg", 1.55, 15, 21, 1.78, 2.15),
    ("Tomato", 0.52, 15, 21, 0.6, 0.73),
    ("Chicken", 1.34, 12, 21, 1.5, 1.81),
    ("Bread", 0.71, 12, 10, 0.8, 0.88),
    ("Corn", 1.21, 12, 10, 1.36, 1.5)
)


@mark.parametrize('name, cost, profit_percentage, tax_percentage, price_per_unit, expected_price_with_tax', params)
def test_calculate_prices(name, cost, profit_percentage, tax_percentage, price_per_unit, expected_price_with_tax):
    product = Product(name, cost, profit_percentage, tax_percentage)
    assert product.calculate_price_per_unit() == price_per_unit
    assert product.calculate_price_with_tax() == expected_price_with_tax


@fixture
def create_cart():
    iceberg = Product("Iceberg", 1.55, 15, 21)
    tomato = Product("Tomato", 0.52, 15, 21)
    chicken = Product("Chicken", 1.34, 12, 21)
    bread = Product("Bread", 0.71, 12, 10)
    corn = Product("Corn", 1.21, 12, 10)
    cart = ShoppingCart()
    cart.add_product(iceberg)
    cart.add_product(iceberg)
    cart.add_product(tomato)
    cart.add_product(chicken)
    cart.add_product(bread)
    cart.add_product(tomato)
    cart.add_product(chicken)
    cart.add_product(bread)
    cart.add_product(corn)
    cart.remove_product(iceberg)
    return cart


def test_display_cart(create_cart):
    result = create_cart.display_cart()
    assert result == [
        ("Product name", "Price with VAT", "Quantity"),
        ("Iceberg", 2.15, 1),
        ("Tomato", 1.46, 2),
        ("Chicken", 3.62, 2),
        ("Bread", 1.76, 2),
        ("Corn", 1.5, 1),
        ("total productos:", 8, "Total price:", 17.33)
    ]