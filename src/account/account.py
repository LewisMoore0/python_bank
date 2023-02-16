class Account:
    def __init__(self, name, owner, balance = 0):
        self.name = name
        self.owner = owner
        self.balance = balance
    
    def check_balance(self):
        return self.balance

    def deposit(self, number):
        self.balance += number
