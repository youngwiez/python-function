# Recursive Function Python

## Pengertian
Function yang memanggil dirinya sendiri di dalam suatu function.
Dapat secara intuitif dan sederhana memecahkan masalah yang sulit diselesaikan dengan teknik prosedural.

Function yang pertama kali dipanggil, adalah function yang terakhir kali selesai 
dan function yang terakhir kali dipanggil, ia adalah function yang paling pertama selesai

Contoh yang sering dipakai dalam recursive function adalah faktorial, menghitung deret angka.

## Kelebihan
1. Function yang rumit dapat dipecah menjadi subfunction yang lebih kecil dengan menggunakan recursive
2. Mampu membuat urutan lebih sederhana dengan recursive dibandingkan menggunakan iteration
3. Membuat kode terlihat sederhana dan efektif

## Kekurangan
1. Banyak memori dan waktu yang diambil oleh recursive function
2. Sulit untuk di-debug

## Contoh
![Contoh Recursive Function](https://www.bhutanpythoncoders.com/wp-content/uploads/2021/12/recursive-function.jpg)

Dari kode di atas, kita membuat basis kasus dengan mengecek apakah x sama dengan 1. Jika ya, maka kita langsung mengembalikan nilai 1. Jika tidak, kita kembalikan nilai x dikalikan dengan faktorial dari x - 1. Fungsi akan terus memanggil dirinya sendiri dengan mengurangi nilai x sampai x sama dengan 1, di mana basis kasus terpenuhi dan fungsi akan berhenti memanggil dirinya.
