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
