Library Management System

Overview of the project

This is a Python-based console application designed to digitize the management of a library system. The application provides a robust menu-driven interface that facilitates two distinct roles: Administrators and Users.

The system utilizes local data structures (dictionaries) to store book records and user information efficiently, allowing for real-time addition, searching, issuing, and returning of books without the need for an external database.

Features

The project is divided into two functional modules:

Administrative Module

    Authentication: Secure login system specifically for library administrators.

    Inventory Management: Add new books with detailed attributes including Serial Number, Name, Author, Copies, Price, and Shelf Number.

    Search Functionality: Locate books using various filters:

        Serial Number

        Book Name

        Author Name

        Price

        Shelf Number.

    Database Viewing: View specific subsets of books based on shelf location or price range.

User Module

    Session Management: Options to Login with existing credentials or Register as a new user.

    Book Issuance: Issue books by searching for Serial Number, Name, or Author.

    Return System: functionality to return books and validate the return against the issuer's name.

Technologies/tools used

    Programming Language: Python 3.x

    Interface: Command Line Interface (CLI)

    Data Structure: Python Dictionaries (Hash Maps) and Lists

Steps to install & run the project

    Prerequisites: Ensure Python is installed on your system.

    File Organization: Download the source code and ensure the following files are located in the same directory:

        main.py

        login.py

        modify_Book.py

        issue_return.py

        view.py

    Execution: Open a terminal or command prompt, navigate to the project directory, and execute the main script:
    Bash

    python main.py

Instructions for testing

To test the full functionality of the application, use the predefined credentials and sample data embedded in the source code.

1. Login Credentials

Role	Menu Selection	User ID	Password	Source
[Administrator	adm	2345	pass@pass	]
[User	user	2343	shayam]	

    Note: You may also select the register option in the User menu to create a temporary user ID and password for the current session.

2. Sample Data

The system initializes with three book records to facilitate immediate testing of Search and Issue features:
[Serial No.,	Book Name,	                   Author,	           Copies,	  Price, self]
[123,        Cosmos,                        Carl Sagan,         3,          500,      7]
[234,        A Brief History of Time,       Stephen Hawking,    4,         300,       8]
[345,        A Brief History of Humankind,  Yuval Noah Harari,  7,         450,       5]
Refer to main.py for the dictionary initialization
