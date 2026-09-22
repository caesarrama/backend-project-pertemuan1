# Backend Project Pertemuan 1

## Deskripsi

Project ini merupakan tugas praktikum mata kuliah Dasar Pemrograman Backend menggunakan framework Flask pada Python.

Project ini dibuat untuk mempelajari dasar-dasar pembuatan Backend API, konfigurasi Python Virtual Environment, pembuatan endpoint, dan standarisasi respons JSON.

## Informasi Project

* **Nama Project:** backend-project-pertemuan1
* **Mata Kuliah:** Dasar Pemrograman Backend
* **Institusi:** STIKOM PGRI Banyuwangi
* **Pertemuan:** 1
* **Framework:** Flask
* **Bahasa Pemrograman:** Python

## Teknologi yang Digunakan

* Python 3.14.3
* Flask 3.1.3
* Python Virtual Environment (venv)

## Struktur Folder

```text
backend-project-pertemuan1/
│
├── venv/
├── app.py
├── requirements.txt
├── .gitignore
└── README.md
```

**Catatan:** Folder `venv/` digunakan untuk lingkungan Python dan tidak diunggah ke repository GitHub karena sudah diatur dalam `.gitignore`.

## Persiapan dan Instalasi

### 1. Clone Repository

Jika project diambil dari repository GitHub:

```bash
git clone https://github.com/username/backend-project-pertemuan1.git
```

Masuk ke folder project:

```bash
cd backend-project-pertemuan1
```

### 2. Membuat Virtual Environment

Jika virtual environment belum tersedia:

```bash
python -m venv venv
```

### 3. Mengaktifkan Virtual Environment

Untuk Windows PowerShell:

```powershell
.\venv\Scripts\Activate.ps1
```

### 4. Menginstall Dependencies

Install library yang dibutuhkan menggunakan file `requirements.txt`:

```bash
pip install -r requirements.txt
```

## Cara Menjalankan Aplikasi

Pastikan virtual environment sudah aktif, kemudian jalankan perintah:

```bash
python app.py
```

Jika berhasil, server akan berjalan pada alamat:

```text
http://127.0.0.1:5000
```

## Dokumentasi Endpoint API

### 1. Root / Health Check Service

**Endpoint:**

```http
GET /
```

**Deskripsi:**

Endpoint ini digunakan untuk mengecek apakah Backend API Service sedang aktif dan berjalan.

**URL:**

```text
http://127.0.0.1:5000/
```

**Contoh Response JSON:**

```json
{
  "status": "success",
  "message": "Backend API Service Aktif dan Berjalan",
  "version": "1.0.0"
}
```

**HTTP Status:** `200 OK`

---

### 2. Status Operasional Server

**Endpoint:**

```http
GET /api/v1/status
```

**Deskripsi:**

Endpoint ini digunakan untuk menampilkan status operasional server, waktu sistem, dan versi Python yang sedang digunakan.

**URL:**

```text
http://127.0.0.1:5000/api/v1/status
```

**Contoh Response JSON:**

```json
{
  "data": {
    "python_version": "3.14.3",
    "server_status": "running",
    "timestamp": "2026-09-22T10:09:35.480801"
  },
  "status": "success"
}
```

**HTTP Status:** `200 OK`

**Catatan:** Nilai `timestamp` akan berubah sesuai waktu saat endpoint dipanggil.

---

### 3. Informasi Akademik dan Perkuliahan

**Endpoint:**

```http
GET /api/v1/info
```

**Deskripsi:**

Endpoint ini digunakan untuk menampilkan informasi mata kuliah dan perkuliahan.

**URL:**

```text
http://127.0.0.1:5000/api/v1/info
```

**Contoh Response JSON:**

```json
{
  "status": "success",
  "data": {
    "course": "Dasar Pemrograman Backend",
    "code": "KK112105",
    "institution": "STIKOM PGRI Banyuwangi",
    "meeting": 1,
    "topic": "Environment Setup & Flask Core Concept"
  }
}
```

**HTTP Status:** `200 OK`

---

### 4. Profil Data Mahasiswa

**Endpoint:**

```http
GET /api/v1/mahasiswa
```

**Deskripsi:**

Endpoint ini digunakan untuk menampilkan contoh data profil mahasiswa (dummy).

**URL:**

```text
http://127.0.0.1:5000/api/v1/mahasiswa
```

**Contoh Response JSON:**

```json
{
  "status": "success",
  "data": {
    "nim": "202611001",
    "nama": "Mahasiswa Backend",
    "prodi": "Teknik Informatika",
    "status_akademik": "Aktif"
  }
}
```

**HTTP Status:** `200 OK`

## Standarisasi Response JSON

Seluruh endpoint pada project ini menggunakan format respons JSON yang seragam.

Atribut yang digunakan:

* `status`: Menunjukkan hasil permintaan.
* `data`: Berisi data yang dikembalikan oleh endpoint.
* `message`: Berisi pesan informasi jika diperlukan.

Seluruh endpoint menggunakan HTTP Status `200 OK` untuk permintaan yang berhasil.

## File Pendukung

### .gitignore

File `.gitignore` digunakan untuk mengabaikan file dan folder tertentu agar tidak ikut diunggah ke repository GitHub.

Contoh isi:

```gitignore
venv/
__pycache__/
*.pyc
.env
```

### requirements.txt

File `requirements.txt` berisi daftar library Python yang dibutuhkan untuk menjalankan project.

Instalasi dependencies:

```bash
pip install -r requirements.txt
```

## Kesimpulan

Project ini berhasil mengimplementasikan Backend API sederhana menggunakan Flask dengan beberapa endpoint, yaitu Root Health Check, Status Operasional Server, Informasi Akademik, dan Profil Data Mahasiswa.

Project ini juga menerapkan Python Virtual Environment, standarisasi respons JSON, serta dokumentasi API menggunakan README.md.
