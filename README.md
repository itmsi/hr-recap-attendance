# HR Recap Attendance

Sistem ini adalah sebuah aplikasi web interaktif yang dibangun menggunakan **Streamlit**. Aplikasi ini dirancang untuk membantu HR (Human Resources) dalam melakukan rekapitulasi data absensi (kehadiran) karyawan. Dengan memanfaatkan pustaka analisis data seperti **Pandas** dan dukungan pemrosesan file Excel melalui **OpenPyXL**, sistem ini memudahkan pengelolaan, analisis, dan visualisasi data kehadiran secara efisien.

## Struktur Direktori

Berikut adalah struktur direktori utama dari sistem ini:

```
hr-recap-attendance/
├── .devcontainer/       # Konfigurasi untuk development container (opsional, bagi pengguna VSCode)
├── .streamlit/          # Konfigurasi khusus untuk aplikasi Streamlit
├── classifiers/         # Direktori untuk file/modul klasifikasi atau pengolahan data tambahan
├── database/            # Direktori untuk menyimpan data/database lokal yang digunakan aplikasi
├── app.py               # Kode sumber utama (main file) dari aplikasi Streamlit
├── Dockerfile           # Konfigurasi untuk membangun image Docker aplikasi ini
├── docker-compose.yml   # Konfigurasi untuk menjalankan aplikasi melalui Docker Compose beserta volumenya
├── requirements.txt     # Daftar dependensi Python yang dibutuhkan untuk menjalankan aplikasi
└── README.md            # Dokumentasi sistem ini
```

## Cara Setup (Tanpa Docker)

Jika Anda ingin menjalankan sistem ini secara langsung di lingkungan lokal Anda (tanpa Docker), ikuti langkah-langkah berikut.

### Kebutuhan Sistem (Prerequisites):
- **Python** (disarankan versi 3.11 atau yang lebih baru)
- **pip** (Python package installer)

### Langkah-langkah:

1. **Clone repositori atau masuk ke direktori proyek:**
   ```bash
   cd /path/to/hr-recap-attendance
   ```

2. **Buat Virtual Environment (Sangat Disarankan):**
   ```bash
   python -m venv venv
   
   # Aktivasi virtual environment (Windows):
   venv\Scripts\activate
   
   # Aktivasi virtual environment (Mac/Linux):
   source venv/bin/activate
   ```

3. **Instal Dependensi:**
   Instal semua pustaka yang dibutuhkan menggunakan `requirements.txt`:
   ```bash
   pip install -r requirements.txt
   ```
   *(Dependensi utama meliputi: `pandas`, `openpyxl`, `streamlit`)*

4. **Jalankan Aplikasi:**
   Setelah semua dependensi terinstal, jalankan aplikasi Streamlit:
   ```bash
   streamlit run app.py
   ```

5. **Akses Aplikasi:**
   Aplikasi akan berjalan secara otomatis di browser Anda, biasanya dapat diakses melalui `http://localhost:8501`.

---

## Cara Setup (Dengan Docker)

Menggunakan Docker adalah cara paling mudah dan konsisten untuk menjalankan aplikasi ini tanpa harus mengonfigurasi environment Python secara manual.

### Kebutuhan Sistem (Prerequisites):
- **Docker** telah terinstal di sistem Anda.
- **Docker Compose** telah terinstal (biasanya sudah termasuk dalam Docker Desktop).

### Langkah-langkah:

1. **Masuk ke direktori proyek:**
   ```bash
   cd /path/to/hr-recap-attendance
   ```

2. **Jalankan Docker Compose:**
   Gunakan perintah berikut untuk membangun image (jika belum ada) dan menjalankan container di background (detached mode):
   ```bash
   docker-compose up -d --build
   ```

3. **Akses Aplikasi:**
   Setelah container berhasil berjalan, buka browser dan akses aplikasi melalui:
   `http://localhost:8501`

4. **Menghentikan Aplikasi:**
   Jika Anda ingin menghentikan aplikasi, jalankan perintah berikut di direktori proyek:
   ```bash
   docker-compose down
   ```

### Catatan Tambahan untuk Docker:
- Konfigurasi `docker-compose.yml` telah mengatur _volume mapping_ (`absensi_db:/app/database`), sehingga data yang tersimpan di dalam direktori `database/` di dalam container akan tetap persisten meskipun container dimatikan atau dihapus.
