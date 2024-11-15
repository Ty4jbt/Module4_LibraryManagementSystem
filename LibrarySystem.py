
# Importing the required classes
from Book import Book
from User import User
from Author import Author

class LibrarySystem:

    # Constructor
    def __init__(self):
        self.books = []
        self.users = []
        self.authors = []

    # Methods
    def add_book(self, book):
        self.books.append(book)

    def add_user(self, user):
        self.users.append(user)

    def add_author(self, author):
        self.authors.append(author)

    def find_book(self, title):
        for book in self.books:
            if book.get_title().lower() == title.lower():
                return book

        return None

    def find_user(self, library_id):
        for user in self.users:
            if user.get_library_id() == library_id:
                return user

        return None

    def find_author(self, name):
        for author in self.authors:
            if author.get_name().lower() == name.lower():
                return author

        return None

    def borrow_book(self, user, book_title):
        book = self.find_book(book_title)
        if book and book.get_availibility():
            book.set_availibility(False)
            user.borrow_book(book_title)
            return True

        return False
    
    def return_book(self, user, book_title):
        book = self.find_book(book_title)
        if book and user.return_book(book_title):
            book.set_availibility(True)
            return True

        return False

    def display_all_books(self):
        for book in self.books:
            print(book)

    def display_all_users(self):
        for user in self.users:
            print(user)

    def display_all_authors(self):
        for author in self.authors:
            print(author)