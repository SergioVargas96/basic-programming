def even_numbers(number):
    if number % 2 == 0:
        return "El numero es par"
    elif number < 0:
        return "El numero es negativo"
    else:
        return "El numero es impar"


even_numbers(0)
