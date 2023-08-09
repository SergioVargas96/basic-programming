class Transactions:

    def __init__(self, date, amount):
        self.date = date
        self.amount = amount


class Account:

    def __init__(self):
        self.full_transactions = []

    def deposit(self, date, amount):
        movement = Transactions(date, amount)
        if amount <= 0:
            print("El monto ingresado no es correcto")
        else:
            self.full_transactions.append(movement)


    def withdraw(self, date, amount):
        if amount <= 0 or amount > sum([movement.amount for movement in self.full_transactions]):
            print("No tiene fondos suficientes: ")
        else:
            movement = Transactions(date, -amount)
            self.full_transactions.append(movement)


    def print_statement(self):
        balance = 0
        print("Date || Amount || Balance")
        for movement in reversed(self.full_transactions):
            balance += movement.amount
            print(f"{movement.date} || {movement.amount} || {balance}")
