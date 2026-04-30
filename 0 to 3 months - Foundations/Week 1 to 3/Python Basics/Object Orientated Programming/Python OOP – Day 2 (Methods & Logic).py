# ********************************************************************* DAY 2: CREATING A Transaction Class - Adding transaction lists to bank account ******************************************************************** #

class Transaction:
    def __init__(self, type, amount):
        self.type = type # "deposit", "withdraw", "transfer"
        self.amount = amount


class BankAccount:
    def __init__ (self, owner, balance):
        self.owner = owner
        self.balance = balance
        self.transactions = []   # store history

# Log Transaction - Deposit or Withdraw

    def deposit(self, amount):
        self.balance += amount
        self.transactions.append(Transaction("deposit", amount))

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            self.transactions.append(Transaction("withdraw", amount))
        else:
            print("Insufficient funds")

    def transfer(self, amount, other_account):
        if amount <= self.balance:
            self.balance -= amount
            other_account.balance += amount

            self.transactions.append(Transaction("transfer out", amount))
            other_account.transactions.append(Transaction("transfer in", amount))
        else:
            print("Insufficient funds")


# Add a Method to View History

    def print_transaction(self):
        for t in self.transactions:
            print(t.type, t.amount)

# ****************************** Updating transaction class - ADDING TIMESTAMPS ************************** #

from datetime import datetime

class Transaction:
    def __init__(self, type, amount, balance_after):
        self.type = type
        self.amount = amount
        self.balance_after = balance_after
        # Adding ability to record current time to Transaction 
        self.timestap = datetime.now()

class BankAccount:
    def __init__ (self, owner, balance):
        self.owner = owner
        self.balance = balance
        self.transactions = []   # store history

# ADDING self.balance feature after functions 

    def deposit(self, amount):
        self.balance += amount
        self.transactions.append(Transaction("deposit", amount, self.balance))

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            self.transactions.append(Transaction("withdraw", amount, self.balance))

    def transfer(self, amount, other_account):
        if amount <= self.balance:
            self.balance -= amount
            other_account.balance += amount

            self.transactions.append(
                Transaction("transfer out", amount, self.balance)
            )

            other_account.transactions.append(
                Transaction("transfer in", amount, other_account.balance)
            )
        else:
            print("Insufficient funds")

# Printing history properly --> UPDATING

    def print_transactions(self):

        for t in self.transactions:
            print(
                f"{t.timestamp} | {t.type} | {t.amount} | Balance: £{t.balance_after}"
            )    

# Last 5 transactions

    def mini_statement(self):
        for t in self.transactions[-5:]:
            print(
                f"{t.timestamp} | {t.type} | {t.amount} | Balance: £{t.balance_after}"
            ) 