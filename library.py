import json
import os

class Book:
    def __init__(self, title: str, author: str, isbn:str):
        self.title = title
        self.author = author
        self.isbn = isbn

    def ___str__(self):
        return f"{self.title} by {self.author} (ISBN: {self.isbn})"
    
    def __repr__(self):
        return f"{self.title} by {self.author} (ISBN: {self.isbn})"
        
class Library:
    def __init__(self, filename: "library.json"):
        self.filename = filename
        self.books = []
        self.load_books()

    def add_book(self, book: Book):
        if not self.find_book(book.isbn):
            self.books.append(book)
            self.save_books()
            return f"Book '{book.title}' added successfully."
        return f"Book with ISBN {book.isbn} already exists."
    
    def remove_book(self, isbn: str):
        book = self.find_book(isbn)
        if book:
            self.books.remove(book)
            self.save_books()
            return f"Book '{book.title}' removed successfully."
        return f"Book with ISBN {isbn} not found."
    
    def list_books(self):
        if not self.books:
            return "No books available in the library."
        return "\n".join(str(book) for book in self.books)
    
    def find_book(self, isbn: str):
        for book in self.books:
            if book.isbn == isbn:
                return book   
        return None

    def load_books(self):
        if os.path.exists(self.filename):
            with open(self.filename, 'r') as file:
                books_data = json.load(file)
                self.books = [Book(**book) for book in books_data]

    def save_books(self):
        with open(self.filename, 'w') as file:
            json.dump([vars(book) for book in self.books], file, indent=4)