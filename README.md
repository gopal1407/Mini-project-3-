# book.py

class Book:
    def __init__(self, title, author, genre, publication_date):
        self.__title = title
        self.__author = author
        self.__genre = genre
        self.__publication_date = publication_date
        self.__availability = True  # True means available, False means borrowed

    def borrow_book(self):
        if self.__availability:
            self.__availability = False
            print(f"{self.__title} has been borrowed.")
        else:
            print(f"{self.__title} is currently unavailable.")

    def return_book(self):
        if not self.__availability:
            self.__availability = True
            print(f"{self.__title} has been returned.")
        else:
            print(f"{self.__title} was not borrowed.")

    def display_book_details(self):
        availability = "Available" if self.__availability else "Borrowed"
        return f"Title: {self.__title}\nAuthor: {self.__author}\nGenre: {self.__genre}\nPublication Date: {self.__publication_date}\nAvailability: {availability}"

## user.py
class User:
    def __init__(self, name, library_id):
        self.__name = name
        self.__library_id = library_id
        self.__borrowed_books = []

    def borrow_book(self, book):
        if len(self.__borrowed_books) < 5:  # Limit to 5 books for simplicity
            book.borrow_book()
            self.__borrowed_books.append(book)
        else:
            print("You can't borrow more than 5 books at a time.")

    def return_book(self, book):
        if book in self.__borrowed_books:
            book.return_book()
            self.__borrowed_books.remove(book)
        else:
            print(f"{book.display_book_details()} was not borrowed by {self.__name}.")

    def display_user_details(self):
        borrowed_titles = [book.display_book_details() for book in self.__borrowed_books]
        return f"Name: {self.__name}\nLibrary ID: {self.__library_id}\nBorrowed Books: {', '.join(borrowed_titles) if borrowed_titles else 'None'}"

### author.py
class Author:
    def __init__(self, name, biography):
        self.__name = name
        self.__biography = biography

    def display_author_details(self):
        return f"Author: {self.__name}\nBiography: {self.__biography}"
#### menu.py

def show_main_menu():
    print("Welcome to the Library Management System!")
    print("Main Menu:")
    print("1. Book Operations")
    print("2. User Operations")
    print("3. Author Operations")
    print("4. Quit")

def show_book_menu():
    print("Book Operations:")
    print("1. Add a new book")
    print("2. Borrow a book")
    print("3. Return a book")
    print("4. Search for a book")
    print("5. Display all books")

def show_user_menu():
    print("User Operations:")
    print("1. Add a new user")
    print("2. View user details")
    print("3. Display all users")

def show_author_menu():
    print("Author Operations:")
    print("1. Add a new author")
    print("2. View author details")
    print("3. Display all authors")

##### main.py

from book import Book
from user import User
from author import Author
from menu import show_main_menu, show_book_menu, show_user_menu, show_author_menu

def main():
    books = []
    users = []
    authors = []
    
    while True:
        show_main_menu()
        choice = input("Please select an option: ")
        
        if choice == '1':  # Book Operations
            show_book_menu()
            book_choice = input("Select an operation: ")
            if book_choice == '1':  # Add a new book
                title = input("Enter the title: ")
                author = input("Enter the author: ")
                genre = input("Enter the genre: ")
                publication_date = input("Enter the publication date: ")
                books.append(Book(title, author, genre, publication_date))
            elif book_choice == '2':  # Borrow a book
                title = input("Enter the title of the book you want to borrow: ")
                book = next((book for book in books if book._Book__title == title), None)
                if book:
                    user = input("Enter your name: ")
                    found_user = next((user for user in users if user._User__name == user), None)
                    if found_user:
                        found_user.borrow_book(book)
                    else:
                        print("User not found.")
            elif book_choice == '3':  # Return a book
                pass  # Similar implementation as borrow_book
            elif book_choice == '4':  # Search for a book
                pass  # Implement search for book by title
            elif book_choice == '5':  # Display all books
                for book in books:
                    print(book.display_book_details())
        
        elif choice == '2':  # User Operations
            show_user_menu()
            user_choice = input("Select an operation: ")
            if user_choice == '1':  # Add a new user
                name = input("Enter the user's name: ")
                library_id = input("Enter the user's library ID: ")
                users.append(User(name, library_id))
            elif user_choice == '2':  # View user details
                pass  # Similar implementation as displaying book details
            elif user_choice == '3':  # Display all users
                for user in users:
                    print(user.display_user_details())

        elif choice == '3':  # Author Operations
            show_author_menu()
            author_choice = input("Select an operation: ")
            if author_choice == '1':  # Add a new author
                name = input("Enter the author's name: ")
                biography = input("Enter the biography: ")
                authors.append(Author(name, biography))
            elif author_choice == '2':  # View author details
                pass  # Display author details
            elif author_choice == '3':  # Display all authors
                for author in authors:
                    print(author.display_author_details())

        elif choice == '4':  # Quit
            break
        else:
            print("Invalid option. Please try again.")

if __name__ == "__main__":
    main()



