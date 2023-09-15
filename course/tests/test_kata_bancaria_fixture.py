from course.src.Kata.kata_bancaria_two import Account
from pytest import mark, fixture


@fixture
def create_account():
    return Account()


params = (
    ("10/01/2012", 1000),
    ("10/01/2012", 5000),
    ("10/01/2012", 2000),
)


@mark.parametrize('date, amount', params)
def test_deposit(create_account, date, amount):
    create_account.deposit(date, amount)
    total = create_account.get_balance()
    assert total == amount


params = (
    ("10/01/2022", 2000, 1500, 2500),
    ("10/01/2022", 3000, 1000, 5000),
)


@mark.parametrize('date, amount, withdraw, expected_total', params)
def test_withdraw(create_account, date, amount, withdraw, expected_total):
    create_account.deposit(date, amount)
    create_account.deposit(date, amount)
    create_account.withdraw(date, withdraw)
    total = create_account.get_balance()
    assert total == expected_total


def test_deposit_multiple(create_account):
    create_account.deposit("10/01/2022", 2000)
    create_account.deposit("10/01/2022", 5000)
    create_account.deposit("10/01/2022", 3500)
    total_deposit = create_account.get_balance()
    assert total_deposit == 10500


def test_account_print_statement(create_account):
    create_account.deposit("10/01/2022", 1000)
    create_account.deposit("11/01/2022", 200)
    create_account.withdraw("12/01/2022", 300)
    result = create_account.print_statement()
    assert result == [
        ('Date', 'Amount', 'Balance'),
        ("12/01/2022", -300, 900),
        ("11/01/2022", 200, 1200),
        ("10/01/2022", 1000, 1000)
    ]
