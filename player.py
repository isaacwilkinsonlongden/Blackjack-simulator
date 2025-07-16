class Player:
    def __init__(self, name, balance=100):
        self.name = name
        self.balance = balance

    def adjust_balance(self, amount):
        self.balance += amount
        


