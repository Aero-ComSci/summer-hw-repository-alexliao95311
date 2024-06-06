# Advanced Library Management System

## Overview
The Advanced Library Management System helps users manage books, library members, and transactions like book issues and returns. It's designed to showcase the use of Object-Oriented Programming (OOP) principles in Python.

## Features
- **Add Books**: Easily add new books to the library inventory.
- **Add Members**: Register new members with the library.
- **Issue Books**: Issue books to members and keep track of them.
- **Return Books**: Manage book returns and update inventory.
- **Search Books**: Find books by title, author, or ISBN.
- **Display Inventory**: View the current inventory of books.

## OOP Principles Used

### Encapsulation
The program uses private attributes (prefixed with double underscores) and provide getter and setter methods to manage these attributes. This keeps the internal state of objects safe from direct access and modification.

### Inheritance
The `EBook` class inherits from the `Book` class, and the `PremiumMember` class inherits from the `Member` class. This allows us to reuse and extend the functionality of the base classes.

### Method Overriding
In the `EBook` and `PremiumMember` classes, the program overrides the `__str__` method to provide additional information specific to e-books and premium members.

### Polymorphism
The program uses base class references (`Book` and `Member`) to manage objects of derived classes (`EBook` and `PremiumMember`). This allows the library system to handle different types of books and members in a uniform way.

### Abstraction
The `Library` class provides clear methods like `add_book`, `add_member`, `issue_book`, and `return_book`. This creates a simple interface for interacting with the system without exposing the internal details.

### Super
The `super` function is used in the `EBook` and `PremiumMember` classes to call the initializer and other methods of the base class. This ensures proper initialization and extends the behavior of the base class.

## Classes and Methods

### Book Class
Represents a book in the library.
- **Attributes**: `title`, `author`, `ISBN`, `quantity`
- **Methods**: `__init__`, `__str__`, `get_ISBN`, `get_quantity`, `set_quantity`

### EBook Class
Represents an e-book in the library, inheriting from the `Book` class.
- **Attributes**: `title`, `author`, `ISBN`, `quantity`, `file_size`
- **Methods**: `__init__`, `__str__`

### Member Class
Represents a library member.
- **Attributes**: `name`, `member_id`, `borrowed_books`
- **Methods**: `__init__`, `__str__`, `borrow_book`, `return_book`

### PremiumMember Class
Represents a premium library member, inheriting from the `Member` class.
- **Attributes**: `name`, `member_id`, `borrowed_books`, `membership_level`
- **Methods**: `__init__`, `__str__`

### Library Class
Manages the overall library operations.
- **Attributes**: `books`, `members`
- **Methods**: `add_book`, `add_member`, `issue_book`, `return_book`, `search_book`, `display_inventory`

## Usage
1. **Add Books**: Create `Book` or `EBook` objects and add them to the library using `add_book`.
2. **Add Members**: Create `Member` or `PremiumMember` objects and add them to the library using `add_member`.
3. **Issue Books**: Issue books to members using `issue_book`.
4. **Return Books**: Return books using `return_book`.
5. **Search Books**: Search for books using `search_book`.
6. **Display Inventory**: Display the current inventory using `display_inventory`.

