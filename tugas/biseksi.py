import pandas as pd

def metode_biseksi(fungsi, batas_bawah, batas_atas, toleransi=1e-6, iterasi_maks=100):
    if fungsi(batas_bawah) * fungsi(batas_atas) > 0:
        print("Tanda fungsi pada interval [a, b] sama. Tidak dapat diterapkan metode Biseksi.")
        return None
    
    hasil_iterasi = []
    
    for langkah in range(1, iterasi_maks + 1):
        titik_tengah = (batas_bawah + batas_atas) / 2
        nilai_tengah = fungsi(titik_tengah)
        galat = abs(batas_atas - batas_bawah)

        hasil_iterasi.append([
            langkah,
            round(batas_bawah, 6),
            round(batas_atas, 6),
            round(titik_tengah, 8),
            round(nilai_tengah, 10),
            round(galat, 10)
        ])
        
        if abs(nilai_tengah) < toleransi or galat < toleransi:
            print(f"Akar ditemukan setelah {langkah} iterasi.")
            break
        
        if fungsi(batas_bawah) * nilai_tengah < 0:
            batas_atas = titik_tengah
        else:
            batas_bawah = titik_tengah

    tabel_hasil = pd.DataFrame(
        hasil_iterasi,
        columns=['Iterasi ke-', 'Batas Bawah (a)', 'Batas Atas (b)', 'Perkiraan Akar (c)', 'f(c)', 'Galat (|b - a|)']
    )

    print("\nTabel Proses Iterasi Metode Biseksi:\n")
    print(tabel_hasil.to_string(index=False))
    
    return titik_tengah

# Fungsi yang ingin dicari akarnya
def fungsi(x):
    return 2*x**2 + 3*x - 4

batas_bawah = -4
batas_atas = 0

akar = metode_biseksi(fungsi, batas_bawah, batas_atas)

print("\nAkar dari f(x) = 0 adalah:", akar)
