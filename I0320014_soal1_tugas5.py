# membuat program untuk menyapa pengunjung
nama = str(input("Masukan Nama: "))
jenis_kelamin = str(input("Masukan Jenis Kelamin: "))

if (jenis_kelamin == "Laki-Laki" or jenis_kelamin == "laki-laki"):
    gender = 'Tuan'
    print ("Selamat Datang,",gender,"",nama,"!")
else:
    gender = 'Nyonya'
    print ("Selamat Datang,",gender,"",nama,"!")