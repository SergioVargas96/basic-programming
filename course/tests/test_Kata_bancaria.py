from course.src.Kata.kata_bancaria_two import Transactions, Account
from pytest import mark

params = (
    ("10/01/2012", 1000),
    ("10/01/2012", 5000),
    ("10/01/2012", 2000),
)

@mark.parametrize('date, amount', params)
def test_deposit(date, amount):
    account = Account()
    account.deposit(date, amount)
    assert len(account.full_transactions) == 1
    assert account.full_transactions[0].date == date
    assert account.full_transactions[0].amount == amount

def test_withdraw():
    account = Account()
    account.deposit("10/01/2022", 2000)
    account.deposit("10/01/2022", 2000)
    account.withdraw("10/01/2022", 1500)
    total = account.get_balance()
    assert total == 2500

def test_deposit_multiple():
    account = Account()
    account.deposit("10/01/2022", 2000)
    account.deposit("10/01/2022", 5000)
    account.deposit("10/01/2022", 3500)
    total_deposit = account.get_balance()
    assert total_deposit == 10500

def test_account_print_statement():
    account = Account()
    account.deposit("10/01/2022", 1000)
    account.deposit("11/01/2022", 200)
    account.withdraw("12/01/2022", 300)
    result = account.print_statement()
    assert result == [
        ('Date', 'Amount', 'Balance'),
        ("12/01/2022", -300, 900),
        ("11/01/2022", 200, 1200),
        ("10/01/2022", 1000, 1000)
    ]
