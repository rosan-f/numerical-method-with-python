def total(*angka):
    hasil = 0
    for i in angka:
        hasil += i
    print("Total:", hasil)

total(1, 2, 3)
total(5, 10, 15, 20)
