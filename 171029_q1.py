class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.is_borrowed = False
    
    def mark_as_borrowed(self):
        if not self.is_borrowed:
            self.is_borrowed = True
            print(f"The book '{self.title}' has been marked as borrowed.")
        else:
            print(f"The book '{self.title}' is already borrowed.")
    
    def mark_as_returned(self):
        if self.is_borrowed:
            self.is_borrowed = False
            print(f"The book '{self.title}' has been marked as returned.")
        else:
            print(f"The book '{self.title}' was not borrowed.")

class LibraryMember:
    def __init__(self, name, member_id):
        self.name = name
        self.member_id = member_id
        self.borrowed_books = []
    
    def borrow_book(self, book):
        if not book.is_borrowed:
            book.mark_as_borrowed()
            self.borrowed_books.append(book)
            print(f"{self.name} has borrowed '{book.title}'.")
        else:
            print(f"Sorry, '{book.title}' is currently not available.")
    
    def return_book(self, book):
        if book in self.borrowed_books:
            book.mark_as_returned()
            self.borrowed_books.remove(book)
            print(f"{self.name} has returned '{book.title}'.")
        else:
            print(f"{self.name} did not borrow '{book.title}'.")
    
    def list_borrowed_books(self):
        if self.borrowed_books:
            print(f"{self.name}'s borrowed books:")
            for book in self.borrowed_books:
                print(f"- {book.title} by {book.author}")
        else:
            print(f"{self.name} has no borrowed books.")

# Interactive code to test borrowing and returning books
def library_system():
    # Sample books
    book1 = Book("The Great Gatsby", "F. Scott Fitzgerald")
    book2 = Book("1984", "George Orwell")
    
    # Sample library member
    member = LibraryMember("Patriciah", "M001")
    
    while True:
        print("\nLibrary System:")
        print("1. Borrow a Book")
        print("2. Return a Book")
        print("3. List Borrowed Books")
        print("4. Exit")
        
        choice = input("Choose an option (1-4): ")
        
        if choice == "1":
            title = input("Enter the title of the book to borrow: ")
            if title == book1.title:
                member.borrow_book(book1)
            elif title == book2.title:
                member.borrow_book(book2)
            else:
                print("Book not found.")
        
        elif choice == "2":
            title = input("Enter the title of the book to return: ")
            if title == book1.title:
                member.return_book(book1)
            elif title == book2.title:
                member.return_book(book2)
            else:
                print("Book not found.")
        
        elif choice == "3":
            member.list_borrowed_books()
        
        elif choice == "4":
            print("Exiting the library system.")
            break
        
        else:
            print("Invalid choice. Please try again.")

# Run the library system
library_system()
