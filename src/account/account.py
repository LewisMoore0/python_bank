class Account:
    def __init__(self, owner: object, balance = 0):
        self.owner = owner
        self.balance = balance
    
    def check_balance(self) -> int:
        return self.balance

    def deposit(self, number: int):
        self.balance += number
    
    def withdraw(self, number: int):
        self.balance -= number
