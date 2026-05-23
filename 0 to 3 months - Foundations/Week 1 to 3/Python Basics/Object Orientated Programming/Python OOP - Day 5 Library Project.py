# 🏗️ Project: Library System (OOP + Composition)

# 📦 Class 1: Book
# Attributes:
# title
# author
# is_borrowed (True/False)

class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.is_burrowed = False

# Methods:
# borrow()
# If already borrowed → reject request
# Otherwise mark as borrowed
    def borrow(self):
        if self.is_burrowed = True:
            print("Unable to burrow this book, this book is already burrowed")

        else:
            print("You have successfully burrowed this book")
            return self.is_burrowed == True
        
    # return_book()
    # Mark book as not borrowed

    def return_book(self):
        self.is_burrowed = False
        print("Book returned")

    # show_info()
    # Display title, author, status

    def show_info(self, title, author, status):
        status = "Burrowed" if self.is_burrowed else "Available" # by default self.is_burrowed is = False
        print(f"{self.title} / {self.author} / {self.is_burrowed}")


# 👤 Class 2: User
# Attributes:
# name
# borrowed_books (list of Book objects)
    
class User:
    def __init__(self, name):
        self.name = name
        self.burrowed_books = []

# borrow_book(book)
# Add book to user’s borrowed list
# Call book.borrow()

    def burrow_book(self, book):
        book.borrow()
        self.burrowed_books.append(book)

# return_book(book)
# Remove book from list
# Call book.return_book()

    def return_book(self, book):
        book.return_book()
        self.burrowed_books.remove(book)

# show_borrowed_books()
# Display all books user currently has
    
    def show_burrowed_books():
        for book in self.burrowed_books:
            print(book.title)

# 🏛️ Class 3: Library (Composition System)
# Goal

# A Library:

# stores books
# stores users
# manages borrowing + returning

# You must include:

# books → dictionary {title: Book}
# users → dictionary {name: User}

class Library:
    def __init__(self):
        self.books = {}
        self.users = {}

# 1. add_book(title, author)

# Must:

# create a Book object
# store it in self.books using title as key

    def add_book(self, title, author):
        book = Book(title, author)
        self.books[title] = book

# 2. add_user(name)

# Must:

# create a User object
# store it in self.users

    def add_user(self, name):
        user = User(name)
        self.users[name] = user

# 3. get_book(title)

# Must:

# return book from dictionary safely
# do NOT crash if missing

    def get_book(self, title):
        if self.books.get(title) is None:
            print("Book can not be found")
        else:
            return Book.title
        
# 4. get_user(name)

# Must:

# return user safely from dictionary

    def get_user(self, name):
        if self.users.get(name) is None:
            print("User can not be found")
        else:
            return User.name
    
# 5. borrow_book(user_name, book_title)

# Flow:

# find user
# find book
# if either missing → stop
# user borrows book

    def burrow_book(self, user_name, book_title):
        user = self.get_user(user_name)
        book = self.get_book(book_title)

        if user is None or book is None:
            print("Cannot find user's name")
            return
        
        else:
            self.burrow_book(book)

# 6. return_book(user_name, book_title)

# Flow:

# find user
# find book
# user returns book

    def return_book(self, user_name, book_title):
        user = self.get_user(user_name)
        book = self.get_book(book_title)

        if user is None or book is None:
            print("Cannot find user's name or book")
            return
        
        else:
            self.return_book(book_title)

# 7. show_all_books()

# Must:

# loop through all books
# show title + availability status

    def show_all_books(self):
        for title, book in self.books.items():
            status = "Burrowed" if book.is_burrowed else "Available"
            print(f"{title} / {status}") 




# -----------------------------------------------------------------------------------

# 🏦 Project: Shopping Cart System (OOP + Composition)

# You are building a basic e-commerce backend.

# 📦 Class 1: Product
# Attributes:
# name
# price
# stock

class Product:
    def __init__(self, name, price, stock):
        self.name = name
        self.price = price
        self.stock = stock

# Methods:
# reduce_stock(amount)
# If stock is enough → reduce it
# Otherwise reject    

    def reduce_stock(self, amount):
        if amount > self.stock:
            print("Not enough stock")
        
        else:
            self.stock -= amount
        
# restock(amount)
# Increase stock

    def restock(self, amount):
        self.stock += amount

# show_info()
# Print name, price, stock

    def show_info(self):
        print(f"{self.name} / {self.price} / {self.stock}")



