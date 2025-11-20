jumlah = int(input("Masukkan jumlah pembelian: "))

total = jumlah * 0.9 if jumlah > 100 else jumlah
print(f"Total yang di bayar: ", total)