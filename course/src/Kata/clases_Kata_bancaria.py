class Transactions:
    def __init__(self, date, amount, account_number):
        self.date = date
        self.amount = amount
        self.account_number = account_number


class Account:
    def __init__(self, account_number):
        self.full_transactions = []
        self.account_number = account_number

    def deposit(self, date, amount):
        transaction = Transactions(date, amount, self.account_number)
        if amount <= 0:
            print("El monto ingresado no es correcto")
        else:
            self.full_transactions.append(transaction)

    def withdraw(self, date, amount):
        if amount <= 0 or amount > sum([transaction.amount for transaction in self.full_transactions]):
            print("No tiene fondos suficientes: ")
        else:
            transaction = Transactions(date, -amount, self.account_number)
            self.full_transactions.append(transaction)

    def print_statement(self):
        balance = 0
        result = [
            ('Date', 'Amount', 'Balance'),
        ]
        for transaction in reversed(self.full_transactions):
            balance += transaction.amount
            result.append(
                (transaction.date, transaction.amount, balance)
            )
        return result

    def get_balance(self):
        return sum(transaction.amount for transaction in self.full_transactions)


account = Account(account_number=1075297647)
account.deposit("2023-07-01", 1000)
account.withdraw("2023-07-02", 200)

print("Transacciones de la cuenta:")
for transaction in account.full_transactions:
    print(f"Fecha: {transaction.date}, Monto: {transaction.amount}, Número de Cuenta: {transaction.account_number}")
print(account.print_statement())
print("\n" + "="*50 + "\n")  # Línea divisoria

class TaxFourXMil(Account):
    def calculate_tax(self):
        total_balance = self.get_balance()
        tax_percentage = 0.04
        tax_amount = total_balance * tax_percentage
        return tax_amount


tax_account = TaxFourXMil(account_number=123456)
tax_account.deposit("2023-07-01", 6000)
tax_account.withdraw("2023-07-02", 1000)

print("Transacciones de la cuenta con impuesto:")
for transaction in tax_account.full_transactions:
    print(f"Fecha: {transaction.date}, Monto: {transaction.amount}, Número de Cuenta: {transaction.account_number}")
print(tax_account.print_statement())
tax_amount = tax_account.calculate_tax()
print("El impuesto es: ", tax_amount)

