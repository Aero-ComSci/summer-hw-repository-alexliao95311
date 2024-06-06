class Member:
    def __init__(self, name, member_id):
        self.__name = name
        self.__member_id = member_id
        self.__borrowed_books = []

    def __str__(self):
        return f"Name: {self.__name}, Member ID: {self.__member_id}, Borrowed Books: {[book.get_ISBN() for book in self.__borrowed_books]}"

    def borrow_book(self, book):
        self.__borrowed_books.append(book)

    def return_book(self, book):
        self.__borrowed_books.remove(book)
