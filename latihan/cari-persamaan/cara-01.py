import numpy as np
import pandas as pd

def cari_akar_otomatis(f, x_min, x_max, step, error_target):
    """
    Fungsi untuk mencari akar otomatis dengan metode tabulasi (tabel)
    """
    results = []
    x = np.arange(x_min, x_max + step, step)
    f_values = np.array([f(val) for val in x])
    
    for i in range(len(x)):
        results.append([i + 1, x[i], f_values[i], abs(f_values[i])])
    
    pasangan_interval = []
    for i in range(len(f_values) - 1):
        if f_values[i] * f_values[i + 1] < 0:
            pasangan_interval.append((x[i], x[i + 1]))
    
    akar_list = []
    for a, b in pasangan_interval:
        while abs(f(a)) > error_target:
            mid = (a + b) / 2
            if f(a) * f(mid) < 0:
                b = mid
            else:
                a = mid
        akar_list.append(round((a + b) / 2, 6))
    
    df = pd.DataFrame(results, columns=["n", "x", "f(x)", "|f(x)|"])
    return akar_list, df


f1 = lambda x: x**4 + x**3 + 2*x - 2
akar1, df1 = cari_akar_otomatis(f1, 0, 1, 0.1, 0.0001)

f2 = lambda x: x + np.exp(x)
akar2, df2 = cari_akar_otomatis(f2, -1, 0, 0.1, 0.001)

f3 = lambda x: np.exp(x) - x + 1
akar3, df3 = cari_akar_otomatis(f3, -2, 0, 0.1, 0.001)

print("=== HASIL TABULASI SOAL 1 ===")
print(df1.to_string(index=False))
print("\nAkar ditemukan pada:", akar1 if akar1 else "Tidak ada akar")

print("\n=== HASIL TABULASI SOAL 2 ===")
print(df2.to_string(index=False))
print("\nAkar ditemukan pada:", akar2 if akar2 else "Tidak ada akar")

print("\n=== HASIL TABULASI SOAL 3 ===")
print(df3.to_string(index=False))
print("\nAkar ditemukan pada:", akar3 if akar3 else "Tidak ada akar")
