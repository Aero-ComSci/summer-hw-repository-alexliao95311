from .book.py import Book

class EBook(Book):
    def __init__(self, title, author, ISBN, quantity, file_size):
        super().__init__(title, author, ISBN, quantity)
        self.__file_size = file_size

    def __str__(self):
        return f"{super().__str__()}, File Size: {self.__file_size}MB"
