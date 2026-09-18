#  Library Management System (CLI)

##  Overview
This project is a Command Line Interface (CLI) application designed to streamline the daily operations of a library. Built using Python, it demonstrates the practical application of Object-Oriented Programming (OOP) concepts such as **Inheritance**, **Encapsulation**, **Polymorphism**, and design patterns (like the **Singleton pattern** for database management). The system allows librarians to manage members, maintain a book catalog, and handle the issuing and returning of books with automatic inventory tracking and fine calculation.

## Features
The system is divided into three major functional modules:
* **Member Management:** Register new library members including librarian (using Polymorphism), view existing member details, and track their borrowing status.
* **Book Catalog & Inventory:** Add new books to the system, search for books by title, and track the number of available copies. It also supports "Reference" books (using Polymorphism) that cannot be borrowed.
* **Issue/Return & Fine Workflow:** Issue books to members, process returns, and automatically update inventory counts. The system automatically calculates late fines if a book is returned past the 14-day due date.
* **Input Validation:** Robust error handling ensures the application does not crash on invalid user inputs (e.g., entering text instead of numbers).

## Technologies and Tools Used
* **Programming Language:** Python 3.x
* **Database:** SQLite3 (using Python's built-in `sqlite3` library for local data persistence)
* **Version Control:** Git & GitHub
* **Testing:** Python `unittest` framework
* **Architecture:** Layered architecture (Presentation ➔ Business Logic  Data Layer)

## Project Structure
```text
LibraryManagementSystem/
│
├── src/
│   ├── db_manager.py      # Singleton pattern for database connection
│   └── library_system.py  # Main running system
│
├── src/
│   ├── __init__.py
│   ├── person.py          # Add memeber/ librarian function, using Inheritance
│   ├── book.py            # Add books function, using Polymorphism
│   ├── transaction.py     # Logic for issuing/returning and fine system
│   └── utils.py           # Helper functions for input validation
│   
│
── tests/
│   └── test_library.py    # Unit tests for core logic
│
── data/
│   └── library.db         # SQLite database
│
── main.py                 # The CLI menu entry point
── README.md
└── statement.md
```

## Running the Application

Open your terminal and run:

```bash
git clone https://github.com/RRRBuildology/library-management-system
cd library-management-system
```

Then in the terminal:
```terminal
python main.py
```

## Screenshots
1. Register New Member

! [Screenshot 1](screenshots/s1.png)

2. Add New Book to Catalog

! [Screenshot 2](screenshots/s2.png)

3. Search for a Book 

! [Screenshot 3](screenshots/s3.png)

4. Issue a Book to Member

! [Screenshot 4](screenshots/s4.png)

5. Return a Book

! [Screenshot 5](screenshots/s5.png)

6.View All Members and Exit 

! [Screenshot 6](screenshots/s6.png)
