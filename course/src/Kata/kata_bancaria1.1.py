class transactions:
    def __init__(self, date, amount):
        self.date = date
        self.amount = amount


class account:
    def __init__(self):
        self.full_transactions = []

    def deposit(self, date, amount):
        movement = transactions(date, amount)
        self.full_transactions.append(movement)

    def withdraw(self, date, amount):
        movement = transactions(date, -amount)
        self.full_transactions.append(movement)

    def print_statement(self):
        balance = 0
        print("Date || Amount || Balance")
        for movement in reversed(self.full_transactions):
            balance += movement.amount
            print(f"{movement.date} || {movement.amount} || {balance}")


cuenta_bancaria = account()
cuenta_bancaria.deposit("10/01/2012", 1000)
cuenta_bancaria.deposit("13/01/2012", 2000)
cuenta_bancaria.withdraw("14/01/2012", 500)
cuenta_bancaria.print_statement()
