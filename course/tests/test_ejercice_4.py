from course.src.class_1.ejercicio4 import calculate_discount_products


def test_amount_greater_20():
    discount, total = calculate_discount_products(20, 200)
    assert discount == 400.0
    assert total == 3600.0


def test_amount_greater_10_lesser_20():
    discount, total = calculate_discount_products(15, 200)
    assert discount == 150.0
    assert total == 2850.0


def test_amount_lesser_10():
    total = calculate_discount_products(9, 200)
    assert total == 1800.0
