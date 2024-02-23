tahun = int(input("Tahun : "))

if tahun % 4 == 0:
    status = ("Tahun kabisat")
else :
    status = ("Bukan tahun kabisat")
print(status)