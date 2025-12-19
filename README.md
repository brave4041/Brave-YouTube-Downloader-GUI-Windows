<div align="center">

# 🎥 Brave Download Manager
**Simple & Modern GUI for YT-DLP**

[![Brave404 - Project](https://img.shields.io/badge/Brave404-Project-red?style=for-the-badge&logo=youtube)](https://github.com/brave4041)
[![Powered By - YT-DLP](https://img.shields.io/badge/Powered_By-YT--DLP-2ea44f?style=for-the-badge)](https://github.com/yt-dlp/yt-dlp)
[![Platform - Windows](https://img.shields.io/badge/Platform-Windows-0078D6?style=for-the-badge&logo=windows)](https://microsoft.com)

**Download YouTube videos smoothly without typing complex commands.**
<br>
*Aplikasi "kulit" (GUI) modern untuk yt-dlp. Sekarang berbasis **PYTHON** agar bisa dijalankan di Windows, Linux, dan macOS!*

[Persiapan] • [Instalasi] • [Cara Pakai] • [Troubleshooting]

</div>

---

![Tampilan Aplikasi Brave Download Manager](https://via.placeholder.com/800x450?text=Preview+Aplikasi+Anda+Di+Sini)
*> **Note:** Tampilan aplikasi yang bersih dan modern (Dark Mode).*

---

## 🌟 Kenapa Pakai Ini?

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
Wajib agar bisa download video kualitas tinggi dan audio MP3.

**Untuk Pengguna Windows:**
1. Buka [Gyan.dev FFMPEG Builds](https://www.gyan.dev/ffmpeg/builds/).
2. Download **`ffmpeg-release-essentials.zip`**, ekstrak/unzip, lalu copas foldernya ke folder project ini.

**Untuk Pengguna Linux / macOS:**
Biasanya cukup install lewat terminal saja:
- **Ubuntu/Debian:** `sudo apt install ffmpeg`
- **macOS (Homebrew):** `brew install ffmpeg`
- **Arch Linux:** `sudo pacman -S ffmpeg`

### 3. 📦 Download Aplikasi Ini (Pilih Salah Satu)

**Opsi 1: Download EXE (Khusus Windows - Paling Mudah)**
- Buka menu **Releases** di sebelah kanan halaman GitHub ini.
- Download file **`Brave_Download_Manager.exe`**.
- Tinggal klik 2x, langsung jalan (tanpa install Python).

**Opsi 2: Download Manual (Zip)**
- Klik tombol **Code** > **Download ZIP** di pojok kanan atas repo ini.
- Ekstrak file zip-nya.
- Anda perlu install Python untuk menjalankan script `.py`.

**Opsi 3: Clone via Git (Semua OS: Windows, Mac, Linux)**
Cara ini lebih cepat jika anda sudah menginstall Git (Wajib di Linux/Mac):
```bash
git clone https://github.com/brave4041/Brave-YouTube-Downloader-GUI-Windows.git
cd Brave-YouTube-Downloader-GUI-Windows
```

---

## 💻 Spesifikasi Sistem (System Requirements)

| Komponen | Spesifikasi Minimum | Rekomendasi |
| :--- | :--- | :--- |
| **Python** | Python 3.8+ | **Python 3.10+** |
| **OS** | Windows 8/10/11, Linux, macOS | **Windows 10/11** atau **Linux Ubuntu** |
| **RAM** | 2 GB | 4 GB+ |
| **Internet** | Stabil (untuk download) | Kencang |

> **Wajib:** Pastikan anda sudah menginstall **PYTHON** di komputer anda. Jika belum, download di [python.org](https://www.python.org/).

---

## 📂 Cara Instalasi (Penyusunan Folder)

Agar aplikasi bekerja sempurna, susun folder seperti ini:

```text
MyDownloader/
├── 📁 ffmpeg/                       <-- (Khusus Windows) Folder FFMPEG
├── 📄 yt-dlp.exe                    <-- (Khusus Windows) Mesin yt-dlp
├── 📄 yt-dlp                        <-- (Khusus Linux/Mac) Mesin yt-dlp tanpa ekstensi
└── 🐍 Brave_Download_Manager.py     <-- Script Utama (Jalan di Semua OS)
```

> **PENTING:**
> - **Windows:** Wajib ada `ffmpeg` folder dan `yt-dlp.exe`.
> - **Linux/Mac:** `ffmpeg` dan `yt-dlp` biasanya sudah terinstall di sistem (path), jadi folder ini bisa lebih bersih. App akan otomatis mendeteksinya.

---

## 📖 Cara Penggunaan

1. **Install Library (Opsional)**
   Aplikasi ini menggunakan `tkinter` (biasanya sudah bawaan Python).
   Jika anda di Linux: `sudo apt-get install python3-tk`

2. **Jalankan Aplikasi**
   - **Windows:** Klik kanan `Brave_Download_Manager.py` -> *Open with Python*, ATAU buka CMD dan ketik:
     ```bash
     python Brave_Download_Manager.py
     ```
   - **Linux/Mac:** Buka terminal dan ketik `python3 Brave_Download_Manager.py`.

3. **Paste Link**
   Salin link video YouTube, lalu tempel (Paste) di kolom **YouTube URL**.

4. **Cek Video**
   Klik tombol `CEK VIDEO`. Tunggu sebentar hingga aplikasi mengambil data resolusi.

5. **Pilih & Download**
   - Pilih kualitas yang diinginkan (misal `Video 1080p` atau `Audio Only`).
   - Klik `DOWNLOAD SEKARANG`.

6. **Selesai!**
   Video anda akan tersimpan otomatis di folder baru bernama **`Hasil Download`**.

---

## ❓ FAQ & Troubleshooting

<details>
<summary><b>❌ Aplikasi tidak mau terbuka / Error saat dibuka</b></summary>
1. **Belum Install Python:** Pastikan anda sudah install Python 3.x.
2. **Library Kurang:** Jika di Linux, pastikan `tkinter` terinstall (`sudo apt install python3-tk`).
3. **Double Click Gagal:** Coba buka lewat terminal/CMD: `python Brave_Download_Manager.py` untuk melihat pesan errornya.
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
