class Account:
    def __init__(self, owner, balance = 0):
        self.owner = owner
        self.balance = balance
    
    def check_balance(self):
        return self.balance

    def deposit(self, number):
        self.balance += number
