from course.src.class_1.ejercicio4 import calculate_discount_products
from pytest import mark

params = (
    (20, 200, 400.0, 3600),
    (15, 200, 150.0, 2850.0),
    (9, 200, 0, 1800.0)
)


@mark.parametrize('amount, price, expected_discount, expected_total', params)
def test_amount_greater_20(amount, price, expected_discount, expected_total):
    discount, total = calculate_discount_products(amount, price)
    assert discount == expected_discount
    assert total == expected_total
