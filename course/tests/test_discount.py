from course.src.class_1.discounts import calculate_discount


def test_with_discount():
    discount, total = calculate_discount(400)
    assert discount == 80.0
    assert total == 320.0


def test_total():
    total = calculate_discount(100)
    assert total == 100
