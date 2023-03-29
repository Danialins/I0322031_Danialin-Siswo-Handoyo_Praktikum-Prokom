#sub utama program
pelanggan = []
alamat = []
nohanphone = []

 #sub program masukkan pelanggan dibuat oleh budi
def masukkanpelanggan():
    pelangganBaru = input("masukkan nama pelanggan = ")
    pelanggan.append(pelangganBaru)
    alamatBaru = input("masukkan alamat pelanggan = ")
    alamat.append(alamatBaru)
    nomorhpBaru = input("masukkan nomor hp = ")
    nohanphone.append(nomorhpBaru)
    
  # sub program masukkan pelanggan dibuat oleh fani
    tampilkandata2 = """
        nama pelanggan   \t: {0}
        alamat pelanggan \t: {1}
        no. telepon      \t: {2}
    """
    def tampilkandata():
        for i in range(0, len(pelanggan)):
            print(tampilkandata2.format(pelanggan[i], alamat[i], nohanphone[i]))
    
    # sub program yang dibuaat oleh ali
        
    jawaban = input("apakah anda ingin memasukkan data pelanggan (ya/tidak)? ")
    while jawaban in ('ya', 'Ya'):
        
        masukkanpelanggan()
        jawaban = input("apakah anda ingin memasukkan data pelanggan (ya/tidak)? ")
    
    masukkanpelanggan()