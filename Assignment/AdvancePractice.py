# Python Intermediate to Advanced Assignment
# Assignment: Implement a Library Management System
# In this assignment, you will build a simple library management system using Python. The system should handle books, users, and lending functionalities. You will need to use object-oriented programming (OOP), decorators, generators, and file handling.

# Task 1: Define the Book Class
# Create a class called Book with the following attributes:

# title (string)
# author (string)
# isbn (string, unique for each book)
# available (boolean, default is True)
# Add a method __str__ that returns a string representation of the book (title, author, and ISBN).

# Task 2: Define the User Class
# Create a class called User with the following attributes:

# name (string)
# user_id (integer, unique for each user)
# borrowed_books (a list to store books borrowed by the user)
# Add a method borrow_book that takes a Book object and adds it to the user's borrowed_books list (if the book is available). Update the book's availability accordingly.

# Add a method return_book that takes a Book object and removes it from the user's borrowed_books list. Update the book's availability.

# Task 3: Create a Library Class
# Define a Library class with the following:

# books (a list to store all books in the library)
# users (a list to store all users registered in the library)
# Add methods to:

# Add a book to the library.
# Register a user to the library.
# Display available books.
# Borrow a book: This method should check if the book is available and assign it to the user.
# Return a book.
# Implement a generator in the Library class to list all books borrowed by a specific user.

# Task 4: Implement a Decorator
# Create a decorator @log_activity that logs every time a book is borrowed or returned. The log should be written to a text file (library_log.txt) with a timestamp, book title, and the action performed.
# Task 5: Handle File Operations
# Write the details of the books and users to a text file called library_data.txt whenever the system is closed.
# On system start, read the library_data.txt file to load books and users into the system.
# Task 6: Add Exception Handling
# Add appropriate exception handling for situations such as:
# Trying to borrow a book that is not available.
# Trying to return a book that was not borrowed by the user.
# Task 7: (Bonus) Command-Line Interface
# If you'd like to take it further, create a command-line interface (CLI) that allows the user to interact with the system by typing commands such as:

# add_book
# register_user
# borrow
# return
# show_available_books
# Submission Guidelines:
# Ensure the code is well-structured and follows good programming practices.
# Comment your code to explain important sections and logic.
# Submit the code along with the library_log.txt and library_data.txt files if applicable.
# Key Concepts Covered:
# Object-Oriented Programming
# Decorators
# Generators
# File Handling
# Exception Handling
# This project will help you practice essential Python skills needed for real-world applications while building something practical and scalable.

# Let me know if you'd like any further clarification or examples on how to implement any part of this assignment!