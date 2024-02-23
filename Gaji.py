gajiBulanan = int(input("Gaji bulanan : "))
masukKerja = int(input("Berapa hari anda masuk kerja : "))
uangTransport = 100000 * masukKerja
uangMakan = 50000 * masukKerja
hariLembur = int(input("Berapa jam kerja lembur anda : "))

if hariLembur <= 2:
    totalLembur = hariLembur * 100000
else : 
    totalLembur = 2 * 100000 + (hariLembur - 2) * 150000
honor = gajiBulanan+uangTransport+uangMakan+totalLembur

print("Uang honor yang didapat Rp.%i"%honor)