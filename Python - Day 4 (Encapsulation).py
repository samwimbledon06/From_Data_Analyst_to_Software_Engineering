class BankAccount():
    def __init__ (self, owner, balance):
        self.owner = owner
        self._balance = balance   # make balance private -> internal (encapsulated)
        self.transactions = []      # store history

    @property # Adding a getter which makes methods read like a variable and makes access controlled
    def balance(self):
        return self._balance

    def deposit(self, amount):
        if amount <= 0:
            print("Deposit amount must be positive.")
        else:
            self._balance += amount
            self.transactions.append(f"Deposited: {amount}")

    def withdraw(self, amount):
        if amount <=0:
            print("Withdrwal amount must be positive.")
        elif amount > self._balance:
            print("Insufficient funds.")
        else:
            self._balance -= amount
            self.transactions.append(f"Withdrew: {amount}")

account = BankAccount("Alex", 1000)

account.deposit(500)
print(account.balance)
account.withdraw(200)
print(account.balance)

account.deposit(-100)  # Invalid deposit
account.withdraw(2000)  # Insufficient funds