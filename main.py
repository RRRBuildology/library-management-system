import sys
import os

# Adding src to path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from core.library_system import LibrarySystem
from src.utils import get_valid_input, get_yes_no_input

def main():
    # Initializing the library
    library = LibrarySystem()
    
    while True:
        for _ in range(2):
            print()
        print("------LIBRARY MANAGEMENT SYSTEM------")
        print("1. Register New Member")
        print("2. Add New Book to Catalog")
        print("3. Search for a Book")
        print("4. Issue a Book to Member")
        print("5. Return a Book")
        print("6. View All Members")
        print("7. Exit System")
        
        # Using get_valid_input to ensure the user enters a number (int)
        choice = get_valid_input("Please enter your choice (1-7): ", int)

        if choice == 1:
            print("\n--- Register Member ---")
            name = get_valid_input("Enter Member Name: ", str)
            email = get_valid_input("Enter Member Email: ", str)
            library.register_member(name, email)
            
        elif choice == 2:
            print("\n--- Add Book ---")
            title = get_valid_input("Enter Book Title: ", str)
            author = get_valid_input("Enter Author Name: ", str)
            copies = get_valid_input("Enter Number of Copies: ", int)
            # Using the yes/no utility for boolean inputs
            is_ref = get_yes_no_input("Is this a Reference book? (y/n): ")
            library.add_book(title, author, copies, is_ref)
            
        elif choice == 3:
            print("\n--- Search Book ---")
            title = get_valid_input("Enter Title to Search: ", str)
            library.search_book(title)
            
        elif choice == 4:
            print("\n--- Issue Book ---")
            mid = get_valid_input("Enter Member ID: ", int)
            bid = get_valid_input("Enter Book ID: ", int)
            library.issue_book(mid, bid)

        elif choice == 5:
            print("\n--- Return Book ---")
            # Showing the user what's borrowed
            library.view_active_transactions()
            tid = get_valid_input("\nEnter Transaction ID to return: ", int)
            library.return_book(tid)
            
        elif choice == 6:
            print("\n--- Member List ---")
            library.view_members()
            
        elif choice == 7:
            print("\nThank you for using the Library Management System. Goodbye!")
            break
            
        else:
            print("\nError: Please enter a valid option between 1 and 6.")

if __name__ == "__main__":
    main()