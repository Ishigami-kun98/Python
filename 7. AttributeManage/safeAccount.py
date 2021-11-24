import account
class safe_account(account.account):
    def __init__(self, initial_amount):
        self._amount = initial_amount
    def save_get(self):
        return self._amount
    def save_set(self, amount):
        assert amount > 0, 'Not admitted operation: the final balance ({0}) MUST be positive'.format(amount)
        self._amount = amount
    amount = property(save_get, save_set, None, "Managed balance against excessive withdrawals")
if __name__ == "__main__":
    a = safe_account(1000)
    print("The current balance is {0}".format(a.balance()))
    a.withdraw(100)
    a.deposit(750)
    print("The current balance is {0}".format(a.balance()))
    a.withdraw(3000)
    print("The current balance is {0}".format(a.balance()))