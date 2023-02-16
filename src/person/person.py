class Person:
    def __init__(self, name, cash = 0):
        self.name = name
        self.cash = cash

    def deposit(self, number, account):
        self.cash -= number
        account.deposit(number)
   


