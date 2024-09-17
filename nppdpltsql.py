from sqlalchemy import create_engine
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Membuat engine SQLAlchemy untuk koneksi MySQL
engine = create_engine("mysql+mysqlconnector://root:@localhost/visdat")

# Membuat DataFrame dari hasil query
query = "SELECT tingkat, nominal FROM biayapendidikan"
df = pd.read_sql(query, engine)

# Menampilkan beberapa baris pertama untuk memeriksa data
print(df.head())

# Mengolah data
tingkat = df['tingkat']
nominal = df['nominal']

# Menggunakan numpy untuk operasi dasar
rata_rata_nominal = np.mean(nominal)
nominal_maksimum = np.max(nominal)
nominal_minimum = np.min(nominal)
nominal_stdev = np.round(np.std(nominal), 2)

# Menampilkan hasil
print(f"Rata-rata Nominal: {rata_rata_nominal}")
print(f"Nominal Maksimum: {nominal_maksimum}")
print(f"Nominal Minimum: {nominal_minimum}")
print(f"Nominal Standar Deviasi: {nominal_stdev}")

# Visualisasi data menggunakan matplotlib
plt.figure(figsize=(10, 6))
plt.plot(tingkat, nominal, marker='o', color='b', label='Nominal Biaya per Tingkat')
plt.title('Grafik Biaya Pendidikan per Tingkat')
plt.xlabel('Tingkat')
plt.ylabel('Nominal')
plt.grid(True)
plt.xticks(rotation=45)
plt.legend()
plt.tight_layout()

# Menyimpan grafik ke file gambar
plt.savefig('grafik_biaya_pendidikan_per_tingkat.png')

# Menampilkan grafik
plt.show()
