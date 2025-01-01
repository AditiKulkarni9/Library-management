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
    
    def borrow_book(self, isbn):
        book = self.books.get(isbn)
        if book and book.get('available', True):
            book['available'] = False
            return True
        return False
    
    def return_book(self, isbn):
        book = self.books.get(isbn)
        if book and not book.get('available', True):
            book['available'] = True
            return True
        return False