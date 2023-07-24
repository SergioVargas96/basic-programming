import datetime
account = {
    'transactions': []
}

transaction = {
    'date': None,
    'amount': None
}


def deposit(amount):
    transaction = {
        'date': datetime.date.today(),
        'amount': amount
    }
    account['transactions'].append(transaction)
    return transaction


def withdraw(amount):
    transaction = {
        'date':datetime.date.today(),
        'amount': - amount
    }
    account['transactions'].append(transaction)
    return transaction

def print_statement():
    balance = 0
    for transaction in account['transactions']:
        print(transaction)

deposit(5000)
deposit(6000)
withdraw(4000)
print_statement()
