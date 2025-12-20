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

### 🅰️ Opsi A: Windows (Paling Mudah)
**Cocok untuk pengguna umum. Tidak perlu install Python/Git.**

1.  **Download:** Unduh file **`Brave_Downloader.exe`**
2.  **Jalankan:** Klik 2x aplikasi.
    *   *Saat pertama kali dibuka, jika FFmpeg belum ada, aplikasi akan otomatis mendownloadnya (~30MB) dan menyetingnya untuk anda.*
3.  **Siap Pakai:** Masukkan Link -> Check URL -> Download.

### 🅱️ Opsi B: (Mac, Linux, Devs)
**Cocok untuk pengguna Mac/Linux atau pengguna Windows yang ingin menjalankan via Source Code.**

1.  **Persiapan Sistem (via Terminal):**
    *   **Linux (Debian/Ubuntu/Kali):**
        ```bash
        sudo apt update && sudo apt install python3-tk ffmpeg
        pip install yt-dlp customtkinter pillow --break-system-packages
        ```
    *   **macOS:**
        ```bash
        brew install python-tk ffmpeg
        pip install yt-dlp customtkinter pillow
        ```

2.  **Gunakan File:**
    *   **Windows:**
        ```bash
        python Brave_Download_Manager.py
        ```
    *   **macOS / Linux:**
        ```bash
        python3 Brave_Download_Manager.py
        ```

---

## ❓ FAQ & Troubleshooting

<details>
<summary><b>⚠️ Tombol Download tidak bisa diklik?</b></summary>
Pastikan anda sudah menekan tombol <b>CHECK URL</b> terlebih dahulu dan format video sudah muncul di menu pilihan.
</details>

<details>
<summary><b>🎵 Error saat download Audio/MP3?</b></summary>
Ini biasanya karena <b>FFmpeg</b> tidak terdeteksi.
<ul>
<li><b>Windows :</b> Tutup aplikasi, hapus file <code>ffmpeg.exe</code> jika ada (yang korup), lalu buka aplikasi lagi agar ia mendownload ulang.</li>
<li><b>Clean Version:</b> Pastikan anda sudah install FFmpeg di komputer anda.</li>
</ul>
</details>

---

## 💻 Spesifikasi Sistem

| Komponen | Windows | Universal Script |
| :--- | :--- | :--- |
| **OS** | Windows 10/11 | Windows, macOS, Linux |
| **Python** | *Tidak Perlu* | Python 3.8+ |
| **FFmpeg** | *Auto-Setup* | Install Manual |
| **Internet** | Wajib | Wajib |

---

<div align="center">

**Brave Downloader v1.0**
<br>
*Created with ❤️ by Brave404*

</div>
