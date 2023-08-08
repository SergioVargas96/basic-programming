import datetime

transacciones = []


def deposit():
    while True:
        consulta = input("¿Desea ingresar un depósito? (S/N): ")
        if not consulta.isalpha() or consulta.upper() != 'S' and consulta.upper() != 'N':
            print("El valor ingresado no es correcto")
        if consulta.upper() == 'N':
            break
        elif consulta.lower() == 's':
            monto = float(input("Ingrese monto a depositar: "))
            if monto <= 0:
                print("El monto ingresado no es correcto")
            else:
                date = datetime.datetime.now().strftime("%d/%m/%Y")
                transacciones.append((date, monto))
                print(f"Se ha depositado {monto} correctamente.")
    withdraw()


def withdraw():
    while True:
        consulta_retiro = input("¿Desea hacer un retiro? (s/n): ")
        if not consulta_retiro.isalpha() or consulta_retiro.upper() != 'S' and consulta_retiro.upper() != 'N':
            print("El valor ingresado no es correcto")
        if consulta_retiro.lower() == 'n':
            print_statement()
            break
        elif consulta_retiro.lower() == 's':
            retiro = float(input("Ingrese la cantidad del retiro: "))
            if retiro <= 0 or retiro > sum([monto for date, monto in transacciones]):
                print("Digito un valor incorrecto o no tiene fondos suficiente: ")
            else:
                date = datetime.datetime.now().strftime("%d/%m/%Y")
                transacciones.append((date, - retiro))
                print(f"Se ha retirado ${retiro} correctamente.")


def print_statement():
    balance = 0
    print("Fecha\t|| Monto\t|| Balance")
    for fecha, monto in reversed(transacciones):
        balance += monto
        print(f"{fecha}|| {monto}|| {balance}")


deposit()