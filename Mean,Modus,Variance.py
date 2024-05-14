# input data
data = []
for i in range (10):
    angka = int(input(f"data ke-{i} : "))
    data.append(angka)

# Menghitung mean
def hitung_mean(data):
    return sum(data) / len(data)

# menghitung modus
def hitung_modus(data):
    frek = [0] * (max(data) + 1)

    for angka in data:
        frek[angka] += 1

    frek_tinggi = max(frek)

    modus = []
    for angka in data:
        if frek[angka] == frek_tinggi and angka not in modus:
            modus.append(angka)
    return modus

# hitung variance
def variance(data):
    m = hitung_mean(data)
    var = sum((x - m) ** 2 for x in data) / len(data)
    return var

# print hasil mean, modus, variance
def hasil():
    mean = hitung_mean(data)
    modus = hitung_modus(data)
    var = variance(data)

    print(f"| mean     |{mean:4} |")

    if len(modus) == 1:
        print(f"| modus    | {modus[0]}   |")
    else :
        print(f"| modus    | {modus}   |")
    print(f"| variance |{var:4} |")
hasil()