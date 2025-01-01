import pytest
from library import Library

def test_add_book():
    lib = Library()
    book = {"isbn": "978-3-16-148410-0", "title": "Example Book", "author": "John Doe", "year": 2020}
    assert lib.add_book(book) == True
    assert lib.get_book("978-3-16-148410-0") == book