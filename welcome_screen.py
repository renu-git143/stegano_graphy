import tkinter as tk
from PIL import Image, ImageTk
import time
import subprocess

def open_main_gui():
    splash.destroy()
    subprocess.Popen(["python", "gui_main.py"], shell=True)  # shell=True helps with some systems

# --- Splash Screen Window ---
splash = tk.Tk()
splash.overrideredirect(True)
splash.geometry("400x300")
splash.configure(bg="#1A1A1A")

# --- Add Logo or Text ---
label = tk.Label(splash, text="Welcome to SteganoGraphy 🕵️‍♀️", font=("Segoe UI", 16, "bold"), fg="white", bg="#1A1A1A")
label.pack(expand=True)

# --- Auto Close After 3 Seconds ---
splash.after(3000, open_main_gui)
splash.mainloop()
