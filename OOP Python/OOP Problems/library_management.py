class Library:
    def __init__(self) -> None:
        self.library = []

    def display_books(self):
        for book_info in self.library:
            print(f"Title: {book_info['title']}\nAuthor: {book_info['author']}\nISBN: {book_info['isbn']}\nAvailable Copies: {book_info['available_copies']}\n")

class Book:
    def __init__(self, title, author, ISBN, available_copies=5) -> None:
        self.title = title
        self.author = author
        self._ISBN = ISBN
        if len(l.library) < 5:
            self.available_copies = available_copies
        else:
            self.available_copies = len(l.library)

        l.library.append({'title': self.title,
                          'author': self.author,
                          'isbn': self._ISBN,
                          'available_copies': self.available_copies
                          })

    def get_isbn(self):
        return self._ISBN

    def display_info(self):
        print(f"Title: {self.title}\nAuthor: {self.author}\nAvailable Copies: {self.available_copies}")


class Person:
    def __init__(self, name, age) -> None:
        self.name = name
        self.age = age

    def display_info(self):
        print(f"Name: {self.name}\nAge: {self.age}")


class Student(Person):
    def __init__(self, name, age, student_id) -> None:
        super().__init__(name, age)
        self.student_id = student_id
        self.books_borrowed = []

    def borrowed_books(self):
        for b in self.books_borrowed:
            print(f"Title: {b.title}\nAuthor: {b.author}")
    
    def borrow_book(self, book):
        self.books_borrowed.append(book)
        for b in l.library:
            if b['title'] == book.title:
                b['available_copies'] -= 1

    def return_book(self, book):
        if book not in self.books_borrowed:
            print("You haven't borrowed this book.")
            return
        for b in l.library:
            if b['title'] == book.title:
                b['available_copies'] += 1

    def display_info(self):
        print(f"Name: {self.name}\nAge: {self.age}\nStudent Id: {self.student_id}")


class Librarian(Person):
    def __init__(self, name, age, employee_id) -> None:
        super().__init__(name, age)
        self._employee_id = employee_id

    def get_employee_id(self):
        return self._employee_id

    def add_book(self, book):
        for b in l.library:
            if b['title'] == book.title:
                print('Book already exists')
                return
        l.library.append({'title': book.title, 'author': book.author, 'isbn': book.get_isbn(),
                          'available_copies': book.available_copies})
        print(f"{book.title} added to the library")

    def remove_book(self, book):
        for b in l.library:
            if b['title'] == book.title:
                l.library.remove(b)
                print(f"{b['title']} removed")
                return
        print('Book doesnot in the library')

    def search_book(self, book):
        for b in l.library:
            if b['title'] == book.title:
                print(f"Title: {b['title']}\nAuthor: {b['author']}\nAvailable Copies: {b['available_copies']}")
                return
        print('Book is not found in the library')
    
    def display_info(self):
        print(f"Name: {self.name}\nAge: {self.age}")


l = Library()

book1 = Book("The Great Gatsby", "F. Scott Fitzgerald", "9780142437019")
book2 = Book("To Kill a Mockingbird", "Harper Lee", "0061120081")
book3 = Book("1984", "George Orwell", "9780451524935")


# print(l.library)
student_1 = Student('Ahammad Nafiz', 20, 152330006)
# student_1.borrow_book(book1)
# print(l.library)
# student_1.borrowed_books()

book4 = Book("The Catcher in the Rye", "J.D. Salinger", "9780241950432")

lian = Librarian('Nafiz', 45, 270349)
lian.add_book(book4)
l.display_books()