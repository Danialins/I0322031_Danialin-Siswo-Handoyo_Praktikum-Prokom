def luas_persegi (p,l):
    luas = (p*l)
    print ("-------------------------")
    print ("luas_persegi: %f" %luas )

def luas_segitiga (p,l):
    luas = (p*l) / 2
    print ("--------------------------")
    print ("luas_segitiga: %f" %luas )

def keliling_persegi(p,l):
    keliling = (p + l) * 2 
    print ("--------------------------")
    print ("keliling_persegi: %f" %keliling )

def luas_kubus(sisi):
    luaskubus=sisi*sisi
    return luaskubus

def volume_kubus(sisi):
    volume = luas_kubus(sisi) * sisi
    return volume 

# Pemanggilan Fungsi
p = int(input("masukkan alas"))
l = int(input("masukkan tinggi"))
sisi = int(input("masukkan sisi kubus"))
luas_persegi (p,l)
luas_segitiga(p,l)
keliling_persegi(p,l)
volume_kubus(sisi)
print("============================")
print ("volume_kubus: %f" %volume_kubus(sisi))




  
