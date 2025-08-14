from pathlib import Path
import pytest 
from library import Book, Library
import os

@pytest.fixture
def temp_library(tmp_path: Path):
    filename = tmp_path / "test_library.json"
    lib = Library(filename)
    yield lib
    if os.path.exists(filename):
        os.remove(filename)

def test_add_book(temp_library: Library):
    book = Book("Test Book", "Test Author", "1234567890")
    result = temp_library.add_book(book)
    assert result == "Book 'Test Book' added successfully."
    assert len(temp_library.books) == 1

def test_remove_book(temp_library: Library):
    book = Book("Test Book", "Test Author", "1234567890")
    temp_library.add_book(book)
    result = temp_library.remove_book("1234567890")
    assert result == "Book 'Test Book' removed successfully."
    assert len(temp_library.books) == 0

def test_persistence(temp_library: Library):
    book = Book("Test Book", "Test Author", "1234567890")
    temp_library.add_book(book)
    temp_library.save_books()

    new_library = Library(temp_library.filename)
    assert len(new_library.books) == 1
    assert new_library.books[0].isbn == "1234567890"
   
