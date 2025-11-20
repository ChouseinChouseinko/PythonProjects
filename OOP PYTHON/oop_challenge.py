# oop_challenge
class BankAccount():
    def __init__(self, owner, balance):
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):

        self.balance = self.balance + amount

    def withdraw(self, amount):
        if self.balance >= amount:
            self.balance = self.balance - amount
        else:
            print("You don't have money to withdraw")


Efniki = BankAccount("Giorgos", 1894)
print(Efniki.owner)
print(Efniki.balance)
Efniki.deposit(250)
print(Efniki.balance)
Efniki.withdraw(144)
print(Efniki.balance)
