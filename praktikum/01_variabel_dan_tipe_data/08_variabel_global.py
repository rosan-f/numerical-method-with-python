x = "Python"

def cetak():
    global x
    x = "JavaScript"
    print("Di dalam fungsi:", x)

cetak()
print("Di luar fungsi:", x)
