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

## Cara Setup di Server dengan Nginx

Jika Anda ingin menjalankan aplikasi ini di server VPS/VM dan mengaksesnya melalui domain, berikut contoh setup yang umum digunakan dengan Nginx sebagai reverse proxy ke Streamlit.

### 1. Siapkan environment di server

Contoh pada Ubuntu/Debian:

```bash
sudo apt update
sudo apt install -y python3 python3-pip python3-venv nginx git
```

Masuk ke direktori proyek, buat virtual environment, lalu install dependensi:

```bash
cd /var/www/hr-recap-attendance
sudo git clone <repo-url> .
sudo python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

### 2. Jalankan aplikasi sebagai service

Buat file service systemd di `/etc/systemd/system/hr-recap-attendance.service`:

```ini
[Unit]
Description=HR Recap Attendance Streamlit App
After=network.target

[Service]
WorkingDirectory=/var/www/hr-recap-attendance
User=www-data
Group=www-data
Environment=PATH=/var/www/hr-recap-attendance/venv/bin:/usr/bin:/bin
ExecStart=/var/www/hr-recap-attendance/venv/bin/streamlit run app.py --server.port 8501 --server.address 127.0.0.1 --server.headless true
Restart=always
RestartSec=5

[Install]
WantedBy=multi-user.target
```

Aktifkan dan jalankan service:

```bash
sudo systemctl daemon-reload
sudo systemctl enable hr-recap-attendance
sudo systemctl start hr-recap-attendance
sudo systemctl status hr-recap-attendance
```

### 3. Konfigurasi Nginx

Buat file konfigurasi Nginx di `/etc/nginx/sites-available/hr-recap-attendance`:

```nginx
server {
    listen 80;
    server_name your-domain.com;

    location / {
        proxy_pass http://127.0.0.1:8501;
        proxy_http_version 1.1;
        proxy_set_header Upgrade $http_upgrade;
        proxy_set_header Connection "upgrade";
        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
        proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
        proxy_set_header X-Forwarded-Proto $scheme;
        proxy_read_timeout 86400;
    }
}
```

Aktifkan konfigurasi:

```bash
sudo ln -s /etc/nginx/sites-available/hr-recap-attendance /etc/nginx/sites-enabled/
sudo nginx -t
sudo systemctl reload nginx
```

### 4. Akses aplikasi

Setelah Nginx aktif, buka aplikasi melalui domain Anda:

```text
http://your-domain.com
```

### 5. Opsional: HTTPS dengan Certbot

Untuk akses HTTPS, Anda bisa menambahkan SSL menggunakan Certbot:

```bash
sudo apt install -y certbot python3-certbot-nginx
sudo certbot --nginx -d your-domain.com
```

> Jika Anda menggunakan domain yang berbeda, ganti `your-domain.com` sesuai nama domain/server Anda.

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
