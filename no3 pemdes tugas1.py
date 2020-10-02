print("PROGRAM BODY MASS INDEX")
berat = float(input("Masukkan Berat Badan Anda(cm): "))
tinggi = float(input("Masukkan Tinggi Badan Anda(kg): "))
Bmi=round (berat / tinggi**2)
print("Hasil Perhitungan: ", Bmi)

if Bmi <18.5:
    print ("Berat badan anda kurang")
elif Bmi >=18.5 and Bmi <=22.9:
    print("Berat badan anda normal")
elif Bmi >=23 and Bmi <=29.9:
    print("Bearat badan anda berlebih")
elif Bmi >=30:
    print ("Obesitas")
