from course.src.class_1.numeros_pares import even_numbers


def test_even_number():
    result = even_numbers(4)
    assert result == "El número es par"


def test_odd_number():
    result = even_numbers(7)
    assert result == "El número es impar"
