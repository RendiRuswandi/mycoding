english = int(input("Masukan nilai : "))
matematika = int(input("Masukan nilai : "))
indonesia = int(input("Masukan nilai : "))
ipa = int(input("Masukan nilai : "))
ips = int(input("Masukan nilai : "))

ratarataSatu = (english + matematika + indonesia) / 3
ratarataDua = (english + matematika + indonesia + ipa + ips) / 5

if ratarataSatu >= 75 :
    kelulusan = "Lulus"
elif ratarataDua >= 70 :
    kelulusan = "Lulus"
elif matematika > 90 and english > 90 :
    kelulusan = "Lulus"
else :
    kelulusa = "Tidak lulus"

print (kelulusan)