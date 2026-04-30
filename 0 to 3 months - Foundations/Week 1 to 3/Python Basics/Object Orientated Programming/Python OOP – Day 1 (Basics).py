# TASK 1 — Car class (guided, but no full solution)

# Create a class Car with:

# Requirements:
# brand
# model
# year

class Car:
    # This creates a blueprint called Car

    def __init__(self, brand, model, year):
        # __init__ runs automatically when you create an object
        # self = the specific object being created

        self.brand = brand  # store brand inside this object
        self.model = model  # store model inside this object
        self.year = year    # store year inside this object

    def describe(self):
        # method that belongs to the object
        # uses the object's stored data (self)
        
        print(f"{self.year} {self.brand} {self.model}")


# Create an object from the class (Car blueprint)
my_car = Car("Toyota", "Corolla", 2020)

# Call method on that specific object
my_car.describe()



# 1. Class: Student

# Each student must have:

# name
# grade (0–100)

class Student:
    def __init__(self, name, grade):
        self.name = name
        self.grade = grade

# Method: is_pass()
# returns True if grade ≥ 50
# otherwise False

    def is_pass(self):
        return self.grade >= 50
# Method: update_grade(new_grade)
# changes the student’s grade
# must reject invalid values (<0 or >100)

# If invalid:

# print "Invalid grade"

    def update_grade(self, new_grade):
        if new_grade > 0 and new_grade < 100:
            self.grade = new_grade
        else:
            print("Invalid grade")

# Method: get_status()

# Returns a message like:

# "Alex has passed"
# "Alex has failed"
        
    def get_status(self):
        if 50<= self.grade < 100:
            print(f"{self.name} has passed")

        else:
            print(f"{self.name} has failed")

# Test Cases (you must write)

# Create 2 students:

# one pass
# one fail

# Then:

# print status for both
# update one grade
# print status again

s1 = Student("Bryan", 67)
s2 = Student("Matt", 34)

# Initial status
s1.get_status()
s2.get_status()

s1.update_grade(34) # updating grade from 67 to 34

s1.get_status()

print(s1.is_pass())
print(s2.is_pass())

# ---------------------------------- sECOND HALF: Using OOP System in Real World ------------------------------ #

# Create a list of students

student_list = [
    {"student": "A",
    "score": 83},
    {"student": "B",
    "score": 24}, 
    {"student": "C",
    "score": 65}, 

]

# Loop through students

for i in student_list:
    student = i.get("student")
    print(student)

# Find the average grade

#Finding total score
total = 0

for i in student_list:
    total += i.get("score")

count = len(student_list)

average_grade = total / count

print(average_grade)

# ********************************************************************* CREATING A BankAccount Class ******************************************************************** #

# Step 1 – Create a Class

# Build a BankAccount class with:

# owner (string)
# balance (number)

class BankAccount:
    def __init__(self, owner, balance):
        self.owner = owner
        self.balance = balance

# Implementing a deposit and withdrawl method

    def deposit(self, amount):
        self.amount = amount
        self.balance += self.amount
        print(self.balance)

    def withdraw(self, amount):
        self.amount = amount
        if amount <= self.balance:
            self.balance -= self.amount
            print(self.balance)
        
        else:
            print("You cant withdraw a invalid amount from your balance")

# Adding a transfer fmethod where transfer money between accounts

    def transfer(self, amount, other_account):
        if amount <= self.balance:
            self.balance -= amount
            other_account.balance += amount

        else:
            print("Insufficient funds")        

# Step 3 – Create Objects

# Make 2 accounts:

# One with £100
# One with £50

b1 = BankAccount("Shaun", 100)
b2 = BankAccount("Chloe", 50)

# Step 4 – Simulate Activity

# Do things like:

# Deposit money
# Withdraw money
# Print final balances

b1.deposit(175)
b2.withdraw(55)


# ********************************************************************* DAY 2: CREATING A Transaction Class - Adding transaction lists to bank account ******************************************************************** #

class Transaction:
    def __init__(self, type, amount):
        self.type = type # "deposit", "withdraw", "transfer"
        self.amount = amount


class BankAccount:
    def __init__ (self, owner, balance):
        self.owner = owner
        self.balance = balance
        self.transaction = []   # store hsitory

# Log Transaction - Deposit or Withdraw

    def deposit(self, amount):
        self.balance += amount
        self.transaction.append(Transaction("deposit", amount))

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            self.transaction.append(Transaction("withdraw", amount))
        
        else:
            print("Insufficient funds")

        


    