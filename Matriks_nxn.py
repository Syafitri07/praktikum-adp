#Input Matriks A
print("/Data Matriks A")
r = int(input("Masukkan jumlah baris : "))
k = int(input("Masukkan jumlah kolom : "))
A = []
for i in range (r):
    matriksA = []
    for j in range (k):
        data = int(input(f"Data [{i}][{j}] : "))
        matriksA.append(data)
    A.append(matriksA)
print()

#Input Matriks B
print("/Data Matriks B")
br = int(input("Masukkan jumlah baris : "))
kl = int(input("Masukkan jumlah kolom : "))
B = []
for v in range (br):
    matriksB = []
    for w in range (kl):
        data1 = int(input(f"Data [{v}][{w}] : "))
        matriksB.append(data1)
    B.append(matriksB)

#Matriks C (Hasil Perkalian Matriks A dan B)
hasil = []
for x in range (0, len(A)):
    kali = []
    for y in range (0, len(A[0])):
        hasil_perkalian = A[x][y] * B[x][y]
        kali.append(hasil_perkalian)
    hasil.append(kali)

#Matriks D (Hasil Penjumlahan Matriks A Transpose dan Matriks B Transpose)
transposeA = [[0,0],[0,0]]
for p in range (len(A)):
    for q in range (len(A[0])):
        transposeA[q][p] = A[p][q] 

transposeB = [[0,0],[0,0]]
for s in range (len(B)):
    for t in range (len(B[0])):
        transposeB[t][s] = B[s][t] 

hasil1 = []
for c in range (0, len(transposeA)):
    sum = []
    for d in range (0, len(transposeA[0])):
        hasil_pertambahan = transposeA[c][d] + transposeB[c][d]
        sum.append(hasil_pertambahan)
    hasil1.append(sum)

#Matriks A, B , C , D
print("\nMatriks A =", A)
print("-----------------------------------------") 
print("\nMatriks B =", B)
print("-----------------------------------------")  
print("\nMatriks C =", hasil)
print("-----------------------------------------") 
print("\nTranspose Matriks A =", transposeA)    
print("Transpose Matriks B =", transposeB) 
print("-----------------------------------------")  
print("\nMatriks D =", hasil1)
print("-----------------------------------------")  