from unittest import TestCase
from person.person import Person
from account.account import Account

class PersonTest(TestCase):

    person = Person('Lewis')
    account = Account(person)

    def test_person(self):
        assert self.person.name == 'Lewis'

    def test_personHasCashAttribute0asDefault(self):
        assert self.person.cash == 0

    def test_personDepositTakesAwayFromCash(self):
        testPerson = Person('Lewis', 150)
        testPerson.deposit(100, self.account) 
        assert testPerson.cash == 50
    
    def test_personDepositIncreasesTargetAccountBalance(self):
        testPerson = Person('Lewis', 200)
        testAccount = Account(testPerson)

        testPerson.deposit(100, testAccount)
        assert testAccount.balance == 100

    def test_personWithdrawIncreasesCash(self):
        testPerson = Person('Lewis', 200)
        testAccount = Account(testPerson)

        testPerson.deposit(100, testAccount)
        testPerson.withdraw(50, testAccount)

        assert testPerson.cash == 150

    def test_personWithdrawDecreasesAccountBalance(self):
        testPerson = Person('Lewis', 200)
        testAccount = Account(testPerson)

        testPerson.deposit(100, testAccount)
        testPerson.withdraw(50, testAccount)

        assert testAccount.balance == 50
