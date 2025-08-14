from library import Book, Library

def display_menu():
    print("\nLibrary Management System")
    print("1. Add Book")
    print("2. Remove Book")
    print("3. List Books")
    print("4. Find Boook")
    print("5. Exit")

def main():
    library = Library("library.json")

    while True:
        display_menu()
        choice = input("Enter your choice (1-5): ")

        if choice == '1':
            title = input("Enter book title: ")
            author = input("Enter book author: ")
            isbn = input("Enter book ISBN: ")
            print(library.add_book(book = Book(title, author, isbn)))

        elif choice == '2':
            isbn = input("Enter book ISBN to remove: ")
            print(library.remove_book(isbn))

        elif choice == '3':
            print("Books in the library:")
            print(library.list_books())

        elif choice == '4':
            isbn = input("Enter book ISBN to find: ")
            book = library.find_book(isbn)
            print(book if book else f"Book with ISBN {isbn} not found.")

        elif choice == '5':
            print("Exiting the Library Management System.")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
