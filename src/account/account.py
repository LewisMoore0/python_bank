class Account:
    def __init__(self, name, balance = 0):
        self.name = name
        self.balance = balance
    
    def check_balance(self):
        return self.balance
