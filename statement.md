# Project Statement

## Problem Statement
Traditional or manual library management systems—often relying on paper records, spreadsheets, or disjointed software—are highly prone to human error. These inefficiencies lead to lost inventory, inaccurate tracking of available book copies, difficulty in managing member borrowing histories, and inconsistent calculation of late fines. There is a clear need for a streamlined, automated, and reliable system to handle these core library operations efficiently.

## Scope of the Project
This project focuses on designing and implementing a lightweight, Command Line Interface (CLI) backend system to handle the core operations of a library. The scope includes:
* **User Management:** Creating and managing library member profiles.
* **Inventory Management:** Adding, searching, and categorizing books (including standard and reference books).
* **Transaction Processing:** Handling the issuing and returning of books, updating inventory counts in real-time, and automatically calculating late fines based on a 14-day borrowing period.
* **Data Persistence:** Utilizing a local SQLite database to ensure data is saved and retrievable across sessions.


## Target Users
* **Librarians / Library Staff:** The primary users who will interact with the system daily to register members, update the book catalog, and process book issues and returns.
* **System Administrators:** Technical users responsible for maintaining the database integrity, managing backups, and overseeing the system's backend logic.

## High-Level Features
* **Persistent Data Storage:** Uses SQLite to securely store member, book, and transaction data locally.
* **Object-Oriented Architecture:** Built using Python OOP principles (Inheritance, Encapsulation, Polymorphism, and Singleton patterns) to ensure the code is modular, scalable, and easy to maintain.
* **Smart Inventory Logic:** Implements polymorphic behavior to distinguish between standard books (which can be borrowed) and reference books (which cannot).
* **Automated Fine Calculation:** Automatically tracks issue dates and calculates monetary fines for books returned past the 14-day due date.
* **Robust Input Validation:** Includes custom utility functions to prevent application crashes from invalid user inputs (e.g., entering text instead of numbers).