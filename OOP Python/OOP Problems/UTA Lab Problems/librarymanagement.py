class Book:
    def __init__(self, title, author, ISBN):
        self.title = title
        self.author = author
        self.ISBN = ISBN
        self.available = True

    def check_out(self):
        if self.available:
            self.available = False
            return True
        return False

    def return_book(self):
        self.available = True

class Library:
    def __init__(self, name):
        self.name = name
        self.books = []

    def add_book(self, book):
        self.books.append(book)

    def remove_book(self, book):
        self.books.remove(book)

    def find_book(self, title):
        for book in self.books:
            if book.title.lower() == title.lower():
                return book
        return None

class Member:
    def __init__(self, name, member_id):
        self.name = name
        self.member_id = member_id
        self.borrowed_books = []

    def borrow_book(self, book):
        if book.check_out():
            self.borrowed_books.append(book)
            return True
        return False

    def return_book(self, book):
        if book in self.borrowed_books:
            book.return_book()
            self.borrowed_books.remove(book)
            return True
        return False

# Scenario
def main():
    # Create a library
    library = Library("Central Library")

    # Create books
    book1 = Book("The Great Gatsby", "F. Scott Fitzgerald", "9780743273565")
    book2 = Book("To Kill a Mockingbird", "Harper Lee", "9780446310789")
    book3 = Book("1984", "George Orwell", "9780451524935")

    # Add books to the library
    library.add_book(book1)
    library.add_book(book2)
    library.add_book(book3)

    # Create members
    member1 = Member("Alice", "M001")
    member2 = Member("Bob", "M002")

    # Alice borrows a book
    book = library.find_book("The Great Gatsby")
    if book and member1.borrow_book(book):
        print(f"{member1.name} has borrowed '{book.title}'")
    else:
        print("Book not available")

    # Bob tries to borrow the same book
    if member2.borrow_book(book):
        print(f"{member2.name} has borrowed '{book.title}'")
    else:
        print(f"'{book.title}' is not available")

    # Alice returns the book
    if member1.return_book(book):
        print(f"{member1.name} has returned '{book.title}'")

    # Bob borrows the book
    if member2.borrow_book(book):
        print(f"{member2.name} has borrowed '{book.title}'")
    else:
        print(f"'{book.title}' is not available")

if __name__ == "__main__":
    main()