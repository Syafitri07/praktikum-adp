# Menambahkan data film
def tambah(Judul, Nama_penulis_skenario, Nama_sutradara, Tahun_rilis):
    with open("film.txt","a") as f:
        f.write(f"{Judul}, {Nama_penulis_skenario}, {Nama_sutradara}, {Tahun_rilis}\n")
    print("Data film berhasil ditambahkan.\n")

# Menghapus data film
def hapus(Judul):
    with open("film.txt","r") as f:
        lines = f.readlines()
    with open("film.txt","w") as f:
        for line in lines:
            if not line.startswith(Judul):
                f.write(line)
    print("Data film berhasil dihapus.\n")

# Mengedit data film
def edit (Judul, Nama_penulis_skenario, Nama_sutradara, Tahun_rilis):
    with open("film.txt","r") as f:
        perfilm = f.readlines()
    with open("film.txt","w") as f:
        for film in perfilm:
            if film.split(",")[0] == Judul:
                f.write(f"{Judul}, {Nama_penulis_skenario}, {Nama_sutradara}, {Tahun_rilis}\n")
            else:
                f.write(film)
    print("Data film telah diubah.\n")

# Menampilkan data film
def menampilkan():
    with open("film.txt","r") as f:
        data_film = f.readlines()
        if data_film:
            print("Kumpulan Film kamu:")
            for data in data_film:
                print(data.strip())
        else:
            print("Film mu tidak ada nih.\n")

#Pilihan Menu
while True:
    print("\nPilihan Menu")
    print("1. Tambah data film")
    print("2. Hapus data film")
    print("3. Edit data film")
    print("4. Menampilkan data film")
    print("5. selesai")

    pil = input("Pilih menu (1/2/3/4/5): ")
    print()

    if pil == "1":
        Judul = input("Judul : ")
        Nama_penulis_skenario = input("Nama penulis skenario : ")
        Nama_sutradara = input("Nama Sutradara : ")
        Tahun_rilis = input("Tahun rilis: ")
        tambah(Judul, Nama_penulis_skenario, Nama_sutradara, Tahun_rilis)
    if pil == "2":
        Judul = input("Masukkan judul yang akan dihapus: ")
        hapus(Judul)
    if pil == "3":
        Judul = input("Judul baru : ")
        Nama_penulis_skenario = input("Nama penulis skenario baru : ")
        Nama_sutradara = input("Nama Sutradara baru : ")
        Tahun_rilis = input("Tahun rilis baru : ")
        edit(Judul, Nama_penulis_skenario, Nama_sutradara, Tahun_rilis)
    if pil == "4":
        menampilkan()
    if pil == "5":
        print("Data film anda telah kami simpan dengan baik. Silahkan buka file baru")
        break