class Library:
    def __init__(self):
        self.books = {}

    def add_book(self, book):
        if book['isbn'] not in self.books:
            self.books[book['isbn']] = book
            return True
        return False

    def get_book(self, isbn):
        return self.books.get(isbn)