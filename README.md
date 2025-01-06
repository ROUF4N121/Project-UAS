# Program Manajemen Buku di Perpustakaan.

- Nama : Roufan Awaluna Romadhon
- NIM : 312410423
- Kelas : TI.24.A.3

---

## Deskripsi
Program ini adalah aplikasi sederhana untuk Manajemen Buku di Perpustakaan, yang dikembangkan mengunnakan konsep Modular dan OOP (Object-Oriented Programming). Program ini memungkinkan pengguna untuk menyimpan data buku, menampilkan daftar buku, dan menjalankan operasi melalui antarmuka berbasis teks. Dengan pendekatan modular, kode dibagi menjadi tiga bagian utama: model (data), view (tampilan), dan controller (logika aplikasi).

---

### Struktur Folder:
```
LibraryBookManagement/
├── main.py                # Program utama untuk menjalankan aplikasi
├── models/
│   └── book.py            # Berisi class untuk pengelolaan data buku
├── views/
│   └── book_view.py       # Berisi class untuk menampilkan data dan input pengguna
└── controllers/
    └── book_controller.py # Berisi class untuk proses logika aplikasi
```

### Fitur Program:
1. **Menambah Buku:**
   - Pengguna dapat menambahkan data buku baru, termasuk judul, penulis, dan tahun penerbitan.
   - Terdapat validasi input untuk memastikan data yang dimasukkan benar.

2. **Melihat Daftar Buku:**
   - Menampilkan daftar buku dalam format tabel sederhana dengan kolom untuk judul, penulis, dan tahun penerbitan.

3. **Navigasi Menu:**
   - Pengguna dapat memilih menu dengan opsi untuk menambahkan buku, melihat daftar buku, atau keluar dari program.
   
### Video Penjelasan:
https://youtu.be/MGTnlBupdk8