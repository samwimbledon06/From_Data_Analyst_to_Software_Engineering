# 🏦 Banking System V3 – Brief
# 🔹 Base Class: Account

# Must have:

# owner
# balance
# transactions (list)

# Methods:

# deposit(amount)
# withdraw(amount)
# transfer(amount, other_account)
# show_balance()
# 🔹 Task 1: SavingsAccount
# Inherits from Account
# Add: interest_rate
# Method: add_interest()
# calculate interest
# add to balance
# store transaction: "Interest added X"
# 🔹 Task 2: CurrentAccount
# Inherits from Account
# Add: overdraft_limit
# Override withdraw(amount):
# allow balance to go below 0 up to overdraft
# block if limit exceeded
# store transaction
# 🔹 Task 3: PremiumAccount
# Inherits from Account
# Modify deposit(amount):
# still run normal deposit logic
# add 1% bonus
# store transaction: "Bonus added X"
# 🔹 Task 4: Transfer System

# Inside Account:

# transfer(amount, other_account)
# move money between accounts
# update BOTH accounts’ transactions

# -------------------------
# Base Class
# -------------------------
class Account:
    def __init__(self, owner, balance):
        self.owner = owner              # store account owner's name
        self.balance = balance          # store balance
        self.transactions = []          # list to track all transactions

    def deposit(self, amount):
        self.balance += amount
        self.transactions.append(f"Deposited £{amount}")

    def withdraw(self, amount):
        if amount > self.balance:
            print("Not enough money")
        else:
            self.balance -= amount
            self.transactions.append(f"Withdrew £{amount}")

    def transfer(self, amount, other_account):
        # transfer money between accounts
        if amount > self.balance:
            print("Not enough money")
        else:
            self.balance -= amount
            other_account.balance += amount

            # log both sides of transaction
            self.transactions.append(f"Sent £{amount} to {other_account.owner}")
            other_account.transactions.append(f"Received £{amount} from {self.owner}")

    def show_balance(self):
        print(f"{self.owner} balance: £{self.balance}")

    def show_transactions(self):
        print(f"\n{self.owner}'s Transactions:")
        for t in self.transactions:
            print("-", t)


# -------------------------
# Savings Account
# -------------------------
class SavingsAccount(Account):
    def __init__(self, owner, balance, interest_rate):
        # use parent setup (owner, balance, transactions)
        super().__init__(owner, balance)
        self.interest_rate = interest_rate  # extra attribute

    def add_interest(self):
        # calculate interest and add to balance
        interest = self.balance * self.interest_rate
        self.balance += interest
        self.transactions.append(f"Interest added £{interest}")


# -------------------------
# Current Account
# -------------------------
class CurrentAccount(Account):
    def __init__(self, owner, balance, overdraft_limit):
        super().__init__(owner, balance)
        self.overdraft_limit = overdraft_limit

    def withdraw(self, amount):
        # override parent withdraw (different rules)
        if amount > self.balance + self.overdraft_limit:
            print("Overdraft limit exceeded")
        else:
            self.balance -= amount
            self.transactions.append(f"Withdrew £{amount}")


# -------------------------
# Premium Account
# -------------------------
class PremiumAccount(Account):
    def deposit(self, amount):
        # extend parent method (use original + extra)
        super().deposit(amount)

        # add 1% bonus
        bonus = amount * 0.01
        self.balance += bonus
        self.transactions.append(f"Bonus added £{bonus}")


# -------------------------
# Testing the system
# -------------------------
s = SavingsAccount("Sam", 1000, 0.05)
c = CurrentAccount("Alex", 500, 200)
p = PremiumAccount("Jamie", 800)

# perform actions
s.add_interest()        # adds interest
c.withdraw(600)         # uses overdraft
p.deposit(100)          # adds bonus

s.transfer(200, c)      # transfer money

# show results
s.show_balance()
c.show_balance()
p.show_balance()

# show transaction history
s.show_transactions()
c.show_transactions()
p.show_transactions()

