class Book:
    def __init__(self, title: str, author: str):
        self.title = title
        self.author = author
    def __str__(self):
        return f"Book: {self.title} by {self.author}"
class Ebook(Book):
    def __init__(self, title: str, author: str, filesize):
        super().__init__(title, author)
        self.filesize = filesize
    def __str__(self):
        return f"Ebook: {self.title} by {self.author}, filesize: {self.filesize}"
class Printbook(Book):
    def __init__(self, title: str, author: str, page_count):
        super().__init__(title, author)
        self.page_count = page_count
    def __str__(self):
        return f"printbook: {self.title} by {self.author}, page count: {self.page_count}"
class Library:
    def __init__(self):
        pass
        self.books = []
    def add_book(self, book):
        self.books.append(book)
    def list_books(self):
        for book in self.books:
            print(book)