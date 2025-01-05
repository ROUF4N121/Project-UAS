from models.book import Book
from views.book_view import BookView

class BookController:
    def __init__(self):
        self.book = Book()
        self.view = BookView()

    def add_book(self):
        data = self.view.request_input()
        if data:
            title, author, year = data
            self.book.add_book(title, author, year)
            print("Buku berhasil ditambahkan!")

    def display_books(self):
        books = self.book.get_books()
        if books:
            self.view.display_books(books)
        else:
            print("Belum ada data buku.")

    def run(self):
        while True:
            print("\nMenu:")
            print("1. Tambah Buku")
            print("2. Lihat Daftar Buku")
            print("3. Keluar")
            try:
                choice = int(input("Pilih menu: "))
                if choice == 1:
                    self.add_book()
                elif choice == 2:
                    self.display_books()
                elif choice == 3:
                    print("Keluar dari program.")
                    break
                else:
                    print("Pilihan tidak valid.")
            except ValueError:
                print("Input harus berupa angka.")
