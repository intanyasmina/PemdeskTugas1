def angkaMax(daftar):
    maksimal=0
    for a in (daftar):
        if a > maksimal:
            maksimal= a
    return maksimal
def angkaMin(daftar1):
    minimal=999
    for b in (daftar1):
        if b < minimal:
            minimal=b
    return minimal

jumlahAngka= []
angka= int(input("Berapa banyak angka "))
for n in range(angka):
    nilai=int(input("Masukkan angka"))
    jumlahAngka.append(nilai)
print("Angka maksimum:",angkaMax(jumlahAngka))
print("Angka minimal:",angkaMin(jumlahAngka))
