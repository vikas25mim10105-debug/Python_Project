# Library Management System

Project Title

Library Management System (CLI)

Overview of the Project

This project is a console-based application written in Python designed to manage the day-to-day operations of a library. It features a dual-login system that separates administrative privileges from standard user functionalities. The system allows administrators to manage the book inventory (add, view, search) and allows users to register, issue, and return books. It utilizes Python data structures (dictionaries and lists) to handle data efficiently in runtime.

Features

The system is divided into two primary modules:

1. Administrative Module

    Secure Login: Access is restricted via ID and Password authentication.

    Add Books: Admins can add new books with details including Serial Number, Name, Author, Copies, Price, and Shelf Number.

    Search Books: Advanced search functionality allowing lookups by:

        Serial Number

        Book Name

        Author Name

        Price

        Shelf ("Self") Number

    View Inventory: Admins can filter views by Shelf Number or a specific Price Range.

2. User Module

    Registration & Login: New users can register with a numeric username and password, or log in with existing credentials.

    Issue Books: Users can issue books by searching for the Serial Number, Name, or Author. The system tracks who issued the book.

    Return Books: A simple interface for users to return borrowed books.

Technologies/Tools Used

    Programming Language: Python 3.x

    Interface: Command Line Interface (CLI) / Console

    Data Storage: Python Dictionaries and Lists (In-memory storage)

Steps to Install & Run the Project

    Prerequisites: Ensure Python (version 3.0 or higher) is installed on your system.

    Download Files: Ensure all the following project files are in the same folder:

        main.py

        login.py

        view.py

        modify_Book.py

        issue_return.py

    Run the Application: Open your terminal or command prompt, navigate to the project folder, and run the following command:
    Bash

    python main.py

Instructions for Testing

Follow these steps to test the various features of the application:

1. Administrative Testing:

    Run the program and type adm for Administrative Login.

    Credentials: Use the hardcoded admin credentials found in the source code:

        ID: 2345

        Password: pass@pass

    Once logged in, try adding a book (type add) or viewing books (type view).

2. User Testing:

    Run the program and type user for User Login.

    Registration: Type register to create a new account (Use numbers for the username).

    Login: Type login. You can use your newly registered account or the default test account:

        ID: 2343

        Password: shayam

    Select issue to borrow a book (e.g., enter Serial Number 123 for "Cosmos").
