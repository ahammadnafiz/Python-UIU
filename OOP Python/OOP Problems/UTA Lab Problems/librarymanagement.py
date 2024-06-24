class Book:
    def __init__(self, title, author, isbn) -> None:
        self.title = title
        self.author = author
        self.isbn = isbn
        self.avaible = True
    
    def check_out(self):
        if self.avaible:
            self.avaible = False
            return True
        return False
    
    def return_book(self):
        self.avaible = True
    
class Library:
    def __init__(self, name) -> None:
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
    def __init__(self, name, member_id) -> None:
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

def main():
    # Create a library
    library = Library("City Central Library")

    # Create books
    book1 = Book("To Kill a Mockingbird", "Harper Lee", "9780446310789")
    book2 = Book("1984", "George Orwell", "9780451524935")
    book3 = Book("Pride and Prejudice", "Jane Austen", "9780141439518")
    book4 = Book("The Catcher in the Rye", "J.D. Salinger", "9780316769174")

    # Add books to the library
    for book in [book1, book2, book3, book4]:
        library.add_book(book)
        print(f"Added '{book.title}' to the library.")

    # Create members
    alice = Member("Alice", "M001")
    bob = Member("Bob", "M002")
    charlie = Member("Charlie", "M003")

    print("\n--- Scenario 1: Borrowing available books ---")
    if alice.borrow_book(book1):
        print(f"{alice.name} has borrowed '{book1.title}'")
    if bob.borrow_book(book2):
        print(f"{bob.name} has borrowed '{book2.title}'")

    print("\n--- Scenario 2: Attempting to borrow an unavailable book ---")
    if charlie.borrow_book(book1):
        print(f"{charlie.name} has borrowed '{book1.title}'")
    else:
        print(f"'{book1.title}' is not available for {charlie.name} to borrow.")

    print("\n--- Scenario 3: Returning a book ---")
    if alice.return_book(book1):
        print(f"{alice.name} has returned '{book1.title}'")

    print("\n--- Scenario 4: Borrowing a recently returned book ---")
    if charlie.borrow_book(book1):
        print(f"{charlie.name} has borrowed '{book1.title}'")

    print("\n--- Scenario 5: Attempting to return a book not borrowed ---")
    if bob.return_book(book3):
        print(f"{bob.name} has returned '{book3.title}'")
    else:
        print(f"{bob.name} cannot return '{book3.title}' as they haven't borrowed it.")

    print("\n--- Scenario 6: Finding a book in the library ---")
    found_book = library.find_book("1984")
    if found_book:
        print(f"Found the book: '{found_book.title}' by {found_book.author}")
    else:
        print("Book not found in the library.")

    print("\n--- Scenario 7: Removing a book from the library ---")
    library.remove_book(book4)
    print(f"Removed '{book4.title}' from the library.")
    if library.find_book("The Catcher in the Rye"):
        print("Book is still in the library.")
    else:
        print("Book is no longer in the library.")

    print("\n--- Scenario 8: Borrowing multiple books ---")
    if alice.borrow_book(book3) and alice.borrow_book(book4):
        print(f"{alice.name} has borrowed both '{book3.title}' and '{book4.title}'")
    print(f"{alice.name} has borrowed {len(alice.borrowed_books)} books in total.")


if __name__ == "__main__":
    main()