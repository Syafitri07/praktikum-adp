#rumus_matematika
#menentukan_volume_tabung_kerucut_dan_limas_segitiga
phi = float("3.14")
print("phi = ")
print(phi)
print("jari-jari = ")
r = int(input())
print("tinggi = ")
t = int(input())
print("alas = ")
a = int(input())
print("tinggi limas = ")
T = int(input())
volume_tabung = phi*r*r*t
volume_kerucut = float(1/3*phi*r*r*t)
volume_limas_segitiga = float(1/6*a*t*T)
print("volume tabung adalah ")
print(volume_tabung)
print("volume kerucut adalah ")
print(volume_kerucut)
print("volume limas segitiga adalah ")
print(volume_limas_segitiga)