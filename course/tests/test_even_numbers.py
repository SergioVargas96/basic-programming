from course.src.class_1.numeros_pares import even_numbers
from pytest import mark

params = (
    (4, "El numero es par"),
    (7, "El numero es impar"),
    (-7, "El numero es negativo"),
    (0, "El numero es par")
)
@mark.parametrize('number, expected_result', params)
def test_even_number(number, expected_result):
    result = even_numbers(number)
    assert result == expected_result