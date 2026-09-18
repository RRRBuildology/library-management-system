class Person:
    def __init__(self, name, email):
        self.name = name
        self.__email = email  # Encapsulation

    def get_email(self):
        return self.__email

    def display_info(self):
        return f"Name: {self.name}, Email: {self.get_email()}"

class Member(Person):
    def __init__(self, name, email, member_id):
        super().__init__(name, email) # Call parent constructor
        self.member_id = member_id
        self.books_borrowed = 0

    def display_info(self):
        # Polymorphism: Overriding the parent method
        base_info = super().display_info()
        return f"{base_info}, ID: {self.member_id}, Borrowed: {self.books_borrowed}"

class Librarian(Person):
    def __init__(self, name, email):
        super().__init__(name, email)
        self.role = "admin"

    def manage_catalog(self):
        return "Librarian has catalog access."