# Fungsi untuk menghitung rata-rata
def rata_rata(data):
    if len(data) == 0:
        return 0
    return sum(data) / len(data)


# Fungsi untuk mengambil nilai yang lulus
def nilai_lulus(data, batas=60):
    hasil = []

    for x in data:
        if x >= batas:
            hasil.append(x)

    return hasil


# Data nilai 10 mahasiswa
nilai = [78, 55, 90, 67, 60, 82, 45, 71, 88, 59]

# Mengolah data
lulus = nilai_lulus(nilai)
banyak = len(nilai)
total = sum(nilai)
rata = rata_rata(nilai)
minimum = min(nilai)
maksimum = max(nilai)
jumlah_lulus = len(lulus)
belum_lulus = banyak - jumlah_lulus

# Menampilkan hasil
print("=== ANALISIS NILAI MAHASISWA ===")
print(f"Data nilai       : {nilai}")
print(f"Banyak data      : {banyak}")
print(f"Total nilai      : {total}")
print(f"Rata-rata        : {rata:.2f}")
print(f"Nilai minimum    : {minimum}")
print(f"Nilai maksimum   : {maksimum}")
print(f"Nilai yang lulus : {lulus}")
print(f"Jumlah lulus     : {jumlah_lulus}")
print(f"Belum lulus      : {belum_lulus}")
# Program praktik analisis nilai mahasiswa Pertemuan 09