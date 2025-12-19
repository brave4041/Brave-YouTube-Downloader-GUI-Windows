<div align="center">

# 🎥 Brave Download Manager
**Simple & Modern GUI for YT-DLP**

[![Brave404 - Project](https://img.shields.io/badge/Brave404-Project-red?style=for-the-badge&logo=youtube)](https://github.com/brave4041)
[![Powered By - YT-DLP](https://img.shields.io/badge/Powered_By-YT--DLP-2ea44f?style=for-the-badge)](https://github.com/yt-dlp/yt-dlp)
[![Platform - Windows](https://img.shields.io/badge/Platform-Windows-0078D6?style=for-the-badge&logo=windows)](https://microsoft.com)

**Download YouTube videos smoothly without typing complex commands.**
<br>
*Aplikasi "kulit" (GUI) modern untuk yt-dlp. Solusi terbaik cara download video YouTube di PC/Laptop Windows dengan mudah, gratis, dan tanpa iklan.*

[Persiapan] • [Instalasi] • [Cara Pakai] • [Troubleshooting] • [Download Gratis]

</div>

---

## 🌟 Kenapa Pakai Ini? (SEO & Features)

Bingung **cara download video YouTube** kualitas tinggi (1080p, 4K, hingga 8K) yang **gratis dan aman**? Aplikasi ini adalah jawabannya.
Berbeda dengan situs downloader online yang penuh iklan atau malware, aplikasi ini menggunakan mesin **yt-dlp** open-source yang legendaris, namun dengan tampilan yang **mudah dipakai (user friendly)**.

Cocok untuk anda yang mencari:
- **YouTube Downloader PC Gratis** tanpa watermark.
- **Cara download video YouTube jadi MP3** (Lagu) dengan cepat.
- **Aplikasi download video YouTube tercepat** dan stabil.
- Download playlist atau video durasi panjang anti gagal.

---

## 🔥 Fitur Utama
- **Tanpa Ngetik Command:** Cukup Copy-Paste link, tidak perlu repot dengan CMD.
- **Kualitas Terbaik:** Mendukung download hingga 4K/8K (tergantung video).
- **Auto-Merge:** Menggabungkan video & audio secara otomatis (menggunakan FFMPEG).
- **Audio Only:** Bisa download lagu saja (Convert to MP3).
- **Modern Dark UI:** Tampilan gelap yang nyaman di mata.

---

## �️ Persiapan Awal (Wajib)

Aplikasi ini bersifat **Modular**. Artinya, mesin utamanya (`yt-dlp`) dan pengolah videonya (`ffmpeg`) harus didownload terpisah agar anda selalu mendapatkan **versi terbaru & terupdate**.

### 1. 📥 Download Core Engine (yt-dlp)
Tanpa ini, aplikasi tidak bisa jalan.
1. Buka [Halaman Rilis yt-dlp Terbaru](https://github.com/yt-dlp/yt-dlp/releases).
2. Cari file **`yt-dlp.exe`** di bagian **Assets**.
3. **Download** file tersebut.

### 2. 🎬 Download Video Processor (FFMPEG)
Wajib agar bisa download video kualitas tinggi (gabung video+audio) dan konversi ke MP3.
1. Buka [Gyan.dev FFMPEG Builds](https://www.gyan.dev/ffmpeg/builds/).
2. Cari link **`ffmpeg-release-essentials.zip`** dan download.
3. **Extract (Unzip)** file tersebut.
4. Anda akan mendapatkan sebuah folder. **Copy seluruh folder tersebut**.

### 3. 📦 Download Aplikasi Ini
- Download file **`Brave_Download_Manager.exe`** dari rilis project ini.

---

## � Cara Instalasi (Penyusunan Folder)

Agar aplikasi bekerja sempurna, **Struktur File** harus benar. Buatlah satu folder baru (misal: `MyDownloader`) dan susun isinya seperti ini:

```text
MyDownloader/
├── 📁 ffmpeg-6.0-essentials_build/  <-- Folder hasil ekstrak FFMPEG
├── 📄 yt-dlp.exe                    <-- Mesin yt-dlp
└── 🚀 Brave_Download_Manager.exe    <-- Aplikasi kita
```

> **PENTING:** Pastikan file exe utama berada satu folder dengan `yt-dlp.exe`. Aplikasi akan otomatis mencari folder FFMPEG di sebelahnya.

---

## 📖 Cara Penggunaan

1. **Jalankan Aplikasi**
   Klik 2x pada **`Brave_Download_Manager.exe`**.
   *(Jika Windows SmartScreen muncul, klik `More Info` -> `Run Anyway`)*.

2. **Paste Link**
   Salin link video YouTube, lalu tempel (Paste) di kolom **YouTube URL**.

3. **Cek Video**
   Klik tombol `CEK VIDEO`. Tunggu sebentar hingga aplikasi mengambil data resolusi.

4. **Pilih & Download**
   - Pilih kualitas yang diinginkan (misal `Video 1080p` atau `Audio Only`).
   - Klik `DOWNLOAD SEKARANG`.

5. **Selesai!**
   Video anda akan tersimpan otomatis di folder baru bernama **`Hasil Download`**.

---

## ❓ FAQ & Troubleshooting

<details>
<summary><b>❌ Aplikasi tidak mau terbuka / Error saat dibuka</b></summary>
Pastikan sistem Windows anda mengizinkan "PowerShell Script execution" atau cukup jalankan sebagai Administrator. Aplikasi ini pada dasarnya adalah script canggih yang dibungkus menjadi EXE.
</details>

<details>
<summary><b>⚠️ Download berhenti di tengah jalan?</b></summary>
Biasanya koneksi internet terputus, atau link video memiliki restriksi (member only/private). Coba download video lain untuk mengetes.
</details>

<details>
<summary><b>🎵 Kok error saat pilih Audio Only?</b></summary>
Pastikan **FFMPEG** sudah terpasang dengan benar sesuai struktur folder di atas. Konversi ke MP3 membutuhkan FFMPEG.
</details>

---

## ⚖️ License & Attribution

**This project is a GUI wrapper for [yt-dlp](https://github.com/yt-dlp/yt-dlp).**
*yt-dlp is a separate project with its own license (The Unlicense).*

This project (the GUI/Interface) is licensed under the **MIT License**.
You are free to use, modify, and distribute this interface code.

> **Note:** This software relies on `yt-dlp.exe` and `ffmpeg` to function. We do not distribute these binaries directly in this repository code; users are instructed to download them from their official sources to ensure compliance and latest updates.

---

<div align="center">

**Enjoy Downloading! 🚀**
<br>
*Modified with ❤️ by Brave404*

</div>
