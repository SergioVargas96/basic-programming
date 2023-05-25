# Pedir un número entero positivo al usuario. Si el dato que el usuario ingresa es inválido, volver a pedirlo hasta que
# sea válido

# def number_positive(parametro):
#     while True:
#         num = parametro
#         if not num.isdigit():
#             print(f"{num} Numero no es un numero entero")
#             break
#         elif int(num) <=0:
#             print(f"El Numero {num} no es es positivo")
#             break
#         else:
#             print(f"El numero ingresado es {num}")
#             break
#
# number_positive("0")

def number_positive_1(parametro):
    while True:
        num = parametro
        if num > 0:
            print(f"El numero ingresado es: {num} ")
            break
        elif num <= 0:
            print(f"{num} no es un numero positivo: ")
            break

number_positive_1(5)