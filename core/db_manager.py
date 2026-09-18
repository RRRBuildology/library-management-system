import sqlite3

class DatabaseManager:
    # This variable holds the single instance of the class
    _instance = None

    def __new__(cls):
        # If an instance doesn't exist, create one. Otherwise, return the existing one.
        if cls._instance is None:
            cls._instance = super(DatabaseManager, cls).__new__(cls)
            cls._instance.connection = sqlite3.connect('data/library.db', check_same_thread=False)
            cls._instance.cursor = cls._instance.connection.cursor()
            cls._instance.setup_tables()
        return cls._instance

    def setup_tables(self):
        # Create tables if they don't exist
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS members (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                email TEXT UNIQUE NOT NULL,
                role TEXT DEFAULT 'member'
            )
        ''')
        
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS books (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                title TEXT NOT NULL,
                author TEXT NOT NULL,
                book_type TEXT DEFAULT 'standard',
                copies_available INTEGER DEFAULT 1
            )
        ''')

        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS transactions (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                member_id INTEGER,
                book_id INTEGER,
                issue_date TEXT,
                return_date TEXT,
                fine_amount REAL DEFAULT 0.0,
                FOREIGN KEY(member_id) REFERENCES members(id),
                FOREIGN KEY(book_id) REFERENCES books(id)
            )
        ''')
        self.connection.commit()

    def get_cursor(self):
        return self.cursor

    def commit(self):
        self.connection.commit()