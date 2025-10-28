daftar_menu = {
    1 : ("Kopi Hitam" , 10000),
    2 : ("Cappucino" , 15000),
    3 : ("Teh Tarik" , 8000),
    4 : ("Roti Bakar" , 12000),
    5 : ("Mie Goreng" , 13000),
}

total = 0
pesanan = {}
jumlah_uang = 0

while True:
    print("\n======== SELAMAT DATANG DI KAFE DARTHA ========")
    print("Daftar Menu :\n")

    for no, (nama, harga) in daftar_menu.items():
        print(f"{no}. {nama} \t: {harga}")

    try:
        jumlah_item = int(input("\nMasukan jumlah item yang ingin di pesan :"))
    except ValueError:
        print("Pilih menu yang tersedia")
        continue

    i = 1
    while i <= jumlah_item:
        try:
            pilihan = int(input(f"\nMasukan nomor menu ke-{i} : "))
        except ValueError:
            print("Input tidak valid")
            continue

        if pilihan in daftar_menu :
            nama, harga = daftar_menu[pilihan]

            while True:
                try:
                    qty = int(input(f"Jumlah pesanan untuk {nama} : "))
                except ValueError:
                    print("input tidak valid")
                    continue

                subtotal = harga * qty
                total += subtotal
                pesanan[nama] = (qty, subtotal)

                i += 1
                break
        else:
            print("Menu tidak tersedia ")
            continue


    while True:
        try:
            jumlah_uang = int(input("Jumlah uang tunai : "))
          
        except ValueError:
            print("input tidak valid")
            continue

        if jumlah_uang >= total:
            kembalian = jumlah_uang - total
            break

        else:
            print("Uang tidak cukup\n")
            continue


    print("\n========== STRUK PEMBAYARAN ==========")
    print(f"{'Menu':<15}{'Qty':>8}{'Subtotal':>15}")
    print("-" * 40)

    for nama, (qty, subtotal) in pesanan.items():
        print(f"{nama:<15}{qty:>8}{'Rp' + format(subtotal, ','):>15}")

    print("-" * 40)
    print(f"{'Total Bayar :':<23}{'Rp' + format(total, ','):>15}")
    print(f"{'Uang Tunai :':<23}{'Rp' + format(jumlah_uang, ','):>15}")
    print(f"{'Kembalian :':<23}{'Rp' + format(kembalian, ','):>15}\n")
    print("Terima kasih telah berkunjung di Kafe Darta")
    break

    