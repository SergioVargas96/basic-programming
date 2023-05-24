# Pedir dos enteros positivos al usuario e imprimir la tabla de multiplicar del primer número hasta el segundo. 

while True:
    try:
        num1 = int(input("Ingrese el primer numero entero positivo: "))
        num2 = int(input("Ingrese el segundo numero entero positivo: "))
        if num1 < 0 and num2 < num1:
            raise ValueError()
        break
    except ValueError:
        print("Debe ingresar dos valores enteros y positivos.")

while True:
    number = num1
    print(f"Tabla de multiplicar del {num1} hasta el {num2}:")
    i = 1
    while i <= num2:
        resultado = number * i
        print(f"{number} x {i} = {resultado}")
        i += 1
    break