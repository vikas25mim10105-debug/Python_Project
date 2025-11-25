Library Management System (LMS)

1. Overview of the Project

This project is a modular, console-based application designed to simulate the digital management of a library's daily operations. It acts as a central database for managing book records and user transactions. The system is built on Modular Programming principles, separating logic into five distinct Python files (main.py, login.py, modify_Book.py, issue_return.py, view.py) to ensure code readability and maintainability.

The application features a Dual-Login System:

    Administrative Module: For librarians to manage the inventory (Add, Search, View).

    User Module: For students/patrons to register, log in, and perform book transactions (Issue, Return).

Data Persistence is handled via In-Memory Data Structures (Python Dictionaries and Lists), allowing for fast runtime operations without the need for an external SQL database.

2. Features

The system provides granular control over library operations through the following features:

 Administrative Features

    Secure Authentication: The system enforces security with a hardcoded Admin ID (2345) and Password (pass@pass). It includes a security counter that locks the login attempt after 4 failed tries.

    Inventory Management (Add Books): Admins can batch-add books. For every book, the system captures detailed metadata:

        Serial Number (Unique ID)

        Book Name

        Author Name

        Number of Copies

        Price

        Shelf Number ("Self no")

    Advanced Search Engine: Admins can locate books using five specific criteria:

        By Serial Number (ser)

        By Book Name (name)

        By Author (author)

        By Price (price)

        By Shelf Location (self)

    Filtered Data Viewing:

        View by Shelf: Displays all books located on a specific library shelf.

        View by Price Range: Displays books that fall within a user-defined price bracket (Lower Limit to Upper Limit).

 User Features

    User Registration: New users can sign up by creating a numeric User Name and a Password. This is stored temporarily in the runtime session.

    Book Issuing System: Users can search for and issue books. The system displays a confirmation message: "You have to return it in 1 week either fine will be charged". Issuing can be done by:

        Serial Number

        Book Name

        Author Name

    Book Return System: A validation mechanism checks the username against the user who issued the book before confirming the return.

3. Technologies/Tools Used

    Primary Language: Python 3.x

    User Interface: Command Line Interface (CLI)

    Key Python Concepts Implemented:

        Data Structures: Heavily utilizes Dictionaries ({key: value}) to map Book IDs to their details and Lists ([]) to store book attributes.

        Modular Programming: Logic is split across login, modify_Book, issue_return, and view modules.

        Control Flow: Uses while True loops for continuous menus and for loops for login attempt counters.

        Exception Handling: Input validation for integer fields (Serial No, Price).

4. Steps to Install & Run the Project

    Prerequisites:

        Install Python (Version 3.6 or higher recommended).

    File Setup:

        Create a folder named Library_System.

        Download and place the following 5 files inside that folder:

            main.py (The entry point)

            login.py (Authentication logic)

            modify_Book.py (Add/Search logic)

            view.py (Display logic)

            issue_return.py (Transaction logic)

    Execution:

        Open Terminal (Mac/Linux) or Command Prompt (Windows).

        Navigate to the folder: cd path/to/Library_System

        Run the application:
        Bash

        python main.py

5. Instructions for Testing

Use the following test data and steps to verify all functionalities:

Scenario A: Admin Workflow

    Run main.py.

    Enter adm when asked for login type.

    Login: Enter ID 2345 and Password pass@pass.

    Action - Add Book:

        Type add.

        Enter number of books: 1.

        Enter details: Serial 999, Name PythonBasics, Author Guido, Copies 5, Price 500, Shelf 10.

    Action - View:

        Type view, then select price.

        Enter Upper Limit 600, Lower Limit 400.

        Result: You should see the "PythonBasics" book you just added.

Scenario B: User Workflow

    Run main.py (or restart if ended).

    Enter user when asked for login type.

    Login: Use the pre-registered test account:

        ID: 2343

        Password: shayam

    Action - Issue Book:

        Type issue.

        Enter Name Shayam.

        Choose ser (Serial Number) and enter 123.

        Result: System confirms "Cosmos book got issued to Shayam".

    Action - Return Book:

        Type return.

        Enter Name Shayam.

        Result: System confirms "Book returned".
