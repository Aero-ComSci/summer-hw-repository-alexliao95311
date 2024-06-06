class Book:
    def __init__(self, title, author, ISBN, quantity):
        self.__title = title
        self.__author = author
        self.__ISBN = ISBN
        self.__quantity = quantity

    def __str__(self):
        return f"Title: {self.__title}, Author: {self.__author}, ISBN: {self.__ISBN}, Quantity: {self.__quantity}"

    def get_ISBN(self):
        return self.__ISBN

    def get_quantity(self):
        return self.__quantity

    def set_quantity(self, quantity):
        self.__quantity = quantity
