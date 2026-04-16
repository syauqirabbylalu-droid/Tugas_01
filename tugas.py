data_tuple = ("apel", "jeruk", "mangga", "pisang")

def tampilkan_tuple():
    print("\nIsi Tuple:", data_tuple)
    print("jumlah Elemen:", len(data_tuple)) 

def akses_halaman(): 
    try :
        index = int(input("masukan indeks: "))
        print("Elemen pada indeks tersebut:", data_tuple[index])
    except:
        print("Index tidak valid!")
        
def slicing_tuple():
    try:
        start = int(input("Start index: "))
        stop = int(input("Stop index: "))
        print("hasil slicing:", data_tuple[start:stop])
    except :
        print("Input tidak valid")
        
def gabung_tuple():
    tup_baru = tuple(input("Masukan elemen tambahan (pisah koma): ").split(","))
    hasil = data_tuple + tup_baru
    print("Hasil penggabungan:", hasil)
    
def ulang_tuple():
    try:
        n = int(input("Berapa kali pengulangan: "))
        hasil = data_tuple * n
        print("Hasil pengulangan:", hasil)
    except:
        print("Input tidak valid!")
    
def ubah_tuple():
    global data_tuple
    print("\nMengubah tuple (via list)...")
    temp_list = list(data_tuple)
    print("Isi saat ini:", temp_list)
    print("1. Tambah data")
    print("2. Ubah data")
    print("3. Hapus data")
    pilihan = input("Pilih: ")

    if pilihan == "1":
        item = input("Masukkan data baru: ")
        temp_list.append(item)
    
    elif pilihan == "2":
        try:
            i = int(input("Index yang diubah: "))
            nilai = input("Nilai baru: ")
            temp_list[i] = nilai
        except:
            print("Index tidak valid!")
            
    elif pilihan == "3":
        try:
            i = int(input("Index yang dihapus: "))
            temp_list.pop(i)
        except:
            print("Index tidak valid!")
            
    # Kembali ke tuple
    data_tuple = tuple(temp_list)
    print("Tuple baru:", data_tuple)
    
# Program utama
while True:
    print("\n==== MENU PRAKTIKUM TUPLE ====")
    print("1. Tampilkan Tuple")
    print("2. Akses Elemen")
    print("3. Slicing Tuple")
    print("4. Gabung Tuple")
    print("5. Ulang Tuple")
    print("6. Ubah Tuple (via List)")
    print("7. Keluar")

    pilih = input("Pilih menu: ")

    if pilih == "1":
        tampilkan_tuple()
    elif pilih == "2":
        akses_halaman()
    elif pilih == "3":
        slicing_tuple()
    elif pilih == "4":
        gabung_tuple()
    elif pilih == "5":
        ulang_tuple()
    elif pilih == "6":
        ubah_tuple()
    elif pilih == "7":
        print("Program selesai.")
        break
    else:
        print("Pilihan tidak valid!")