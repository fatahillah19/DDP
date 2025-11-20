# Data bensin
bensin = {
    "pertalite": {"harga": 10000, "jarak_tempuh": 12},
    "pertamax": {"harga": 14000, "jarak_tempuh": 13},
    "pertamax turbo": {"harga": 17000, "jarak_tempuh": 13.5}
}

# Data kota
kota = {
    "jakarta": 20,
    "bekasi": 35.7,
    "depok": 5,
    "tangerang": 99,
    "bogor": 120.6
}

# Input
kendaraan = input("Nama kendaraan (mobil/motor): ")
jenis_bensin = input("Jenis bensin (Pertalite, Pertamax, Pertamax Turbo): ").lower()
tujuan = input("Kota yang dituju: ").lower()

# Ambil data
harga = bensin[jenis_bensin]["harga"]
jarak_tempuh = bensin[jenis_bensin]["jarak_tempuh"]
jarak_kota = kota[tujuan]

# Perhitungan
pemakaian = jarak_kota / jarak_tempuh
total_harga = pemakaian * harga

# Output
print("\n=== HASIL PERHITUNGAN ===")
print("Nama Kendaraan :", kendaraan)
print("Jenis Bensin   :", jenis_bensin.title())
print("Kota Tujuan    :", tujuan.title())
print("Pemakaian Bensin:", round(pemakaian, 2), "liter")
print("Total Harga     : Rp", round(total_harga))
