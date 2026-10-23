# Pertemuan 09 - List dan Pengolahan Data Numerik

**Nama:** Sela Widiyanti
**NIM:** 2225250176
**Kelas:** 3F

## Tujuan

Praktik ini bertujuan untuk memahami penggunaan list pada Python serta menerapkannya dalam pengolahan data numerik sederhana. Materi yang dipelajari meliputi pembuatan list, akses indeks, slicing, manipulasi elemen, perulangan, perhitungan statistik, fungsi, dan pengolahan nilai mahasiswa berdasarkan batas kelulusan.

## Struktur Program

Proyek ini terdiri dari enam file latihan dan satu file praktik utama.

```text
pertemuan-09-list-NIM/
├── README.md
├── .gitignore
├── latihan/
│   ├── 01_buat_list.py
│   ├── 02_indeks_slicing.py
│   ├── 03_manipulasi_list.py
│   ├── 04_agregasi_nilai.py
│   ├── 05_filter_kelulusan.py
│   └── 06_fungsi_statistik.py
└── praktik/
    └── analisis_nilai_mahasiswa.py
```

### Penjelasan File

- `01_buat_list.py`: membuat list nilai dan menghitung banyak data.
- `02_indeks_slicing.py`: mengambil elemen menggunakan indeks dan slicing.
- `03_manipulasi_list.py`: mengubah, menambah, menyisipkan, dan menghapus elemen.
- `04_agregasi_nilai.py`: menghitung total, rata-rata, minimum, dan maksimum.
- `05_filter_kelulusan.py`: menyeleksi nilai yang memenuhi batas kelulusan 60.
- `06_fungsi_statistik.py`: menghitung rata-rata menggunakan fungsi.
- `analisis_nilai_mahasiswa.py`: mengolah nilai mahasiswa dan menampilkan ringkasan statistik serta informasi kelulusan.

## Cara Menjalankan

1. Buka folder proyek di Visual Studio Code.
2. Pastikan Python 3 sudah terpasang.
3. Buka menu Terminal, kemudian pilih New Terminal.
4. Jalankan program menggunakan perintah berikut.

Menjalankan latihan:

```bash
python latihan/01_buat_list.py
python latihan/02_indeks_slicing.py
python latihan/03_manipulasi_list.py
python latihan/04_agregasi_nilai.py
python latihan/05_filter_kelulusan.py
python latihan/06_fungsi_statistik.py
```

Menjalankan praktik utama:

```bash
python praktik/analisis_nilai_mahasiswa.py
```

Jika perintah `python` tidak dikenali, coba gunakan `py` pada Windows atau `python3` pada macOS/Linux.

## Hasil Praktik Utama

Program menggunakan 10 data nilai mahasiswa:

`[78, 55, 90, 67, 60, 82, 45, 71, 88, 59]`

Ringkasan hasil yang diharapkan:

| Keterangan | Hasil |
|---|---:|
| Banyak data | 10 |
| Total nilai | 695 |
| Rata-rata | 69.50 |
| Nilai minimum | 45 |
| Nilai maksimum | 90 |
| Jumlah lulus | 7 |
| Jumlah belum lulus | 3 |

Batas kelulusan yang digunakan adalah 60. Mahasiswa dinyatakan lulus apabila nilainya lebih besar atau sama dengan 60.

## Test Case

Hasil aktual berikut merupakan hasil yang diharapkan dari kode yang telah dibuat. Verifikasi kembali melalui VS Code sebelum menyelesaikan laporan.

| No. | Data uji | Pengujian | Hasil yang diharapkan | Status |
|---|---|---|---|---|
| 1 | `[60, 70, 80]` | Rata-rata | 70.00 | Perlu diverifikasi |
| 2 | `[60, 70, 80]` | Minimum dan maksimum | 60 dan 80 | Perlu diverifikasi |
| 3 | `[60, 70, 80]` | Jumlah lulus | 3 | Perlu diverifikasi |
| 4 | `[59, 60, 61]` | Batas kelulusan | 2 lulus | Perlu diverifikasi |
| 5 | `[]` | Rata-rata list kosong | 0 tanpa error | Perlu diverifikasi |

Ubah kolom status menjadi **Lulus** setelah pengujian benar-benar dilakukan dan hasilnya sesuai. Jika hasil berbeda, periksa kembali kode dan ulangi pengujian.

## Refleksi

Setelah mengerjakan latihan ini, saya memahami bahwa list dapat digunakan untuk menyimpan banyak nilai dalam satu variabel sehingga data lebih mudah dikelola. Saya juga mempelajari cara mengakses elemen menggunakan indeks, mengambil sebagian data dengan slicing, serta menghitung statistik menggunakan fungsi Python.

Salah satu hal yang perlu diperhatikan adalah indeks list dimulai dari 0, bukan 1. Selain itu, list kosong harus diperiksa sebelum menghitung rata-rata agar tidak terjadi pembagian dengan nol.

**Kesalahan yang saya temukan dan perbaiki:** [Tuliskan kesalahan yang benar-benar kamu alami selama praktik dan bagaimana kamu memperbaikinya.]

## Referensi dan Bantuan

- Bahan Ajar Algoritma dan Pemrograman, Pertemuan 09: List/Array dan Pengolahan Data Numerik Sederhana.
- Python Software Foundation, Python 3 Documentation: Data Structures.
- Bantuan AI digunakan untuk memahami instruksi, menyusun langkah pengerjaan, dan membantu penulisan kode. Seluruh kode dan hasil pengujian akan diperiksa serta dipahami kembali oleh saya.
