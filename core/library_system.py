from core.db_manager import DatabaseManager
from datetime import datetime, timedelta

class LibrarySystem:
    def __init__(self):
        # Initialize the database connection
        self.db = DatabaseManager()
        self.cursor = self.db.get_cursor()

    # --- Member Function ---
    def register_member(self, name, email):
        try:
            self.cursor.execute("INSERT INTO members (name, email) VALUES (?, ?)", (name, email))
            self.db.commit()
            print(f"Success: {name} registered.")
        except Exception as e:
            print(f"Error: {e} (Email might already exist)")

    def view_members(self):
        self.cursor.execute("SELECT * FROM members")
        rows = self.cursor.fetchall()
        if not rows:
            print("No members found.")
            return
        print(f"\n{'ID':<5} | {'Name':<15} | {'Email'}")
        print("-" * 40)
        for row in rows:
            print(f"{row[0]:<5} | {row[1]:<15} | {row[2]}")

    # --- Book Function ---
    def add_book(self, title, author, copies, is_reference=False):
        book_type = "reference" if is_reference else "standard"
        self.cursor.execute("INSERT INTO books (title, author, book_type, copies_available) VALUES (?, ?, ?, ?)", 
                            (title, author, book_type, copies))
        self.db.commit()
        print(f"Success: Added '{title}' to catalog.")

    def search_book(self, title):
        self.cursor.execute("SELECT * FROM books WHERE title LIKE ?", (f"%{title}%",))
        rows = self.cursor.fetchall()
        if not rows:
            print("No books found.")
            return
        print(f"\n{'ID':<5} | {'Title':<20} | {'Author':<15} | {'Copies'}")
        print("-" * 55)
        for row in rows:
            print(f"{row[0]:<5} | {row[1]:<20} | {row[2]:<15} | {row[4]}")

    # --- Transaction Function ---
    def issue_book(self, member_id, book_id):
        # Check if member exists
        self.cursor.execute("SELECT id FROM members WHERE id=?", (member_id,))
        if not self.cursor.fetchone():
            print("Error: Member ID not found.")
            return

        # Check if book exists and get its details
        self.cursor.execute("SELECT copies_available, book_type FROM books WHERE id=?", (book_id,))
        book_data = self.cursor.fetchone()
        
        if not book_data:
            print("Error: Book ID not found.")
            return
            
        copies, b_type = book_data
        
        if b_type == "reference":
            print("Error: Cannot issue Reference books.")
            return

        if copies > 0:
            # Decrease the available copies in the database
            self.cursor.execute("UPDATE books SET copies_available = copies_available - 1 WHERE id=?", (book_id,))
            
            # Record the transaction
            date_str = datetime.now().strftime("%Y-%m-%d")
            self.cursor.execute("INSERT INTO transactions (member_id, book_id, issue_date) VALUES (?, ?, ?)", 
                                (member_id, book_id, date_str))
            self.db.commit()
            print("Success: Book issued! (Due in 14 days)")
        else:
            print("Error: No copies available to borrow.")

    # --- Show Active Transactions ---
    def view_active_transactions(self):
        """Shows all books that haven't been returned yet."""
        # JOINing the tables to show Names and Titles
        query = """
            SELECT t.id, m.name, b.title, t.issue_date 
            FROM transactions t
            JOIN members m ON t.member_id = m.id
            JOIN books b ON t.book_id = b.id
            WHERE t.return_date IS NULL
        """
        self.cursor.execute(query)
        rows = self.cursor.fetchall()
        
        if not rows:
            print("No active borrowings found.")
            return
            
        print(f"\n{'Trans ID':<10} | {'Member Name':<15} | {'Book Title':<20} | {'Issue Date'}")
        print("-" * 65)
        for row in rows:
            print(f"{row[0]:<10} | {row[1]:<15} | {row[2]:<20} | {row[3]}")

    # --- Book Return Function ---
    def return_book(self, transaction_id):
        """Processes the return, calculates fines, and updates inventory."""
        # 1. Fetching the active transaction
        self.cursor.execute("SELECT * FROM transactions WHERE id=? AND return_date IS NULL", (transaction_id,))
        trans = self.cursor.fetchone()
        
        if not trans:
            print("Error: Transaction ID not found or book already returned.")
            return

        trans_id, member_id, book_id, issue_date, return_date, fine = trans

        # 2. Calculating Fine (14 days limit, Rs. 1 per day late)
        issue_dt = datetime.strptime(issue_date, "%Y-%m-%d")
        due_dt = issue_dt + timedelta(days=14)
        today = datetime.now()

        calculated_fine = 0.0
        if today > due_dt:
            days_late = (today - due_dt).days
            calculated_fine = days_late * 1.0  # Rs. 1 fine per day

        # 3. Update the transaction record in DB
        today_str = today.strftime("%Y-%m-%d")
        self.cursor.execute("UPDATE transactions SET return_date=?, fine_amount=? WHERE id=?",
                            (today_str, calculated_fine, transaction_id))

        # 4. Add the book copy back to inventory
        self.cursor.execute("UPDATE books SET copies_available = copies_available + 1 WHERE id=?", (book_id,))
        
        self.db.commit()
        
        if calculated_fine > 0:
            print(f"Success! Book returned. It was {int((today - due_dt).days)} days late.")
            print(f"Fine Amount: Rs. {calculated_fine:.2f}")
        else:
            print("Success! Book returned on time. No fine.")