# Variabel global
x = "Python"   # variabel global

def cetak():
    global x   # akses & ubah variabel global
    x = "JavaScript"
    print("Di dalam fungsi:", x)

cetak()
print("Di luar fungsi:", x)
