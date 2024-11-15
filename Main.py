
# Importing the required classes from the files
from LibrarySystem import LibrarySystem
from Book import Book
from User import User
from Author import Author

# Importing the regular expression module for date validation and library ID format
import re

# Creating an instance of the LibrarySystem class
library = LibrarySystem()

# Main menu function runs until the user chooses to quit
def main_menu():
    while True:
        print("-\nWelcome to the Library Managment System.")
        print("Main Menu:")
        print("1. Book Operations")
        print("2. User Operations")
        print("3. Author Operations")
        print("4. Quit")

        choice = input("Enter your choice (1-4): ")

        if choice == "1":
            book_operations()
        elif choice == "2":
            user_operations()
        elif choice == "3":
            author_operations()
        elif choice == "4":
            print("Thank you for using the Library Managment System.")
            break
        else:
            print("Invalid choice. Please try again.")

# Book operations function
def book_operations():
    while True:
        print("\nBook Operations:")
        print("1. Add Book")
        print("2. Borrow Book")
        print("3. Return Book")
        print("4. Search for a Book")
        print("5. Display All Books")
        print("6. Back to Main Menu")

        choice = input("Enter your choice (1-6): ")

        if choice == "1":
            add_book()
        elif choice == "2":
            borrow_book()
        elif choice == "3":
            return_book()
        elif choice == "4":
            search_book()
        elif choice == "5":
            library.display_all_books()
        elif choice == "6":
            break
        else:
            print("Invalid choice. Please try again.")

# User operations function
def user_operations():
    while True:
        print("\nUser Operations:")
        print("1. Add a new User")
        print("2. View user details")
        print("3. Display all users")
        print("4. Back to Main Menu")

        choice = input("Enter your choice (1-4): ")

        if choice == "1":
            add_user()
        elif choice == "2":
            view_user_details()
        elif choice == "3":
            library.display_all_users()
        elif choice == "4":
            break
        else:
            print("Invalid choice. Please try again.")

# Author operations function
def author_operations():
    while True:
        print("\nAuthor Operations:")
        print("Add a new author")
        print("View author details")
        print("Display all authors")
        print("Back to Main Menu")

        choice = input("Enter your choice (1-4): ")

        if choice == "1":
            add_author()
        elif choice == "2":
            view_author_details()
        elif choice == "3":
            library.display_all_authors()
        elif choice == "4":
            break
        else:
            print("Invalid choice. Please try again.")

# Add book function that uses Regex to validate the date format
def add_book():
    title = input("Please enter the book title: ")
    author = input("Please enter the author name: ")
    genre = input("Please enter the genre: ")
    publication_date = input("Please enter the publication date (YYYY-MM-DD): ")

    if not re.match(r"\d{4}-\d{2}-\d{2}", publication_date):
        print("Invalid date format. Please use YYYY-MM-DD.")
        return

    book = Book(title, author, genre, publication_date)

    library.add_book(book)

    print(f"Book '{title}' added successfully!")

# Borrow book function to let the user borrow a book if available
def borrow_book():
    user_id = input("Please enter your library ID: ")
    book_title = input("Please enter the book title you want to borrow: ")

    user = library.find_user(user_id)

    if user:
        if library.borrow_book(user, book_title):
            print(f"'{book_title}' borrowed successfully by {user.get_name()}!")
        else:
            print(f"'{book_title}' is already borrowed by someone else.")

    else:
        print("User not found.")

# Return book function to let the user return a book if borrowed
def return_book():
    user_id = input("Please enter your library ID: ")
    book_title = input("Please enter the book title you want to return: ")

    user = library.find_user(user_id)

    if user:
        if library.return_book(user, book_title):
            print(f"'{book_title}' returned successfully by {user.get_name()}!")
        else:
            print(f"Book return failed. Please check if the {user.get_name()} has borrowed the book.")

    else:
        print("User not found.")

# Search book function to let the user search for a book by title
def search_book():
    title = input("Please enter the book title: ")
    book = library.find_book(title)

    if book:
        print(book)
    else:
        print("Book not found.")

# Add user function to let the user add a new user
def add_user():
    name = input("Please enter the user name: ")
    library_id = input("Please enter the library ID: ")

    # Uses Regex to validate the library ID format
    if not re.match(r"\d{3}", library_id):
        print("Invalid library ID format. Please use 3 digits.")
        return

    user = User(name, library_id)
    library.add_user(user)
    print(f"User '{name}' added successfully!")

# View user details function to let the user view the details of a user and the books borrowed
def view_user_details():
    library_id = input("Please enter the library ID: ")
    user = library.find_user(library_id)

    if user:
        print(user)
        print("Borrowed Books:")
        for book in user.get_borrowed_books():
            print(f"- {book}")

    else:
        print("User not found.")

# Add author function to let the user add a new author
def add_author():
    name = input("Please enter the author name: ")
    biography = input("Please enter the author biography: ")

    author = Author(name, biography)
    library.add_author(author)
    print(f"Author '{name}' added successfully!")

# View author details function to let the user view the details of an author
def view_author_details():
    name = input("Please enter the author name: ")
    author = library.find_author(name)

    if author:
        print(author)
        print(f"Biography: {author.get_biography()}")

    else:
        print("Author not found.")

if __name__ == "__main__":
    main_menu()

