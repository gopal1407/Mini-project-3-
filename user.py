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
