def menu():
	print("--Menghitung Luas dan Keliling Persegi--")
	print("1. Luas")
	print("2, Keliling")
	choose=int(input("masukkan pilihan anda = "))
	if choose==1:
		print(luas1())
	elif choose==2:
		print(keliling1())
	else:
		print("yang anda input tidak ada di menu")

		
def luas1():
        print("----------------------")
        print("====Menghitung Luas Persegi====")
        s=int(input("masukkan sisi ="))
        luas = (s*s)
        return luas

def keliling1():
        print("----------------------")
        print("====Menghitung Luas Persegi====")
        s=int(input("masukkan sisi ="))
        keliling = (4*s)
        return keliling
menu()
        
