class account:
    def __init__(self, initial_amount):
        self.amount = initial_amount
    def balance(self):
        return self.amount
    def withdraw(self, amount):
        self.amount -= amount
    def deposit(self, amount):
        self.amount += amount;
    
if __name__ == "__main__":
    a = account(1000)
    print("The current balance is {0}".format(a.balance()))
    a.withdraw(100)
    a.deposit(750)
    print("The current balance is {0}".format(a.balance()))
    a.withdraw(3000)
    print("The current balance is {0}".format(a.balance()))