# Optimasi Produksi Media Kultur Jaringan

## Deskripsi Proyek

Proyek ini merupakan implementasi Pemrograman Linear menggunakan Python untuk menyelesaikan permasalahan optimasi produksi media tanam kultur jaringan pada laboratorium bioteknologi.

Terdapat dua jenis media yang diproduksi, yaitu Media Agar Cokelat dan Media Agar Hijau. Program bertujuan untuk menentukan jumlah produksi optimal dari kedua jenis media agar memperoleh keuntungan maksimum dengan mempertimbangkan keterbatasan bahan baku yang tersedia.

Program dikembangkan dalam bentuk aplikasi web sederhana menggunakan Flask. Proses optimasi dilakukan menggunakan SciPy, sedangkan visualisasi grafik dibuat menggunakan Matplotlib.

## Model Matematika

### Variabel Keputusan

- \(x\) = jumlah produksi Media Agar Cokelat dalam liter.
- \(y\) = jumlah produksi Media Agar Hijau dalam liter.

### Fungsi Tujuan

Memaksimalkan keuntungan:

\[
Z = 25.000x + 30.000y
\]

### Kendala

Kendala nutrisi organik:

\[
2x + y \leq 16
\]

Kendala hormon pertumbuhan:

\[
x + 3y \leq 18
\]

Batas nonnegatif:

\[
x \geq 0,\quad y \geq 0
\]

## Teknologi dan Pustaka

Proyek ini menggunakan teknologi dan pustaka berikut:

- **Python** — bahasa pemrograman utama.
- **Flask** — framework untuk membangun aplikasi web.
- **SciPy** — menyelesaikan optimasi Pemrograman Linear menggunakan fungsi `linprog`.
- **NumPy** — mendukung perhitungan numerik dan pembuatan data grafik.
- **Matplotlib** — memvisualisasikan garis kendala, daerah layak, dan solusi optimal.
- **io** — menyimpan grafik sementara di memori.
- **base64** — mengubah gambar grafik agar dapat ditampilkan pada halaman HTML.

## Struktur Proyek

```text
optimasi-media-kultur-jaringan/
├── app.py
├── README.md
└── templates/
    └── index.html
```

Keterangan:

- `app.py` berisi proses optimasi, pembuatan grafik, dan konfigurasi aplikasi Flask.
- `templates/index.html` berisi antarmuka web untuk menampilkan hasil optimasi dan grafik.
- `README.md` berisi dokumentasi proyek dan panduan penggunaan.

## Instalasi dan Menjalankan Program

### 1. Persyaratan

Pastikan Python sudah terinstal pada komputer.

### 2. Clone Repositori

```bash
git clone <URL_REPOSITORI_GITHUB>
```

Masuk ke direktori proyek.

### 3. Instal Pustaka

Jalankan perintah berikut pada terminal:

```bash
pip install Flask numpy matplotlib scipy
```

### 4. Jalankan Aplikasi

Jalankan program menggunakan perintah:

```bash
python app.py
```

### 5. Buka Aplikasi

Buka browser dan akses alamat berikut:

```text
http://127.0.0.1:5000
```

Halaman aplikasi akan menampilkan hasil optimasi, penggunaan bahan baku, dan grafik penyelesaian.

## Hasil Optimasi

Berdasarkan model matematika yang digunakan, solusi optimal yang diharapkan adalah sebagai berikut:

| Informasi | Hasil |
|---|---:|
| Produksi Media Agar Cokelat | 6 liter |
| Produksi Media Agar Hijau | 4 liter |
| Keuntungan maksimum | Rp270.000 |
| Nutrisi organik digunakan | 16 gram |
| Hormon pertumbuhan digunakan | 18 gram |

Kombinasi produksi tersebut menggunakan seluruh persediaan nutrisi organik dan hormon pertumbuhan serta menghasilkan keuntungan maksimum sebesar Rp270.000.

## Fitur Aplikasi

1. Menghitung kombinasi produksi yang memberikan keuntungan maksimum.
2. Menampilkan jumlah produksi optimal setiap jenis media.
3. Menghitung penggunaan dan sisa bahan baku.
4. Menampilkan grafik garis kendala dan daerah layak.
5. Menandai titik solusi optimal pada grafik.

## Tujuan Proyek

Proyek ini dibuat untuk memenuhi tugas Ujian Tengah Semester (UTS) mata kuliah Pemodelan dan Simulasi, dengan menerapkan konsep Pemrograman Linear dalam permasalahan optimasi produksi.

## Pengembang

- Anggota kelompok: [Nama Anggota Kelompok]
- Mata kuliah: Pemodelan dan Simulasi