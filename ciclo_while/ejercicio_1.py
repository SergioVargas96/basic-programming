while True:
    num = input("Digite un numero : ")
    if num.isdigit() and int(num) > 0:
        numero = int(num)
        print(f"El numero ingresado fue {numero}.")
        break
    else:
        print("Debe ingresar solo numeros enteros y positivos.")

        
