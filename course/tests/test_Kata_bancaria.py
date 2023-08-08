from course.src.Kata.kata_bancaria_one import Transactions, Account

def test_create_transactions():
    transaction = Transactions("10/01/2012", 1000)
    assert transaction.date == "10/01/2012"
    assert transaction.amount == 1000


def test_deposit():
    account = Account()
    account.deposit("10/01/2012", 1000)
    assert len(account.full_transactions) == 1
    assert account.full_transactions[0].date == "10/01/2012"
    assert account.full_transactions[0].amount == 1000


def test_withdraw():
    account = Account()
    account.withdraw("11/01/2012", -500)
    assert account.full_transactions[0].date == "11/01/2012"
    assert account.full_transactions[0].amount == 500