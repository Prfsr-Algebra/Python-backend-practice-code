class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self._is_checked_out = False
    def checkout(self):
        #check if a book hasn't beent checked out before
        if not self._is_checked_out:
            self._is_checked_out = True
            return True
        return False
    def return_book(self):
        if self._is_checked_out:
            self._is_checked_out = False
            return True
        return False
    def availability(self):
        return not self._is_checked_out
class Library:
    def __init__(self):
        self._books = []
    def add_book(self, book):
        self._books.append(book)
    def check_out_book(self, title):
        for book in self._books:
            if book.title == title and book.availability():
                self._books.remove(book)
            return True
        return False
    def return_book(self, title):
        for book in self._books:
            if book.title == title and not book.availability:
                self._books.append(book)
                return True
            return False
    def list_available_books(self):
        """List all available books."""
        for book in self._books:
            if book.availability():
                print(f"{book.title} by {book.author}")