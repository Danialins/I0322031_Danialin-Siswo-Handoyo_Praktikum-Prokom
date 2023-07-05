#Membuat modul
import math

#volume dan Luas permukaan kubus 
def kubus (sisi):
    volume = sisi**3
    luas_permukaan = 6 * sisi**2
    return volume, luas_permukaan

#volume dan luas permukaan balok
def balok(panjang, lebar, tinggi):
    volume = panjang * lebar * tinggi
    luas_permukaan = 2 * (panjang * lebar + panjang * tinggi + lebar * tinggi)
    return volume, luas_permukaan

#volume dan luas permukaan bola
def bola(jari_jari):
    volume = (4/3) * math.pi * jari_jari**3
    luas_permukaan = 4 * math.pi * jari_jari**2
    return volume, luas_permukaan