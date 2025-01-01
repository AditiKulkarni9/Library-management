import pytest
from library import Library

def test_add_book():
    lib = Library()
    book = {"isbn": "978-3-16-148410-0", "title": "Example Book", "author": "John Doe", "year": 2020}
    assert lib.add_book(book) == True
    assert lib.get_book("978-3-16-148410-0") == book
    

def test_borrow_book():
    lib = Library()
    book = {"isbn": "978-3-16-148410-0", "title": "Example Book", "author": "John Doe", "year": 2020}
    lib.add_book(book)
    
    # Borrowing an available book
    assert lib.borrow_book("978-3-16-148410-0") == True
    assert lib.get_book("978-3-16-148410-0")['available'] == False
    
    # Attempting to borrow an already borrowed book
    assert lib.borrow_book("978-3-16-148410-0") == False

def test_borrow_nonexistent_book():
    lib = Library()
    assert lib.borrow_book("non-existent-isbn") == False
    
def test_return_book():
    lib = Library()
    book = {"isbn": "978-3-16-148410-0", "title": "Example Book", "author": "John Doe", "year": 2020}
    lib.add_book(book)
    lib.borrow_book("978-3-16-148410-0")
    
    # Returning a borrowed book
    assert lib.return_book("978-3-16-148410-0") == True
    assert lib.get_book("978-3-16-148410-0")['available'] == True
    
    # Attempting to return a book that wasn't borrowed
    assert lib.return_book("978-3-16-148410-0") == False

def test_return_nonexistent_book():
    lib = Library()
    assert lib.return_book("non-existent-isbn") == False
    
def test_view_available_books():
    lib = Library()
    book1 = {"isbn": "978-3-16-148410-0", "title": "Example Book", "author": "John Doe", "year": 2020}
    book2 = {"isbn": "978-1-16-148411-1", "title": "Another Book", "author": "Jane Smith", "year": 2021}
    
    lib.add_book(book1)
    lib.add_book(book2)
    lib.borrow_book(book1['isbn'])
    
    available_books = lib.view_available_books()
    assert len(available_books) == 1
    assert available_books[0]['isbn'] == book2['isbn']