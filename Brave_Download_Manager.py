import customtkinter as ctk
import tkinter as tk
from tkinter import messagebox
import yt_dlp
import threading
import os
import sys
import shutil
from PIL import Image

if sys.platform == "win32":
    import ctypes

APP_TITLE = "Brave Downloader"
APP_SIZE = "850x530"
DOWNLOAD_FOLDER = "Hasil Download"

COLOR_BG = "#0f0f0f"
COLOR_CARD = "#1a1a1a"
COLOR_ACCENT = "#D80000"
COLOR_ACCENT_HOVER = "#A00000"
COLOR_TEXT_MAIN = "#FFFFFF"
COLOR_TEXT_SUB = "#AAAAAA"

ctk.set_appearance_mode("Dark")

class MyLogger:
    def debug(self, msg): pass
    def warning(self, msg): pass
    def error(self, msg): print(msg)

class BraveDownloaderApp(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.title(APP_TITLE)
        self.geometry(APP_SIZE)
        self.configure(fg_color=COLOR_BG)
        self.resizable(False, False)
        
        if sys.platform == "win32":
            try:
                myappid = 'brave404.downloader'
                ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID(myappid)
            except:
                pass
        
        self.cwd = os.path.dirname(os.path.abspath(__file__))
        
        try:
            icon_name = "cat_icon.ico" if sys.platform == "win32" else "cat_icon.png"
            self.icon_path = os.path.join(self.cwd, icon_name)
            
            if os.path.exists(self.icon_path):
                if sys.platform == "win32":
                    self.iconbitmap(self.icon_path)
                else:
                    img = tk.PhotoImage(file=self.icon_path)
                    self.wm_iconphoto(True, img)
        except Exception as e:
            print(f"Icon load error: {e}")
            
        self.output_dir = os.path.join(self.cwd, DOWNLOAD_FOLDER)
        if not os.path.exists(self.output_dir):
            os.makedirs(self.output_dir, exist_ok=True)

        self.setup_ui()
        
        self.ffmpeg_path = self.find_ffmpeg()
        if not self.ffmpeg_path:
            messagebox.showwarning("FFmpeg Missing", 
                                 "FFmpeg was not found in your system.\n\n"
                                 "You can still download videos, but High Quality merging and MP3 conversion will fail.\n"
                                 "Please install FFmpeg and add it to your PATH.")

    def find_ffmpeg(self):
        sys_path = shutil.which("ffmpeg")
        if sys_path: return sys_path
        
        ext = ".exe" if sys.platform == "win32" else ""
        local_path = os.path.join(self.cwd, "ffmpeg" + ext)
        if os.path.exists(local_path): return local_path
        
        return None

    def setup_ui(self):
        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(0, weight=1)

        self.main_card = ctk.CTkFrame(self, fg_color=COLOR_CARD, corner_radius=20, border_color="#333333", border_width=1)
        self.main_card.grid(row=0, column=0, padx=20, pady=(20, 50), sticky="nsew")
        
        self.main_card.grid_columnconfigure(0, weight=1)
        self.main_card.grid_rowconfigure(0, weight=0)
        self.main_card.grid_rowconfigure(1, weight=0)
        self.main_card.grid_rowconfigure(2, weight=0)
        self.main_card.grid_rowconfigure(3, weight=0)
        self.main_card.grid_rowconfigure(4, weight=1)
        self.main_card.grid_rowconfigure(5, weight=0)

        self.lbl_brand = ctk.CTkLabel(self.main_card, text="BRAVE DOWNLOADER", font=("Impact", 28), text_color=COLOR_ACCENT)
        self.lbl_brand.grid(row=0, column=0, pady=(30, 5))
        
        self.lbl_subtitle = ctk.CTkLabel(self.main_card, text="Premium YouTube Media Manager", font=("Arial", 12), text_color=COLOR_TEXT_SUB)
        self.lbl_subtitle.grid(row=1, column=0, pady=(0, 20))

        self.frame_input = ctk.CTkFrame(self.main_card, fg_color="transparent")
        self.frame_input.grid(row=2, column=0, padx=30, pady=10, sticky="ew")
        self.frame_input.grid_columnconfigure(0, weight=1)

        self.entry_url = ctk.CTkEntry(
            self.frame_input, 
            placeholder_text="🔗 Paste YouTube Link here...", 
            height=50, 
            font=("Arial", 14),
            corner_radius=12,
            border_color="#444444",
            fg_color="#0a0a0a"
        )
        self.entry_url.grid(row=0, column=0, sticky="ew")

        self.frame_actions = ctk.CTkFrame(self.main_card, fg_color="transparent")
        self.frame_actions.grid(row=3, column=0, padx=30, pady=20, sticky="ew")
        self.frame_actions.grid_columnconfigure(0, weight=1)
        self.frame_actions.grid_columnconfigure(1, weight=2)
        self.frame_actions.grid_columnconfigure(2, weight=1)

        self.btn_check = ctk.CTkButton(
            self.frame_actions, 
            text="CHECK URL", 
            command=self.start_check, 
            height=45, 
            font=("Arial", 12, "bold"),
            fg_color="#222222", 
            hover_color="#333333",
            border_color="#444444",
            border_width=1,
            corner_radius=10
        )
        self.btn_check.grid(row=0, column=0, sticky="ew", padx=(0, 10))

        self.option_format = ctk.CTkOptionMenu(
            self.frame_actions, 
            values=["Wait for check..."], 
            height=45, 
            state="disabled", 
            font=("Arial", 12),
            fg_color="#0a0a0a",
            button_color="#222222",
            button_hover_color="#333333",
            corner_radius=10,
            text_color=COLOR_TEXT_SUB
        )
        self.option_format.grid(row=0, column=1, sticky="ew", padx=10)

        self.btn_download = ctk.CTkButton(
            self.frame_actions, 
            text="DOWNLOAD", 
            command=self.start_download, 
            height=45, 
            font=("Arial", 13, "bold"),
            fg_color=COLOR_ACCENT, 
            hover_color=COLOR_ACCENT_HOVER,
            corner_radius=10,
            state="disabled"
        )
        self.btn_download.grid(row=0, column=2, sticky="ew", padx=(10, 0))

        self.frame_info = ctk.CTkFrame(self.main_card, fg_color="#141414", corner_radius=10)
        self.frame_info.grid(row=4, column=0, padx=30, pady=(0, 20), sticky="nsew")
        self.frame_info.grid_columnconfigure(0, weight=1)
        
        self.lbl_video_title = ctk.CTkLabel(self.frame_info, text="", font=("Arial", 14, "bold"), text_color="white", wraplength=700)
        self.lbl_video_title.grid(row=0, column=0, pady=(15, 5), padx=20)
        
        self.lbl_video_meta = ctk.CTkLabel(self.frame_info, text="", font=("Arial", 12), text_color="gray")
        self.lbl_video_meta.grid(row=1, column=0, pady=(0, 15), padx=20)

        self.frame_progress = ctk.CTkFrame(self.main_card, fg_color="transparent")
        self.frame_progress.grid(row=5, column=0, padx=30, pady=(0, 30), sticky="ew")
        self.frame_progress.grid_columnconfigure(0, weight=1)

        self.lbl_status = ctk.CTkLabel(self.frame_progress, text="Ready to start", font=("Arial", 11), text_color="gray")
        self.lbl_status.grid(row=0, column=0, sticky="w", pady=(0, 5))

        self.lbl_percent = ctk.CTkLabel(self.frame_progress, text="", font=("Arial", 12, "bold"), text_color=COLOR_ACCENT)
        self.lbl_percent.grid(row=0, column=1, sticky="e", pady=(0, 5))

        self.progress_bar = ctk.CTkProgressBar(self.frame_progress, height=8, corner_radius=4, progress_color=COLOR_ACCENT, fg_color="#333333")
        self.progress_bar.grid(row=1, column=0, columnspan=2, sticky="ew")
        self.progress_bar.set(0)
        
        self.lbl_footer = ctk.CTkLabel(self, text="Brave404 Edition | v1.0", font=("Arial", 10, "bold"), text_color=COLOR_ACCENT)
        self.lbl_footer.place(relx=0.5, rely=0.95, anchor="center")

        self.video_info = None
        self.formats_map = {} 

    def start_check(self):
        url = self.entry_url.get().strip()
        if not url:
            self.lbl_status.configure(text="Please insert a valid URL", text_color="red")
            return

        self.btn_check.configure(state="disabled")
        self.option_format.configure(state="disabled")
        self.btn_download.configure(state="disabled")
        self.lbl_status.configure(text="Fetching video metadata...", text_color="white")
        self.progress_bar.configure(mode="indeterminate")
        self.progress_bar.start()

        threading.Thread(target=self.check_video_thread, args=(url,), daemon=True).start()

    def check_video_thread(self, url):
        try:
            ydl_opts = {
                'quiet': True,
                'no_warnings': True,
                'logger': MyLogger(), 
            }
            with yt_dlp.YoutubeDL(ydl_opts) as ydl:
                info = ydl.extract_info(url, download=False)
            
            self.video_info = info
            self.formats_map = {}
            
            options = []
            
            formats = info.get('formats', [])
            seen_res = set()
            video_formats = []
            
            for f in formats:
                if f.get('vcodec') != 'none' and f.get('height'):
                    h = f['height']
                    if h not in seen_res:
                        seen_res.add(h)
                        video_formats.append(h)
            
            video_formats.sort(reverse=True)
            for res in video_formats:
                label = f"VIDEO {res}p (High Quality)"
                options.append(label)
                self.formats_map[label] = str(res)
            
            options.append("AUDIO ONLY (MP3 Premium)")
            self.formats_map["AUDIO ONLY (MP3 Premium)"] = "audio_only"

            self.after(0, lambda: self.update_ui_after_check(options, info))

        except Exception as e:
            self.after(0, lambda: self.show_error(f"Error: {str(e)[:100]}..."))

    def update_ui_after_check(self, options, info):
        self.progress_bar.stop()
        self.progress_bar.configure(mode="determinate")
        self.progress_bar.set(0)
        
        if not options:
            self.lbl_status.configure(text="No downloadable formats found.", text_color="red")
            self.btn_check.configure(state="normal")
            return

        self.option_format.configure(values=options, state="normal")
        self.option_format.set(options[0])
        
        self.btn_check.configure(state="normal")
        self.btn_download.configure(state="normal")
        
        title = info.get('title', 'Unknown')
        uploader = info.get('uploader', 'Unknown')
        duration = info.get('duration_string', '')
        
        self.lbl_video_title.configure(text=title)
        self.lbl_video_meta.configure(text=f"{uploader} • {duration}")
        
        self.lbl_status.configure(text="Video found. Select format and download.", text_color="#2CC985")

    def show_error(self, msg):
        self.progress_bar.stop()
        self.progress_bar.configure(mode="determinate")
        self.progress_bar.set(0)
        self.lbl_status.configure(text=msg, text_color="red")
        self.btn_check.configure(state="normal")

    def start_download(self):
        selection = self.option_format.get()
        url = self.entry_url.get().strip()

        if selection not in self.formats_map:
            messagebox.showwarning("Action Required", "Please click 'CHECK URL' first.")
            return

        if not selection or not url: return

        self.btn_download.configure(state="disabled")
        self.btn_check.configure(state="disabled")
        self.entry_url.configure(state="disabled")
        self.option_format.configure(state="disabled")
        
        self.lbl_status.configure(text="Initializing download...", text_color="white")
        self.progress_bar.set(0)
        self.lbl_percent.configure(text="0%")

        threading.Thread(target=self.download_thread, args=(url, selection), daemon=True).start()

    def download_thread(self, url, selection):
        value = self.formats_map.get(selection)
        
        ydl_opts = {
            'outtmpl': os.path.join(self.output_dir, '%(title)s.%(ext)s'),
            'progress_hooks': [self.progress_hook],
            'logger': MyLogger(),
            'no_mtime': True,
            'restrictfilenames': True,
        }

        if self.ffmpeg_path:
             ydl_opts['ffmpeg_location'] = self.ffmpeg_path
        
        if value == "audio_only":
            ydl_opts['format'] = 'bestaudio/best'
            ydl_opts['postprocessors'] = [{
                'key': 'FFmpegExtractAudio',
                'preferredcodec': 'mp3',
                'preferredquality': '320',
            }]
        else:
            height = value
            ydl_opts['format'] = f"bv*[height<={height}]+ba[ext=m4a]/b[height<={height}] / best"
            ydl_opts['merge_output_format'] = 'mp4'

        try:
            with yt_dlp.YoutubeDL(ydl_opts) as ydl:
                ydl.download([url])
            
            self.after(0, self.download_complete_success)
        except Exception as e:
            error_message = str(e)
            self.after(0, lambda: self.download_complete_error(error_message))

    def progress_hook(self, d):
        if d['status'] == 'downloading':
            try:
                total = d.get('total_bytes') or d.get('total_bytes_estimate')
                downloaded = d.get('downloaded_bytes', 0)
                
                if total:
                    progress_float = downloaded / total
                    percent_str = f"{progress_float*100:.1f}%"
                else:
                    progress_float = 0
                    percent_str = "..."

                if progress_float < 0: progress_float = 0
                if progress_float > 1: progress_float = 1
                
                speed = d.get('speed')
                speed_str = f"{speed/1024/1024:.2f} MB/s" if speed else "-"
                    
                eta = d.get('eta')
                eta_str = f"{eta}s" if eta else "-"
                
                msg = f"Downloading at {speed_str} • ETA: {eta_str}"
                
                self.after(0, lambda: self.update_progress_ui(progress_float, percent_str, msg))
            except Exception as e:
                print(f"Progress Error: {e}") 
        
        elif d['status'] == 'finished':
            self.after(0, lambda: self.update_progress_ui(1.0, "COMPLETE", "Finalizing file..."))

    def update_progress_ui(self, val, percent_text, status_text):
        self.progress_bar.set(val)
        self.lbl_percent.configure(text=percent_text)
        self.lbl_status.configure(text=status_text, text_color="white")

    def download_complete_success(self):
        self.lbl_status.configure(text="Download Successfully Completed!", text_color=COLOR_ACCENT)
        self.progress_bar.set(1)
        self.lbl_percent.configure(text="✓")
        self.reset_ui()
        messagebox.showinfo("Brave Downloader", "Your file has been downloaded successfully!")

    def download_complete_error(self, error_msg):
        self.lbl_status.configure(text="Download Failed", text_color="red")
        self.progress_bar.set(0)
        self.reset_ui()
        messagebox.showerror("Download Error", f"An error occurred:\n{error_msg}")

    def reset_ui(self):
        self.btn_download.configure(state="normal")
        self.btn_check.configure(state="normal")
        self.entry_url.configure(state="normal")
        self.option_format.configure(state="normal")

if __name__ == "__main__":
    app = BraveDownloaderApp()
    app.mainloop()
