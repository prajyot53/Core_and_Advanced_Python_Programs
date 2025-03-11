class Library:
    # Class Attributes
    total_books = 0  # Represents total books available in the library
    all_books = []  # Stores a list of all books available

    def __init__(self, name):
        # Instance Attributes
        self.name = name  # Name of the library member
        self.borrowed_books = []  # List to keep track of borrowed books

    def borrow_book(self, book):
        """
        Method to borrow a book from the library
        - Checks if the book is available
        - Adds the book to the member's borrowed list
        - Removes the book from the library's available books
        - Decreases total_books count
        """
        if book in Library.all_books:
            self.borrowed_books.append(book)
            Library.all_books.remove(book)
            Library.total_books -= 1
            print(f"{self.name} borrowed '{book}'.")
        else:
            print("Book not available.")

    def return_book(self, book):
        """
        Method to return a book to the library
        - Adds the book back to the library's available books
        - Removes the book from the member's borrowed list
        - Increases total_books count
        """
        if book in self.borrowed_books:
            self.borrowed_books.remove(book)
            Library.all_books.append(book)
            Library.total_books += 1
            print(f"{self.name} returned '{book}'.")
        else:
            print("This book was not borrowed.")

    @classmethod
    def view_library_books(cls):
        """
        Class method to display the total number of books and all available books in the library
        """
        print(f"Total books in library: {cls.total_books}")
        print("Available books:", ", ".join(cls.all_books) if cls.all_books else "No books available")

# Adding books to the library
Library.all_books = ["Python Basics", "Data Science Handbook", "Machine Learning", "Algorithms"]
Library.total_books = len(Library.all_books)

# Creating a member
member1 = Library("Prajyot")

# Viewing available books
Library.view_library_books()

# Borrowing a book
member1.borrow_book("Python Basics")
Library.view_library_books()

# Returning a book
member1.return_book("Python Basics")
Library.view_library_books()


""" O/p:- Total books in library: 4
Available books: Python Basics, Data Science Handbook, Machine Learning, Algorithms
Prajyot borrowed 'Python Basics'.
Total books in library: 3
Available books: Data Science Handbook, Machine Learning, Algorithms
Prajyot returned 'Python Basics'.
Total books in library: 4
Available books: Data Science Handbook, Machine Learning, Algorithms, Python Basics"""
