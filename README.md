# Bot WhatsApp Manajemen Grup

Ini adalah contoh kode untuk membuat bot WhatsApp yang dirancang untuk mengelola grup, yang dibuat menggunakan library [pywabot](https://github.com/khazulys/pywabot).

## Fitur

*   **Penanganan Perintah:** Bot dapat merespons perintah yang dikirim oleh pengguna.
*   **Manajemen Grup:** Fungsi untuk mengelola aktivitas dan anggota grup.
*   **Penanganan Media:** Kemampuan untuk memproses dan mengelola pesan media yang dikirim di grup.
*   **Deteksi Spam:** Fitur dasar untuk mendeteksi dan menangani pesan spam.
*   **Utilitas Admin:** Alat bantu untuk administrator grup.
*   **Utilitas Moderasi:** Fungsi untuk membantu memoderasi percakapan dalam grup.

## Prasyarat

*   Python 3.8 atau lebih tinggi
*   Akun WhatsApp yang aktif

## Instalasi

1.  **Clone repositori ini:**
    ```bash
    git clone https://github.com/khazulys/example-group-management.git
    cd example-group-management
    ```

3.  **Install dependensi yang dibutuhkan:**
    ```bash
    pip install -r requirements.txt
    ```

## Penggunaan

Untuk menjalankan bot, gunakan perintah berikut:

```bash
python main.py
```

Bot akan memulai dan terhubung ke WhatsApp.

## Struktur Proyek

```
/
├── main.py             # Titik masuk utama aplikasi
├── requirements.txt    # Daftar dependensi Python
├── config/
│   └── settings.py     # Pengaturan dan konfigurasi aplikasi
├── handlers/
│   ├── command_handler.py  # Menangani perintah dari pengguna
│   ├── group_handler.py    # Menangani event terkait grup
│   ├── media_handler.py    # Menangani pesan media
│   └── spam_handler.py     # Menangani pesan spam
└── utils/
    ├── admin_utils.py      # Fungsi bantuan untuk admin
    └── moderation_utils.py # Fungsi bantuan untuk moderasi
```

## Kontribusi

Kontribusi sangat diterima! Silakan buat *pull request* atau buka *issue* untuk mendiskusikan perubahan yang ingin Anda buat.

## Lisensi

Proyek ini dilisensikan di bawah Lisensi MIT. Lihat file `LICENSE` untuk detailnya.
