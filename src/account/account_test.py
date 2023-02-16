from account.account import Account
from unittest import TestCase

class AccountTest(TestCase):

    newAccount = Account('Lewis')

    def test_account(self):
        assert self.newAccount.name == 'Lewis'

    def test_accountBalanceIsZeroOnCreation(self):
        assert self.newAccount.balance == 0

    def test_checkBalanceReturnsBalance(self):
        assert self.newAccount.check_balance() == 0

    def test_depositMoneyIncreasesBalance(self):
        self.newAccount.deposit(100)
        assert self.newAccount.check_balance() == 100