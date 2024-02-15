# 1. Membuat dasar kode terlebih dulu
def angka (i):
  print(f'Angka ke {i}')

# angka dipanggil beberapa kali
angka(1)
angka(2)
angka(3)
# output -> Angka ke 1, Angka ke 2, Angka ke 3

# 2. Membuat batas dari perulangan
def angka (batas, i = 1): #batas = batas perulangan, i = penanda iterasi ke berapa (opsional)
  print(f'Angka ke {i}')

# angka dipanggil beberapa kali
angka(3)
angka(3, 2)
angka(3, 3)
# output -> Angka ke 1, Angka ke 2, Angka ke 3

# 3. Membuat recursive function
# misal ingin menampilkan 10 angka
def angka (batas, i = 1): # parameter batas selalu bernilai 10, i bernilai 1-10
  print(f'Angka ke {i}')

  if (i < batas):
    # disini recursive function terjadi, apabila nilai 1 sudah mencapai batas,
    # maka recursive function berhenti
    angka(batas, i + 1)

# memanggil fungsi angka untuk pertama kali
angka(10)
# output -> Angka ke 1, Angka ke 2, ...., Angka ke 10

# 4. Percobaan bagaimana bila print() nya diletakkan di akhir function (setelah recursive)?
def angka (batas, i = 1):
  if (i < batas):
    # disini recursive function terjadi
    angka(batas, i + 1)

  print(f'Perulangan ke {i}') # print() pindah disini

# memanggil fungsi angka untuk pertama kali
angka(10)
# output -> Angka ke 10, Angka ke 9, ..., Angka ke 1 (terbalik)

# Penyebab, berikut alur kerja dari kode itu:
i = 1
batas = 3

if i < batas:
  iDua = i + 1
  if iDua < batas:
    iTiga = iDua + 1
    if iTiga < batas:
      iEmpat = iTiga + 1
      if iEmpat < batas:
        iLima = iEmpat + 1
        # dan seterusnya
        print(iLima)
      print(iEmpat)
    print(iTiga)
  print(iDua)
print(i)

# Alur kode:
"""
1. Yang pertama dipanggil adalah function angka(10)
2. Lalu function memanggil dirinya sendiri sebelum melakukan print()
3. print() akan bekerja saat proses recursive sudah selesai, 
alias setelah pengambilan function angka() yang kedua selesai
4.  Namun ternyata, ketika memanggil recursive yang kedua kalinya,
dia langsung memanggil dirinya sendiri untuk yang ketiga kalinya.
Dia hanya akan melakukan perintah print() ketika proses pemanggilan yang ketiga selesai.
5. Begitulah seterusnya hingga proses recursive berakhir, 
sehingga perintah print() yang pertama kali dilakukan adalah yang ketiga.

Dengan kata lain: Fungsi yang pertama kali dipanggil, adalah fungsi yang terakhir kali selesai. 
Dan fungsi yang terakhir kali dipanggil, ia adalah fungsi yang paling pertama selesai.
"""