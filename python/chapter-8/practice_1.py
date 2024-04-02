class Account:
    def __init__(self, balance):
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        self.balance -= amount

    def get_balance(self):
        return self.balance

    def __str__(self):
        return f'Account balance: {self.balance}'



a1 = Account(1000)
print(a1.get_balance())
a1.deposit(500)
print(a1.get_balance())
a1.withdraw(200)
print(a1.get_balance())
print(a1)
# Output:
