from .book import Book
from .ebook import EBook
from .member import Member
from .premium_member import PremiumMember

class Library:
    def __init__(self):
        self.__books = []
        self.__members = []

    def add_book(self, book):
        self.__books.append(book)

    def add_member(self, member):
        self.__members.append(member)

    def issue_book(self, member_id, ISBN):
        member = next((m for m in self.__members if m._Member__member_id == member_id), None)
        book = next((b for b in self.__books if b.get_ISBN() == ISBN), None)

        if member and book and book.get_quantity() > 0:
            member.borrow_book(book)
            book.set_quantity(book.get_quantity() - 1)
            print(f"Book '{book.get_ISBN()}' issued to {member._Member__name}.")
        else:
            print("Cannot issue book.")

    def return_book(self, member_id, ISBN):
        member = next((m for m in self.__members if m._Member__member_id == member_id), None)
        book = next((b for b in self.__books if b.get_ISBN() == ISBN), None)

        if member and book:
            member.return_book(book)
            book.set_quantity(book.get_quantity() + 1)
            print(f"Book '{book.get_ISBN()}' returned by {member._Member__name}.")
        else:
            print("Cannot return book.")

    def search_book(self, **kwargs):
        for book in self.__books:
            if all(getattr(book, k) == v for k, v in kwargs.items()):
                print(book)

    def display_inventory(self):
        for book in self.__books:
            print(book)
