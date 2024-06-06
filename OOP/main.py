from library.book import Book
from library.ebook import EBook
from library.member import Member
from library.premium_member import PremiumMember
from library.library import Library

def main():
    # Creating a library instance
    library = Library()

    # Adding books
    book1 = Book("The Great Gatsby", "F. Scott Fitzgerald", "123456789", 5)
    ebook1 = EBook("1984", "George Orwell", "987654321", 3, 2)
    library.add_book(book1)
    library.add_book(ebook1)

    # Adding members
    member1 = Member("Alice", "M001")
    premium_member1 = PremiumMember("Bob", "M002", "Gold")
    library.add_member(member1)
    library.add_member(premium_member1)

    # Issuing a book
    library.issue_book("M001", "123456789")

    # Returning a book
    library.return_book("M001", "123456789")

    # Searching for a book
    library.search_book(title="1984")

    # Displaying the inventory
    library.display_inventory()

if __name__ == "__main__":
    main()
