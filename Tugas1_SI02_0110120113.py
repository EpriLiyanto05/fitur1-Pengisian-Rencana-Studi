#Fitur 1 : Pengisian Rencana Studi Bagi Mahasiswa
print("Fitur Pengisian Rencana Studi")
#Disini Mahasiswa akan diminta untuk memasukkan NIM nya, dengan format 01102XXYYY, dengan XX adalah tahun masuk dan YYY adalah urutan daftar mahasiswa.
NIM = input("Masukkan NIM: ")
jumlahhuruf = len(NIM)
#jika Mahasiswa masuk pada tahun 2020 berarti memasukkan angka 20, dan hanya dapat mengambil 20 SKS
if jumlahhuruf == 10 and NIM[5:7]== "20":
  print("Anda mahasiswa tahun pertama. Anda bisa mengambil paling banyak 20 SKS.")
  print()
  jumlahsks = 0
  while True:
    jumlah = print("Jumlah SKS yang diambil: ", jumlahsks)
#silahkan masukkan mata kuliah yang akan di ambil, dan ketik huruf kapital "X" jika selesai
    a = input("Masukkan nama mata kuliah yang diambil atau X untuk selesai: ")
    if a == "X":
      print("Pengisian Rencana studi selesai.")
      break
#masukkanlah jumlah SKS mata kuliah tersebut
    b = int(input("Masukkan beban SKS mata kuliah tersebut: "))
    jumlahsks = jumlahsks + b
#jumlah SKS yang dapat diambil oleh mahasiswa tahun pertama adalah 20 SKS, jika lebih maka otomatis program akan berhenti
    if jumlahsks <= 20:
     print("Berhasil mengambil mata kuliah", a, "dengan bobot", b, "SKS")
    elif jumlahsks >= 20:
      print("Jumlah SKS melebihi SKS maksimal. Pengisian Rencana Studi Selesai.")
      break
    print()
#jika Mahasiswa masuk pada tahun 2019 berarti memasukkan angka 19, dan dapat mengambil 22 SKS
elif jumlahhuruf == 10 and NIM[5:7]== "19":
  print("Anda mahasiswa tahun kedua. Anda bisa mengambil paling banyak 22 SKS.")
  print()
  jumlahsks = 0
  while True:
    jumlah = print("Jumlah SKS yang diambil: ", jumlahsks)
#silahkan masukkan mata kuliah yang akan di ambil, dan ketik huruf kapital "X" jika selesai
    a = input("Masukkan nama mata kuliah yang diambil atau X untuk selesai: ")
    if a == "X":
      print("Pengisian Rencana studi selesai.")
      break
#masukkanlah jumlah SKS mata kuliah tersebut
    b = int(input("Masukkan beban SKS mata kuliah tersebut: "))
    jumlahsks = jumlahsks + b
#jumlah SKS yang dapat diambil oleh mahasiswa tahun kedua adalah 22 SKS, jika lebih maka otomatis program akan berhenti
    if jumlahsks <= 22:
     print("Berhasil mengambil mata kuliah", a, "dengan bobot", b, "SKS")
    elif jumlahsks >= 22:
      print("Jumlah SKS melebihi SKS maksimal. Pengisian Rencana Studi Selesai.")
      break
    print()
#jika Mahasiswa masuk pada tahun 2018 berarti memasukkan angka 18, dan dapat mengambil 24 SKS
elif jumlahhuruf == 10 and NIM[5:7]== "18":
  print("Anda mahasiswa tahun ketiga. Anda bisa mengambil paling banyak 24 SKS.")
  print()
  jumlahsks = 0
  while True:
    jumlah = print("Jumlah SKS yang diambil: ", jumlahsks)
#silahkan masukkan mata kuliah yang akan di ambil, dan ketik huruf kapital "X" jika selesai
    a = input("Masukkan nama mata kuliah yang diambil atau X untuk selesai: ")
    if a == "X":
      print("Pengisian Rencana studi selesai.")
      break
#masukkanlah jumlah SKS mata kuliah tersebut
    b = int(input("Masukkan beban SKS mata kuliah tersebut: "))
    jumlahsks = jumlahsks + b
#jumlah SKS yang dapat diambil oleh mahasiswa tahun kedua adalah 24 SKS, jika lebih maka otomatis program akan berhenti
    if jumlahsks <= 24:
     print("Berhasil mengambil mata kuliah", a, "dengan bobot", b, "SKS")
    elif jumlahsks >= 24:
      print("Jumlah SKS melebihi SKS maksimal. Pengisian Rencana Studi Selesai.")
      break
    print()
#jika Mahasiswa masuk pada tahun 2017 berarti memasukkan angka 17, dan dapat mengambil 26 SKS
elif jumlahhuruf == 10 and NIM[5:7]== "17":
  print("Anda mahasiswa tahun keempat. Anda bisa mengambil paling banyak 26 SKS.")
  print()
  jumlahsks = 0
  while True:
    jumlah = print("Jumlah SKS yang diambil: ", jumlahsks)
#silahkan masukkan mata kuliah yang akan di ambil, dan ketik huruf kapital "X" jika selesai
    a = input("Masukkan nama mata kuliah yang diambil atau X untuk selesai: ")
    if a == "X":
      print("Pengisian Rencana studi selesai.")
      break
#masukkanlah jumlah SKS mata kuliah tersebut
    b = int(input("Masukkan beban SKS mata kuliah tersebut: "))
    jumlahsks = jumlahsks + b
#jumlah SKS yang dapat diambil oleh mahasiswa tahun kedua adalah 26 SKS, jika lebih maka otomatis program akan berhenti
    if jumlahsks <= 26:
     print("Berhasil mengambil mata kuliah", a, "dengan bobot", b, "SKS")
    elif jumlahsks >= 26:
      print("Jumlah SKS melebihi SKS maksimal. Pengisian Rencana Studi Selesai.")
      break
    print()
else:
  print("NIM tidak valid")
