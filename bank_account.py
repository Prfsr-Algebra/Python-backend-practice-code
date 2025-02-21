class Insufficient_error(Exception):
    def __init__(self, amount):
        self.amount = amount
    def __str__(self):
        return f"sorry! you don't have up to {self.amount}"
class BankAccount:
    def __init__(self, balance):
        self.balance = balance
    def deposit(self, amount):
        self.balance += amount
        print(f"your new balance is {self.balance}")
    def withdraw(self, amount):
        self.balance -= amount
        print(f"your new balance is {self.balance}")
    def display_balance(self):
        print(f"your balance is {self.balance}")
        return self.balance
    def show_balance(self):
        return self.balance
