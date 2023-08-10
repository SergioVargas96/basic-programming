class Transactions:

    def __init__(self, date, amount):
        self.date = date
        self.amount = amount


class Account:

    def __init__(self):
        self.full_transactions = []

    def deposit(self, date, amount):
        transaction = Transactions(date, amount)
        if amount <= 0:
            print("El monto ingresado no es correcto")
        else:
            self.full_transactions.append(transaction)


    def withdraw(self, date, amount):
        if amount <= 0 or amount > sum([transaction.amount for transaction in self.full_transactions]):
            print("No tiene fondos suficientes: ")
        else:
            transaction = Transactions(date, -amount)
            self.full_transactions.append(transaction)


    def print_statement(self):
        balance = self.get_balance()
        result = [
            ('Date', 'Amount', 'Balance'),
        ]
        for transaction in reversed(self.full_transactions):
            result.append(
                (transaction.date, transaction.amount, balance)
            )
            balance -= transaction.amount
        return result

    def get_balance(self):
        return sum(transaction.amount for transaction in self.full_transactions)
