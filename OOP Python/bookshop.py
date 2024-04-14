class BookShop:
    def __init__(self):
        # Initialize the bookstore with an empty list of books
        self.all_books = []

    def add_book(self, book):
        # Add a book to the bookstore inventory
        self.all_books.append({'title': book.title, 'author': book.author, 'price': book.price, 'quantity': book.quantity})

    def available_books(self):
        # Display information about all available books
        for book in self.all_books:
            for key, value in book.items():
                print(f"{key}: {value}")
            print()

    def sell_books(self, book_title, quantity):
        # Sell books by updating the quantity in the inventory
        for book in self.all_books:
            if book['title'] == book_title:
                if book['quantity'] >= quantity:
                    book['quantity'] -= quantity
                    print(f"Sold {quantity} copies of {book_title}. Remaining quantity: {book['quantity']}")
                else:
                    print(f"Insufficient quantity for {book_title}")
                return
        print(f"Book not found: {book_title}")

    def order_new_books(self, book):
        # Order new books and add them to the inventory
        self.all_books.append({'title': book.title, 'author': book.author, 'price': book.price, 'quantity': book.quantity})
        print(f"Ordered {book.quantity} copies of {book.title} from the publisher.")

# Define the Book class
class Book:
    def __init__(self, title, author, price, quantity):
        self.title = title
        self.author = author
        self.price = price
        self.quantity = quantity

# Create a BookShop instance
bookstore = BookShop()

# Add books to the bookstore inventory
book_1 = Book('Misir Ali', 'Humayun Ahmed', 250, 10)
bookstore.add_book(book_1)

# Display available books
bookstore.available_books()

# # Sell books
bookstore.sell_books('Misir Ali', 3)

# # Display available books after selling
bookstore.available_books()

# # Order new books
new_book = Book('New Book', 'New Author', 15, 20)
bookstore.order_new_books(new_book)

# # Display available books after ordering
bookstore.available_books()
