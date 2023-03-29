#fungsi untuk menampilkan data base
bunga = ["mawar,anggrek,dandelion,matahari,lili,melati,tulip"]

def tampil_data ():
    print("daftar nama yang ada")
    if len(bunga)==0:
        print("belum ada data bunga")
    else :
        for indek in range (0,len(bunga)):
            print("no = ", indeks, " " , bunga [indeks])