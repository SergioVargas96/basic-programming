from course.src.Kata.kata_bancaria_two import Transactions, Account
from pytest import mark

params = (
    ("10/01/2012", 1000),
    ("10/02/2012", 5000),
    ("10/01/2012", 2000),
)
@mark.parametrize('date, amount', params)
def test_create_transactions(date, amount):
    transaction = Transactions(date, amount)
    assert transaction.date == date
    assert transaction.amount == amount

@mark.parametrize('date, amount', params)
def test_deposit(date, amount):
    account = Account()
    account.deposit(date, amount)
    assert len(account.full_transactions) == 1
    assert account.full_transactions[0].date == date
    assert account.full_transactions[0].amount == amount

def test_deposit_multiple():
    account = Account()
    account.deposit("10/01/2022", 2000)
    account.deposit("10/01/2022", 5000)
    account.deposit("10/01/2022", 3500)
    assert len(account.full_transactions) == 3
    total_deposit = sum(movement.amount for movement in account.full_transactions)
    assert total_deposit == 10500

def test_withdraw():
    account = Account()
    account.deposit("10/01/2022", 2000)
    account.deposit("10/01/2022", 2000)
    account.withdraw("10/01/2022", 1500)
    assert len(account.full_transactions) == 3
    assert account.full_transactions[2].amount == -1500
    total = sum(movement.amount for movement in account.full_transactions)
    assert total == 2500


