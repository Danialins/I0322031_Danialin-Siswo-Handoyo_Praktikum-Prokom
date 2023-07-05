a =int(input("masukkan jumlah penumpang: "))
b =input ("masukkan tujuan: ")
tol = input("apakah lewat jalan tol (ya/tidak) : ")
member = input ("apakah member (ya/tidak): ")

# jalur biasa
#tujuan 
if b == "semarang":
    biaya = 120000
    if member == "ya":
        diskon = 0.20
elif b == "jakarta":
    biaya = 250000
    if member == "ya":
        diskon = 0.15
elif b == "surabaya":
    biaya = 200000
    if member == "ya":
        diskon = 0.30
elif b == "malang":
    biaya = 240000
    if member == "ya":
        diskon = 0.10
else:
    print("kota tujuan belum terdaftar")

# jalur 
if tol == "ya":
    output = "melewati_tol"
    tol = 75000
elif tol == "tidak":
    output = "tidak melewati tol"
    tol = 0
else :
    print("perintah tidak valid")

# print output
total = ((int(a)*int(biaya)) + (int(a)*int(tol)))*(1-diskon)
print (total)










