
class Book:

    # Constructor
    def __init__(self, title, author, genre, publication_date):
        self.__title = title
        self.__author = author
        self.__genre = genre
        self.__publication_date = publication_date
        self.__availibility = True

    # Getters

    def get_title(self):
        return self.__title

    def get_author(self):
        return self.__author

    def get_genre(self):
        return self.__genre

    def get_publication_date(self):
        return self.__publication_date

    def get_availibility(self):
        return self.__availibility

    # Setters

    def set_availibility(self, status):
        self.__availibility = status

    def __str__(self):
        return f"{self.__title} by, {self.__author}, Genre: {self.__genre}, Publication Date: {self.__publication_date} - {'Availible' if self.__availibility else 'Borrowed'}"