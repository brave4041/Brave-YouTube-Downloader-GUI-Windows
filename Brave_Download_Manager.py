import tkinter as tk
from tkinter import ttk, messagebox, scrolledtext
import subprocess
import threading
import json
import os
import sys
import platform

APP_TITLE = "Powered by yt-dlp | Modified by Brave404"
APP_SIZE = "640x490" 
BG_COLOR = "#1e1e23" 
FG_COLOR = "#f5f5f5"
ACCENT_COLOR = "#8B0000" 
BTN_BG = "#000000"
INPUT_BG = "#323232"
INPUT_FG = "#ffffff"

if platform.system() == "Windows":
    FONT_MAIN = ("Segoe UI", 10)
    FONT_BOLD = ("Segoe UI", 9, "bold")
    FONT_BIG_BOLD = ("Segoe UI", 10, "bold")
    FONT_SMALL = ("Segoe UI", 8)
elif platform.system() == "Darwin":
    FONT_MAIN = ("Helvetica Neue", 12)
    FONT_BOLD = ("Helvetica Neue", 12, "bold")
    FONT_BIG_BOLD = ("Helvetica Neue", 13, "bold")
    FONT_SMALL = ("Helvetica Neue", 10)
else: 
    FONT_MAIN = ("DejaVu Sans", 10)
    FONT_BOLD = ("DejaVu Sans", 9, "bold")
    FONT_BIG_BOLD = ("DejaVu Sans", 10, "bold")
    FONT_SMALL = ("DejaVu Sans", 8)

class BraveDownloaderApp:
    def __init__(self, root):
        self.root = root
        self.root.title(APP_TITLE)
        self.root.geometry(APP_SIZE)
        self.root.configure(bg=BG_COLOR)
        self.root.resizable(False, False)

        self.cwd = os.getcwd()
        self.ytdlp_path = self.find_executable("yt-dlp")
        self.ffmpeg_path = self.find_ffmpeg()
        self.output_dir = os.path.join(self.cwd, "Hasil Download")

        if not os.path.exists(self.output_dir):
            os.makedirs(self.output_dir)

        self.setup_ui()
        self.log(f"Selamat Datang di {APP_TITLE}")
        self.log(f"System: {platform.system()} {platform.release()}")
        
        if not self.ytdlp_path:
            messagebox.showerror("Error", "yt-dlp tidak ditemukan!\nPastikan yt-dlp ada di folder yang sama atau terinstall di system path.")
            self.log("[!] Error: yt-dlp missing.")
        else:
            self.log(f"[v] Found yt-dlp: {self.ytdlp_path}")

        if self.ffmpeg_path:
            self.log(f"[v] Found FFMPEG: {self.ffmpeg_path}")
        else:
            self.log("[!] FFMPEG not found (Audio merge might fail). check folder structure.")

    def find_executable(self, name):
        ext = ".exe" if platform.system() == "Windows" else ""
        local_path = os.path.join(self.cwd, name + ext)
        if os.path.exists(local_path):
            return local_path
        import shutil
        return shutil.which(name)

    def find_ffmpeg(self):
        ext = ".exe" if platform.system() == "Windows" else ""
        if os.path.exists(os.path.join(self.cwd, "ffmpeg" + ext)):
            return os.path.join(self.cwd, "ffmpeg" + ext)
        
        for root, dirs, files in os.walk(self.cwd):
            if "ffmpeg" + ext in files:
                return os.path.join(root, "ffmpeg" + ext)
        
        import shutil
        return shutil.which("ffmpeg")

    def setup_ui(self):
        style = ttk.Style()
        style.theme_use('clam')
        style.configure("TLabel", background=BG_COLOR, foreground="LightGray", font=FONT_MAIN)
        style.configure("TButton", background=BTN_BG, foreground=FG_COLOR, font=FONT_BOLD, borderwidth=1)
        style.map("TButton", background=[('active', ACCENT_COLOR)])
        
        lbl_url = ttk.Label(self.root, text="YouTube URL:")
        lbl_url.place(x=25, y=20)

        self.entry_url = tk.Entry(self.root, width=50, bg=INPUT_BG, fg=INPUT_FG, font=FONT_MAIN, bd=1, relief="solid")
        self.entry_url.place(x=25, y=45, width=430, height=26)

        self.btn_check_frame = tk.Frame(self.root, bg="Red", bd=0)
        self.btn_check_frame.place(x=470, y=43, width=130, height=30)
        
        self.btn_check = tk.Button(self.btn_check_frame, text="CEK VIDEO", bg="Black", fg="White", font=FONT_BOLD, 
                                   command=self.start_check_video, cursor="hand2", activebackground="#333", activeforeground="White",
                                   relief="flat", bd=0)
        self.btn_check.place(x=1, y=1, width=128, height=28)

        lbl_res = ttk.Label(self.root, text="Pilih Kualitas:")
        lbl_res.place(x=25, y=95)

        self.combo_res = ttk.Combobox(self.root, state="readonly", font=FONT_MAIN)
        self.combo_res.place(x=140, y=92, width=200, height=26)

        self.btn_download = tk.Button(self.root, text="DOWNLOAD SEKARANG", bg=ACCENT_COLOR, fg="White", font=FONT_BIG_BOLD, command=self.start_download, state="disabled", cursor="hand2", relief="flat", activebackground="#A00000", activeforeground="White")
        self.btn_download.place(x=360, y=90, width=240, height=32)

        self.log_area = scrolledtext.ScrolledText(self.root, width=80, height=20, bg="#141414", fg="LimeGreen", font=("Consolas", 10))
        self.log_area.place(x=25, y=140, width=575, height=250)
        self.log_area.configure(state='disabled', relief="flat")

        lbl_footer = ttk.Label(self.root, text="Powered by yt-dlp | Modified by Brave404", font=FONT_SMALL, foreground="DimGray")
        lbl_footer.place(x=25, y=420)

    def log(self, msg):
        self.log_area.configure(state='normal')
        self.log_area.insert(tk.END, msg + "\n")
        self.log_area.see(tk.END)
        self.log_area.configure(state='disabled')

    def start_check_video(self):
        url = self.entry_url.get().strip()
        if not url:
            messagebox.showwarning("Warning", "URL tidak boleh kosong!")
            return
        
        self.btn_check.config(state="disabled")
        self.btn_download.config(state="disabled")
        self.combo_res.set('')
        self.combo_res['values'] = []
        
        threading.Thread(target=self.check_video_thread, args=(url,), daemon=True).start()

    def check_video_thread(self, url):
        self.log("-" * 30)
        self.log(f"[*] Analyzing: {url}")
        
        try:
            cmd = [self.ytdlp_path, "--dump-single-json", "--no-warnings", url]
            
            startupinfo = None
            if platform.system() == "Windows":
                startupinfo = subprocess.STARTUPINFO()
                startupinfo.dwFlags |= subprocess.STARTF_USESHOWWINDOW

            proc = subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True, startupinfo=startupinfo, encoding='utf-8')
            stdout, stderr = proc.communicate()

            if proc.returncode != 0:
                raise Exception(stderr)

            data = json.loads(stdout)
            title = data.get('title', 'Unknown Title')
            uploader = data.get('uploader', 'Unknown Channel')
            
            self.log(f"[+] Judul: {title}")
            self.log(f"[+] Channel: {uploader}")

            formats = data.get('formats', [])
            res_set = set()
            for f in formats:
                if f.get('vcodec') != 'none' and f.get('height'):
                    res_set.add(f['height'])
            
            sorted_res = sorted(list(res_set), reverse=True)
            options = [f"Video {r}p" for r in sorted_res]
            options.append("Audio Only (MP3)")
            
            def update_ui():
                self.combo_res['values'] = options
                if options:
                    self.combo_res.current(0)
                    self.btn_download.config(state="normal")
                self.btn_check.config(state="normal")
                self.log("[v] Analysis Done.")
            
            self.root.after(0, update_ui)

        except Exception as e:
            def error_ui():
                self.log(f"[!] Error: {str(e)}")
                self.btn_check.config(state="normal")
            self.root.after(0, error_ui)

    def start_download(self):
        selection = self.combo_res.get()
        url = self.entry_url.get().strip()
        if not selection or not url: return

        self.btn_download.config(state="disabled")
        self.btn_check.config(state="disabled")

        threading.Thread(target=self.download_thread, args=(url, selection), daemon=True).start()

    def download_thread(self, url, selection):
        self.log("-" * 30)
        self.log(f"[*] DOWNLOADING: {selection}")
        self.log("[*] Do not close the window...")

        cmd = [self.ytdlp_path]
        
        if "Audio Only" in selection:
            cmd += ["-f", "bestaudio/best", "--extract-audio", "--audio-format", "mp3"]
        else:
            height = ''.join(filter(str.isdigit, selection))
            fmt = f"bv*[height<={height}]+ba[ext=m4a]/bv*[height<={height}]+ba/b[height<={height}]"
            cmd += ["-f", fmt, "--merge-output-format", "mp4"]

        if self.ffmpeg_path:
             cmd += ["--ffmpeg-location", self.ffmpeg_path]
        
        out_tmpl = os.path.join(self.output_dir, "%(title)s.%(ext)s")
        cmd += ["-o", out_tmpl]
        cmd += ["--no-mtime"]
        
        cmd.append(url)

        try:
            startupinfo = None
            if platform.system() == "Windows":
                 startupinfo = subprocess.STARTUPINFO()
                 startupinfo.dwFlags |= subprocess.STARTF_USESHOWWINDOW

            process = subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, 
                                       text=True, startupinfo=startupinfo, encoding='utf-8', bufsize=1)
            
            for line in iter(process.stdout.readline, ''):
                if line:
                    self.root.after(0, self.log, line.strip())
            
            process.stdout.close()
            process.wait()

            if process.returncode == 0:
                self.root.after(0, lambda: messagebox.showinfo("Success", "Download Selesai!"))
                self.root.after(0, lambda: self.log("[v] DOWNLOAD COMPLETED!"))
            else:
                 self.root.after(0, lambda: self.log("[!] Download Failed."))

        except Exception as e:
            self.root.after(0, lambda: self.log(f"[!] Error: {e}"))

        def reset_btn():
            self.btn_download.config(state="normal")
            self.btn_check.config(state="normal")
        
        self.root.after(0, reset_btn)

if __name__ == "__main__":
    try:
        root = tk.Tk()
        app = BraveDownloaderApp(root)
        root.mainloop()
    except Exception as e:
        with open("error_log.txt", "w") as f:
            f.write(str(e))
