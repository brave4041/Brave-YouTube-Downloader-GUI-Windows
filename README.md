<div align="center">

# 🎥 Brave Download Manager
**Simple & Modern GUI for YT-DLP**

[![Brave404 - Project](https://img.shields.io/badge/Brave404-Project-red?style=for-the-badge&logo=youtube)](https://github.com/brave4041)
[![Powered By - YT-DLP](https://img.shields.io/badge/Powered_By-YT--DLP-2ea44f?style=for-the-badge)](https://github.com/yt-dlp/yt-dlp)
[![Platform - Windows](https://img.shields.io/badge/Windows-0078D6?style=for-the-badge&logo=windows)](https://microsoft.com)
[![Platform - Linux](https://img.shields.io/badge/Linux-FCC624?style=for-the-badge&logo=linux&logoColor=black)](https://linux.org)
[![Platform - macOS](https://img.shields.io/badge/macOS-000000?style=for-the-badge&logo=apple)](https://apple.com)

**Download YouTube videos smoothly without typing complex commands.**
<br>
*Aplikasi "kulit" (GUI) modern untuk yt-dlp. Berbasis **PYTHON** agar bisa dijalankan di Windows, Linux, dan macOS!*

[Persiapan] • [Instalasi & Penggunaan] • [Troubleshooting]

</div>

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

## 🚀 Cara Instalasi & Penggunaan (Step-by-Step)

### Pilih metode yang sesuai dengan OS anda:

**A. Pengguna Windows (Paling Mudah ⭐)**
1. **Download:** Ambil file **`Brave_Download_Manager_Bundled.exe`** di release [v1.0](https://github.com/brave4041/Brave-YouTube-Downloader-GUI-Windows/releases/tag/v1.0).
2. **Buat Folder:** Buat folder baru (misal: `YouTube Downloader`) dan masukkan file EXE tadi ke dalamnya (Wajib, agar hasil download rapi).
3. **Jalankan:** Klik 2x file aplikasi tersebut (Langsung jalan, tanpa install apapun).
4. **Mulai Download:**
   - **Paste Link** YouTube di kolom input.
   - Klik **Cek Video** -> Pilih kualitas.
   - Klik **DOWNLOAD**. File akan muncul di folder `Hasil Download`.

**B. Pengguna Linux / macOS / Developer**
1. **Setup Awal:**
   - Clone repo: `git clone https://github.com/brave4041/Brave-YouTube-Downloader-GUI-Windows.git`
   - Install dependency (sesuai OS):
     ```bash
     # --- Ubuntu / Debian / Kali Linux ---
     sudo apt update && sudo apt install python3-tk ffmpeg
     pip install yt-dlp --break-system-packages

     # --- macOS ---
     brew install python-tk ffmpeg && pip install yt-dlp
     ```
2. **Jalankan:** Buka terminal, ketik `python3 Brave_Download_Manager.py`.
3. **Mulai Download:** (Sama seperti langkah nomor 3 di atas).

---

## 💻 Spesifikasi Sistem (System Requirements)

| Komponen | Spesifikasi Minimum | Rekomendasi |
| :--- | :--- | :--- |
| **Python** | Python 3.8+ | **Python 3.10+** |
| **OS** | Windows 8/10/11, Linux, macOS | **Windows 10/11** atau **Linux Ubuntu** |
| **RAM** | 2 GB | 4 GB+ |
| **Internet** | Stabil (untuk download) | Kencang |

> **Wajib (Linux / macOS / Developer):** Pastikan anda sudah menginstall **PYTHON** di komputer anda. Jika belum, download di [python.org](https://www.python.org/).
> **(Pengguna Windows Bundled TIDAK PERLU install Python).**

---

## ❓ FAQ & Troubleshooting

<details>
<summary><b>❌ Aplikasi tidak mau terbuka / Error saat dibuka</b></summary>
1. **Belum Install Python (Linux/Mac/Dev):** Pastikan anda sudah install Python 3.x.
2. **Library Kurang (Linux/Mac):** Pastikan `tkinter` terinstall.
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
