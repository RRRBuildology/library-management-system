from datetime import datetime, timedelta

class Transaction:
    def __init__(self, member_id, book_id):
        self.member_id = member_id
        self.book_id = book_id
        self.issue_date = datetime.now()
        self.due_date = self.issue_date + timedelta(days=14) # 2 weeks loan
        self.return_date = None
        self.fine = 0.0

    def return_book(self):
        self.return_date = datetime.now()
        if self.return_date > self.due_date:
            days_late = (self.return_date - self.due_date).days
            self.fine = days_late * 1.0 # $1 per day fine
        return self.fine