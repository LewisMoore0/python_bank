from account.account import Account
from person.person import Person
from unittest import TestCase

class AccountTest(TestCase):

    newPerson = Person('Lewis')
    newAccount = Account(newPerson)

    def test_accountBalanceIsZeroOnCreation(self):
        assert self.newAccount.balance == 0

    def test_checkBalanceReturnsBalance(self):
        assert self.newAccount.check_balance() == 0

    def test_depositMoneyIncreasesBalance(self):
        self.newAccount.deposit(100)
        assert self.newAccount.check_balance() == 100

    def test_accountHasPersonObjectOwnerOnCreation(self):
        assert self.newAccount.owner == self.newPerson

    def test_accountWithdrawDecreasesBalance(self):
        testPerson = Person('Lewis')
        testAccount = Account(testPerson)
        testAccount.deposit(100)
        testAccount.withdraw(50)

        assert testAccount.balance == 50

    def test_accountTransactionHistoryReturnsLastFiveTransactions(self):
        testPerson = Person('Lewis')
        testAccount = Account(testPerson)

        testAccount.deposit(100)
        testAccount.withdraw(50)
        testAccount.deposit(1000)
        testAccount.withdraw(500)
        testAccount.withdraw(250)

        assert testAccount.show_transaction_history() == [
            ['withdraw', 250, 300],
            ['withdraw', 500, 550],
            ['deposit', 1000, 1050],
            ['withdraw', 50, 50],
            ['deposit', 100, 100]
        ]

