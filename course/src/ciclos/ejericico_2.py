# Pedir dos enteros positivos al usuario e imprimir la tabla de multiplicar del primer número hasta el segundo. 

def multiplication_numbers_1():
    while True:
        try:
            num1 = int(input("Ingrese el primer numero entero positivo: "))
            num2 = int(input("Ingrese el segundo numero entero positivo: "))
            if num1 < 0 and num2 < num1:
                raise ValueError()
            break
        except ValueError:
            print("Debe ingresar dos valores enteros y positivos.")

    number = num1
    print(f"Tabla de multiplicar del {num1} hasta el {num2}:")
    i = 1
    while i <= num2:
        resultado = number * i
        print(f"{number} x {i} = {resultado}")
        i += 1


def multiplication_numbers_2(num1, num2):
    while True:
        try:
            if num1 < 0 and num2 < 0:
                raise ValueError()
            break
        except ValueError:
            print("Debe ingresar dos valores enteros y positivos.")

    number = num1
    print(f"Tabla de multiplicar del {num1} hasta el {num2}:")
    i = 1
    while i <= num2:
        resultado = number * i
        print(f"{number} x {i} = {resultado}")
        i += 1