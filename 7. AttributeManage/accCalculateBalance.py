class account_calculated_balance:
    def __init__(self, initial_amount):
        self._deposits = initial_amount
        self._withdrawals = 0
    def deposit(self, amount):
        self._deposits += amount
    def withdraw(self, amount):
        self._withdrawals += amount
    def calculated_balance(self):
        return self._deposits - self._withdrawals
    def zeroing_balance(self):
        self._deposits = 0
        self._withdrawals = 0
    balance = property(calculated_balance, None, zeroing_balance, "Calculate Balance")

if __name__ == "__main__":
    a = account_calculated_balance(1000)
    print("The current balance is {0}".format(a.balance))
    a.withdraw(100)
    a.deposit(750)
    print("The current balance is {0}".format(a.balance))
    a.withdraw(3000)
    print("The current balance is {0}".format(a.balance))
    del a.balance
    print("The current balance is {0}".format(a.balance))
    a.deposit(750)
    print("The current balance is {0}".format(a.balance))