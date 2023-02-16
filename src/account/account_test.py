from account.account import Account
from unittest import TestCase

class AccountTest(TestCase):
    def test_account(self):
        newAccount = Account('Lewis')
        assert newAccount.name == 'Lewis'
