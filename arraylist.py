# Fungsi untuk menambahkan teman ke dalam list
def tambahkan_teman(teman, nama):
    teman.append(nama)
    print("Teman", nama, "telah ditambahkan.")

# Fungsi untuk menghapus teman dari list
def hapus_teman(teman, nama):
    if nama in teman:
        teman.remove(nama)
        print("Teman", nama, "telah dihapus.")
    else:
        print("Teman", nama, "tidak ditemukan dalam daftar.")

# Fungsi untuk menampilkan semua teman dalam list
def tampilkan_nama(teman):
    if teman:
        print("Daftar Teman:")
        for nama in teman:
            print("-", nama)
    else:
        print("Daftar teman kosong.")

# List untuk menyimpan nama-nama teman
daftar_teman = []

# Menu utama
while True:
    print("\nMenu:")
    print("1. Tambahkan Teman")
    print("2. Hapus Nama")
    print("3. Tampilkan Nama")
    print("4. Exit")

    pilihan = input("Pilih menu: ")

    if pilihan == '1':
        nama_teman = input("Masukkan nama teman yang ingin ditambahkan: ")
        tambahkan_teman(daftar_teman, nama_teman)
    elif pilihan == '2':
        nama_teman = input("Masukkan nama teman yang ingin dihapus: ")
        hapus_teman(daftar_teman, nama_teman)
    elif pilihan == '3':
        tampilkan_nama(daftar_teman)
    elif pilihan == '4':
        print("Terima kasih!")
        break
    else:
        print("Menu tidak valid. Silakan pilih kembali.")
