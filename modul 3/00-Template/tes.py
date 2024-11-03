# Meminta input dari pengguna
angka = int(input("Masukkan sebuah bilangan bulat: "))

# Menggunakan statement if untuk menentukan genap atau ganjil
if angka % 2 == 0:
    print(f"{angka} adalah bilangan genap.")
else:
    print(f"{angka} adalah bilangan ganjil.")