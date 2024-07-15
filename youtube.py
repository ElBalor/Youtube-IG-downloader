import yt_dlp
import tkinter as tk
from tkinter import filedialog

def download_video(url, save_path):
    try:
        ydl_opts = {
            'outtmpl': f'{save_path}/%(title)s.%(ext)s',
            'format': 'best',
            # You can add login details if required:
            # 'username': 'YOUR_YOUTUBE_USERNAME',
            # 'password': 'YOUR_YOUTUBE_PASSWORD',
        }

        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([url])
        print("Video downloaded Successfully!")

    except Exception as e:
        print(e)


def open_file():
    folder = filedialog.askdirectory()
    if folder:
        print(f"Selected Folder: {folder}")
    return folder    

if __name__ == "__main__":
    root = tk.Tk()
    root.withdraw()

    video_url = input("Please Enter a YouTube url: ")
    save_dir = open_file()

    if save_dir:
        print("Started Download...")
        download_video(video_url, save_dir) 
    else:     
         print("Invalid save location...") 

# url = ""
# save_path = r"C:\Users\Heylel Yaka\Downloads\you"

# download_video(url, save_path)
