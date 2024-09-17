import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Membaca dataset dari file Excel
file_path = 'Dataset_Studi_Kasus.xlsx'  # Sesuaikan dengan lokasi file
df = pd.read_excel(file_path, sheet_name='Pemasukan Bulanan')

# Menampilkan beberapa baris pertama untuk memeriksa data
print(df.head())

# Menggunakan pandas untuk mengolah data
# Pastikan kolom bulan dan pemasukan sesuai dengan dataset
# Asumsi kolom bernama 'Bulan' dan 'Pemasukan'
bulan = df['Bulan']
pemasukan = df['Pemasukan']

# Menggunakan numpy untuk melakukan beberapa operasi dasar
# Misalnya, menghitung rata-rata, maksimum, dan minimum dari pemasukan
rata_rata_pemasukan = np.mean(pemasukan)
pemasukan_maksimum = np.max(pemasukan)
pemasukan_minimum = np.min(pemasukan)
pemasukan_stdev = np.std(pemasukan)

# Membulatkan hasil menggunakan np.round
pemasukan_stdev = np.round(pemasukan_stdev, 2)

print(f"Rata-rata Pemasukan: {rata_rata_pemasukan}")
print(f"Pemasukan Maksimum: {pemasukan_maksimum}")
print(f"Pemasukan Minimum: {pemasukan_minimum}")
print(f"Pemasukan Standar Deviasi: {pemasukan_stdev}")

# Visualisasi data menggunakan matplotlib
plt.figure(figsize=(10, 6))
plt.plot(bulan, pemasukan, marker='o', color='b', label='Pemasukan Bulanan')
plt.title('Grafik Pemasukan Bulanan')
plt.xlabel('Bulan')
plt.ylabel('Pemasukan')
plt.grid(True)
plt.xticks(rotation=45)
plt.legend()
plt.tight_layout()

# Menyimpan grafik ke file gambar
plt.savefig('grafik_pemasukan_bulanan.png')

# Menampilkan grafik
plt.show()
