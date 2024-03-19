
print("---------------MENU_PAKET----------------")

print("1. Paket A = Rp.25000")
print("2. Paket B = Rp.30000")
print("3. Paket C = Rp.45000")
nomor = int(input("\nMasukkan pilihan: "))
porsi = int(input("Berapa porsi: "))

if nomor == 1:
    biayapaket = porsi*25000
    print(porsi, "porsi paket A = Rp.", biayapaket)
elif nomor == 2:
    biayapaket = porsi*30000
    print(porsi, "porsi paket B = Rp.", biayapaket)
elif nomor == 3:
    biayapaket = porsi*45000
    print(porsi, "porsi paket C = Rp.", biayapaket)
else : print("Tidak jenis paket")

print("------JARAK_DARI_RUMAH_KE_PERUSAHAAN------")

print("1. Ongkir < 500 m          = gratis")
print("2. 500 m < Ongkir < 1.5 km = Rp. 10000")
print("3. Ongkir >= 1.5 km        = Rp. 20000")
nomor = int(input("\nMasukkan pilihan : "))
            
if nomor == 1:
    ongkir = 0
    print("Ongkir = Rp.", ongkir)
elif nomor == 2:
    ongkir = 10000
    print("Ongkir = Rp.", ongkir)
elif nomor == 3:
    ongkir = 20000
    print("ongkir = Rp.", ongkir)
else : print("Tidak Ada Pilihan")

totalharga = biayapaket + ongkir
print("Total Harga Anda adalah", totalharga)