# program Grading Nilai
nama = str(input("Masukan Nama: "))
nilai = int(input("Masukan Nilai: "))

hasil = None
if(nilai >= 85 and nilai <=100):
    hasil = 'A'
    print("Hallo",nama,"! Nilai anda setelah dikonversi adalah",hasil)
elif(nilai >= 80 and nilai <=84):
    hasil = 'A-'
    print("Hallo",nama,"! Nilai anda setelah dikonversi adalah",hasil)
elif(nilai >= 75 and nilai <=79):
    hasil = 'B+'
    print("Hallo",nama,"! Nilai anda setelah dikonversi adalah",hasil)
elif(nilai >= 70 and nilai <=74):
    hasil = 'B'
    print("Hallo",nama,"! Nilai anda setelah dikonversi adalah",hasil)
elif(nilai >= 65 and nilai <=69):
    hasil = 'C+'
    print("Hallo",nama,"! Nilai anda setelah dikonversi adalah",hasil)
elif(nilai >= 60 and nilai <=64):
    hasil = 'C'
    print("Hallo",nama,"! Nilai anda setelah dikonversi adalah",hasil)
elif(nilai < 60):
    hasil = 'E'
    print("Hallo",nama,"! Nilai anda setelah dikonversi adalah",hasil)
else:
    print("invalid number")