transacciones = []

class cuenta:

    def deposito(self, fecha, monto):
        transacciones.append((fecha,monto))

    def retiro(self, fecha, monto):
        transacciones.append((fecha, -monto))

    def extracto(self):
        balance=0
        print("Fecha || Monto || Balance")
        for fecha, monto in transacciones:
            balance += monto
            print(f"{fecha} || {monto} || {balance}")


extracto_cuenta = cuenta()
extracto_cuenta.deposito("01-07-2023", 5000)
extracto_cuenta.deposito("05-07-2023", 10000)
extracto_cuenta.retiro("30-07-2023", 2000)
extracto_cuenta.extracto()
