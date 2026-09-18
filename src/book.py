class Book:
    def __init__(self, title, author, copies):
        self.title = title
        self.author = author
        self.copies = copies

    def can_borrow(self):
        return self.copies > 0

    def get_details(self):
        return f"{self.title} by {self.author} ({self.copies} left)"

class ReferenceBook(Book):
    # This book cannot be borrowed, only read in library
    def can_borrow(self):
        return False 

    def get_details(self):
        return f"{self.title} by {self.author} [Reference Only - Do Not Remove]"