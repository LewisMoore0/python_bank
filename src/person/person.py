class Person:
    def __init__(self, name: str, cash = 0):
        self.name = name
        self.cash = cash

    def deposit(self, number: int, account: object):
        self.cash -= number
        account.deposit(number)

    def withdraw(self, number: int, account: object):
        self.cash += number
        account.withdraw(number)
   


