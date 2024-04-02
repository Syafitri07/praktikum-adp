print("========Toko Baju Edisi Lebaran 2024========")
daftar_belanja = {
    "gamis anak": 135000,
    "gamis dewasa": 220000,
    "koko anak": 90000,
    "koko dewasa": 150000,
    "rok kargo anak": 140000,
    "rok kargo dewasa": 200000,
    "baju blus anak cewek": 50000,
    "baju blus dewasa cewek": 70000,
    "celana anak cowok": 70000,
    "celana dewasa cowok": 156000,
    "jilbab": 20000
}
total_harga = 0
keranjang = {}
while True:
    print("\nDaftar Belanja")
    for belanja, harga in daftar_belanja.items():
        print(f"{belanja} : Rp.{harga}")
    beli = input("Masukkan 'nama' belanjaan anda (atau ketik 'selesai' untuk selesai belanja): ")

    if beli.lower() == "selesai":
        break

    if beli in daftar_belanja:
        if beli in keranjang:
            keranjang[beli] += 1
        else:
            keranjang[beli] = 1
        total_harga += daftar_belanja[beli]
        print(f"{beli} ditambahkan ke dalam keranjang")
    else: print("Barang tidak tersedia. Silahkan pilih belanja lainnya")

if total_harga >= 400000:
    diskon = 0.1 * total_harga
else:
    diskon = 0

total_belanja_setelah_diskon = total_harga - diskon

print("\nDaftar belanja anda:")
for belanja, jumlah in keranjang.items():
    print(f"- {belanja} : {jumlah} pcs")

print("========================")
print(f"Total Harga: Rp.{total_harga:.2f}")
print(f"diskon 10%: Rp.{diskon:.2f}")
print(f"Total Harga Setelah Diskon: Rp.{total_belanja_setelah_diskon:.2f}")
print("========================")
print("Terimakasih sudah berbelanja")
print("Selamat Hari Raya Idul Fitri")
print("========================")