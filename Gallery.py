import os
import tkinter as tk
from tkinter import filedialog

# Function to select a directory
def select_directory():
    directory = filedialog.askdirectory()
    return directory

# Function to list all videos in the selected directory
def list_videos(directory):
    videos = []
    for filename in os.listdir(directory):
        if filename.endswith('.mp4') or filename.endswith('.avi'):
            videos.append(filename)
    return videos

# Function to create a video gallery
def create_gallery(directory, videos):
    # Code to create the video gallery (e.g., using a GUI library such as PyQt or PyGTK)
    pass

# Tkinter GUI code
root = tk.Tk()
root.title("Video Gallery Creator")

directory_label = tk.Label(root, text="Directory:")
directory_label.pack()

directory_entry = tk.Entry(root)
directory_entry.pack()

select_directory_button = tk.Button(root, text="Select Directory", command=lambda: directory_entry.insert(0, select_directory()))
select_directory_button.pack()

create_gallery_button = tk.Button(root, text="Create Gallery", command=lambda: create_gallery(directory_entry.get(), list_videos(directory_entry.get())))
create_gallery_button.pack()

root.mainloop()
