print("========== CAFE YOGA ==========")
print("======= SELAMAT DATANG =======\n")
pembeli = input ("Masukkan nama Pembeli: ")

menu = {
    '1': {'item': 'Americano', 'harga': 40000},
    '2': {'item': 'Cappucino', 'harga': 20000},
    '3': {'item': 'Latte', 'harga': 30000},
    '4': {'item': 'Mocha ', 'harga': 15000},
    '5': {'item': 'Chocolate', 'harga': 15000}
}

def tampilkan_menu():
    print("="*35)
    print("Menu Minuman:")
    print("="*35)
    print("{:<5} {:<20} {:<10}".format("No", "Item", "Harga"))
    print("-"*35)
    for key, value in menu.items():
        print("{:<5} {:<20} {:<10}".format(key, value['item'], f"Rp {value['harga']}"))
    print()

def kasir():
    pesanan = {}
    while True:
        tampilkan_menu()
        pilihan = input("Pilih nomor menu (atau ketik 'selesai' untuk mengakhiri): ")
        
        if pilihan.lower() == 'selesai':
            break
        
        if pilihan in menu:
            jumlah = int(input(f"Jumlah {menu[pilihan]['item']}: "))
            pesanan[menu[pilihan]['item']] = {'jumlah': jumlah, 'harga': menu[pilihan]['harga']}
        else:
            print("Menu tidak tersedia. Silakan pilih nomor menu yang benar.")

    return pesanan

def hitung_total(pesanan):
    total = 0
    for item, info in pesanan.items():
        total += info['jumlah'] * info['harga']
    return total

def cetak_struk(pesanan, total_harga):
    print("\n--- Struk Pembelian ---")
    print("Nama Pembeli: ", pembeli)
    for item, info in pesanan.items():
        print(f"{info['jumlah']} {item} - Rp {info['jumlah'] * info['harga']}")
    print("----------------------")
    print(f"Total Harga: Rp {total_harga}")
    print("Terima kasih atas pembelian Anda!") 

def main():
    daftar_pesanan = kasir()
    total_harga = hitung_total(daftar_pesanan)
    cetak_struk(daftar_pesanan, total_harga)


if __name__ == "__main__":
    main()