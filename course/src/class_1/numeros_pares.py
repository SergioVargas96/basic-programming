def even_numbers(number):
    if number % 2 == 0:
        return "El número es par"
    elif number < 0:
        return "El numero es negativo"
    else:
        return "El número es impar"


even_numbers(0)
