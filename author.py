class Author:
    def __init__(self, name, biography):
        self.__name = name
        self.__biography = biography

    def display_author_details(self):
        return f"Author: {self.__name}\nBiography: {self.__biography}"
