class BookView:
    @staticmethod
    def display_books(data):
        print("\nDaftar Buku:")
        print("+--------------------+--------------------+------+\n| Judul              | Penulis            | Tahun|\n+--------------------+--------------------+------+")
        for book in data:
            print(f"| {book['title']:<18} | {book['author']:<18} | {book['year']:<4} |")
        print("+--------------------+--------------------+------+")

    @staticmethod
    def request_input():
        try:
            title = input("Masukkan Judul Buku: ")
            author = input("Masukkan Nama Penulis: ")
            year = int(input("Masukkan Tahun Terbit: "))
            return title, author, year
        except ValueError:
            print("Input tidak valid. Pastikan tahun berupa angka.")
            return None
