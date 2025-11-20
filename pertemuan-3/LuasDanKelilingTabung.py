# Program 5: Luas dan Keliling Tabung
import math

a = float(input("Masukkan jari-jari tabung (cm): "))
b = float(input("Masukkan tinggi tabung (cm): "))

luas_permukaan = 2 * math.pi * a * (a + b)  
keliling_alas = 2 * math.pi * a 

print("Luas permukaan tabung:", luas_permukaan, "cm²")
print("Keliling alas tabung:", keliling_alas, "cm")
