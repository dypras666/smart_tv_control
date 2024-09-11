# Smart TV Control

Script Python ini memungkinkan Anda mengendalikan smart TV menggunakan perintah ADB (Android Debug Bridge) melalui koneksi jaringan. Script ini menyediakan antarmuka command-line sederhana untuk melakukan berbagai tindakan seperti menyalakan/mematikan TV, mengontrol volume, mengganti channel, dan navigasi.

## Fitur

- Menyalakan/mematikan TV
- Kontrol volume (naik, turun, mute)
- Mengganti channel
- Navigasi (home, back, menu, pad arah)
- command-line sederhana

## Prasyarat

- Python 3.x
- ADB (Android Debug Bridge) terinstal dan tersedia di PATH sistem Anda
- Smart TV yang mendukung koneksi ADB melalui jaringan

## Instalasi

1. Clone repository ini atau unduh file script-nya.
2. Pastikan Anda telah menginstal Python 3.x di sistem Anda.
3. Instal ADB jika belum ada. Anda bisa mengunduhnya sebagai bagian dari Android SDK Platform Tools.

## Cara Mengubah Alamat IP TV

Sebelum menjalankan script, Anda perlu mengatur alamat IP TV Anda. Berikut langkah-langkahnya:

1. Buka file `smart_tv_control.py` menggunakan editor teks.
2. Cari fungsi `main()` di bagian bawah script.
3. Temukan baris yang berisi: `tv_ip = "192.168.1.5"  # IP address smart tv`
4. Ganti "192.168.1.5" dengan alamat IP smart TV Anda.
   Contoh: Jika alamat IP TV Anda adalah 192.168.0.100, maka ubah baris tersebut menjadi:
   ```python
   tv_ip = "192.168.0.100"  # IP address smart tv
   ```
5. Simpan perubahan pada file.

Catatan: Anda dapat menemukan alamat IP TV Anda biasanya di pengaturan jaringan TV. Pastikan TV dan komputer Anda terhubung ke jaringan yang sama.

## Penggunaan

1. Pastikan smart TV dan komputer yang menjalankan script ini berada dalam jaringan yang sama.
2. Aktifkan debugging ADB pada smart TV Anda (lihat manual TV Anda untuk instruksi).
3. Jalankan script:

   ```
   python smart_tv_control.py
   ```

4. Ikuti menu di layar untuk mengendalikan TV Anda.

## Opsi Menu

1. Nyalakan/Matikan
2. Volume Naik
3. Volume Turun
4. Mute
5. Ganti Channel
6. Home
7. Kembali
8. Menu
9. Navigasi (Atas/Bawah/Kiri/Kanan/Enter)
0. Keluar

## Kontrol Navigasi

Saat dalam mode navigasi (opsi 9), gunakan tombol berikut:

- 'u': Atas
- 'd': Bawah
- 'l': Kiri
- 'r': Kanan
- 'e': Enter
- 'q': Keluar dari mode navigasi

## Pemecahan Masalah

- Jika Anda tidak dapat terhubung ke TV, pastikan bahwa:
  - TV dan komputer Anda berada dalam jaringan yang sama
  - Debugging ADB diaktifkan pada TV Anda
  - Alamat IP di script cocok dengan alamat IP TV Anda
  - Firewall TV Anda tidak memblokir koneksi
- Jika perintah tidak berfungsi, coba putuskan koneksi dan hubungkan kembali menggunakan alat command line ADB.

## Berkontribusi

Kontribusi, masalah, dan permintaan fitur dipersilakan. Jangan ragu untuk memeriksa halaman masalah jika Anda ingin berkontribusi.

## Lisensi

[MIT](https://choosealicense.com/licenses/mit/)