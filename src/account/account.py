class Account:
    def __init__(self, owner: object, balance = 0, transactions = []):
        self.owner = owner
        self.balance = balance
        self.transactions = transactions
    
    def check_balance(self) -> int:
        return self.balance

    def deposit(self, number: int):
        self.balance += number
        self.transactions.insert(0, ['deposit', number, self.balance])
    
    def withdraw(self, number: int):
        self.balance -= number
        self.transactions.insert(0, ['withdraw', number, self.balance])


    def show_transaction_history(self):
        if len(self.transactions) > 5:
            return self.transactions[:5]
        return self.transactions