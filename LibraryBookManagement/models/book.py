class Book:
    def __init__(self):
        self.books = []

    def add_book(self, title, author, year):
        self.books.append({"title": title, "author": author, "year": year})

    def get_books(self):
        return self.books
