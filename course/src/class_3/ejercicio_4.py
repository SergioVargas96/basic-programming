num_1 = int(input("DIGITE EL PRIMER NUMERO: "))
num_2 = int(input("DIGITE EL SEGUNDO NUMERO: "))

print("Sus numeros son: ", num_1 ," , ",num_2)
print("Menu de operaciones: (1)Para multiplicar, (2)Para Sumar, (3)Para restar, (4)para dividir")
operation = int(input("Digite la operación que desea realizar: "))

if operation == 1:
    resultado = num_1 * num_2
    print("El resultado de la multiplicación es: " , resultado)
elif operation == 2:
    resultado = num_1 + num_2
    print("El resultado de la suma es: " , resultado)
elif operation == 3:
    resultado = num_1 - num_2
    print("El resultado de la resta es: " , resultado)
elif operation == 4:
    resultado = num_1 / num_2
    print("El resultado de la división es: " , resultado)

else:
    print("No ha seleccionado una opción valida !!")