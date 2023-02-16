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